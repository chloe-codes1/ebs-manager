import boto3

from configs.configs import VOLUME_FILE
from utils.file_handler import write_json


class EC2Handler:

    def __init__(self):
        self.ec2_resource = boto3.resource('ec2')
        self.ec2_client = boto3.client('ec2')

    def get_ec2_tags(self, instance_id):
        tags = []
        try:
            instance = self.ec2_resource.Instance(instance_id)
            tags = instance.tags
        except Exception as e:
            print(e, instance_id)
        return tags
    
    def get_vpc_id(self, instance_id):
        instance_info = self.ec2_client.describe_instances(
            InstanceIds=[
                instance_id
            ]
        )
        vpc_id = instance_info['Reservations'][0]['Instances'][0]['VpcId']
        return vpc_id

    def describe_volumes(self):
        volumes = self.ec2_client.describe_volumes()
        write_json(title=VOLUME_FILE, contents=volumes)
        return volumes
