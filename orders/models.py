from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from utils.generate_code import generate_code
from products.models import Product
from accounts.models import Address

ORDER_STATUS = (
    ('Received', 'Received'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_owner', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=12)
    code = models.CharField(default=generate_code, max_length=8,unique=True)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    delivery_address = models.ForeignKey(Address,related_name='delivery_address',on_delete=models.SET_NULL,null=True, blank=True)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL,null=True,blank=True)
    total = models.FloatField()
    total_with_coupon = models.FloatField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # generate a unique code before saving the order
        if not self.code:
            self.code = generate_code()
            while Order.objects.filter(code=self.code).exists():
                # regenerate code if it already exists
                self.code = generate_code()
        super().save(*args, **kwargs)




class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orderdetail_product',on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()


class Coupon(models.Model):
    code = models.CharField(max_length=20)
    star_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    quantity = models.IntegerField()
    discount = models.FloatField()

    def save(self, *args, **kwargs):
        week = datetime.timedelta(days=7)
        self.end_date = self.star_date + week #adding 7 days
        super(Coupon, self).save(*args, **kwargs)