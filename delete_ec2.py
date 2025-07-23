import boto3

client = boto3.client('ec2')

# Call describe_instances
response = client.describe_instances()

# Extract instance IDs
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Print all instance IDs
print("EC2 Instance IDs:", instance_ids)

for i in instance_ids:
    print(i)

'''
    response1 = client.stop_instances(
        InstanceIds=[
            'i-0e2d1662c2190ff65',
        ],
    )

    response2 = client.terminate_instances(
        InstanceIds=[
            'i-0d2c809a3acc2987e',
        ],
    )

    print(response2)'''