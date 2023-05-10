from datetime import datetime, date

from django.shortcuts import render, redirect
from .models import Category, Income, Costs


# Create your views here.
def main(request):
    incomes = Income.objects.all()
    costs = Costs.objects.all()
    return render(request, 'fin_app/index.html', {'incomes': incomes, 'costs': costs},)


def category(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            cl = Category(name=name)
            cl.save()
        return redirect(to='/')
    return render(request, 'fin_app/category.html', {})

def income(request):
    if request.method == 'POST':
        summa = request.POST['summa']
        income_date = request.POST['income_date']
        list_categories = request.POST.getlist('categories')
        if summa and income_date:
            categories = Category.objects.filter(name__in=list_categories)
            income = Income.objects.create(summa=summa, income_date=income_date,)
            for category in categories.iterator():
                income.categories.add(category)
        return redirect(to='/')

    categories = Category.objects.all()
    return render(request, 'fin_app/income.html', {"categories": categories})


def cost(request):
    if request.method == 'POST':
        summa = request.POST['summa']
        cost_date = request.POST['cost_date']
        list_categories = request.POST.getlist('categories')
        if summa and cost_date:
            categories = Category.objects.filter(name__in=list_categories)
            cost = Costs.objects.create(summa=summa, cost_date=cost_date,)
            for category in categories.iterator():
                cost.categories.add(category)
        return redirect(to='/')

    categories = Category.objects.all()
    return render(request, 'fin_app/cost.html', {"categories": categories})


def filter(request):
    if request.method == 'POST':
        start_date = request.POST['from']
        end_date = request.POST['to']
        print(type(start_date))
        print(end_date)
        # list_categories = request.POST.getlist('categories')
        if start_date and end_date:
            # categories = Category.objects.filter(name__in=list_categories)
            filtered_income = Income.objects.filter(income_date__range=(start_date, end_date))
            filtered_costs = Costs.objects.filter(cost_date__range=(start_date, end_date))
            income_sum = 0
            costs_sum = 0
            for summa in filtered_income:
                income_sum += summa.summa

            for summa in filtered_costs:
                costs_sum += summa.summa

            # for category in categories.iterator():
            #     cost.categories.add(category)

        return render(request, 'fin_app/filter_results.html', {'incomes': filtered_income, 'costs': filtered_costs, 'income_sum': income_sum, 'costs_sum': costs_sum})


    # categories = Category.objects.all()
    return render(request, 'fin_app/filter.html')



def income_detail(request, income_id):
    income = Income.objects.get(pk=income_id)
    income.category_list=','.join([str(name) for name in income.categories.all()])
    return render(request, 'fin_app/detail_income.html', {'income':income})


def cost_detail(request, cost_id):
    cost = Costs.objects.get(pk=cost_id)
    cost.category_list=','.join([str(name) for name in cost.categories.all()])
    return render(request, 'fin_app/detail_cost.html', {'cost':cost})

def delete_income(request, income_id):
    income = Income.objects.get(pk=income_id)
    income.delete()
    return redirect(to='/')

def delete_cost(request, cost_id):
    cost = Costs.objects.get(pk=cost_id)
    cost.delete()
    return redirect(to='/')