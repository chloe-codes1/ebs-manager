import pytest

from utils.file_handler import write_json
from configs.configs import variables, VOLUME_FILE


@pytest.fixture()
def setup_path():
    variables['FILE_PATH'] = '../test/samples/'


class TestFileHandler:

    def test_write_json(self, setup_path):
        test_dict = {'Test': 'Testing...'}
        write_json(title=VOLUME_FILE, contents=test_dict)
