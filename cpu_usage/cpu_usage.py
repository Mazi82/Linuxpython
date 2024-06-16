#!/usr/bin/env python3

import os
import sys
import time
import psutil

def check_memory_usage(threshold_bytes):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem = proc.info['memory_info'].rss  # Resident Set Size
            if mem >= threshold_bytes:
                processes.append((proc.info['pid'], proc.info['name'], mem))
        except psutil.NoSuchProcess:
            continue
    return processes

def write_report(processes, report_file):
    with open(report_file, 'w') as f:
        for pid, name, mem in processes:
            f.write(f"{pid} {name} {mem}\n")

def alert():
    print('\a')  # This is will produce a sound

def main(threshold, interval):
    threshold_bytes = int(threshold[:-1]) * (1024 ** {'K': 1, 'M': 2, 'G': 3}[threshold[-1].upper()])
    interval_seconds = int(interval) * 60

    while True:
        processes = check_memory_usage(threshold_bytes)
        if processes:
            alert()
            write_report(processes, '/tmp/cpu_usage_rapport.txt')
        time.sleep(interval_seconds)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: cpu_usage.py <threshold> <interval>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
