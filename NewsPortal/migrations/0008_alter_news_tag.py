# Generated by Django 4.2 on 2023-05-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0007_alter_news_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='NewsPortal.newstag', verbose_name='Теги'),
        ),
    ]