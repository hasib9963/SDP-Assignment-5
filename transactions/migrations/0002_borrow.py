# Generated by Django 4.2.7 on 2024-02-14 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_images'),
        ('readers', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('borrow_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.userlibraryaccount')),
            ],
        ),
    ]
