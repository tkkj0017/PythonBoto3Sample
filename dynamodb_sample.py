import boto3
import  json
import time

TABLE = 'sample-table'

def create_json_file():
    # TODO
    return

def large_data_write():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE)
    with open('') as json:
        items = json.load(json)
        with table.batch_writer() as batch:
            start_time = time.perf_counter()
            for item in items:
                batch.put_item(Item=item)
            end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print("データ投入にかかった時間(秒): " + elapsed_time)