from django.shortcuts import render , HttpResponse , redirect
from .models import Record , Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
    a = 1
    return render(request , "app/hello.html" , {"key":a})
@login_required
def frontpage(request):
    user = request.user
    # records = Record.objects.filter()
    record_form = RecordForm(initial={"balance_type":"支出"})
    # records = Record.objects.filter(user=)
    records = Record.objects.filter()
    income_list = [record.cash for record in records if record.balance_type == "收入"]
    outcome_list = [record.cash for record in records if record.balance_type == "支出"]
    income = sum(income_list) if len(income_list) > 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) > 0 else 0
    net = income-outcome
    # return render(request , "app/index.html" , {"records":records , "income":income ,
    #                                        "outcome":outcome , "net":net})
    return render(request , "app/index.html" , locals())

@login_required
def setting(request):
    categories = Category.objects.filter()
    return render(request, "app/settings.html", locals())

@login_required
def addCategory(request):
    if request.method == "POST":
        posted_data = request.POST
        category = posted_data["add_category"]
        Category.objects.get_or_create(category=category)
        # categories = Category.objects.filter()
        # return render(request, "app/settings.html", locals())
    return redirect("/settings") # 導回一個url (urls.py)

@login_required
def deleteCategory(request , category):
    Category.objects.filter(category=category).delete()
    return redirect("/settings")

@login_required
def addRecord(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("/") # 返回首頁

@login_required
def deleteRecord(request):
    if request.method == "POST":
        id = request.POST["delete_val"]
        Record.objects.filter(id = id).delete()
    return redirect("/") # 返回首頁