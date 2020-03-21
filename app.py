import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
from dash.dependencies import Input, Output

colors = {
    'background': '#C71585',
    'text': '#F0FFFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Привет! Это страничка любви от Ильдара',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Всем кискам пис, всем пискам кис', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Markdown('''
                 **Коль в вышку хочешь -  [заходи](https://biology.hse.ru).**''',style={
        'textAlign': 'left',
        'color': colors['text']
        }),
     html.Div([
            html.Img(src='https://avatars.mds.yandex.net/get-zen_doc/1885679/pub_5e0e6426dddaf400b1f69393_5e0e69cfec575b00b10ec9e6/scale_1200',style={
'width':'10%', 'margin-left':50, 'margin-top':20, 'textAlign': 'center'})
            ]),
    html.Div([
            html.Img(src='https://sun9-5.userapi.com/c857224/v857224433/12bdca/po8ujLC4PR8.jpg',style={
'width':'75%', 'margin-left':90, 'margin-top':25, 'textAlign': 'center'})
            ]),

    html.Label('Насколько мы любим вышку'),
    dcc.Slider(
            id='my-slider',
            min=1,
            max=10,
            marks={i: 'Меладзе {}'.format(i) for i in range(11)},
            value=10,
            ),
            html.Div(id='slider-output-container'),

    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Моё сердце принадлежит...', value='tab-1'),
        dcc.Tab(label='Я достаю из широких штанин', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Высшей школе экономики')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Дубликатом бесценного груза Читайте, завидуйте Я - БВИшник престижного российского ВУЗа!')
        ])
    

            
if __name__ == '__main__':
    app.run_server(debug=True)