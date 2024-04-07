# -*- coding: utf-8 -*-
"""FT_MobileNet_Inference

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/ft-mobilenet-inference-da646c93-6050-43bd-95a1-d0bc5665951e.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20240407/auto/storage/goog4_request%26X-Goog-Date%3D20240407T104201Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D95cf86a6cef6552f9c18012ab4ec51faa16817045035fa7a937cc32667442dd65935c54792d07b046d4f9e777dcd7e49e34d335a050abfffe2b81b3064ca302de4c93a12e2dba2c2467b5c87a13fba6c12fdc2b4c5710e5d36eebd26cc5b3595a13c5adcdf72cdc61708931d8fc8a1e20fed6757d99110cbacc4236972bfd1e825ddc9e1281d633e48aefa25b79078ce07c0aff1dc93b243768fff56eac418649accf242f0042f3245efff8bf0c36991eb042f3407a6367bb1140d429552dd3985ba9363e7d8f70d447a3565543e0d07402d9d75d25c121f394ea191d41d3c0e24853c8686dd6c2e1f392def9809eaaeb8ae979faaac0d276214eca3338cda53
"""

# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATA SOURCES
# TO THE CORRECT LOCATION (/kaggle/input) IN YOUR NOTEBOOK,
# THEN FEEL FREE TO DELETE THIS CELL.
# NOTE: THIS NOTEBOOK ENVIRONMENT DIFFERS FROM KAGGLE'S PYTHON
# ENVIRONMENT SO THERE MAY BE MISSING LIBRARIES USED BY YOUR
# NOTEBOOK.

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'daal-chawal-img:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F4748200%2F8051496%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240407%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240407T104200Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D77e74245e9c166c6208aaa09707129ac36fba8ab35826e479f1ffdf9b0ae53e559ee7c45e3cae9b563b4b5d47b16f446e682976d2261bb3a55f5165163fb03a896c608b65cdf3cd75aa8382808c87d2afd0b9653948bc46e7bdc6e34e93d2df1587d0c3fed2c9ada1cca2305da84d6d37d93d053d761af7fc3bc56469b586988b2b775fde591efd6096b5642e45e60c50a92416f37cc3812f6ef7b720a5142f1e37f22db59386cb36d616a89ef5786c5a9ac40b4025c9586681a430fa12c1e35d4091d5f4b015ecf9d5768980cd1c6ff712918cafe873003641d8af173c722ecd5f08a7b42d83a84b3e44bb75c53a41e0912a4b1d845adfdf0a2d01090b82e40,gajar-ka-halwa:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F4748837%2F8052393%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240407%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240407T104200Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D5d6cae62138798bf7880d6df1eea791f77b0c3231ad1fe2cf84bb2b420040870b2cdebae93ed0ba29dea854d11ec58115f93edd75febc0840ec53fab18daf09d5ece34c9a36bd7ae4ffc17243486533e0607a43919749e6b38fa37924b23c0f9a472ea03e5b8aeb8aeaeb254f8eb3f026f605f80000c94414077409719955ef64a6f59a658a526ba122be3a1fd8405d66efa8e75e89e685b3b8b181aa9605d36ad83ecd69b1079ee62959efe957b1c03b3412a8331f8d6abc25405bb26d8502362dd9aec7279455f83dfc66310d202901ca7cadf7405d95341e7e536e09bbb68c1eab0e0fc61d725bf07773952ce723cf3426353a422ea4ed64afb09865e1cf2'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')

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

!git clone https://huggingface.co/AgamP/MobileNetV2_Food_Classif_e20

import transformers
from transformers import TFPreTrainedModel
import tensorflow

loaded_model=tensorflow.keras.models.load_model("/kaggle/working/MobileNetV2_Food_Classif_e20/mobilenet_sft.keras")

loaded_model.summary()

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

import cv2
from tensorflow.keras.preprocessing.image import img_to_array


def preprocess_image(input_path):
    image=cv2.imread(input_path)
    image=cv2.resize(image,(224,224))
    image_array=img_to_array(image)
    image_array=np.expand_dims(image_array,axis=0)
    return image_array
def prediction(image_path):

    image_array=preprocess_image(image_path)
    prediction=loaded_model.predict(image_array,batch_size=1)
    print(prediction.shape)
    decoded_prediction=decode_prediction(prediction)
    print(decoded_prediction)

def decode_prediction(pred):
    predicted_label_index=np.argmax(pred)
    predicted_class=class_labels[predicted_label_index]
    return predicted_class


image_path="/kaggle/input/gajar-ka-halwa/images.jpeg"
prediction(image_path)