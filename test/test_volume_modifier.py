import pytest

from ebs.volume_modifier import VolumeModifier
from utils.file_handler import write_json
from configs.configs import variables


@pytest.fixture()
def setup_path():
    variables['FILE_PATH'] = '../test/samples/'


@pytest.fixture()
def volume_modifier():
    return VolumeModifier()


class TestVolumeModifier:

    def test_modify_volume_type(self, volume_modifier, setup_path):
        """
        Wait at least 6 hours between modifications per volume
        """
        volume_id = ''
        res = volume_modifier.modify_volume_type(volume_id)
        write_json(title='test_modify_volume_type.json', contents=res)
