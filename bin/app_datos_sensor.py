import os
import time
import requests
import threading


def DataSensor():
    DateStar="2023-08-01T08:00:00"
    DateEnd="2023-08-01T08:23:59"

    url= os.getenv('GetVehicles')#GURADAMOS LA URL DONDE ESTAS¿N LOS DATOS DEL VEHICULO
    token={"token": os.getenv('Token')}#EL TOKEN
    try:
            PlacasAutos= requests.post(url,json=token)
            if PlacasAutos.status_code==200:
                     Placas=PlacasAutos.json()
                     for Placa_X in Placas:#Recorremos Todas las Placas
                         print(Placa_X["plate"])
                         Vehiculo=str(Placa_X["plate"])                  
                         url=os.getenv('GetRoute')
                         token={"token": os.getenv('TOKEN'), "plate": Vehiculo,"fromDate": DateStar, "toDate": DateEnd}
                         DatosAuto= requests.post(url,json=token)
                         if(DatosAuto.status_code==200):
                             DatosAuto=DatosAuto.json()
                             if(len(DatosAuto)!=0):
                                 for sensor in DatosAuto[0]["sensors"]:
                                     print("Sensor Activado "+str(sensor["idIo"])+"  | Valor "+str(sensor["val"])+"  | Hora del Error "+str(sensor["timestamp"]["Date"])+"  | CordenadaX "+str(sensor["location"]["coordinates"][0])+"  | CordenadaY "+str(sensor["location"]["coordinates"][1]))
                             else:
                                     print("Sin Sensores")
                         else:
                             print("Error al encontrar Auto")
                     print("----------")
            
    except Exception as err:
         print(err)

#CRITERIO DE ARRANQUE: SE REGULA SEGÚN A CLIENTE
def timer(timer_runs):  
    while timer_runs.is_set():              
             try: 
                 DataSensor()                             
             except Exception as error: 
                 print (error)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
             time.sleep(10)   #ACA SE REGULA EL TIEMPO DE EJECUCION DEL BOT     
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#Arrancamos el Sustema Cada Minuntos Despues de Realizar Cada Caso  
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,)) 
t.start()





