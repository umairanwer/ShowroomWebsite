from django.db import models

# Create your models here.

class Showroom(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    telephone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    staff_pic = models.ImageField(null=True, blank=True)

    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name='showroom', null=True)

    def __str__(self):
        return self.name
    
class CarBrand(models.Model):
    name = models.CharField(max_length=50, null=True)
    pic =  models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    pic =  models.ImageField(null=True, blank=True)
    carBrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=True, related_name='carbrand')

    def __str__(self):
        return self.name
    
    def get_pic_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
        else:
            return '/media/car_placeholder.png'

class Engine(models.Model):
    name = models.CharField(max_length=50, default='None Selected', null=True)
    engCapacity = models.IntegerField(null=True)
    engNum =  models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.engNum

class CarFeature(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    name = models.CharField(max_length=50, default='Unnamed')
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    mileage = models.IntegerField(null=True)
    pic =  models.ImageField(null=True, blank=True)
    chassis_num = models.CharField(max_length=50, primary_key=True)

    carModel = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='carmodels', null=True)
    features = models.ManyToManyField(CarFeature, related_name='features')
    engine = models.OneToOneField(Engine, on_delete=models.CASCADE, related_name='engine', default='None')

    def __str__(self):
        return self.name
    
    def get_pic_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
        else:
            return '/media/car_placeholder.png'

    def get_price(self):
        return f'{self.price:,}'