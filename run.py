from flask import Flask,request,jsonify,render_template
import student_db
import test_model
import functions
import result

app=Flask(__name__)

@app.route('/') #default
def home_page():
    return render_template('home.html')

@app.route('/get_subject_names',methods=['GET'])
def get_subject_names():
    response=jsonify({
        'subjects':test_model.get_subject_names()
    })
    return response

@app.route('/result_predict',methods=['GET','POST'])
def result_predict():
    if request.method=='POST':
        data=request.form
        print(data)
        maths=int(data['maths'])
        physics=int(data['physics'])
        chemistry=int(data['chemistry'])
        print('maths,physics,chemistry',maths,physics,chemistry)
        result = test_model.get_result_predict(maths,physics,chemistry)
        student_db.save_predicted_result(maths, physics, chemistry, result)
        return ('student result: {}'.format(result))
    return render_template('home.html')      

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = student_db.student_register_details(data)

    return jsonify({'msg':response})

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response = student_db.student_login_details(data)
    return jsonify({'msg':response})


if __name__=="__main__":
    print("starting the python flask for insurance........")
    app.run(host='0.0.0.0',port=5002)
