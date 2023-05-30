from producer1 import insert as insert1
from producer2 import insert as insert2
import json

def test_conection():
    assert insert1(json.dumps({"id": "2", "price": 88})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "1", "price": 87})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 73})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 72})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 70})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 68})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "1", "price": 67})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 67})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 69})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 68})) == 'shardId-000000000000'
    assert insert1(json.dumps({"id": "2", "price": 66})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 88})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "1", "price": 87})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 73})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 72})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 70})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 68})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "1", "price": 67})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 67})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 69})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 68})) == 'shardId-000000000000'
    assert insert2(json.dumps({"id": "2", "price": 66})) == 'shardId-000000000000'
    