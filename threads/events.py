import threading


event = threading.Event()

#
# Cette fonction attends un evenement pour
# effectuer certaines actions

def myfunction():
    print("Waiting for event to trigger")
    event.wait()
    print("Event was triggered ! Performoing action XYZ now")


t = threading.Thread(target=myfunction)
t.start()


# Nous allons declencher un evenement
x = input(" Do you want to trigger the event ? (y/n)")
if x == "y":
    event.set()

