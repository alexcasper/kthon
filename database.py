import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate(".so.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

def write_update(person = 'alexcasper',iteration = '1', data = {'lets':'go'}):
    doc_ref = db.collection("users").document(person).collection('updates').document(iteration)
    doc_ref.set(data)

def write_profile(person = 'alexcasper'):
    doc_ref = db.collection("users").document(person)
    data = {'name':'alex'}
    doc_ref.set(data)

write_profile()