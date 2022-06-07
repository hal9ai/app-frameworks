from dash import Dash
import dash
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
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
    html.Div(id='output-image-upload'),
    html.Div(id='modify-image'),
])


def parse_contents(contents, filename, date):
    return html.Div([
        html.Img(src=contents),
        html.Hr(),
    ])


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
#        with open(os.path.join("TempDir", list_of_names.name), "wb") as f:
#            f.write(list_of_names.getbuffer())
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@app.callback(Output('modify-image', 'children'),
              Input('upload-image', 'value'))
#              State('upload-image', 'filename'))
def update_output(val):
    if val is not None:
        try:
            img = np.array(Image.open(f"assets/{input}"))
        except OSError:
            raise PreventUpdate

        fotos_mod = []

        img = img / 255.  # normalices the array
        fotos_mod.append(img)  # 'save' the image in fotos_mod

        x = np.array(fotos_mod)  # turns fotos_mod to an array

        model = tf.keras.models.load_model('model_1.h5')  # load the pretrained model

        children = model.predict(x)  # obtains the new image with the model

        return children

if __name__ == '__main__':
    app.run_server(debug=True)
