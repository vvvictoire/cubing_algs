# Generated by Django 3.1 on 2020-08-25 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algs_site', '0006_auto_20200820_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithm',
            name='algorithm_set',
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/case')),
                ('alt_text', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=200)),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algs_site.puzzle')),
            ],
        ),
        migrations.AddField(
            model_name='algorithm',
            name='case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='algs_site.case'),
        ),
    ]
