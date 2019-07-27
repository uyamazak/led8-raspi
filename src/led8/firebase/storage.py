from datetime import timedelta
from google.cloud.exceptions import GoogleCloudError
from . import bucket


def upload_photo(file_obj, path, expiration_days=7):
    blob = bucket.blob(path)
    file_obj.seek(0)
    try:
        blob.upload_from_file(file_obj, content_type="image/jpeg")
    except GoogleCloudError as e:
        print(e)
        return False
    else:
        return blob.generate_signed_url(timedelta(days=expiration_days))
