# Generated by Django 3.0.4 on 2020-03-11 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phoneapp', '0008_auto_20200311_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=10, verbose_name='小分类名'),
        ),
        migrations.CreateModel(
            name='Sgood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='商品名')),
                ('madedate', models.DateTimeField(auto_now_add=True, verbose_name='生产时间')),
                ('desc', models.CharField(max_length=10, verbose_name='描述')),
                ('price', models.IntegerField(default=188, verbose_name='价格')),
                ('view', models.IntegerField(default=0, verbose_name='浏览量')),
                ('img', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sgoods', to='phoneapp.Category', verbose_name='小分类')),
            ],
        ),
    ]