# app/models.py

# 1. Importamos el único objeto 'db' que necesitamos
#    Este objeto 'db' fue creado en tu app/__init__.py
from . import db

# Esta clase representa la tabla "institucion" que creaste manualmente
class Institucion(db.Model):
    
    # El nombre exacto de la tabla en PostgreSQL
    __tablename__ = 'institucion'

    # --- Columnas que coinciden con tu "CREATE TABLE" ---
    
    # id (serial primary key) se mapea a db.Integer, primary_key=True
    id = db.Column(db.Integer, primary_key=True)
    
    # escuela (varchar(150)) se mapea a db.String(150)
    escuela = db.Column(db.String(150), nullable=True)
    
    # localidad (varchar(100)) se mapea a db.String(100)
    localidad = db.Column(db.String(100), nullable=True)
    
    # requerimiento (text) se mapea a db.Text
    requerimiento = db.Column(db.Text, nullable=True)

    # Nota:
    # Dejamos nullable=True porque en tu comando "CREATE TABLE".

    def __repr__(self):
        # Función opcional para ayudar a depurar
        return f'<Institucion {self.escuela}>'