from flask import Flask,request,jsonify
import json
from config import Config
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/getMetadata', methods = ['GET'])
def getMetadata()   :
    imageData = {'status': 'success', 'message': 'Metadata retrieved successfully'}
    return jsonify(imageData),200


@app.route('/uploadImage', methods = ['POST'])
def uploadImage():
    image = request.files['image']
    image.save(f'Images/{image.filename}')
    imageData = {'status': 'success', 'message': 'Image uploaded successfully'}
    return jsonify(imageData),200


@app.route('/getImages', methods=['GET'])
def getImages():
    image_files = []
    for filename in os.listdir('Images'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_files.append(filename)
    return jsonify(image_files),200




if __name__ == '__main__':
    app.run(host= Config.HOST,debug=Config.DEBUG, port=Config.PORT)