#pip3 install dash
#pip3 install dash-bootstrap-components
#pip3 install requests
#pip3 install pandas

#from cgitb import text
#from click import style
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
from run_File import *




# while(True):
#     if __name__ == "__main__":
#         app = start_program()
#         app.run_server(debug=True)
#     print("sleeping..")
#     time.sleep(60)
#     print("starting...")
app = start_program()

if __name__ == "__main__":
    app.run_server(debug=True)