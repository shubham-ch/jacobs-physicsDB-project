from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import file

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
