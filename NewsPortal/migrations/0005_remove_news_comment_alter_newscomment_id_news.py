# Generated by Django 4.1.5 on 2023-05-11 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0004_newscomment_id_news_alter_news_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comment',
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='id_news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.news', verbose_name='Новость'),
        ),
    ]
