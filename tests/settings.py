import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, 'files')
FILES_LIST = os.listdir(FILES_DIR)
RESOURCES_DIR = os.path.join(CURRENT_DIR, 'resources')
ARCHIVE = os.path.join(RESOURCES_DIR, 'archive.zip')
