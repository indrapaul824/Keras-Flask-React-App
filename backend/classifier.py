import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from PIL import Image, ImageFile
from numpy import expand_dims
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
ImageFile.LOAD_TRUNCATED_IMAGES = True

model = MobileNetV2(weights='imagenet')


def getPrediction(img_bytes, model):
    img = Image.open(img_bytes)
    img = img.convert('RGB')
    img = img.resize((224, 224), Image.NEAREST)

    numpy_img = image.img_to_array(img)
    img_batch = expand_dims(numpy_img, axis=0)

    pro_img = preprocess_input(img_batch, mode='caffe')
    preds = model.predict(pro_img)

    return preds


def classifyImage(file):
    preds = getPrediction(file, model)
    prediction = decode_predictions(preds, top=1)

    res = str(prediction[0][0][1])
    return res
