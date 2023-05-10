from django.contrib import admin
from .models import Category, Income, Costs, IncomeToCategory, CostsToCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Costs)
admin.site.register(IncomeToCategory)
admin.site.register(CostsToCategory)