import threading
import time

office_safety = threading.Lock()
counter_safety = threading.Lock()

'''
as u can say we have to modify some parts in order to use this timeout solution

but this doesn't solve the actual problem since the unregistered patient meets the registered patient in the counter

which is not good 
'''

def office(name, register=False):
    if not office_safety.acquire(timeout=0.04):  
        print(f"{name} waiting for the office to be available")
    
    print(f'{name} has entered the office')
    
    if register:
        print(f"creating the new entry for {name}")
        time.sleep(3)

        counter(name)
    else:
        print(f"updating the Database for {name} as vaccinated")

    print(f"{name} has left the office")
    
    if office_safety.locked():
        office_safety.release()


def counter(name):
    if not counter_safety.acquire(timeout=0.07):  # waits until the patient gets vaccinated
        print(f"{name} is waiting for the office to be available")
        
    print(f"{name} has entered the counter")
    print(f"vaccinating {name}")
    
    time.sleep(6)
    
    print(f"{name} has left the counter")
    
    if counter_safety.locked():
        counter_safety.release()
        
    office(name, False)


def hospital(name, registered=False):
    if registered:
        counter(name)
    else:
        office(name, True)

unregistered_patient = threading.Thread(target=hospital, args=("Mr W", False))
registered_patient = threading.Thread(target=hospital, args=("Mr X", True))
unregistered_patient.start()
registered_patient.start()
