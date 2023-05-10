from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    path('income/', views.income, name='income'),
    path('cost/', views.cost, name='cost'),
    path('filter/', views.filter, name='filter'),
    path('income_detail/<int:income_id>', views.income_detail, name = 'income_detail'),
    path('cost_detail/<int:cost_id>', views.cost_detail, name = 'cost_detail'),
    path('delete_income/<int:income_id>', views.delete_income, name='delete_income'),
    path('delete_cost/<int:cost_id>', views.delete_cost, name='delete_cost')
]