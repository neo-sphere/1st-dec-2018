from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

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

# django signal 
@receiver(post_save, sender=Transaction) # signal_type , sender=ModelName
def balance_update(sender, instance, created, **kwargs):
    """
    to communicate with other apps we use signal concept of sender and receiver
    """
    if created: # created value is False on update, True on create 
        sender_user = instance.from_user # object of User class
        receiver_user = instance.to_user # object of User class 
        ammount = instance.balance
        sender_user.account.balance -= ammount # decrease balance of user instance 
        receiver_user.account.balance += ammount # inscrease balance of user instance 
        sender_user.account.save() # will update balance
        receiver_user.account.save() # will update balance 



