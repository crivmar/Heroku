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

@app.route('/libro/<isbn>', methods=["GET","POST"])
def detalle(isbn):
    v=False
    for i in documento:
        if i.get('isbn')==isbn:
            titulo=i.get('title')
            miniatura=i.get('thumbnailUrl')
            num=i.get('pageCount')
            desc=i.get('longDescription')
            autor=i.get('authors')
            cate=i.get('categories')
            if i.get('status')=='MEAP':
                v=True     
    return render_template("detalle.html",titulo=titulo,miniatura=miniatura, num=num, desc=desc, autor=autor, cate=cate, v=v)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)