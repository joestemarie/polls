# Generated by Django 2.2.1 on 2019-06-01 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('n_size', models.PositiveIntegerField()),
                ('field_date_start', models.DateField()),
                ('field_date_end', models.DateField()),
                ('release_link', models.URLField()),
                ('methodology', models.CharField(choices=[('P', 'Phone'), ('O', 'Online')], max_length=1)),
                ('sample', models.CharField(choices=[('RV', 'Registered Voters'), ('LV', 'Likely Voters'), ('A', 'Adults')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pollster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_json', models.TextField()),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.Candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.Question')),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='pollster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.Pollster'),
        ),
    ]