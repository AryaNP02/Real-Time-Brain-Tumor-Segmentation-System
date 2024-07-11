import numpy as np
from flask import Flask, flash, request, jsonify
from werkzeug.utils import secure_filename
from keras.models import load_model
import os
import cv2
from PIL import Image

from flask import render_template

app = Flask(__name__)


model_seg = load_model("Final_unet_ model.hdf5", compile=False)
from flask import render_template

l, h = 256, 256


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/segment", methods=["GET"])
def segment():
    return render_template("segment.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        imagefile = request.files["image"]
        if imagefile.filename == "":
            return render_template("segment.html")

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, "static", secure_filename(imagefile.filename)
        )

        imagefile.save(file_path)

        # os.remove ( file_path )

        X = np.empty((1, 256, 256, 3))
        img = cv2.imread(file_path)
        img = cv2.resize(img, (256, 256))
        img1 = img
        img = np.array(img, dtype=np.float64)

        # standardising the image
        img -= img.mean()
        img /= img.std()
        # converting the shape of image from 256,256,3 to 1,256,256,3
        X[0,] = img

        # make prediction of mask
        predict = model_seg.predict(X)
        filename= imagefile.filename
        # print(type(predict))

        ###############################################################################
        # check if  the  mri image  have tumor or not ..
        # # note : the model return an  "array" : region where brain tumor is present  , so we dont require probability ..
        ##   drop probability..

        if predict.round().astype(int).sum() == 0:
            print("NO TUMOR")
            # RENDER THE PAGE FOR NO TUMOR ..

            return render_template("no_tumor.html", image_path=filename)

        else:
            
            pred = np.array(predict).squeeze().round()

            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

            img1[pred == 1] = (
                0,
                255,
                255,
            ) 
             ##   this color code -- determines what color be the tumor region would be.
            ## edit : if u want  to chng the color   of the marked region : format :(Red , Blue , Green)

            # plt.imshow(img1)   # this code( 2 lines )will show  the segmented mask  in a pop-up windows
            # plt.show()

            cv2.imwrite(
                "static/mask.jpeg", img1
            )  ##  save the image in folder: result_mask .With name  of image : "mask.png"
            # print(pred.shape)

            ##   show the page for when tumor is "detected" original image and the segmented image . ( the  mask.png)

            return render_template("tumor.html", image_path=filename)
    ###############################################################################################

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
