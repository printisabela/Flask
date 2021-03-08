from app import app
from flask import request, render_template, redirect, url_for
from app.models.forms import ComentarioForm
from app.models.carro import Carro
from app.models.comentario import Comentario

from app import db




@app.route("/carros")
def carros():


  carros = Carro.query.all()
  return render_template("carros.html", carros=carros)

@app.route("/comentarios/<int:id>/novo", methods=['GET', 'POST'])
def novo_comentario(id):
  form = ComentarioForm()
  carro = Carro.query.get(id)
  if form.validate_on_submit():
    c = Comentario(nome_usuario=form.nome.data, corpo=form.corpo.data,
      autor=carro,
      nota=form.nota.data)
    db.session.add(c)
    db.session.commit()
    return redirect(url_for("carros"))
  return render_template("comentario_novo.html", form=form)

@app.route("/comentarios/<int:id>", methods=['GET', 'POST'])
def comentarios(id):
  carro = Carro.query.get(id)
  print(carro)
  comentarios = carro.comentarios
  print(comentarios)
  return render_template("comentarios.html", comentarios=comentarios)