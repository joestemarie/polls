# Generated by Django 2.2.1 on 2019-06-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='sample_method',
            field=models.CharField(choices=[('LS', 'Listed'), ('RD', 'Random-digit Dialing'), ('PL', 'Panel')], default='RD', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='methodology',
            field=models.CharField(choices=[('Phone', (('LC', 'Live Caller'), ('IV', 'IVR'))), ('Online', (('WS', 'Web Survey'),))], max_length=2),
        ),
    ]
