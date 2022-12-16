from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.description}'


class Affiliate(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return '%d, %s, %d, %s' % (self.id, self.name, self.age, self.mail)


class Appointment(models.Model):
    date = models.DateField(auto_now=False, editable=True)
    hour = models.TimeField(auto_now=False, editable=True)
    idTest = models.ForeignKey(
        Test, related_name='appoTest', null=True, on_delete=models.CASCADE)
    idAffiliate = models.ForeignKey(
        Affiliate, related_name='appoAffiliate', null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return '%d, %s, %s, %d, %d' % (self.id, self.date, self.hour,
                                       self.idTest, self.idAffiliate)
