from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30, unique=True)
    short_description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='imgs', blank=True, null=True)
    slug = models.SlugField(max_length=30)

    def __str__(self):
    	return self.product_name


class Advantage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	short_advant_name = models.CharField(max_length=30)
	short_advant_description = models.CharField(max_length=255)

	def __str__(self):
		return self.product.product_name

class Description(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	desc_image = models.ImageField(upload_to='imgs', blank=True, null=True)
	desc_text = models.TextField()

	def __str__(self):
		return self.product.product_name