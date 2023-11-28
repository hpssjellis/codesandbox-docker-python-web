from flask import Flask, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
import tensorflowjs as tfjs
import zipfile
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './myUp'
app.config['CONVERTED_MODEL_FOLDER'] = './myConverted'
app.config['MODEL_ZIP_PATH'] = 'myZipped/model.zip'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'json', 'bin'}


def zipdir(ziph, *file_paths):
    for file_path in file_paths:
        ziph.write(file_path, os.path.basename(file_path))


def convert_tfjs_to_keras(tfjs_model_path):
    keras_model_path = os.path.join(
        app.config['CONVERTED_MODEL_FOLDER'], 'converted_model.h5')
    tflite_model_path = os.path.join(
        app.config['CONVERTED_MODEL_FOLDER'], 'model.tflite')
    c_header_path = os.path.join(
        app.config['CONVERTED_MODEL_FOLDER'], 'model.h')

    try:
        # Convert TFJS to Keras
        model = tfjs.converters.load_keras_model(tfjs_model_path)
        model.save(keras_model_path)
        print(f"Keras model saved to {keras_model_path}")

        # Convert Keras to TFLite
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()
        with open(tflite_model_path, 'wb') as f:
            f.write(tflite_model)
        print("TFLite model saved successfully")

        # Convert TFLite to C Header
        subprocess.run(['xxd', '-i', tflite_model_path,
                       c_header_path], check=True)
        print("TFLite model converted to C header file successfully")

        # Zip only the TFLite model and the C header file
        with zipfile.ZipFile(app.config['MODEL_ZIP_PATH'], 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(zipf, tflite_model_path, c_header_path)
        print("Zipped TFLite and C header files successfully")

    except Exception as e:
        print(f"An error occurred: {e}")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return 'No files part in the request'

        files = request.files.getlist('files[]')
        if not files:
            return 'No files selected'

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        tfjs_model_path = os.path.join(
            app.config['UPLOAD_FOLDER'], files[0].filename)
        convert_tfjs_to_keras(tfjs_model_path)

        return redirect(url_for('download_model'))

    return '''
    <!doctype html>
    <title>Upload multiple files</title>
    <h1>Upload TensorFlow.js Model and Weights</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=files[] multiple>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/download_model')
def download_model():
    try:
        return send_file(app.config['MODEL_ZIP_PATH'], as_attachment=True)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
