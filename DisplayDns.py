import os

def display_dns():
    output = os.popen('nslookup google.com').read()
    print("Current DNS settings:")
    print(output)

if __name__ == "__main__":
    display_dns()
