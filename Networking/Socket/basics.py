import socket

sample = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # use ipv4 address and tcp protocol
# sample = socket.socker(socket.AF_INET6, socket.SOCK_DGRAM)  # use ipv6 address and udp protocol
sample.connect(("www.python.org", 80))
# after this socket is destroyed
