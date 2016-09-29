from django.db import models


class Subscription(models.Model):

    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subsriptions"

    def __str__(self):
        return self.name
