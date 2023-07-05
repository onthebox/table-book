from django.db import models


class RestaurantChain(models.Model):
    chain_name = models.CharField(max_length=256)
    chain_id = models.AutoField(primary_key=True, db_column='chain_id')
    
    def __str__(self):
        return f'{self.chain_name}'
    
    class Meta:
        db_table = 'restaurant_chain'


class BranchAddress(models.Model):
 
    country_name = models.CharField(max_length=512)
    city_name = models.CharField(max_length=512)
    street_name = models.CharField(max_length=512)
    building_name = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'branch_adress'


class RestaurantBranch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    chain_id = models.ForeignKey(RestaurantChain, on_delete=models.CASCADE, db_column='chain_id')
    contact_number = models.IntegerField()
    email = models.CharField()
    number_of_tables = models.IntegerField()
    address = models.OneToOneField(BranchAddress, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.chain_id}'
    
    class Meta:
        db_table = 'restaurant_branch'



