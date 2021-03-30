import threading
import time


# Example of how multithreading saves time

def generate_numbers(container, from_, to_):
    for number in range(from_, to_):
        container.append(number)


tank = []
checkpoint1 = time.time()

for batches in range(0, 10000, 100):
    batch = threading.Thread(target=generate_numbers, args=(tank, batches, batches + 100))
    batch.start()

checkpoint2 = time.time()
tank2 = []
generate_numbers(tank2, 0, 10000)
checkpoint3 = time.time()

print(f"Single Thread takes: {checkpoint2 - checkpoint1} and multithreading takes: {checkpoint3 - checkpoint2}")
