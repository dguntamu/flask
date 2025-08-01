from flask import Flask,redirect,url_for,render_template,Response
import cv2


app = Flask(__name__)
camera = cv2.VideoCapture(0)


@app.route('/')
def home():
    return render_template('camera_home.html')


@app.route('/video')
def video():
    return Response(generate_frames(),mimetype = 'multipart/x-mixed-replace; boundary=frame')


def generate_frames():
    
    #read the camera frames continueosly
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')


if __name__ == '__main__':
    app.run(debug = True)
