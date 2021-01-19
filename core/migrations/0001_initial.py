# Generated by Django 3.1.3 on 2021-01-12 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('reportagem', models.TextField(max_length=800)),
                ('autor', models.CharField(max_length=50)),
                ('tweet', models.TextField(blank=True, max_length=500)),
                ('url_foto', models.TextField(blank=True, max_length=500)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=255)),
                ('data', models.DateField(auto_now_add=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='core.noticia')),
            ],
        ),
    ]
