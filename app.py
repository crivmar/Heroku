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
    mensaje=""
    for i in documento:
        if isbn==i.get("isbn"):
            try:
                titulo=i.get('title')
                miniatura=i.get('thumbnailUrl')
                num=i.get('pageCount')
                desc=i.get('longDescription')
                autor=i.get('authors')
                cate=i.get('categories')
                if i.get('status')=='MEAP':
                    mensaje='Este libro no ha sido publicado.'
            except:
                abort(404)
    return render_template("detalle.html",titulo=titulo,miniatura=miniatura, num=num, desc=desc, autor=autor, cate=cate, mensaje=mensaje)

@app.route('/categoria/<categoria>', methods=["GET","POST"])
def categoria(categoria):

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)