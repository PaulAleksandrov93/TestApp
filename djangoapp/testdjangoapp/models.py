from django.db import models

class CMenu(models.Model):
    name = models.CharField('Name', max_length=100)
    url = models.CharField('Link', max_length=255)
    position = models.PositiveBigIntegerField('Position', default=1)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('position',)
        verbose_name = 'menu items'


