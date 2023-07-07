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

result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Jamelkowski"}})

print('-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')  

found_student = students.find_one({'student_id': 1007})
print(f"Student ID: {found_student['student_id']}")
print(f"First Name: {found_student['first_name']}")
print(f"Last Name: {found_student['last_name']}")