import socket
import struct

MCAST_GRP = '224.1.1.2'
MCAST_PORT = 5007

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live for messages to 1 so they don't go past the local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send a message to the multicast group
message = 'Hello, multicast world!'
sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))