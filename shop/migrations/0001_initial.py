# Generated by Django 4.0.6 on 2022-07-17 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_products/', verbose_name='Изображение товара')),
                ('name', models.CharField(max_length=30, verbose_name='Название товара')),
                ('text', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата объявления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
