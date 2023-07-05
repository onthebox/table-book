from django.db import models

# Create your models here.


class RestaurantChain(models.Model):
    chain_id = models.AutoField(primary_key=True, db_column='chain_id')
    chain_name = models.CharField(max_length=256)

    class Meta:
        db_table = 'restaurant_chain'


class RestaurantBranch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    chain_id = models.ForeignKey(RestaurantChain, on_delete=models.CASCADE, db_column='chain_id', related_name='branches')
    contact_number = models.CharField(max_length=12)  # For example +12345678901
    email = models.EmailField(max_length=250)
    number_of_tables = models.IntegerField()

    class Meta:
        db_table = 'restaurant_branch'


class BranchAdress(models.Model):
    branch_id = models.OneToOneField(RestaurantBranch, on_delete=models.CASCADE, primary_key=True, db_column='branch_id')
    country_name = models.CharField(max_length=512)
    city_name = models.CharField(max_length=512)
    street_name = models.CharField(max_length=512)
    building_name = models.CharField(max_length=256)

    class Meta:
        db_table = 'branch_adress'


class BranchSeatings(models.Model):
    branch_id = models.OneToOneField(RestaurantBranch, on_delete=models.CASCADE, primary_key=True, db_column='branch_id')
    current_seatings = models.JSONField()
