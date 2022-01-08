"""
created at: 2021-01-08

Boto3のサンプルコード
"""


import pprint
import boto3
import sys
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')


def s3_list_objects():
    # バケットオブジェクトの一覧を取得する
    response = s3.list_objects_v2(
        Bucket="takeya-s3-sample"
    )
    # pprint.pprint(response)
    for r in response["Contents"]:
        k = r["Key"]
        print(k)


# Paginator
# データ量が大量(数万以上)の場合に条件に合う最初の1000件を返す
def paginater(bucket, prefix):
    paginater = s3.get_paginator("list_objects_v2")
    response_iterator = paginater.paginate(Bucket=bucket, Prefix=prefix)
    results = []
    for response in response_iterator:
        for x in response["Contents"]:
            results.append(x["Key"])

    pprint.pprint(results)
    return results


# Waiter
# 処理を完了してから次の処理を進めたい場合に便利
# ex) EC2インスタンスを起動し起動が完了するまで待つ
def waiter():
    ec2 = boto3.client("ec2")

    response = ec2.start_instamces(InstamceIds=["%インスタンスID%"])
    waiter = ec2.get_waiter('instance_status_ok')
    wait_response = waiter.wait(InstanceIds=["%インスタンスID%"])
    pprint.pprint(wait_response)
    return wait_response


# Session
# AWSへの接続に必要な「認証などの情報を設定する時に使う
# sessionよりも環境変数で指定する方がおすすめ
def session():
    session = boto3.session.Session(region_name="us-west-2")
    s3 = session.client("s3")


# Response Error
def response_error(key):
    response = s3.delete_objects(
        Bucket="my-bucket",
        Delete={"Objects": [{"key": key}]}
    )

    # エラーの確認
    if len(response["Errors"]) > 0:
        for err in response["Errors"]:
            # エラー情報を標準エラー出力に出す
            print(err, file=sys.stderr)


# Exception Error
# 例外を調べる→https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html
def exception_error():
    try:
        response = s3.create_bucket(Bucket="test")
    # Boto3で定義されている例外のキャッチ
    except s3.exceptions.BucketAlreadyExists as e:
        print(e)
    # AWS REST APIドキュメントで定義された例外のキャッチ
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print(e)
        else:
            raise e

