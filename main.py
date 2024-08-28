import os
import subprocess

def print_logo():
    print("""
      █████████╗██╗███╗   ███╗███╗   ███╗██╗   ██╗
       ╚══██╔══╝██║████╗ ████║████╗ ████║╚██╗ ██╔╝
          ██║   ██║██╔████╔██║██╔████╔██║ ╚████╔╝ 
          ██║   ██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝  
          ██║   ██║██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║   
          ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝   

       """)
    print("Hello, it's Timmy here!\n")


def print_menu():
    print("What do you want?")
    print("1. Port Scanner")
    print("2. Network Traffic Monitor")
    print("3. Network Scanner")
    print("4. Exit")

def run_tool(option):
    if option == '1':
        subprocess.run(['python', 'port_scanner.py'])
    elif option == '2':
        process = subprocess.Popen(['python', 'network_traffic_monitor.py'])
        print("Press 'q' and Enter to stop monitoring...")
        process.wait() 
        print("Monitoring stopped. Returning to main menu...")
    elif option == '3':
        subprocess.run(['python', 'network_scanner.py'])
    elif option == '4':
        print("Exiting Timmy. Goodbye!")
        exit()
    else:
        print("Invalid option! Please try again.\n")

def main():
    while True:
        os.system('cls')  
        print_logo()
        print_menu()
        choice = input("\nEnter your choice: ")
        run_tool(choice)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
