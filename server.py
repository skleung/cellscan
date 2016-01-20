import os
import cv_algorithms
from flask import Flask
from flask import *
from werkzeug import secure_filename

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    resp = app.make_response("")
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(file_path)
            json_dict = dict(num_circles = cv_algorithms.count_circles(file_path))
            return jsonify(**json_dict)
    return resp

if __name__ == "__main__":
    app.run(debug=True)


