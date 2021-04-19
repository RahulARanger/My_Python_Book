import threading
import time
from socket import timeout

office_safety = threading.Lock()
counter_safety = threading.Lock()

# this is an example for the bad lock practices


'''

Here when the unregistered patient walks in then they go to db (locks save_db)
and meantime when the registered patient walks in he/ she goes to the counter for vaccination 
and they will have to go to the DB room which is locked since it's being occupied by the unregistered patient

'''


def office(name, register=False):
    global office_safety, office_safety
    
    office_safety.acquire(timeout=0.01)
    print(f'{name} has entered the office')
    if register:
        print(f"creating the new entry for {name}")
        time.sleep(3)

        print(f"waiting for the counter to be available")
        while counter_safety.locked():
            pass

    else:
        print(f"updating the Database for {name} as vaccinated")

    print(f"{name} has left the office")
    office_safety.release()


def counter(name):
    global office_safety, office_safety
    counter_safety.acquire()
    print(f"{name} has entered the counter")
    print(f"vaccinating {name}")
    time.sleep(6)
    print("waiting for the office to be available")
    while office_safety.locked():
        pass
    print(f"{name} has left the counter")
    counter_safety.release()


def hospital(name, registered=False):
    if registered:
        counter(name)
        office(name, False)
    else:
        office(name, True)
        counter(name)


unregistered_patient = threading.Thread(target=hospital, args=("Mr W", False))
registered_patient = threading.Thread(target=hospital, args=("Mr X", True))
unregistered_patient.start()
registered_patient.start()
