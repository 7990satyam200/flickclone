from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class harvest_type(models.Model):
    """
    Model representing a Crop Genre
    """
    crop_type = models.CharField(max_length= 50, unique = True)
    crop_type_description = models.CharField(max_length = 300)
    crop_type_image = models.ImageField(upload_to='crop_type_image', blank=True)
    def get_absolute_url(self):
        return reverse('sale_crop_proceeds')
    def __str__(self):
        return self.crop_type


class crops(models.Model):
    """
    Model representing a specific crop of Genre
    (i.e. Tea is specific type of plantation of crops).
    """
    crop_name = models.CharField(max_length =50)
    crop_description = models.CharField(max_length= 300)
    crop_image = models.ImageField(upload_to='crop_image', blank=True)
    crop_harvest_type = models.ForeignKey(harvest_type, related_name = 'crops', on_delete='CASCADE')
    def __str__(self):
        return self.crop_name
    def get_absolute_url(self):
        return reverse('sellCrop', args = [str(self.id)])



class sell_harvested_crops(models.Model):
    """
    Model representing a accepting details from farmers for assisting
    in making sell of harvested crops.
    """
    quantity = models.IntegerField(default = 0, help_text= 'In tonnes')
    farm_image = models.ImageField(upload_to='farm_image', blank=True)
    harvest_variety= models.CharField(max_length= 100)
    h_description = models.CharField(max_length = 500)
    crops = models.ForeignKey(crops, related_name = 'sellCrops', on_delete = 'CASCADE')
    sold_by = models.ForeignKey(User, related_name='farmers', on_delete='CASCADE')

    PREMIUM = 'P'
    VERY_GOOD = 'VG'
    GOOD = 'G'
    JUST_RIGHT = 'JR'
    quality_standards = [
        (PREMIUM, 'PREMIUM'),
        (VERY_GOOD, 'VERY GOOD'),
        (GOOD, 'GOOD'),
        (JUST_RIGHT, 'JUST RIGHT'),
    ]
    quality = models.CharField(
        max_length=2,
        choices=quality_standards,
        default=PREMIUM,
        blank = True,
        help_text='Quality of crop'
        )
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}  {1} sold by {2}'.format(self.quality, self.crops, self.sold_by)




class buy_harvested_Crop(models.Model):
    """
    Model for buy harvested crops against the sale made by farmer.
    """
    quantity = models.IntegerField(default =0, help_text = 'In tonnes')
    buy_crops = models.ForeignKey(sell_harvested_crops, related_name = 'buy_harvested_Crops', on_delete= 'CASCADE')
    buyer =  models.ForeignKey(User, related_name='mybuyers', on_delete='CASCADE')
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} tonnes {1} ordered by {2}'.format(self.quantity, self.buy_crops, self.buyer)
