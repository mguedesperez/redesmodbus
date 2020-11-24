from pyModbusTCP.server import ModbusServer
from pyModbusTCP.client import ModbusClient
from datetime import datetime

server = ModbusServer("127.0.0.1", 12345, no_block=True)
aclient = ModbusClient(host="127.0.0.1", port=12345)

try:
    print("Iniciando server..")
    server.start()
    print("Server online")
    aclient.open()
    
    while True:
    
        aclient.write_single_register(0,int(datetime.now().time().strftime("%S")))
    
        continue
except:
    print("Desligando server....")
    aclient.close()
    server.stop()
    print("Server desligado")