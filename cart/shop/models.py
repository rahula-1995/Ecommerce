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
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
class Users(models.Model):
    userid=models.AutoField(primary_key=True)
    email=models.CharField(max_length=90)
    password=models.CharField(max_length=90)