
from flask import Flask, request, render_template
import pandas as pd
from hybrid_model import recommend_hybrid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = recommend_hybrid(query)
        return render_template('results.html', results=results)
    return render_template('index.html')
