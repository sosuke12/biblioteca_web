# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Autor(models.Model):
    id_autor = models.AutoField(db_column='id_Autor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autor'


class AutorHasDocumental(models.Model):
    autor_id_autor = models.ForeignKey(Autor, db_column='Autor_id_Autor')  # Field name made lowercase.
    documental_id_documental = models.ForeignKey('Documental', db_column='Documental_id_Documental')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autor_has_documental'
        unique_together = (('Autor_id_Autor', 'Documental_id_Documental'),)


class AutorHasLibro(models.Model):
    autor_id_autor = models.ForeignKey(Autor, db_column='Autor_id_Autor')  # Field name made lowercase.
    libro_id_libro = models.ForeignKey('Libro', db_column='Libro_id_Libro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autor_has_libro'
        unique_together = (('Autor_id_Autor', 'Libro_id_Libro'),)


class Carnet(models.Model):
    id_carnet = models.IntegerField(db_column='id_Carnet')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario_id_usuario = models.ForeignKey('Usuario', db_column='Usuario_id_Usuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carnet'
        unique_together = (('id_Carnet', 'Usuario_id_Usuario'),)


class Documental(models.Model):
    id_documental = models.AutoField(db_column='id_Documental', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=45)  # Field name made lowercase.
    ejemplar = models.IntegerField(db_column='Ejemplar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documental'


class DocumentalHasTema(models.Model):
    documental_id_documental = models.ForeignKey(Documental, db_column='Documental_id_Documental')  # Field name made lowercase.
    tema_id_tema = models.ForeignKey('Tema', db_column='Tema_id_Tema')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documental_has_tema'
        unique_together = (('Documental_id_Documental', 'Tema_id_Tema'),)


class Editoriales(models.Model):
    id_editoriales = models.AutoField(db_column='id_Editoriales', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'editoriales'


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleados'


class Estanteria(models.Model):
    id_estanteria = models.AutoField(db_column='id__Estanteria', primary_key=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    codigo = models.CharField(db_column='Codigo', unique=True, max_length=45)  # Field name made lowercase.
    lugar = models.CharField(db_column='Lugar', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estanteria'


class Libro(models.Model):
    id_libro = models.AutoField(db_column='id_Libro', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=70)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=45)  # Field name made lowercase.
    ejemplares = models.IntegerField(db_column='Ejemplares')  # Field name made lowercase.
    editoriales_id_editoriales = models.ForeignKey(Editoriales, db_column='Editoriales_id_Editoriales')  # Field name made lowercase.
    estanteria_id_estanteria = models.ForeignKey(Estanteria, db_column='Estanteria_id__Estanteria')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'libro'


class LibroDigital(models.Model):
    id_libro_digital = models.IntegerField(db_column='id_Libro_digital', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=70, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    editoriales_id_editoriales = models.ForeignKey(Editoriales, db_column='Editoriales_id_Editoriales')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'libro_digital'


class LibroDigitalHasAutor(models.Model):
    libro_digital_id_libro_digital = models.ForeignKey(LibroDigital, db_column='Libro_digital_id_Libro_digital')  # Field name made lowercase.
    autor_id_autor = models.ForeignKey(Autor, db_column='Autor_id_Autor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'libro_digital_has_autor'
        unique_together = (('Libro_digital_id_Libro_digital', 'Autor_id_Autor'),)


class LibroHasTema(models.Model):
    libro_id_libro = models.ForeignKey(Libro, db_column='Libro_id_Libro')  # Field name made lowercase.
    tema_id_tema = models.ForeignKey('Tema', db_column='Tema_id_Tema')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'libro_has_tema'
        unique_together = (('Libro_id_Libro', 'Tema_id_Tema'),)


class Periodicos(models.Model):
    id_periodicos = models.IntegerField(db_column='id_Periodicos', primary_key=True)  # Field name made lowercase.
    fecha_publicacion = models.DateField(db_column='Fecha_publicacion')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodicos'


class Prestamos(models.Model):
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    fecha_limite = models.DateField()
    multa = models.IntegerField()
    usuario_id_usuario = models.ForeignKey('Usuario', db_column='Usuario_id_Usuario', primary_key=True)  # Field name made lowercase.
    libro_id_libro = models.ForeignKey(Libro, db_column='Libro_id_Libro', blank=True, null=True)  # Field name made lowercase.
    periodicos_id_periodicos = models.ForeignKey(Periodicos, db_column='Periodicos_id_Periodicos', blank=True, null=True)  # Field name made lowercase.
    documental_id_documental = models.ForeignKey(Documental, db_column='Documental_id_Documental', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prestamos'


class Tema(models.Model):
    id_tema = models.AutoField(db_column='id_Tema', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=45)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tema'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='id_Usuario', primary_key=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', unique=True, max_length=15)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=60)  # Field name made lowercase.
    carnet_id = models.CharField(db_column='Carnet_id', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    documental_id_documental = models.ForeignKey(Documental, db_column='Documental_id_Documental')  # Field name made lowercase.
    periodicos_id_periodicos = models.ForeignKey(Periodicos, db_column='Periodicos_id_Periodicos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
