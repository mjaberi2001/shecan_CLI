import psutil
import time

def monitor_network_traffic():
    old_value = psutil.net_io_counters()
    print("Monitoring network traffic... (Press Ctrl+C to stop)")
    try:
        while True:
            time.sleep(1)  
            new_value = psutil.net_io_counters()

            sent = new_value.bytes_sent - old_value.bytes_sent
            received = new_value.bytes_recv - old_value.bytes_recv

            print(f"Sent: {sent / 1024:.2f} KB | Received: {received / 1024:.2f} KB")

            old_value = new_value
    except KeyboardInterrupt:
        print("\nExiting network traffic monitor.")

if __name__ == "__main__":
    monitor_network_traffic()
