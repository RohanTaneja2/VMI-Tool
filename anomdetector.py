class AnomalyDetector:
    def __init__(self):
        self.alert_count = 0

    def detect_anomalies(self, processes):
        """
        Basic anomaly detection by comparing processes.
        You can extend this method with more complex logic.
        """
        suspicious_processes = []

        for process in processes:
            if "malicious_process" in process.name:
                suspicious_processes.append(process)
                self.alert_count += 1

        return suspicious_processes

    def is_alert_needed(self):
        return self.alert_count >= 5
