

def create_queue():
    sqs_client = boto3.client("sqs", region_name="us-west-2")
    response = sqs_client.create_queue(
        QueueName="my-new-queue",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    print(response)
