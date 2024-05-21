from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()
