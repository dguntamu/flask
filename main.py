## Integration HTML with FLASK
## HTTP verb GET and POST

from flask import Flask,redirect,url_for,render_template,request


#Web Server Gateway Interface
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return render_template('index.html');

@app.route('/success/<int:score>')
def success(score):
    # final_result = ''
    # if score >= 50:
    #     final_result = 'PASS'
    # else:
    #     final_result = "FAIL"
    # return render_template('result.html',res = final_result);

    #dictionry example

    res = ''
    if score >= 50:
        res = 'PASSED'
    else:
        res = 'FAILED'

    exp = {'score':score,'str_res':res,'test':123,'test2':345} #dictionary declaration


    return render_template('result.html',res = exp);

@app.route('/fail/<int:score>')
def fail(score):
    return "Failed with score :: "+str(score);

''' Building URL dynamically '''
@app.route('/result/<int:marks>')
def result(marks):
    status = ''

    if marks < 35:
        status = 'fail'
    else:
        status = 'success'

    return redirect(url_for(status,score=marks))


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        avg = (science+maths+c+datascience)/4
        if avg >= 50:
            result = 'success'
        else:
            result = 'fail'

        return redirect(url_for(result,score = avg))


if __name__ == '__main__':
    app.run(debug = True)