# VMI-Tool

This project is a Python-based Virtual Machine Introspection (VMI) tool designed to monitor and analyze the state of virtual machines for security purposes. The tool detects malicious activity or intrusions by leveraging LibVMI to inspect the internal state of VMs in real-time.

### Features
- Process Monitoring: Listens to and logs all processes running inside a virtual machine.
- Anomaly Detection: Detects suspicious processes and alerts the user.
- Logging: Logs monitoring activities and detected anomalies.
- Alerting: Sends real-time alerts when suspicious activities are detected.
- Extensible Design: Easily extendable to include more complex detection algorithms, memory introspection, or network traffic analysis.

### Project Structure
```bash
vm_monitor/
│
├── __init__.py
├── config.py          # Configuration settings
├── monitor.py         # Main monitoring logic
├── vmi_interface.py   # LibVMI interface handling
├── logger.py          # Logging mechanism
├── detector.py        # Anomaly detection logic
├── alert.py           # Alerting system
└── main.py            # Entry point for the application
```

### Prerequisites
- Python 3.x
- LibVMI: Virtual Machine Introspection library for accessing the VM state.
- A Hypervisor: A virtual machine running on a hypervisor like Xen or KVM.

### Installation
#### 1. Install Dependencies
Before running the tool, you need to install the necessary dependencies.
##### On Ubuntu:
```bash
sudo apt-get install cmake libglib2.0-dev libjson-c-dev libyajl-dev
```

#### 2. Install LibVMI
```bash
# Clone the LibVMI repository
git clone https://github.com/libvmi/libvmi.git
cd libvmi

# Build and install
mkdir build
cd build
cmake ..
make
sudo make install
```

#### 3. Clone this Repo
```bash
git clone https://github.com/RohanTaneja2/VMI-Tool.git
cd VMI-Tool
```

#### 4. Install Python Dependencies
If additional Python packages are required (e.g., for advanced analysis or alerting), you can install them using pip:
```bash
pip install -r requirements.txt
```

### Usage
#### Config
###### Before running the tool, update the config.py file to match your environment:

- DOMAIN_NAME: The name of the virtual machine to monitor.
- LOG_FILE: The file where logs will be stored.
- ALERT_THRESHOLD: The threshold for triggering alerts based on detected anomalies.
- MONITOR_INTERVAL: The interval in seconds between each monitoring cycle.

##### Here is an Example of its usage:
```python
# config.py

class Config:
    DOMAIN_NAME = "example_vm"          # Replace with your VM's name
    LOG_FILE = "vm_monitor.log"         # Set the path to the log file
    ALERT_THRESHOLD = 5                 # Number of detected anomalies before an alert is triggered
    MONITOR_INTERVAL = 10               # Set the monitoring interval in seconds
```

#### Running the Tool
To start monitoring the virtual machine, run the following command:
```bash
python3 main.py
```

### Logs
Logs are stored in the file specified in config.py (default: vm_monitor.log). You can review these logs to analyze the monitoring activities and detected anomalies.

### Alerts
Alerts are printed to the console when suspicious activity is detected. You can extend the alert.py module to integrate with other alerting systems (e.g., email, SMS).

### Extending the Tool
- Process Whitelisting: Add a whitelist of known safe processes to ignore in the anomaly detection.
- Memory Introspection: Extend the VMI interface to inspect memory regions.
- Advanced Detection: Implement more sophisticated algorithms for detecting anomalies.

### Contributing & Contact 
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.
If you have any questions or need further assistance, feel free to open an issue or contact the project maintainer at rtaneja2020@gmail.com
