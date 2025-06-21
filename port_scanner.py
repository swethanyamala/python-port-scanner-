import socket
from datetime import datetime

target = "google.com"

print("-" * 50)
print("Scanning Target: " + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Could not connect to server.")