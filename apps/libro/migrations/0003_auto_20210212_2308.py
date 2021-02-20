# Generated by Django 3.1.3 on 2021-02-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('chasis', models.CharField(max_length=15)),
                ('noPlaca', models.CharField(blank=True, max_length=20)),
                ('compania', models.CharField(blank=True, max_length=50)),
                ('fechaOrden', models.CharField(blank=True, max_length=20)),
                ('endoso', models.CharField(blank=True, max_length=20)),
                ('FechaEndoso', models.CharField(blank=True, max_length=20)),
                ('Estado', models.CharField(choices=[('Pendiente de Placa', 'Pendiente de Placa'), ('placa y matricula', 'placa y matricula'), ('placa y copia M.', 'placa y copia M.'), ('placa entregada', 'placa entregada'), ('Endosando', 'Endosando'), ('Matricula Lista', 'Matricula Lista'), ('placa y M. Entregada', 'placa y M. Entregada')], default=None, max_length=22)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cedula', models.BooleanField(default=True)),
                ('Comentario', models.TextField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
