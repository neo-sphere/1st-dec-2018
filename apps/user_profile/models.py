from django.db import models


class Profile(models.Model):
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    occupation = models.CharField(max_length=20)

    def __str__(self):
        return 'Contact No: {} , Date of Birth: {}'.format(self.contact_no,
                                                        self.dob)

