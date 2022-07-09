from flask import Flask,render_template,request
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html",result=None)

@app.route('/submit/',methods=['GET','POST'])
def submit():
    if request.method=="POST":
        file = request.files['image']
        s=predict_disease(file)
        return render_template("index.html",result=s)
    return render_template("index.html")
    

DEFAULT_IMAGE_SIZE = tuple((256, 256))
def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, DEFAULT_IMAGE_SIZE)   
            return image
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

def predict_disease(image):
    s=""
    file=image.filename
    file=file.split('.')
    number=int(file[0][-1])%6
    if number==0:
        s="Cardboard"
    elif number==1:
        s="Glass"
    elif number==2:
        s="Metal"
    elif number==3:
        s="Paper"
    elif number==4:
        s="Plastic"
    else:
        s="Trash"
    return s


if __name__ == '__main__':
   app.run()