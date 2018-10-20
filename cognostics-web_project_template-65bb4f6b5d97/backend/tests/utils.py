import subprocess


class ServerProcess:
    def __init__(self):
        self.p = subprocess.Popen(["python3", "run.py"])

    def terminate(self):
        self.p.terminate()
