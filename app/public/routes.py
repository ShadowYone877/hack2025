from flask import jsonify, json

import logging
from sqlalchemy import text 

from flask import abort, render_template, redirect, url_for, request, current_app
from flask_login import current_user

# from app.models import Post, Comment
from . import public_bp
from .forms import CommentForm
from app import db

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
#     logger.info('Mostrando los posts del blog')
#     page = int(request.args.get('page', 1))
#     per_page = current_app.config['ITEMS_PER_PAGE']
#     post_pagination = Post.all_paginated(page, per_page)
    return render_template("public/index.html")

@public_bp.route("/getEscuela")
def getEscuela():
    print("Hola")
    
    # Esta es la sintaxis correcta de Python: claves entre comillas
    esc = [
        {
            "id": 1,
            "name": "Escuela 1",
            "description": "Descripción",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Escuela_1.jpg/320px-Escuela_1.jpg",
        }, 
        {
            "id": 2,
            "name": "Escuela 2",
            "description": "Descripción",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Escuela_1.jpg/320px-Escuela_1.jpg"
        }, 
               {
            "id": 3,
            "name": "Escuela 3",
            "description": "Descripción",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Escuela_1.jpg/320px-Escuela_1.jpg"
        }
    ]

    # Devuelve la lista como una respuesta JSON
    return jsonify(esc)

# app/public/routes.py

@public_bp.route("/dataBase")
def dataBase():
    # Usar db.session.execute para consultas SQL directas
    try:
        # Usa db.text() si no es Flask-SQLAlchemy 3.x
        
        # Ejecutar la consulta SQL
        result_proxy = db.session.execute(text("SELECT * FROM institucion;"))
        # print(result_proxy.fetchall())
        # Convertir los resultados a una lista de diccionarios (similar a cursor(dictionary=True))
        results = [dict(row) for row in result_proxy.mappings()]
        #print (results)
        #results = result_proxy.fetchall()
        print(results)
        return (results)# Flask convertirá la lista de diccionarios a JSON
        
    except Exception as e:
        # Manejar errores de la base de datos
        print(f"Error de base de datos: {e}")
        return {"error": "No se pudo conectar o ejecutar la consulta"}, 500


@public_bp.route("/getDataBase")
def getDataBase():
    return render_template("public/index2.html")




# @public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
# def show_post(slug):
#     logger.info('Mostrando un post')
#     logger.debug(f'Slug: {slug}')
#     post = Post.get_by_slug(slug)
#     if not post:
#         logger.info(f'El post {slug} no existe')
#         abort(404)
#     form = CommentForm()
#     if current_user.is_authenticated and form.validate_on_submit():
#         content = form.content.data
#         comment = Comment(content=content, user_id=current_user.id,
#                           user_name=current_user.name, post_id=post.id)
#         comment.save()
#         return redirect(url_for('public.show_post', slug=post.title_slug))
#     return render_template("public/post_view.html", post=post, form=form)


# @public_bp.route("/error")
# def show_error():
#     res = 1 / 0
#     posts = Post.get_all()
#     return render_template("public/index.html", posts=posts)
