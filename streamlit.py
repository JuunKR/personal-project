import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
import pandas as pd


@st.cache(allow_output_mutation=True)
def load():
    words = pd.read_csv('csv/ksx100.csv', encoding='UTF-8')
    words = np.array(words)
    words = words.reshape(2350,)
    ksx = {}
    for i, j in enumerate(words):
        ksx[j] = i 

   
    return load_model('save/model_save_best.h5'), list(ksx)
    
model, ksx = load()

st.write('한글 음절 인식')

CANVAS_SIZE = 192

col1, col2 = st.beta_columns(2)

with col1:
    canvas = st_canvas(
        fill_color='#FFFFFF',
        stroke_width=7,
        stroke_color='#000000',
        background_color='#FFFFFF',
        width=192,
        height=192,
        drawing_mode='freedraw',
        key='canvas'
    )

if canvas.image_data is not None:
    img = canvas.image_data.astype('uint8')
    img = cv2.resize(img, (32, 32))
    preview_img = cv2.resize(img, (192, 192))

    col2.image(preview_img)

    x = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = np.array(x, dtype=np.float32)
    x = x.reshape((-1, 32, 32, 3))
    x = x / 255.

    y = model.predict(x).squeeze()
    result = tf.argmax(y)

    # st.write('## Result: %d' % np.argmax(y))
    # st.bar_chart(y)

    st.write(f' ## Result: {ksx[result]}')

    most_arg = y.argsort()[::-1][:5]
    most_val = [f'{y[idx]*100:.8f}' for idx in most_arg]
    chars = [f'{ksx[idx]}' for idx in most_arg]
    
    chart_data = pd.DataFrame(
        np.array([most_val, chars]).T, columns=['Prob(%)', 'Pred'])
    st.write(chart_data)

    '''
    streamlit run streamlit.py
    '''