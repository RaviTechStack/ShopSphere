# Generated by Django 4.1.5 on 2024-07-26 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wblog', '0006_comment_prod_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('prod_quantity', models.IntegerField(default=1)),
                ('prod_color', models.CharField(max_length=50)),
                ('prod_size', models.CharField(max_length=3)),
                ('orderUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wblog.allproducts')),
            ],
        ),
    ]
