import boto3
import json
import random

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

num_records = 100 
base=80

def insert(line):
    #kinesis_client = boto3.client('kinesis', region_name='us-east-1')
    response = kinesis_client.put_record(
        StreamName='Parcial3',  
        Data=line,
        PartitionKey=partition_key
    )
    return(response['ShardId'])
    

for i in range(num_records):
    
    record = {
        'id': f'{random.randint(1, 2)}',
        'price': base+random.randint(-2, 2)
    }
    base=record['price']

    data_string = json.dumps(record)
    partition_key = record['id']
    insert(data_string)
    print("Inserción:",data_string)