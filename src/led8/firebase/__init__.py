import firebase_admin
from firebase_admin import credentials, firestore, storage
from os import environ

STORAGE_BUCKET = environ['FIREBASE_STORAGE_BUCKET']
SERVICE_ACCOUNT_KEY = environ.get('FIREBASE_SERVICE_ACCOUNT_KEY', './keys/serviceAccountKey.json')

cred = credentials.Certificate(SERVICE_ACCOUNT_KEY)
firebase_admin.initialize_app(cred, {'storageBucket': STORAGE_BUCKET})

client = firestore.client()
bucket = storage.bucket()
SERVER_TIMESTAMP = firestore.SERVER_TIMESTAMP
