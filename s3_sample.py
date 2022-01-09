"""
created at: 2021-01-09
Boto3(S3)のサンプルコード
"""


import pprint
import boto3
from botocore.exceptions import ClientError
import json


# S3と接続(ClientAPIとResourceAPI)
CLIENT = boto3.client('s3')
RESOURCE = boto3.resource('s3')
BUCKET_NAME = '%BUCKET_NAME%'
OBJECT_KEY = '%OBJECT_KEY%'


# 特定のファイル(オブジェクト)の詳細情報を取得
def get_file_detail(bucket_name = '', path = ''):
    # Resource API
    bucket = RESOURCE.Bucket(BUCKET_NAME)
    object = bucket.Object(OBJECT_KEY)
    response = object.get()['Body']
    pprint.pprint(json.loads(response.read().decode('utf-8')))

    # Client API
    # response = CLIENT.get_object(
    #     Bucket = BUCKET_NAME,
    #     Key = OBJECT_KEY
    # )
    # body = response['Body'].read()
    # # json.dumps(response)
    # pprint.pprint(response)


# 特定のフォルダのファイル一覧を返す
def get_file_list_by_folder_name():
    return


get_file_detail()