import socket
import threading
import concurrent.futures

print_lock = threading.Lock()
ip = input("Enter the IP to scan:")
def scan(ip,port):
    scanner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            print(f"{port} is open!!!")
    except:
        pass
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exe:
    for port in range(1000):
        exe.submit(scan,ip,port)
