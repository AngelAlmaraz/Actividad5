import time
import os


def evaluate_forks(num):
    forks = []
    for n in num:
        forks.append(False) if n<=0 else forks.append(True)
    return forks

#Creamos una funcion para mostrar el pid de cada proceso
def print_pid():
    print("Child: ", os.getpid())

#Crearemos a un padre y a 10 hijos
parent = [1,1,1,1]
child1 = [0,1,1,1]
child2 = [1,0,1,1]
child3 = [0,0,1,1]
child4 = [1,1,0,1]
child5 = [0,1,0,1]
child6 = [1,0,0,1]
child7 = [0,0,0,1]
child8 = [1,1,1,0]
child9 = [0,1,1,0]
child10 =[1,0,1,0]

#Crearemos una lista vacia, en la que meteremos a los hijos 
children = []

children.append(child1)
children.append(child2)
children.append(child3)
children.append(child4)
children.append(child5)
children.append(child6)
children.append(child7)
children.append(child8)
children.append(child9)
children.append(child10)



n1 = os.fork()
time.sleep(1)
n2 = os.fork()
time.sleep(1)
n3 = os.fork()
time.sleep(1)
n4 = os.fork()
time.sleep(1)

forks = [n1,n2,n3,n4]

res = evaluate_forks(forks)


#iteramos la lista e imprimimos los pid de los hijos
for child in children:
    if res == child[0:len(forks)]:
        print_pid()
