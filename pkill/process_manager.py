import os
import subprocess

def get_processes_by_name(name):
    processes = []
    try:
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.splitlines()
        for line in lines[1:]:
            if name in line:
                parts = line.split(None, 10)
                pid = int(parts[1])
                processes.append((pid, line))
    except Exception as e:
        print(f"Error: {e}")
    return processes

def kill_process_by_pid(pid):
    try:
        os.kill(pid, 9)
        print(f"Process {pid} has been killed.")
    except Exception as e:
        print(f"Error: {e}")

