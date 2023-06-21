from dev_utils import classes
from django.db import models


class RestaurantChain(classes.DevRepr, models.Model):

    chain_name = models.CharField(max_length=250, primary_key=True)
    chain_id = models.IntegerField()


class RestaurantBranch(classes.DevRepr, models.Model):

    branch_id = models.IntegerField(primary_key=True)
    branch_name = models.ForeignKey(RestaurantChain, on_delete=models.CASCADE)
