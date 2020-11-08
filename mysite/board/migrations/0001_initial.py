# Generated by Django 3.1.1 on 2020-09-18 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('detail', models.TextField(max_length=500)),
                ('count', models.IntegerField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='user_upload_files/%Y%m%d/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(max_length=300)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user')),
            ],
        ),
    ]