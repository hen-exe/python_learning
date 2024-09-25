# to run: python 2_funfact.py

import json # used to work with JSON data
import requests  # send HTTP requests using Python
from pywebio.input import * # build web apps for python
from pywebio.output import *
from pywebio.session import *

def get_fun_fact():
    clear()

    # URL
    url = "https://catfact.ninja/fact"

    # GET request
    response = requests.get(url)

    # convert JSON to Python
    data = json.loads(response.text)
    
    # get fact from data
    cat_fact = data['fact']

    put_column([
        put_html('''
        <div style="padding: 5px; text-align:center; font-family:Arial; background-color:#f5e3b8; border-radius:5px; margin-bottom:10px;">
            <h2 style="font-size:30px; color:#9c7616;">Cat Fun Facts</h2
        </div>
    '''),
        style(put_text(cat_fact), "color:#b3891e; font-size:18px; text-align:center; margin-top:10px;"),

        put_button(
            "Click me!", color="secondary",
            onclick=get_fun_fact # no parenthesis so it can wait for button click
        )
    ])

   

if __name__ == '__main__':
    put_column([
        put_html('''
        <div style="padding: 5px; text-align:center; font-family:Arial; background-color:#f5e3b8; border-radius:5px; margin-bottom:10px;">
            <h2 style="font-size:30px; color:#9c7616;">Cat Fun Facts</h2
        </div>
    '''),
        put_button(
            "Click me!", color="secondary",
            onclick=get_fun_fact # no parenthesis so it can wait for button click
        )
    ])
    
    hold()