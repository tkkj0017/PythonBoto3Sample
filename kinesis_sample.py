import pprint
import boto3

def get_data_all_shards():
    kinesis = boto3.client('kinesis')
    stream_name = "%stream_name%"
    limit = 100

    shards = kinesis.list_shards(
        StreamName=stream_name
    )

    data = []
    for shard in shards['Shards']:
        shard_id = shard['ShardId']
        iterator = kinesis.get_shard_iterator(
            StreamName=stream_name,
            ShardId=shard_id,
            ShardIteratorType='TRIM_HORIZON'
        )
        # pprint.pprint(iterator)
        response = kinesis.get_records(
            ShardIterator=str(iterator['ShardIterator']),
            Limit=limit
        )
        pprint.pprint(response)
        data.append(response['Records'])
    pprint.pprint(data)

def get_record_by_shard_id():
    shard_id = 'shardId-000000000000'
    iterator = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='TRIM_HORIZON'
    )
    # pprint.pprint(iterator)
    response = kinesis.get_records(
        ShardIterator=str(iterator['ShardIterator']),
        Limit=limit
    )
    pprint.pprint(response)

def put_data():
    kinesis = boto3.client('kinesis')
    stream_name = "%stream_name%"
    data = 'data'
    partition_key = '2'

    response = kinesis.put_records(
        Records=[
            {
                'Data': data,
                'PartitionKey': partition_key
            }
        ],
        StreamName = stream_name
    )
    pprint.pprint(response)
