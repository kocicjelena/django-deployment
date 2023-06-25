from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     """
#     User Profile 
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     city = models.CharField(max_length=30, blank=True)
#     dob = models.DateField(null=True, blank=True)


# class MyCustomUser(models.Model):
#   # user fields
  
#   def save(self, *args, **kwargs):
#     super(MyCustomUser, self).save(*args, **kwargs)
#     profile = Profile(user=self)
#     profile.save()

# fruits ={
#     ('Apple','Apple'),
#     ('Mango','Mango'),
#     ('Banana','Banana'),
#     ('Orange','Orange')
# }
 
# class Stock(models.Model):
#     available_item = models.CharField(max_length=10, choices=fruits)
#     available_quantity = models.IntegerField()
 
#     def __str__(self):
#         return self.available_item
 
#     class Meta:
#         verbose_name = 'Stock'
#         verbose_name_plural = 'Stocks'

# class Purchase(models.Model):
#     item = models.CharField(max_length=10, choices=fruits)
#     quantity = models.IntegerField()
 
#     def __str__(self):
#         return self.item
 
#     class Meta:
#         verbose_name = 'Purchase'
#         verbose_name_plural = 'Purchases'

# class Topping(models.Model):
#     # ...
#     pass

# class Pizza(models.Model):
#     # ...
#     toppings = models.ManyToManyField(Topping)