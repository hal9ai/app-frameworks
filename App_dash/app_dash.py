from dash import Dash
from dash import html

import numpy as np
from dash import dcc
from dash.dependencies import Input, Output, State
import base64
import tensorflow as tf
from PIL import Image


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Changing Brightness in Images', style={'textAlign': 'center',
                                                                      'marginTop': 40, 'marginBottom': 40}),
    html.Div(dcc.Upload(id='upload-image', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={'width': '90%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
               'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'},
        # Allow multiple files to be uploaded
        multiple=True)),
    html.Div(id='output-image-upload', style = {'width':'35%','display':'inline-block'}),
    html.Div(id='modify-image', style = {'width':'35%','display':'inline-block'}),
])


def parse_contents(contents, string):
    return html.Div([
        html.H6(str(string)),
        html.Img(src=contents)
])


model = tf.keras.models.load_model('model_1.h5')  # load the pretrained model


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'))
def update_output(list_of_contents):
    if list_of_contents is not None:
        encoded_data = list_of_contents[0][22:]
        decoded_data = base64.b64decode(encoded_data)          # decode base64 string data

        img_file = open('original.jpg', 'wb')                  # write the decoded data back to original format in  file
        img_file.write(decoded_data)
        img_file.close()

        children = [parse_contents(list_of_contents[0], 'Original Image')]

        return children


@app.callback(Output('modify-image', 'children'),
              Input('upload-image', 'contents'))
def update_output(val):
    if val is not None:
        img = np.array(Image.open('original.jpg'))

        fotos_mod = []

        img = img / 255.  # normalices the array
        fotos_mod.append(img)  # 'save' the image in fotos_mod

        x = np.array(fotos_mod)  # turns fotos_mod in an array

        test_predictions = model.predict(x)

        b = test_predictions.shape[1:4]
        c = test_predictions.reshape(b)
        modify = Image.fromarray((c * 255).astype(np.uint8))

        modify.save('modify.jpg')

        children = parse_contents(modify, 'Modify Image')

        return children


if __name__ == '__main__':
    app.run_server(debug=True)