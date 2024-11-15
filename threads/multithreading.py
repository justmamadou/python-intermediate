import threading

def function1():
    for i in range(10000):
        print("Function1")
def function2():
    for i in range(10000):
        print("Function2")

t1= threading.Thread(target=function1)
t2=threading.Thread(target=function2)

t1.start()
t2.start()