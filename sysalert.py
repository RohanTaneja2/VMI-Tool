import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from logger import Logger

class AlertSystem:
    def __init__(self):
        self.alert_count = 0
        self.logger = Logger()

    def send_console_alert(self, message):
        """Send an alert to the console."""
        print(f"ALERT: {message}")
        self.logger.log(f"Console Alert: {message}", level="warning")

    def send_email_alert(self, message, recipient_email):
        """Send an alert via email."""
        try:
            msg = MIMEMultipart()
            msg['From'] = Config.EMAIL_SENDER
            msg['To'] = recipient_email
            msg['Subject'] = 'VM Monitoring Alert'

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
            server.starttls()
            server.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
            server.sendmail(Config.EMAIL_SENDER, recipient_email, msg.as_string())
            server.quit()

            self.logger.log(f"Email Alert sent to {recipient_email}: {message}", level="warning")
            print(f"Email alert sent to {recipient_email}.")
        except Exception as e:
            self.logger.log(f"Failed to send email alert: {e}", level="error")
            print(f"Failed to send email alert: {e}")

    def send_alert(self, message, alert_type="console", recipient_email=None):
        """Send an alert based on the specified type."""
        if alert_type == "console":
            self.send_console_alert(message)
        elif alert_type == "email" and recipient_email:
            self.send_email_alert(message, recipient_email)
        else:
            print(f"Invalid alert type: {alert_type}. Defaulting to console alert.")
            self.send_console_alert(message)

        self.alert_count += 1

    def reset_alert_count(self):
        """Reset the alert count."""
        self.alert_count = 0
        self.logger.log("Alert count reset", level="info")

    def get_alert_count(self):
        """Get the current alert count."""
        return self.alert_count
