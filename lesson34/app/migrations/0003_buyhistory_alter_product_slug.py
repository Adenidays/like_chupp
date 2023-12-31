# Generated by Django 4.2.6 on 2023-10-20 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyHistory',
            fields=[
                ('cart_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.cart')),
                ('buy_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('app.cart',),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
