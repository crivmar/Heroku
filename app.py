## IMPORTAR LIBRERIAS Y MODULOS ##

from flask import Flask, render_template, abort
import os, json

app= Flask(__name__)






port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)