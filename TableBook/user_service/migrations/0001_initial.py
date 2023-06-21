# Generated by Django 4.2.2 on 2023-06-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantChain',
            fields=[
                ('chain_name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('chain_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantBranch',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_service.restaurantchain')),
            ],
        ),
    ]
