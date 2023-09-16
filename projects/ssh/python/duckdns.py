import urllib.request
import socket

domain = ""
token = ""
privateip = "?"

# Create a socket and connect to a remote server (e.g., Google's DNS server)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.4.4", 80))
privateip = s.getsockname()[0]
print(privateip)


print(privateip)

req = urllib.request.Request(f'https://www.duckdns.org/update?domains={domain}&token={token}&ip={privateip}')
content = urllib.request.urlopen(req).read()
print(content.decode('utf-8'))

