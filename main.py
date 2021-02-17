from ebs.volume_checker import VolumeChecker

if __name__ == "__main__":
    volume_checker = VolumeChecker()
    volume_checker.check_types()
    volume_checker.check_if_asg_exists()
