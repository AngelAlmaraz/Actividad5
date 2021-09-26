#En multiprocessing se aceptan dos tipos de canales de comunicacion, que son las queues y los pipes.
#Las queues son process y thread safe,mientras que con las ppipes puede haber problemas si es que dos 
#procesos intentan escribir en un mismo sitio al mismo tiempo. 


class MyClasesita(object):
    def __init__(self,name):
        self.name = name

    def nombraProceso(self):
        nombre_proceso = current_process().name
        print(f"Este es el proceso", nombre_proceso , " dedicado a ", self.name)

def trabajo(q):
    obj = q.get()
    obj.nombraProceso()

if __name__ == '__main__':
    #Crearemos un proceso p, al cual por medio de una queue le pasaremos una instancia de mi Clasesita, de nombre Carlitos
    q = Queue()
    p = Process(target=trabajo, args=(q,))
    p.start()

    q.put(MyClasesita("Carlitos"))

    #Esperamos a que el trabajo termine
    q.close()
    q.join_thread()
    p.join()
