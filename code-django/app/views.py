from fileinput import filename
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import file
from .forms import fileForm

# Create your views here.


def home(request):
    file_data = file.objects.all()
    # here the main.html from templates is attached by adding path in DIR settings/templates/ file
    return render(request, 'base/home.html', {'name': file_data})


# def storeFile(request):
#     # here name refers to the dictionary we created in mainPage named file
#     temp = file(name=request.POST['filename'])
#     temp.save()
#     return HttpResponseRedirect('/main/')


# def deleteFile(request, file_id):
#     temp = file.objects.get(id=file_id)
#     temp.delete()
#     return HttpResponseRedirect('/main/')

def database(request):
    output_database = file.objects.all()
    return render(request, 'base/database.html',
                  {'output_database': output_database})


def database_followup(request, file_id):
    database_followup = file.objects.get(pk=file_id)
    return render(request, 'base/database_followup.html', {'database_followup': database_followup})


def search_database(request):
    if request.method == "POST":
        searched = request.POST['searched']
        data = file.objects.filter(
            nameOfFile__contains=searched) | file.objects.filter(nameOfLectures__contains=searched) | file.objects.filter(fields__contains=searched)
        return render(request, 'base/search.html', {'searched': searched, 'data': data})
    else:
        return render(request, 'base/search.html', {})


def add_forms(request):
    submitted = False
    if request.method == "POST":
        form = fileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_forms?submitted=True')
    else:
        form = fileForm
        if 'submitted' in request.GET:
            submitted = True

    form = fileForm
    return render(request, 'base/add_forms.html', {'form': form, 'submitted': submitted})
