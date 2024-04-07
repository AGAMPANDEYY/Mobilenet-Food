# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/app-py-392a9b85-6687-4e26-907b-73bc89934e94.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20240407/auto/storage/goog4_request%26X-Goog-Date%3D20240407T105239Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D109d4744a9eb15a73689fbf1a781854941badee391d85ea65427eb42118fd6e2cf84925684194e08932b09b63059646414db649e44ebb1a888d98c11253b6a51660e33adb1a4526a3f3d306300f38b76c54ebf736a1fff07aa63d4468d0422cb855fba1819a7d30f7e146e89ee3e65955356b37385a632beb0c027c82548845b0186e6f19b8d2a13afe12de7ff32391ee6c797abfe26dd0e09f85033b03367a0950be0f60201af7a31921c40fa5a4e81948a43f7e62409751847cf4e60517ae5a906b1a737a042516076b758dcfda01b016d4e959d8a761df0fa6217e66e73d0e8871911531598ade9be48e1f8bc7b8c1586834a4e8c2980b67cc7e80256c292
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import streamlit as st
import cv2
import transformers
import tensorflow
import cv2
from tensorflow.keras.preprocessing.image import img_to_array

#!git clone https://huggingface.co/AgamP/MobileNetV2_Food_Classif_e20

loaded_model=tensorflow.keras.models.load_model("mobilenet_sft.keras")





#image_path="/kaggle/input/gajar-ka-halwa/images.jpeg"


def main():
    st.title("Indian Food Classification")
    st.write("Hello! upload an image to know the food name")
    st.sidebar.image("happystocks_technologies_logo.jpeg")
    st.sidebar.title("About")
    st.sidebar.write("This app uses a pre-trained MobileNetV2 model to classify food images into one of 80 categories.")
    st.sidebar.write("To use the app, simply upload an image and the app will display the predicted class label.")
    

    uploaded_file=st.file_uploader("Choose image file ", type=['jpg','png'])
    if uploaded_file is not None:
        image_path= uploaded_file.name
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())


        class_labels = ['adhirasam', 'aloo_gobi', 'aloo_matar', 'aloo_methi', 'aloo_shimla_mirch',
               'aloo_tikki', 'anarsa', 'ariselu', 'bandar_laddu', 'basundi', 'bhatura',
               'bhindi_masala', 'biryani', 'boondi', 'butter_chicken', 'chak_hao_kheer',
               'cham_cham', 'chana_masala', 'chapati', 'chhena_kheeri', 'chicken_razala',
               'chicken_tikka', 'chicken_tikka_masala', 'chikki', 'daal_baati_churma',
               'daal_puri', 'dal_makhani', 'dal_tadka', 'dharwad_pedha', 'doodhpak',
               'double_ka_meetha', 'dum_aloo', 'gajar_ka_halwa', 'gavvalu', 'ghevar',
               'gulab_jamun', 'imarti', 'jalebi', 'kachori', 'kadai_paneer', 'kadhi_pakoda',
               'kajjikaya', 'kakinada_khaja', 'kalakand', 'karela_bharta', 'kofta',
               'kuzhi_paniyaram', 'lassi', 'ledikeni', 'litti_chokha', 'lyangcha',
               'maach_jhol', 'makki_di_roti_sarson_da_saag', 'malapua', 'misi_roti',
               'misti_doi', 'modak', 'mysore_pak', 'naan', 'navrattan_korma', 'palak_paneer',
               'paneer_butter_masala', 'phirni', 'pithe', 'poha', 'poornalu', 'pootharekulu',
               'qubani_ka_meetha', 'rabri', 'ras_malai', 'rasgulla', 'sandesh', 'shankarpali',
               'sheer_korma', 'sheera', 'shrikhand', 'sohan_halwa', 'sohan_papdi',
               'sutar_feni', 'unni_appam']


        def preprocess_image(input_path):
              image=cv2.imread(input_path)
              image=cv2.resize(image,(224,224))
              image_array=img_to_array(image)
              image_array=np.expand_dims(image_array,axis=0)
              return image_array
        def prediction(image_path):

              image_array=preprocess_image(image_path)
              prediction=loaded_model.predict(image_array,batch_size=1)
              decoded_prediction=decode_prediction(prediction)
              return decoded_prediction

        def decode_prediction(pred):
              predicted_label_index=np.argmax(pred)
              predicted_class=class_labels[predicted_label_index]
              return predicted_class

        predicted_class=prediction(image_path)

        st.image(image_path, caption=f"Predicted Food: {predicted_class}", use_column_width=True)

        st.download_button(
            label=f"Download image ({predicted_class})",
            data=open(image_path, "rb").read(),
            file_name=f"{predicted_class}.jpg",
            mime="image/jpeg",
        )

if __name__=="__main__":
    main()
