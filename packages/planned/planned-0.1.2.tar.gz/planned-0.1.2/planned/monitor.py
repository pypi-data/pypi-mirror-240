import subprocess
import time


class TargetMonitor:
    def __init__(self, command):
        self.command = command

    def is_process_running(self):
        try:
            output = subprocess.check_output(
                self.command, stderr=subprocess.STDOUT
            ).decode("utf-8")
            return output != ""
        except subprocess.CalledProcessError as e:
            # pgrepが0以外の終了コードで終了した場合（つまりプロセスが見つからなかった場合）
            return e.returncode != 1


class MonitorContent:
    def __init__(self, monitor):
        self.monitor = monitor

    def wait_for_process_end(self):
        while True:
            if not self.monitor.is_process_running():
                print("The monitored process has ended.")
                return True
            time.sleep(1)


class PostProcessAction:
    def __init__(self, action):
        self.action = action

    def execute(self):
        print("Executing post-process action...")
        self.action()


class Planned:
    def __init__(self, command, action):
        self.target_monitor = TargetMonitor(command)
        self.monitor_content = MonitorContent(self.target_monitor)
        self.post_process_action = PostProcessAction(action)

    def run_monitoring(self):
        if self.monitor_content.wait_for_process_end():
            self.post_process_action.execute()
