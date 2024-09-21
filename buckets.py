import boto3


# number_of_buckets function displays number of buckets
def number_of_buckets(num):
    client = boto3.client('s3')
    
    # Call list_buckets function and put into a buckets result
    buckets = client.list_buckets()

    count = 0
    for bucket in buckets['Buckets']:
        print(f"Processing bucket number-[{count}]")

        if count < num:
            # Keep processing
            current_bucket = bucket['Name']
            print(f"Found Bucket: {current_bucket}")
            # Functions Logs from Lambda:
            # START RequestId: c... Version: $LATEST
            # Processing bucket number-[0]
            # Found Bucket: alfredo-noah
            # Processing bucket number-[1]
            # Found Bucket: aws-logs-561744971673-us-east-1
            # Processing bucket number-[2]

            # Increment count after each loop
            count += 1
        else:
            return

def lambda_handler(event, context):
    # Grab the number out of an event
    number = event['number']
    # Run that number
    number_of_buckets(number)

    return number