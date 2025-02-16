from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.CharField(max_length=100)
    is_booked = models.BooleanField()

class Booking(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)