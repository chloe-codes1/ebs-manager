import boto3


class VolumeModifier:

    def __init__(self):
        self.ec2_client = boto3.client('ec2')

    def modify_volume_type(self, volume_id):
        response = self.ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3'
        )
        return response
