from flask import Flask,redirect,url_for
#Web Server Gateway Interface
app = Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return "Passed with score : "+ str(score);


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


if __name__ == '__main__':
    app.run(debug = True)