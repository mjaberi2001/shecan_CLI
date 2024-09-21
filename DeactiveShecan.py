import os
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def get_connected_interfaces():
    output = os.popen('ipconfig').readlines()
    connected_interfaces = []
    current_interface = None

    for line in output:
        line = line.strip()

        if "adapter" in line:
            current_interface = line.split("adapter ")[1].replace(":", "").strip()
        
        if "IPv4 Address" in line or "IPv4" in line:
            if current_interface and current_interface not in connected_interfaces:
                if "VMware" not in current_interface:
                    connected_interfaces.append(current_interface)

    return connected_interfaces

def remove_dns(interface):
    try:
        os.system(f'netsh interface ip set dns name="{interface}" dhcp')
        print(GREEN + f"DNS settings removed successfully for {interface}." + RESET)
    except Exception as e:
        print(RED+ f"Failed to remove DNS for {interface}: {e}" + RESET)

if __name__ == "__main__":
    connected_interfaces = get_connected_interfaces()
    if connected_interfaces:
        for interface in connected_interfaces:
            remove_dns(interface)  
    else:
        print(RED + "No active network interfaces found." +RESET)
