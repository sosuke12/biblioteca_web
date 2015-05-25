# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(serialize=False, primary_key=True, db_column='id_Autor')),
                ('nombre', models.CharField(max_length=45, db_column='Nombre')),
                ('nacionalidad', models.CharField(max_length=45, db_column='Nacionalidad')),
            ],
            options={
                'db_table': 'autor',
            },
        ),
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id_carnet', models.IntegerField(serialize=False, primary_key=True, db_column='id_Carnet')),
                ('codigo', models.CharField(max_length=45, null=True, db_column='Codigo', blank=True)),
            ],
            options={
                'db_table': 'carnet',
            },
        ),
        migrations.CreateModel(
            name='Documental',
            fields=[
                ('id_documental', models.AutoField(serialize=False, primary_key=True, db_column='id_Documental')),
                ('titulo', models.CharField(max_length=45, db_column='Titulo')),
                ('ejemplar', models.IntegerField(db_column='Ejemplar')),
            ],
            options={
                'db_table': 'documental',
            },
        ),
        migrations.CreateModel(
            name='Editoriales',
            fields=[
                ('id_editoriales', models.AutoField(serialize=False, primary_key=True, db_column='id_Editoriales')),
                ('nombre', models.CharField(max_length=45, db_column='Nombre')),
                ('direccion', models.CharField(unique=True, max_length=45, db_column='Direccion')),
            ],
            options={
                'db_table': 'editoriales',
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, db_column='Nombre')),
                ('codigo', models.CharField(max_length=45, db_column='Codigo')),
            ],
            options={
                'db_table': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Estanteria',
            fields=[
                ('id_estanteria', models.AutoField(serialize=False, primary_key=True, db_column='id__Estanteria')),
                ('codigo', models.CharField(unique=True, max_length=45, db_column='Codigo')),
                ('lugar', models.CharField(max_length=300, db_column='Lugar')),
            ],
            options={
                'db_table': 'estanteria',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(serialize=False, primary_key=True, db_column='id_Libro')),
                ('titulo', models.CharField(max_length=70, db_column='Titulo')),
                ('isbn', models.CharField(unique=True, max_length=45, db_column='ISBN')),
                ('ejemplares', models.IntegerField(db_column='Ejemplares')),
            ],
            options={
                'db_table': 'libro',
            },
        ),
        migrations.CreateModel(
            name='LibroDigital',
            fields=[
                ('id_libro_digital', models.IntegerField(serialize=False, primary_key=True, db_column='id_Libro_digital')),
                ('titulo', models.CharField(max_length=70, null=True, db_column='Titulo', blank=True)),
                ('isbn', models.CharField(max_length=45, null=True, db_column='ISBN', blank=True)),
            ],
            options={
                'db_table': 'libro_digital',
            },
        ),
        migrations.CreateModel(
            name='Periodicos',
            fields=[
                ('id_periodicos', models.IntegerField(serialize=False, primary_key=True, db_column='id_Periodicos')),
                ('fecha_publicacion', models.DateField(db_column='Fecha_publicacion')),
                ('nombre', models.CharField(unique=True, max_length=45, db_column='Nombre')),
                ('cantidad', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'periodicos',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id_tema', models.AutoField(serialize=False, primary_key=True, db_column='id_Tema')),
                ('nombre', models.CharField(unique=True, max_length=45, db_column='Nombre')),
                ('descripcion', models.CharField(max_length=45, null=True, db_column='Descripcion', blank=True)),
            ],
            options={
                'db_table': 'tema',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(serialize=False, primary_key=True, db_column='id_Usuario')),
                ('dni', models.CharField(unique=True, max_length=15, db_column='DNI')),
                ('nombre', models.CharField(max_length=60, db_column='Nombre')),
                ('carnet_id', models.CharField(max_length=45, unique=True, null=True, db_column='Carnet_id', blank=True)),
                ('correo', models.CharField(max_length=45, unique=True, null=True, db_column='Correo', blank=True)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='AutorHasLibro',
            fields=[
                ('autor_id_autor', models.ForeignKey(primary_key=True, db_column='Autor_id_Autor', to='pagina.Autor')),
                ('libro_id_libro', models.ForeignKey(primary_key=True, db_column='Libro_id_Libro', serialize=False, to='pagina.Libro')),
            ],
            options={
                'db_table': 'autor_has_libro',
            },
        ),
        migrations.CreateModel(
            name='LibroDigitalHasAutor',
            fields=[
                ('libro_digital_id_libro_digital', models.ForeignKey(primary_key=True, db_column='Libro_digital_id_Libro_digital', serialize=False, to='pagina.LibroDigital')),
                ('autor_id_autor', models.ForeignKey(primary_key=True, db_column='Autor_id_Autor', to='pagina.Autor')),
            ],
            options={
                'db_table': 'libro_digital_has_autor',
            },
        ),
        migrations.CreateModel(
            name='LibroHasTema',
            fields=[
                ('libro_id_libro', models.ForeignKey(primary_key=True, db_column='Libro_id_Libro', serialize=False, to='pagina.Libro')),
                ('tema_id_tema', models.ForeignKey(primary_key=True, db_column='Tema_id_Tema', to='pagina.Tema')),
            ],
            options={
                'db_table': 'libro_has_tema',
            },
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField(null=True, blank=True)),
                ('fecha_limite', models.DateField()),
                ('multa', models.IntegerField()),
                ('usuario_id_usuario', models.OneToOneField(primary_key=True, db_column='Usuario_id_Usuario', serialize=False, to='pagina.Usuario')),
                ('documental_id_documental', models.ForeignKey(to='pagina.Documental', db_column='documental_id_documental')),
            ],
            options={
                'db_table': 'prestamos',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='documental_id_documental',
            field=models.ForeignKey(to='pagina.Documental', db_column='Documental_id_Documental'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='periodicos_id_periodicos',
            field=models.ForeignKey(to='pagina.Periodicos', db_column='Periodicos_id_Periodicos'),
        ),
        migrations.AddField(
            model_name='librodigital',
            name='editoriales_id_editoriales',
            field=models.ForeignKey(to='pagina.Editoriales', db_column='Editoriales_id_Editoriales'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editoriales_id_editoriales',
            field=models.ForeignKey(to='pagina.Editoriales', db_column='Editoriales_id_Editoriales'),
        ),
        migrations.AddField(
            model_name='libro',
            name='estanteria_id_estanteria',
            field=models.ForeignKey(to='pagina.Estanteria', db_column='Estanteria_id__Estanteria'),
        ),
        migrations.AddField(
            model_name='carnet',
            name='usuario_id_usuario',
            field=models.OneToOneField(db_column='Usuario_id_Usuario', to='pagina.Usuario'),
        ),
        migrations.AddField(
            model_name='prestamos',
            name='libro_id_libro',
            field=models.ForeignKey(to='pagina.Libro', db_column='Libro_id_Libro'),
        ),
        migrations.AddField(
            model_name='prestamos',
            name='periodico_id_periodico',
            field=models.ForeignKey(to='pagina.Periodicos', db_column='periodico_id_periodico'),
        ),
        migrations.AddField(
            model_name='librodigital',
            name='autores',
            field=models.ManyToManyField(to='pagina.Autor', through='pagina.LibroDigitalHasAutor'),
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='pagina.Autor', through='pagina.AutorHasLibro'),
        ),
        migrations.AddField(
            model_name='libro',
            name='temas',
            field=models.ManyToManyField(to='pagina.Tema', through='pagina.LibroHasTema'),
        ),
        migrations.AddField(
            model_name='autor',
            name='libros',
            field=models.ManyToManyField(to='pagina.Libro', through='pagina.AutorHasLibro'),
        ),
    ]
