from django.db import models

class Contract(models.Model):   
    name = models.CharField(max_length=10000,default='no name')
    Desciption =  models.TextField(max_length=10000)
    try_days=  models.SmallIntegerField(default=7)
    start_date= models.DateField(auto_now_add=True)
    end_date= models.DateField()
    Cost= models.IntegerField()
    is_active= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
