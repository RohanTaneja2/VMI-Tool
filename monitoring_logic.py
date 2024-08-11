import time
from vmi_interface.py import VMIInterface
from logger.py import Logger
from detector.py import AnomalyDetector
from alert.py import AlertSystem
from config.py import Config

class Monitor:
    def __init__(self):
        self.logger = Logger()
        self.detector = AnomalyDetector()
        self.alert_system = AlertSystem()
        self.vmi = VMIInterface(Config.DOMAIN_NAME)

    def start_monitoring(self):
        if not self.vmi.initialize():
            self.logger.log("Failed to initialize VMI", level="error")
            return

        while True:
            processes = self.vmi.list_processes()
            suspicious = self.detector.detect_anomalies(processes)

            if suspicious:
                for process in suspicious:
                    self.logger.log(f"Suspicious process detected: {process.name}, PID: {process.pid}")
                    self.alert_system.send_alert(f"Suspicious process: {process.name}, PID: {process.pid}")

            if self.detector.is_alert_needed():
                self.logger.log("Alert threshold reached", level="warning")
                self.alert_system.send_alert("Multiple anomalies detected in VM")
                self.detector.reset_alert_count()

            time.sleep(Config.MONITOR_INTERVAL)

        self.vmi.close()
