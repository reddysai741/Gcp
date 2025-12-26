from google.cloud import firestore

db = firestore.Client(database="sainath")


doc_ref = db.collection('users').add({
    'name': 'rash',
    'mail': 'rash@gmail.com',
    'role': 'pro analyst',
    'age': 24
})


print("Users age >= 21")
for doc in db.collection('users').where('age', '>=', 21).stream():
    print(f'{doc.id} => {doc.to_dict()}')


db.collection('users').document(doc_ref[1].id).update({
    'age': 23
})
print(f"Updated user {doc_ref[1].id} age to 23")


query = db.collection('users').where('name', '==', 'vasu')

for doc in query.stream():
    db.collection('users').document(doc.id).delete()
    print(f"Deleted user with name {doc.id}")
    print(f'{doc.id} => {doc.to_dict()}')
