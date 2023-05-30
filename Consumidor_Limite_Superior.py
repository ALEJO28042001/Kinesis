import boto3
import json

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

stream_name = 'Parcial3'  
shard_iterator_type = 'TRIM_HORIZON'  

response = kinesis_client.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType=shard_iterator_type
)['ShardIterator']

record_limit = 200  

response = kinesis_client.get_records(
    ShardIterator=shard_iterator,
    Limit=record_limit
)

records = response['Records']

#Franja Superior
procesados=[]
accion_1=[]
accion_2=[]
Bollingener_1=0
Bollingener_2=0


# Cargar los datos desde el archivo JSON
for record in records:
    data = json.loads(record['Data'])
    if data['id']=='1':
        accion_1.append((data['price']))
    if data['id']=='2':
        accion_2.append((data['price']))

period=10
sma=[]
std=[]

for i in range(period, len(accion_1)):
    period_prices = accion_1[i-period:i]
    sma.append(sum(period_prices) / period)
    std.append((sum((price - sma[-1]) ** 2 for price in period_prices) / period) ** 0.5)

upper_band = [sma[i] + 2 * std[i] for i in range(len(sma))]

def comprobacion_clasificacion(i):
    if i == 1:
        return len(accion_1)
    if i == 2:
        return len(accion_2)
    return -1

# Iterar sobre los datos y mostrar una alerta cuando el precio supere la franja superior
for i in range(len(accion_1)):
    if accion_1[i] > upper_band[i-period]:
        print(f'¡Alerta! El precio de la acción 1 en el punto {i} supera la franja superior de Bollinger.')

period=10
sma=[]
std=[]

for i in range(period, len(accion_2)):
    period_prices = accion_1[i-period:i]
    sma.append(sum(period_prices) / period)
    std.append((sum((price - sma[-1]) ** 2 for price in period_prices) / period) ** 0.5)

upper_band = [sma[i] + 2 * std[i] for i in range(len(sma))]

# Iterar sobre los datos y mostrar una alerta cuando el precio supere la franja superior
for i in range(len(accion_2)):
    if accion_2[i] > upper_band[i-period]:
        print(f'¡Alerta! El precio de la acción 2 en el punto {i} supera la franja superior de Bollinger.')