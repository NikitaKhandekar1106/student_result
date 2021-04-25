import pickle
import json
import numpy as np


file_path=r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\student\stud_model.pickle'
model=pickle.load(open(file_path,'rb'))

def get_subject_names():
        with open(r"C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\student\stud_columns.json", "r") as f:
            subject_cols= json.load(f)['result_columns']
        return subject_cols[:3]

global result
global total,avg
def get_result_predict(maths,physics,chemistry):
    total=maths+physics+chemistry
    avg=total/3
    if total>125:
        return('PASS')
    elif total<125:
        return('FAIL')

if __name__=='__main__':
    print(get_result_predict(75,85,90))



