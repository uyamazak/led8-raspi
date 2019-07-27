from . import client, SERVER_TIMESTAMP

COMMAND_COLLECTION_PATH = 'commands'
PHOTO_COLLECTION_PATH = 'photos'

command_collection_ref = client.collection(COMMAND_COLLECTION_PATH)
get_latest_command = command_collection_ref\
    .order_by('timestamp', direction='DESCENDING')\
    .limit(1)

photo_collection_ref = client.collection(PHOTO_COLLECTION_PATH)

def add_photo(data_dict):
    photo_data = {
        'path': data_dict.get('path'),
        'url': data_dict.get('url'),
        'uid': data_dict.get('uid'),
        'status': data_dict.get('status'),
        'timestamp': SERVER_TIMESTAMP,
    }
    return photo_collection_ref.add(photo_data)

