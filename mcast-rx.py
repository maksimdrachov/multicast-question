import socket
import struct

MCAST_GRP = "224.1.1.1"
MCAST_PORT = 5007
SETUP_WITH_ANY = True
RECEIVE_LOOP = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if SETUP_WITH_ANY:
    sock.bind(("", MCAST_PORT)) # in linux: sock.bind((MCAST_GRP, MCAST_PORT)) works
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    print(f"mreq: {mreq}")
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
else:
    INTERFACE = "0.0.0.0"
    sock.bind((INTERFACE, MCAST_PORT))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(INTERFACE))


# Retrieve the membership information for the socket
# This works in linux, but not in windows
local_addr, local_port = sock.getsockname()
print(f"local Address: {local_addr}") # 0.0.0.0 in windows, MCAST_GRP in linux
print(f"Local Port: {local_port}")
# Reaching the membership information for the socket throught is not possible using getsocopt:
# https://tldp.org/HOWTO/Multicast-HOWTO-6.html
# print(f"socket: {sock.getsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP)}")

while RECEIVE_LOOP:
    print(sock.recv(10240))