import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def main():
    try:
        target_ip = input("Enter the target IP: ")
        port_range = input("Enter the port range (e.g., 1-100): ")
        start_port, end_port = map(int, port_range.split('-'))
        
        open_ports = scan_ports(target_ip, start_port, end_port)
        
        if open_ports:
            print(f"Open ports on {target_ip}:")
            for port in open_ports:
                print(f"Port {port}")
        else:
            print(f"No open ports found on {target_ip}.")
    except ValueError:
        print("Failed to complete task. Please ensure you input the port range in the format 'start-end' (e.g., 1-100).")

if __name__ == "__main__":
    main()
