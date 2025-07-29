import boto3
from flask import json


ec2 = boto3.client('ec2')

# Get all EBS snapshots
response = ec2.describe_snapshots(OwnerIds=['self'])

# Get all active EC2 instance IDs
instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
active_instance_ids = set()
snapshot_ids = set()

print(json.dumps(response, indent=2))
print("**********************************************************************")
print(json.dumps(instances_response, indent=2))

for reservation in instances_response['Reservations']:
    for instance in reservation['Instances']:
        active_instance_ids.add(instance['InstanceId'])

for snapshot in response['Snapshots']:
    snapshot_id = snapshot['SnapshotId']
    volume_id = snapshot.get('VolumeId')
    snapshot_ids.add(volume_id)

    if not volume_id:
        # delete snapshot if it has no associated volume
        print(f"Deleting snapshot {snapshot_id} with no associated volume.")
        ec2.delete_snapshot(SnapshotId=snapshot_id)

    else:
        try:
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(json.dumps(volume_response, indent=2 ))
            if not volume_response['Volumes'][0]['Attachments']:
                # delete snapshot if volume is not attached to any instance
                print(f"Deleting snapshot {snapshot_id} for volume {volume_id} not attached to any instance.")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
        except Exception as e:
            print(f"Error describing volume {volume_id}: {e}")


print(active_instance_ids)
print(snapshot_ids)
