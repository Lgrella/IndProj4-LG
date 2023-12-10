from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
#books_df = pd.read_csv('books.csv')

@app.route('/')
def index():
    return "Welcome to my flask app!"