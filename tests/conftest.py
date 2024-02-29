import os
from zipfile import ZipFile
import pytest
from tests.settings import RESOURCES_DIR, ARCHIVE, FILES_LIST, FILES_DIR


@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if not os.path.exists(os.path.join(RESOURCES_DIR)):
        os.mkdir(RESOURCES_DIR)
    with ZipFile(ARCHIVE, 'w') as archive:
        for file in FILES_LIST:
            archive_file = os.path.join(FILES_DIR, file)
            archive.write(archive_file, arcname=os.path.basename(archive_file))
    yield
    os.remove(os.path.join(RESOURCES_DIR, 'archive.zip'))
    os.rmdir(RESOURCES_DIR)
