import subprocess
import platform

os_name = platform.system()

print("\n Welcome to the Live Network Scanner \n")
print(f" Detected Platform: {os_name}")

def specific_ping_windows(host):
    result = subprocess.run(["ping", "-n", "4", "-w", "200", host], capture_output=True, text=True)
    print("Exit Code:", result.returncode)
    print("STDOUT:", result.stdout)
    if result.returncode == 0:
        print(f"[+] {host} is Reachable")
    else:
        print(f"[-] {host} is Unreachable")

def specific_ping_linux(host):
    result = subprocess.run(["ping", "-c", "4", "-W", "1", host], capture_output=True, text=True)
    print("Exit Code:", result.returncode)
    print("STDOUT:", result.stdout)
    if result.returncode == 0:
        print(f"[+] {host} is Reachable")
    else:
        print(f"[-] {host} is Unreachable")

def ping_range_windows(ip_base):
    first_ip = int(input("Your First IP (last octet): "))
    last_ip = int(input("Your Last IP (last octet): "))
    for i in range(first_ip, last_ip + 1):
        ip = f"{ip_base}.{i}"
        result = subprocess.run(["ping", "-n", "1", "-w", "200", ip], capture_output=True, text=True)
        if "TTL=" in result.stdout:
            print(f"[+] {ip} is alive")
        else:
            print(f"[-] {ip} is dead")

def ping_range_linux(ip_base):
    first_ip = int(input("Your First IP (last octet): "))
    last_ip = int(input("Your Last IP (last octet): "))
    for i in range(first_ip, last_ip + 1):
        ip = f"{ip_base}.{i}"
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], capture_output=True, text=True)
        if "ttl=" in result.stdout.lower():
            print(f"[+] {ip} is alive")
        else:
            print(f"[-] {ip} is dead")


while True:
    print('''
        Choose Your Platform:
        1. Linux
        2. Windows
    ''')
    user_platform = int(input("Selected platform is (1/2): "))

    print('''
        Choose Scan Mode:
        1. Scan a Range of IPs
        2. Ping a Specific IP
    ''')
    user_mode = int(input("Selected mode is (1/2): "))

    if user_mode == 1:
        ip_base = input("Enter the base IP (example: 192.168.1): ")
        if user_platform == 1:
            ping_range_linux(ip_base)
        elif user_platform == 2:
            ping_range_windows(ip_base)
        else:
            print("Invalid platform selected!")

    elif user_mode == 2:
        ip = input("Enter the IP address to ping: ")
        if user_platform == 1:
            specific_ping_linux(ip)
        elif user_platform == 2:
            specific_ping_windows(ip)
        else:
            print("Invalid platform selected!")

    else:
        print("Invalid mode selected!")
    
    print('''
          Do you want to Exit: 
          1. Yes    2. No \n''')    
    try:
        restart = input("Which one (Y|N): ").lower()
        if restart != "n":
            break
        else:
            continue
    except Exception as e:
        print("SomeThing is wrong....!!!!", e)




