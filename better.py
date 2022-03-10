from flask import Flask, render_template, Response, request, send_from_directory
import cv2

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    return render_template('better.html')

@app.route('/video/<string:file_name>')
def stream(file_name):
    video_dir = './video'
    return send_from_directory(directory=video_dir, path=file_name)

if __name__ == "__main__":
    app.run(debug=True)