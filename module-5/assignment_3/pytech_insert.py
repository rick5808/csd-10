from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.gksk1qf.mongodb.net'

client = MongoClient(url)
db = client.pytech
students = db.get_collection("students")

print("-- INSERT STATEMENTS --")

student_doc = { "student_id": 1007, "first_name": "Thorin", "last_name": "Oakenshield" }
id = students.insert_one(student_doc).inserted_id
print(f"Inserted student record {student_doc['first_name']} {student_doc['last_name']} into the students collection with document_id {id}")

student_doc = { "student_id": 1008, "first_name": "Bilbo", "last_name": "Baggins" }
id = students.insert_one(student_doc).inserted_id
print(f"Inserted student record {student_doc['first_name']} {student_doc['last_name']} into the students collection with document_id {id}")

student_doc = { "student_id": 1009, "first_name": "Frodo", "last_name": "Baggins" }
id = students.insert_one(student_doc).inserted_id
print(f"Inserted student record {student_doc['first_name']} {student_doc['last_name']} into the students collection with document_id {id}")
