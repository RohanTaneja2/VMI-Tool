# config.py

class Config:
    DOMAIN_NAME = "example_vm"
    LOG_FILE = "vm_monitor.log"
    ALERT_THRESHOLD = 5
    MONITOR_INTERVAL = 10

    # Email Configuration
    EMAIL_SENDER = "your_email@example.com"
    EMAIL_PASSWORD = "your_email_password"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
