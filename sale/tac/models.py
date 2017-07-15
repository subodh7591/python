from django.db import models


class Item(models.Model):
    item_logo=models.CharField(max_length=1000)
    item_name=models.CharField(max_length=100)
    item_price=models.CharField(max_length=50)
    item_status=models.CharField(max_length=40)

class Detail(models.Model):
    item= models.ForeignKey(Item,on_delete=models.CASCADE)
    seller_info=models.CharField(max_length=1000)
    general_detail=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    item_spec=models.CharField(max_length=500)
    delivery=models.CharField(max_length=75)

    def __str__(self):
        return self.seller_info







