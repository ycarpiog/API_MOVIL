import os
import time
import requests
import datetime
import threading
import pandas as pd
import json
global TimeEndSave
utc_time = datetime.datetime.utcnow()
TimeEndSave=utc_time.strftime('%Y-%m-%dT%H:%M:%S')
my_dict={"Fecha": TimeEndSave }
with open('data.json', 'w') as fp:
    json.dump(my_dict, fp)    
    
def DataSensor():
    with open('data.json', 'r') as fp:
         data = json.load(fp) 
    utc_time = datetime.datetime.utcnow()
    DateStar=utc_time.strftime('%Y-%m-%dT%H:%M:%S')    
    DateEnd=data["Fecha"]
    try:    
            print("Hora de Inicio="+str(DateEnd)+" | Hota Final="+str(DateStar))       
            with open('data.json', 'w') as fp:
                  my_dict={"Fecha": DateStar }                
                  json.dump(my_dict, fp)  
    except Exception as err:
         print(err)
    

#CRITERIO DE ARRANQUE: SE REGULA SEGÚN A CLIENTE
def timer(timer_runs):  
    while timer_runs.is_set():              
             try: 
                 result=DataSensor()
                 print(result)                  
             except Exception as error: 
                 print (error)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
             time.sleep(60)   #ACA SE REGULA EL TIEMPO DE EJECUCION DEL BOT     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#Arrancamos el Sustema Cada Minuntos Despues de Realizar Cada Caso  
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,)) 
t.start()


