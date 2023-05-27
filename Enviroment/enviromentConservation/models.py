from django.db import models

class Place(models.Model):
    name = models.CharField(max_length= 200)

    class Meta:
        verbose_name = "Place"
        db_table = "Place"

class ScheduleTask(models.Model):
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    date_used = models.DateTimeField()
    message = models.TextField()

    class Meta:
        verbose_name = "Schedule Task"
        db_table = "Schedule Task"

class NumbersPlace(models.Model):
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    phone_number = models.BigIntegerField()

    class Meta:
        verbose_name = "Numbers Place"
        db_table = "Numbers Place"
