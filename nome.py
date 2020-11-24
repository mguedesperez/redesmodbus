from pyModbusTCP.server import ModbusServer

server = ModbusServer("127.0.0.1", 12345, no_block=True)

try:
    print("Iniciando server..")
    server.start()
    print("Server online")
    while True:
        continue
except:
    print("Desligando server....")
    server.stop()
    print("Server desligado")