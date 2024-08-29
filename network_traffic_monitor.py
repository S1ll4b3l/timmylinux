import psutil
import time
import sys
import termios
import tty
import select

def monitor_traffic(interval=1):
    old_value = psutil.net_io_counters().bytes_recv
    
    while True:
        if is_key_pressed():
            break

      
        new_value = psutil.net_io_counters().bytes_recv
        received = new_value - old_value
        print(f"Bytes received: {received}")
        old_value = new_value
        time.sleep(interval)

def is_key_pressed():
    dr, dw, de = select.select([sys.stdin], [], [], 0)
    if dr:
        char = sys.stdin.read(1)
        if char == 'q':
            return True
    return False

def main():
    print("Monitoring network traffic... Press 'q' to stop.\n")
    try:
        monitor_traffic()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin.fileno())
        main()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
