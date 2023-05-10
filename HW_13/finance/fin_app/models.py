from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)

    def __str__(self):
        return self.name


class Income(models.Model):
    summa = models.FloatField(max_length=25, null=False)
    income_date = models.DateTimeField(auto_now_add=False)
    categories = models.ManyToManyField(Category, through='IncomeToCategory')

    def __str__(self):
        return self.summa


class Costs(models.Model):
    summa = models.FloatField(max_length=25, null=False)
    cost_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='CostsToCategory')

    def __str__(self):
        return self.summa


class IncomeToCategory(models.Model):
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CostsToCategory(models.Model):
    cost = models.ForeignKey(Costs, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
