from django.db import models

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=15)  # Changed to CharField for better handling

    def __str__(self):
        return self.name  # Return name instead of id for better readability


# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')  # Organized images

    def __str__(self):
        return self.product_name  # Returns product name in admin panel


# Orders Model
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    oid = models.CharField(max_length=150, blank=True)
    amountpaid = models.CharField(max_length=500, blank=True)
    payment_status = models.CharField(max_length=20, blank=True)  # Fixed typo
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"Order {self.order_id} - {self.name}"  # Meaningful string


# Order Updates Model
class OrderUpdate(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=1)  # Add default=1 temporarily
    update_desc = models.TextField()

    
    def __str__(self):
        return self.update_desc[:7] + "...."
