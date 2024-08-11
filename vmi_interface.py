import libvmi
from libvmi import Libvmi, VMIException

class VMIInterface:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.vmi = None

    def initialize(self):
        try:
            self.vmi = Libvmi(self.domain_name)
            print(f"Connected to VM: {self.domain_name}")
        except VMIException as e:
            print(f"Failed to connect to VM {self.domain_name}: {e}")
            return False
        return True

    def list_processes(self):
        if self.vmi:
            try:
                return self.vmi.list_processes()
            except VMIException as e:
                print(f"Error listing processes: {e}")
        return []

    def close(self):
        if self.vmi:
            self.vmi.close()
