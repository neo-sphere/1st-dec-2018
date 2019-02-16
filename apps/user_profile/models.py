from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mobile_no_is_numeric(mobile_no):
    if not mobile_no.isnumeric():
        raise ValidationError(
            _('"%(num)s" is not valid mobile number'),
            params={'num':mobile_no }
            )
class Profile(models.Model):
    MALE = 'm'
    FEMALE = 'f'

    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    contact_no = models.CharField(max_length=15, unique=True,
                                verbose_name='Mobile No',
                                help_text='98XXXXXXXX',
                                validators=[validate_mobile_no_is_numeric,])

    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    dob = models.DateField()
    occupation = models.CharField(max_length=20)

    def __str__(self):
        return 'Contact No: {} , Date of Birth: {}'.format(self.contact_no,
                                                        self.dob)

