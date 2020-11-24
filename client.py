from pyModbusTCP.client import ModbusClient

client = ModbusClient(host="127.0.0.1", port=12345)
client.open()