# Generated by Django 4.1.4 on 2023-01-02 10:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='appcafe.article')),
            ],
        ),
    ]
