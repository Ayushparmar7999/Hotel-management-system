# Generated by Django 5.0.2 on 2024-03-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0010_rename_itemmodel_paymentmodel_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(max_length=200)),
                ('CEmail', models.EmailField(max_length=254)),
                ('CPnumber', models.IntegerField()),
                ('CMessage', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='PaymentModel',
            new_name='ItemModel',
        ),
    ]
