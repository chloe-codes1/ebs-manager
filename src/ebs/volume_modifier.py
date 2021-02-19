import boto3

from configs.configs import DESIRED_EBS_TYPE

class VolumeModifier:

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def modify_volume_type(self, volume_id):
        response = self.ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType=DESIRED_EBS_TYPE
        )
        return response
