#Packages import
import streamlit as st
import seaborn as sns
from PIL import Image
import os

#Ours functions
from functions import save_uploaded_file, modify_image

sns.set_theme(style="darkgrid")
sns.set()

st.title('Changing Brightness in Images')

uploaded_file = st.file_uploader("To continue, please upload an image", type=['.jpg', '.png'])

if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        predictions = modify_image(os.path.join('TempDir/', uploaded_file.name))    #modify the image

        image = Image.open(uploaded_file)                                           #original image

        col1, col2 = st.columns([1, 1])                                             #split the window in 2
        with col1:
            st.write('Original Image:')
            st.image(image, width=300)                                              #show the original image

        with col2:
            st.write('Modify Image:')
            st.image(predictions, width=300)                                        #show the modified image

