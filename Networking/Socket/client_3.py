from multiprocessing.connection import Client
import socket

client = Client((socket.gethostname(), 6969))
client.send(True)
client.send(False)
client.send("hello there\nand here goes")
client.close()
