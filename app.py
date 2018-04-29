from flask import Flask, render_template, request, redirect, make_response
from matplotlib.figure import Figure
import os
import requests
from Percolation import Percolation
import matplotlib.pyplot as plt, mpld3
import matplotlib as mpl

n = 0;
p = 0;
perc = None;

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def my_form_size():
    s = int(request.form['matrixSize'])
    p = float(request.form['probability'])

    perc = Percolation(s , p)

    plt.figure(figsize=(5,5))
    c = mpl.colors.ListedColormap(['white', 'black', 'blue'])
    n = mpl.colors.Normalize(vmin=0,vmax=2)

    perc.do_flow()
    plt.matshow(perc.a, cmap=c, norm=n)

    fig = plt.gcf()
    html_output = mpld3.fig_to_html(fig)

    return render_template('percolation.html', size = s, prob = p, plot = html_output, percolates = perc.percolates())


if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port, threaded=True)
