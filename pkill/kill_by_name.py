import argparse
from process_manager import get_processes_by_name, kill_process_by_pid

def main():
    parser = argparse.ArgumentParser(description='Kill processes by name.')
    parser.add_argument('name', help='Name of the process to kill')
    parser.add_argument('-i', '--info', action='store_true', help='Show process information')
    args = parser.parse_args()

    processes = get_processes_by_name(args.name)

    if not processes:
        print(f"No processes found with name {args.name}.")
        return

    if args.info:
        for pid, line in processes:
            print(line)
        return

    if len(processes) == 1:
        kill_process_by_pid(processes[0][0])
    else:
        print("Multiple processes found:")
        for pid, line in processes:
            print(line)
        
        choice = input("Enter the PID of the process to kill or 'all' to kill all processes: ")
        
        if choice.lower() == 'all':
            for pid, _ in processes:
                kill_process_by_pid(pid)
        else:
            try:
                pid = int(choice)
                kill_process_by_pid(pid)
            except ValueError:
                print("Invalid input.")

if __name__ == '__main__':
    main()
