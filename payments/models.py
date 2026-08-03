from django.db import models

class Payment(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255, blank=True)
    paid_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} ({self.reference})"
