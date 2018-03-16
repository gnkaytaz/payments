import boto3

def tables_init():

    # Get the service resource.
    dynamodb = boto3.client('dynamodb')

    # Create the DynamoDB table.
    try:
        table = dynamodb.create_table(
            TableName='investors',
            KeySchema=[
                {
                    'AttributeName': 'InvestorID',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'ChatID',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'InvestorID',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'ChatID',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except dynamodb.exceptions.ResourceInUseException:
    # do something here as you require
        print("Error. The tables was created already")
        return 1
    pass

    # Print out some data about the table.
    print(table)

def registration(chat_id, refund_address):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('investors')

    table.put_item(
        Item={
            'InvestorID': refund_address,
            'ChatID': chat_id,
            'RefundAddress': refund_address,
        }
    )

    return 0

def main():
    #tables_init()
    registration('jaser_chat', '1ACLdrtUGsKLaRTfWGxF3NH5PxyAr1M31b')

if __name__ == "__main__":
    main()

