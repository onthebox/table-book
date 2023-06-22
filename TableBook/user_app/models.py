from django.db import models
from user_service.models import RestaurantBranch
# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='user_id')
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class ReserveTables(models.Model):
    reservation_id = models.AutoField(primary_key=True, db_column='reservation_id')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    branch_id = models.ForeignKey(RestaurantBranch, on_delete=models.CASCADE, db_column='branch_id')
    table_id = models.IntegerField(db_column='table_id')
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    class Meta:
        db_table = 'reserved_tables'
