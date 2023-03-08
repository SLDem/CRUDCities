from django.db import models


class Mayor(models.Model):
    """
    Model for creating mayors.
    """
    objects: models.Manager()

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_of_job_start = models.DateField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class City(models.Model):
    """
    Model for creating cities.
    """
    objects: models.Manager()

    name = models.CharField(max_length=40)
    population = models.IntegerField()
    date_of_foundation = models.DateField()
    mayor = models.OneToOneField(Mayor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Citie"  # because admin site doesn't recognise english punctuation

    def __str__(self):
        return self.name


class Street(models.Model):
    """
    Model for creating streets for cities.
    """
    objects: models.Manager()

    name = models.CharField(max_length=60)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
