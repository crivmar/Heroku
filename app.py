## IMPORTAR LIBRERIAS Y MODULOS ##

from flask import Flask, render_template, abort
import os, json

app= Flask(__name__)

## GUARDAR LA INFORMACIÓN ##

with open('./books.json') as f:
    documento=json.load(f)


## PROGRAMA PRINCIPAL ##

@app.route ('/', methods=["GET","POST"])
def index():
    return render_template("index.html",documento=documento)    




port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)