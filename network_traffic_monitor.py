import psutil
import time
import threading
import sys
import msvcrt  # Khusus untuk Windows

def monitor_traffic(interval=1):
    old_value = psutil.net_io_counters().bytes_recv
    while True:
        if msvcrt.kbhit() and msvcrt.getch().decode('utf-8') == 'q':
            break
        new_value = psutil.net_io_counters().bytes_recv
        received = new_value - old_value
        print(f"Bytes received: {received}")
        old_value = new_value
        time.sleep(interval)

def main():
    print("Monitoring network traffic...\n")
    try:
        monitor_traffic()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
