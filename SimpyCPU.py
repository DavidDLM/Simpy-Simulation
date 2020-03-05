#SimpySimulation
import simpy
import random
"""
New: Llega un proceso, espera que se le asigne RAM. Numero al
azar entre 1 y 10. Si hay memoria  disponible, puede pasar
al estado de ready. En caso contrario permanece en cola.

ready: el proceso esta listo para correr, pero espera a que lo
atienda el CPU. El proceso tiene un contador con las instrucciones
a realizar. Numero al azar entre 1 y 10. Cuando s e desocupa el
CPU puede pasar a utilizarlo.

running: El CPU atiende el proceso realizando 3 instrucciones. Al
completarse, el proceso se retira del CPU. Si faltan realizar menos
de 3 instrucciones, el CPU se libera. Si no, se realiza de nuevo
el proceso.
    * Si quedan 0 instrucciones: estado "terminated"
    * Waiting: se genera un numero entre 1 y 2. Si es 1, el proceso
    pasa a la cola de waiting y despues a la cola de ready.
    * Ready: Si el numero es 2, pasa automaticamente a la cola
    ready.
    
    - Numeros generados con random.expovariate(1.0 / interval)
    - RAM: RAM = simpy.Container(env, init = 100, capacity = 100)
        RAM.get(memoria), RAM.put(memoria) memoria: requerida
        para RAM.
        
"""

ready = False
random_seed = 10
instrucciones_maximas = [1, 10]
ram_maximo = [1, 10]

#env : environment
#available_ram: ram disponible (1,10)
#num_instrucciones: numero de instrucciones (1,10)
#duration: duracion de las instrucciones  en ser procesadas (max 3)

def main():
    env = simpy.Environment()
    env.process(procesar_instrucciones(env))
    env.run(until=1)
    print("Simulacion completa")
    

def procesar_instrucciones(env):
    while True:
        MAX_RAM = simpy.Container(env, init=100, capacity=100)
        
        used_ram1 = random.randint(1,10)
        max_instructions1 = random.randint(1,10)
        
        used_ram2 = random.randint(1,10)
        max_instructions2 = random.randint(1,10)
        
        used_ram3 = random.randint(1,10)
        max_instructions3 = random.randint(1,10)
        
        #Instruccion1
        print("Un proceso de "+str(max_instructions1)+" instrucciones procesada en t = " +str(env.now)+". Requiere "+str(used_ram1)+" de la RAM")
        if (max_instructions1 < 4):
            print("Se ejecutaran las instrucciones a un costo de " + str(used_ram1)+" de RAM. Esperando a que el CPU las pase a un estado READY")
            
            if(used_ram1 < 100):
                ready =True
                MAX_RAM.put(used_ram1)
                print("Proceso en estado READY ya que hay RAM suficiente para ejecutarlo.")
                if(ready == True):
                    yield env.timeout(1)
            
        elif (max_instructions1 >= 4):
            print("Se ejecutaran solamente 3 instrucciones de "+str(max_instructions1)+" a un costo de " + str(used_ram1)+" de RAM. "+str(100-used_ram1)+" de RAM disponibles")
            
            if(max_instructions1-3 >= 3):
                print("Instrucciones restantes pasando a la cola Waiting. Instrucciones restantes pasando al estado READY.")
                print("Quedan "+str(max_instructions1-3)+" instrucciones por realizar. Ocuparan "+str(used_ram2)+" de RAM para ser ejecutadas.")
                MAX_RAM.put(used_ram2)
                if(used_ram1+used_ram2 < 100):
                    print("Proceso en estado READY ya que hay RAM suficiente para ejecutarlo.")
                    if(max_instructions1-3-3 < 3):
                        print("Quedan "+str(max_instructions1-3-3)+" instrucciones por realizar. Ocuparan "+str(used_ram3)+" de RAM para ser ejecutadas. " +str(100-used_ram1-used_ram2)+" de RAM disponibles")
                        MAX_RAM.put(used_ram3)
                        if(max_instructions1-3-3-3>3):
                            yield env.timeout(1)
                            print("Quedan "+str(max_instructions1-3-3-3)+" instrucciones por realizar. Ocuparan "+str(used_ram3)+" de RAM para ser ejecutadas. "+str(100-used_ram1-used_ram2)+" de RAM disponibles")
                        else:
                            print("Liberando CPU")
                            yield env.timeout(1)
                    else:
                        print("Liberando CPU")
                        yield env.timeout(1)
                else:
                    print("RAM llena.")
                
                
                
                
                
            elif(max_instructions1-3 < 3):
                print("Liberando CPU")
            
            if(used_ram1 < 100):
                ready =True
                MAX_RAM.put(used_ram1)
                print("Proceso en estado READY ya que hay RAM suficiente para ejecutar las instrucciones." )
                
                if(ready == True):
                    yield env.timeout(1)
                    
        #Instrucciones restantes
       
        
                
            
            
        """
        #Instruccion2
        print("Otro proceso de "+str(max_instructions2)+" instrucciones procesada en t = " +str(env.now)+". Requiere "+str(used_ram2)+" de la RAM")
        if (max_instructions2 < 4 and  used_ram2 < 10-used_ram1):
            yield env.timeout(1)
            print("Se ejecutaron las instrucciones a un costo de " + str(used_ram2)+" de RAM")
        elif (max_instructions2 >= 4):
            print("Se ejecutaron solamente 3 instrucciones de "+str(max_instructions2)+" a un costo de " + str(used_ram2)+" de RAM")
        elif(used_ram2 > 10-used_ram1):
            print("***No hay suficiente RAM para  ejecutar el proceso con instrucciones***")
            
        #Instruccion3   
        print("Otro proceso de "+str(max_instructions3)+" instrucciones procesada en t = " +str(env.now)+". Requiere "+str(used_ram3)+" de la RAM")
        if (max_instructions3 < 4 and  used_ram3 < 10-used_ram1-used_ram2):
            yield env.timeout(1)
            print("Se ejecutaron las instrucciones a un costo de " + str(used_ram3)+" de RAM")
        elif (max_instructions3 >= 4):
            print("Se ejecutaron solamente 3 instrucciones de "+str(max_instructions3)+" a un costo de " + str(used_ram3)+" de RAM")
        elif(used_ram3 > 10-used_ram1-used_ram2):
            print("***No hay suficiente RAM para  ejecutar el proceso con instrucciones***")
        """
if __name__ == "__main__":
    main()
