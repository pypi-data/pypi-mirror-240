# Generated by Django 3.1.14 on 2022-05-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_merge_20220512_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='total_annotations',
            field=models.IntegerField(db_index=True, default=0, help_text='Number of total annotations for the current task except cancelled annotations', verbose_name='total_annotations'),
        ),
    ]
