import threading

def function():
    for i in range(50):
        print("Hello world!")

t1 = threading.Thread(target=function)
t1.start()

# with join the main thread will wait until thread 1 is finish
t1.join()

print("Another Text")