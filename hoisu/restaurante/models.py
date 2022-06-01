from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.



Categoria=(
    ('Buffet', 'Buffet'),
    ('Comida rápida', 'Comida rápida'),
    ('Casual', 'Casual'),
    ('De autor', 'De autor'),
    ('Gourmet', 'Gourmet'),
    ('Temático', 'Temático')
)
Ciudad=(
    ('Armenia', 'Armenia'),
    ('Buenavista', 'Buenavista'),
    ('Calarcá', 'Calarcá'),
    ('Circasia', 'Circasia'),
    ('Córdoba', 'Córdoba'),
    ('Filandia', 'Filandia'),
    ('Génova', 'Génova'),
    ('Montenegro', 'Montenegro'),
    ('Pijao', 'Pijao'),
    ('Salento', 'Salento')
)

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cell = models.CharField(max_length=15, default=0)
    city = models.CharField(max_length=20, choices=Ciudad, default="Armenia")
    price_min = models.CharField(max_length=10)
    price_max = models.CharField(max_length=50)
    menu = models.ImageField(upload_to='restaurant/menu', null=True)
    email = models.EmailField()
    description = models.TextField()
    type = models.CharField(max_length=20, choices=Categoria, default="Gourmet")
    place = models.CharField(max_length=50)
    principal_image = models.ImageField(upload_to='restaurant/principal-img', null=True)
    parking = models.BooleanField()
    credit_card = models.BooleanField()
    debit_card = models.BooleanField()
    slug = models.SlugField(unique=True)



    def __str__(self):
        return self.name


class Users(models.Model):
    userName = models.CharField(max_length=250, primary_key=True)
    names = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    password1 = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)

    def __str__(self):
        return self.userName

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    cell = models.IntegerField()
    customers = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    reservation = models.DateTimeField()

