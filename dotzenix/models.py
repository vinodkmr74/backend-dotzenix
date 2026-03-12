from django.db import models
from django.core.validators import RegexValidator

class ContactBar(models.Model):
    email = models.EmailField()
    address = models.CharField(max_length=255)
    mob = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\d{10,15}$',
                message="Mobile number must be 10-15 digits"
            )
        ]
    )
    linkedin = models.URLField() 

    def __str__(self):
        return self.email
    
    #..........menu_item company.............
class MenuItemCompany(models.Model):
    company = models.CharField(max_length=255,blank=True,null=True)
    company_path = models.CharField(max_length=255,blank=True,null=True)
    industries = models.CharField(max_length=255,blank=True,null=True)
    industries_path = models.CharField(max_length=255,blank=True,null=True)      
         
    def __str__(self):
            return self.company or ""
        
#..........menu_item services.............
class MenuItemServices(models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class MenuItemServiceItems(models.Model):
    service = models.ForeignKey(
        MenuItemServices,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=255, blank=True)
    path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    # ..............products...............
class MenuItemProducts(models.Model):
    product = models.CharField(max_length=255,blank=True,)
    product_path = models.CharField(max_length=255,blank=True,)

    def __str__(self):
        return self.product
    
 #..........slider_item.............
class Slider(models.Model):
    image = models.ImageField(upload_to="slider_images/")
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text    
