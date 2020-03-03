import tkinter
import threading
import time
def a ():
    janela=tkinter.Tk()
    janela.mainloop()

def b ():
    print('Ola')

def c ():
    for i in (range(0,9)):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target = a)
t2 = threading.Thread(target = b)
t3 = threading.Thread(target = c)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()