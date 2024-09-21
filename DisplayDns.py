import os

def get_active_dns():
    output = os.popen('ipconfig /all').readlines()

    current_interface = None
    dns_servers = {}  

    print("Current DNS settings for active network interfaces:\n")

    for i, line in enumerate(output):
        line = line.strip()

        if "adapter" in line.lower():
            current_interface = line.strip()
        
        if "DNS Servers" in line:
            dns_list = []
            for j in range(i+1, len(output)):
                next_line = output[j].strip()
                if not next_line or not next_line[0].isdigit(): 
                    break
                dns_list.append(next_line)
            if dns_list:
                dns_servers[current_interface] = dns_list

    if dns_servers:
        for interface, dns in dns_servers.items():
            print(f"{interface}: {', '.join(dns)}")
    else:
        print("No active DNS settings found.")

if __name__ == "__main__":
    get_active_dns()
