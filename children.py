from multiprocessing import Process
import os

#Creamos una funcion de info para ver el pid de los procesos hijos
def info():
    print("Child, pid = ", os.getpid())

if __name__ == '__main__':
    #Imprimimos el pid del padre
    print("Padre, pid = ",os.getpid())
    
    #Creamos 10 procesos hijos, e impromimos su pid con la funcion info()
    for i in range(10):
        p = Process(target=info, args=())
        p.start()
        p.join()
