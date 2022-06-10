from dash import Dash
import dash
from dash import html
import os

import numpy as np
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import base64
import tensorflow as tf
from PIL import Image


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(id='parent', children=[
    html.H1(id='H1', children='Changing Brightness in Images', style={'textAlign': 'center',
                                                                      'marginTop': 40, 'marginBottom': 40}),
    html.Div(dcc.Upload(id='upload-image', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
               'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'},
        # Allow multiple files to be uploaded
        multiple=True)),
    html.Div(id='output-image-upload', style = {'width':'30%','display':'inline-block'}),
    html.Div(id='modify-image', style = {'width':'30%','display':'inline-block'}),
])


def parse_contents(contents, filename, date):
    return html.Div([
        html.H6("Original Image"),
        html.Img(src=contents)
])

def parse_contents_modify(contents):
    print('okokokok')
    return html.Div([
        html.H6("Modify Image"),
        html.Img(src=contents)
])

@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))


def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]

#        for name in list_of_contents:
#            with open('original.jpg', 'wb') as file:
#                file.write(bytes(name, encoding='utf-8'))

        #with open(os.path.join("original.jpg"), "wb") as f:
        #    f.write(base64.b64decode(str(list_of_names)))
        return children


@app.callback(Output('modify-image', 'children'),
              Input('upload-image', 'contents'))
#              State('upload-image', 'filename'))
def update_output(val):
    if val is not None:
        img = np.array(Image.open('modify.jpg'))

        fotos_mod = []
        print('oki')

        img = img / 255.  # normalices the array
        fotos_mod.append(img)  # 'save' the image in fotos_mod

        x = np.array(fotos_mod)  # turns fotos_mod in an array

        model = tf.keras.models.load_model('model_1.h5')  # load the pretrained model

        test_predictions = model.predict(x)

        b = test_predictions.shape[1:4]
        c = test_predictions.reshape(b)
        modify = Image.fromarray((c * 255).astype(np.uint8))

        modify.save('modify.jpg')

        children = parse_contents_modify(modify)

        return children


if __name__ == '__main__':
    app.run_server(debug=True)