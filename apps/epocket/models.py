from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    # one user multiple transaction 
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='to_user')
    balance = models.DecimalField(max_digits=4, decimal_places=2)
    # save date when the model is created , NOTE auto_now_add 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Transaction Date')

    def __str__(self):
        return 'From: {} To: {} Transfer Amount: {}'.format(
                    self.from_user, self.to_user, self.balance)




