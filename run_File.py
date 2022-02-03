#from cgitb import text
#from click import style
#from tkinter import font
import dash
#from tenacity import retry_unless_exception_type
import dash_core_components as dcc
import plotly.express as px
import os
import pandas as pd
import requests
from os.path import exists
import dash_bootstrap_components as dbc
import dash_html_components as html
import json
import csv
from datetime import datetime
from datetime import date
import time

search_url = "https://api.github.com/repos/veeamhub/veeam-healthcheck/releases"
outfile = 'outfile'

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
server = app.server

query_params = {'query': 'download_count'}


def get_date():
    return date.today()
    #print(t)
    #return t.to_string

def write_output(today, total_count):
    data=[today, total_count]
    with open(r'outfile', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def init_output():
    fields=['date','count']
    with open(r'outfile', 'x') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

def meth1():
    print("I'm the run file!")

def get_app():
    return app
def start_program():
    r = requests.get(search_url)
    myobj = r.json()

    total_count = 0
    for p in myobj:
        if "assets" in p:
            for asset in p['assets']:
                total_count += asset['download_count']
                date = asset['updated_at'].split('T')[0]
            
                
        else:
            print ("No data")
    today = datetime.today()
    td = datetime.today().strftime('%Y-%m-%d')
    if exists(outfile):
        write_output(td, total_count)
    else:
        init_output()
        write_output(td,total_count)


    csv_file = pd.read_csv('outfile')
    df = pd.DataFrame(csv_file)
    df = df.drop_duplicates(subset="date",keep='last',inplace=False)

    df['daily_count'] = df['count'].diff()

    #fig = px.scatter(csv_file, x="date", y="count", text="count")
    fig = px.bar(df, x="date", y="count", text="count", title="Cumulative Downloads by Day")
    #fig.update_traces(textposition="top left")
    colors = {"background": "#1d6b5b", "text": "#54b948", "dark": "#005f4b"}
    fig.update_traces(marker_color='#54b948')
    fig.update_layout(
        plot_bgcolor=colors["dark"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
        title={},
            font=dict(color="white", family="Tahoma"),
    )


    
    fig2 = px.line(df, x="date", y="daily_count", markers=True, text="daily_count", title="Daily Download Count")
    fig2.update_traces(textposition="top left",line_color='#54b948')
    fig2.update_layout(
        plot_bgcolor=colors["dark"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
        title={},
            font=dict(color="white", family="Tahoma"),
    )

    app.layout = html.Div(
        style={"backgroundColor": colors["background"]},
        children=[
            html.H1(
                children="vHC Downloads by Date",
                style={"textAlign": "center", "color": "white"},
            ),
            html.Div(
                children="This is a simple graph of total vHC downloads and daily downloads by date.",
                style={"textAlign": "center", "color": "white"},
            ),
            dcc.Graph(id="vHC-Downloads", figure=fig),
            dcc.Graph(id="DownloadsByDay", figure=fig2)
        ]

    )
    return app
