import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
collection_ref = db.collection("人選之人─造浪者")

docs = collection_ref.get() 

for doc in docs:
    print("演員:{},劇中腳色是{}".format(doc.to_dict()["name"], doc.to_dict()["role"]))
