from pymongo import MongoClient

url = 'mongodb+srv://admin:admin@cluster0.gksk1qf.mongodb.net'

client = MongoClient(url)
db = client.pytech
students = db.get_collection("students")

print('-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --')  

found_students = students.find({})
for found_student in found_students:
   print(f"Student ID: {found_student['student_id']}")
   print(f"First Name: {found_student['first_name']}")
   print(f"Last Name: {found_student['last_name']}") 
   print()

print("-- INSERT STATEMENTS --")

student_doc = { "student_id": 1010, "first_name": "John", "last_name": "Doe" }
id = students.insert_one(student_doc).inserted_id
print(f"Inserted student record {student_doc['first_name']} {student_doc['last_name']} into the students collection with document_id {id}")
print()

print('-- DISPLAYING STUDENT TEST DOC --')  

found_student = students.find_one({'student_id': 1010})
print(f"Student ID: {found_student['student_id']}")
print(f"First Name: {found_student['first_name']}")
print(f"Last Name: {found_student['last_name']}")
print()

students.delete_one({"student_id": 1010})

print('-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --')  

found_students = students.find({})
for found_student in found_students:
   print(f"Student ID: {found_student['student_id']}")
   print(f"First Name: {found_student['first_name']}")
   print(f"Last Name: {found_student['last_name']}") 
   print()