from ec2.ec2_handler import EC2Handler
from utils.file_handler import write_file, write_json
from configs.configs import DEVEL_VPC, MANAGE_VPC, PRODUCT_VPC


class VolumeChecker:

    def __init__(self):
        ec2_handler = EC2Handler()
        self.volumes = ec2_handler.describe_volumes()['Volumes']

    def check_types(self):
        gp2 = gp3 = total = 0
        etc = []
        for volume in self.volumes:
            volume_type = volume['VolumeType']
            if volume_type == 'gp2':
                gp2 += 1
            elif volume_type == 'gp3':
                gp3 += 1
            else:
                etc.append(volume_type)
            total += 1

        print(f'Total: {total}, gp2: {gp2}, gp3: {gp3}, etc: {len(etc)}')

    def check_if_asg_exists(self):
        ec2_handler = EC2Handler()
        devel_asg_exists, product_asg_exists, manage_asg_exists, devel_asg_non_exists, product_asg_non_exists, manage_asg_non_exists, no_IID_tag, not_attached_ebs = (set() for _ in range(8))

        for volume in self.volumes:
            attachment, volume_id, volume_type = volume['Attachments'], volume['VolumeId'], volume['VolumeType']

            if not len(attachment):
                not_attached_ebs.add(volume_id)
                continue

            instance_id = attachment[0]['InstanceId']
            vpc_id = ec2_handler.get_vpc_id(instance_id)
            tags = ec2_handler.get_ec2_tags(instance_id)

            IID = [tag['Value'] for tag in tags if tag['Key'] == 'IID']
            env = _check_vpc_env(vpc_id)

            if volume_type == 'gp2':
                if not IID:
                    no_IID_tag.add(volume_id)

                elif IID[0] == 'yes':
                    if env == 'DEVEL':
                        devel_asg_exists.add(volume_id)
                    elif env == 'PRODUCT':
                        product_asg_exists.add(volume_id)
                    elif env == 'MANAGE':
                        manage_asg_exists.add(volume_id)

                elif IID[0] == 'no':
                    if env == 'DEVEL':
                        devel_asg_non_exists.add(volume_id)
                    elif env == 'PRODUCT':
                        product_asg_non_exists.add(volume_id)
                    elif env == 'MANAGE':
                        manage_asg_non_exists.add(volume_id)

        print(f'ASG exists: {len(devel_asg_exists) + len(product_asg_exists) + len(manage_asg_exists)} -> PRODUCT: {len(product_asg_exists)}, DEVEL: {len(devel_asg_exists)}, MANAGE: {len(manage_asg_exists)}')
        print(f'No ASG exits: {len(devel_asg_non_exists) + len(product_asg_non_exists) + len(manage_asg_non_exists)} -> PRODUCT: {len(product_asg_non_exists)}, DEVEL: {len(devel_asg_non_exists)}, MANAGE: {len(manage_asg_non_exists)}')
        print(f'No IID Tag: {len(no_IID_tag)}, Not attached EBS: {len(not_attached_ebs)}')

        # asg exists
        write_file('product_asg_exists', product_asg_exists)
        write_file('devel_asg_exists', devel_asg_exists)

        # asg non exists
        write_file('product_asg_non_exists', product_asg_non_exists)
        write_file('devel_asg_non_exists', devel_asg_non_exists)
        write_file('manage_asg_non_exists', manage_asg_non_exists)

        write_file('not_attached_ebs', not_attached_ebs)


def _check_vpc_env(vpc_id):
    if vpc_id.endswith(DEVEL_VPC):
        env = 'DEVEL'
    elif vpc_id.endswith(PRODUCT_VPC):
        env = 'PRODUCT'
    elif vpc_id.endswith(MANAGE_VPC):
        env = 'MANAGE'

    return env