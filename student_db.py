from pymongo import MongoClient

db_name='student_db'
myclient=MongoClient('mongodb://localhost:27017/')
db=myclient[db_name]
collection_student=db['student_details']
collection_marks=db['marks_details']

def student_register_details(student_data):
    student_dict={}
    student_dict['name']=student_data['name']
    student_dict['password']=student_data['password']
    student_dict['gender']=student_data['gender']
    collection_student.insert_one(student_dict)
    return 'success'

def student_login_details(login_details):
    student_dict={}
    student_dict['name']=login_details['name']
    student_dict['password']=login_details['password']
    response= collection_student.find_one(login_details)
    
    if not response:
        return 'invalid username or password'
    return 'successfully logged in'

def save_predicted_result(maths,physics,chemistry,result):
    marks_details={'maths':maths,'physics':physics,
                   'chemistry':chemistry,'result':result}
    collection_marks.insert_one(marks_details)
    
    return'saved successfully'



