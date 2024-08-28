from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def main():
    target_ip = input("Enter the target IP range (e.g., 192.168.1.0/24): ")
    devices = scan_network(target_ip)

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    print("-"*40)

    for device in devices:
        print(f"{device['ip']:16}    {device['mac']:20}")

if __name__ == "__main__":
    main()
