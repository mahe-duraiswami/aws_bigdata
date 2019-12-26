import boto3

client = boto3.client('dynamodb')

response = client.create_table(
	AttributeDefinitions = [
		{'AttributeName': 'CustomerID','AttributeType': 'N'},
		{'AttributeName': 'OrderID','AttributeType': 'S',},
		],
	KeySchema = [
		{'AttributeName':'CustomerID','KeyType':'HASH'},
		{'AttributeName': 'OrderID','KeyType':'RANGE',},
		],
    ProvisionedThroughput={'ReadCapacityUnits': 5,'WriteCapacityUnits': 5,},
    TableName='OrderInfo',
)

print(response)