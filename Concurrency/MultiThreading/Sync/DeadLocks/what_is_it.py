import threading
import time

office_safety = threading.Lock()
counter_safety = threading.Lock()

# this is an example for the bad lock practices


'''

Here consider a unregistered and registered patient visits the hospital

For unregistered patient they have first visit the office (for registration) and the counter ( for vaccination)
but for the registered patient they have to visit the counter (for vaccination) and the office ( for updating themselves as vaccinated)

the locks office_safety and counter_safety doesn't allow patients to visit teh office and counter respectively if it's occupied


so when the unregistered patient visits the office and when the registered patient visits the counter, the

unregistered patient waits for the registered patient to his/ her work in the counter. The
and the registered patient waits for the unregistered patient to his/ her work at the office.
'''


def office(name, register=False):
    with office_safety:
        print(f'{name} has entered the office')
        
        if register:
            print(f"creating the new entry for {name}")
            
            time.sleep(3)

            print(f"{name} is waiting for the counter to be available")
            
            while counter_safety.locked():
                pass
            
        else:
            print(f"updating the Database for {name} as vaccinated")
        
        print(f"{name} has left the office")
        
        if register:
            counter(name)


def counter(name):
    with counter_safety:
        print(f"{name} has entered the counter")
        print(f"vaccinating {name}")
        
        time.sleep(6)
        
        print(f"{name} is waiting for the office to be available")
        
        while office_safety.locked():
            pass
        
        print(f"{name} has left the counter")


def hospital(name, registered=False):
    return counter(name) if registered else office(name, True)

unregistered_patient = threading.Thread(target=hospital, args=("Mr W", False))
registered_patient = threading.Thread(target=hospital, args=("Mr X", True))
unregistered_patient.start()
registered_patient.start()
