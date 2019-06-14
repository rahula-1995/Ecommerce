from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50,default='Nothing')
    desc = models.CharField(max_length=300,default='NOTHING')
    pub_date = models.DateField(default='2019-10-15')
    image = models.ImageField(upload_to='shop/images', default="")
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name