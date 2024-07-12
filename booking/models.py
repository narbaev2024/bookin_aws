from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=16)
    country = models.CharField(max_length=16)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField(default=0)
    capacity = models.CharField(max_length=32)
    price_per_night = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.capacity

class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')


class Booking(models.Model):
    user = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ("Бронь", "Бронь"),
        ("Куплено", "Куплено"),
        ("Свободно", "Свободно")
    )
    status = models.CharField(verbose_name="Статус номера", max_length=16, choices=STATUS_CHOICES, blank=True)

    def __str__(self):
        return self.user