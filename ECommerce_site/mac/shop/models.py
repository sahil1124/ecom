from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default=" ")
    subcategory=models.CharField(max_length=50,default=" ")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=3000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default=" ")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,default=" ")
    phone=models.IntegerField(default=" ")
    desc=models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=500)
    zip_code=models.CharField(max_length=111)
    phone=models.IntegerField(default=" ")



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
