#Packages imports
from keras.preprocessing import image
import tensorflow as tf
import os
import streamlit as st
import numpy as np

#Function to save the upload file
def save_uploaded_file(uploaded_file):
    with open(os.path.join("TempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success("The upload file {} was saved in the folder TempDir".format(uploaded_file.name))

#Function to modify the image
def modify_image(img_path):
    fotos_mod = []                     #here we will save the image
    img = image.load_img(img_path)     #load the image from the image path
    img = image.img_to_array(img)      #transform the image in an array
    img = img/255.                     #normalices the array
    fotos_mod.append(img)              #'save' the image in fotos_mod

    x = np.array(fotos_mod)            #turns fotos_mod to an array

    model = tf.keras.models.load_model('model_1.h5')      #load the pretrained model

    test_predictions = model.predict(x)                   #obtains the new image with the model

    return test_predictions

