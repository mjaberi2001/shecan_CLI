import os
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def get_active_interface():
    output = os.popen('ipconfig').readlines()

    connected_interface =[]
    current_interface = None


    for line in output:
        line = line.strip();

        if "adapter" in line:
            current_interface = line.split("adapter ")[1].replace(":","").strip()


        if "IPv4 Address" in line or "IPv4" in line:
            if current_interface and "VMware" not in current_interface and current_interface not in connected_interface:
                connected_interface.append(current_interface)
    
    return connected_interface

def set_dns(interface,dns1,dns2):
    try:
        os.system(f'netsh interface ip set dns name="{interface}" static {dns1}')
        os.system(f'netsh interface ip add dns name="{interface}" {dns2} index=2')
        print(GREEN + f"DNS settings updated successfully for {interface}." + RESET)
    except Exception as e:
        print(RED + f"Failed to set DNS: {e}"+ RESET)



if __name__ == "__main__":
    interface = get_active_interface()
    if interface:
        primary_dns = "8.8.8.8"
        secondary_dns = "8.8.4.4"
        for intf in interface:
            set_dns(intf,primary_dns,secondary_dns)
    else:
        print(RED + "No active netwrk interface found" + RESET)