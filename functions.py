import pickle,json
import numpy as np


result_cols=None
model=None
def load_saved_artifacts():
    print('loading artifacts started............')
    global result_cols

    with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\student\stud_columns.json','r') as f:
        result_cols=json.load(f)['result_columns']
        
    global model
    if model is None:
           with open(r'C:\Users\Shamali\Desktop\Velocity python 2jan21\Nikita Velocity\FLASK\student\stud_model.pickle', 'rb') as f:
                model = pickle.load(f)

    print("loading saved artifacts...done")


global result
global total,avg
def result_predict(maths,physics,chemistry):
    total=maths+physics+chemistry
    avg=total/3
    if total>125:
        return('PASS')
    elif total<125:
        return('FAIL')    
    

def get_subject_names():
    return result_cols[:3]

if __name__=='__main__':
    load_saved_artifacts()
    print(get_subject_names())
    res=result_predict(75,85,90)
    print(res)

