# Generated by Django 5.0.6 on 2024-06-13 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_question_max_score_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='category',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='result',
            name='difficulty',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.difficulty', verbose_name='Nível'),
        ),
    ]
