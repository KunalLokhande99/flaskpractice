### Krish Naik
### Create a simple flask application

from flask import Flask, render_template, request, redirect, url_for

### creating the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to Home Page </h1>"

@app.route('/welcome')
def welcome():
    return "<h1> Welcome to the Flask Tutorials by Krish Naik </h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "GREAT!! Result is PASSED and the score is : "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "SORRY!! Result is FAILED and the score is "+str(score)


@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3

        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))
        return render_template('result.html',results=average_marks)


if __name__=='__main__':
    app.run(debug=True)
