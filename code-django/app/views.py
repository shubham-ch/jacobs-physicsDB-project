
from fileinput import filename
import io
from unicodedata import name
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib import messages
from .models import file
from .forms import fileForm
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Import Pagination (Page system for database)
from django.core.paginator import Paginator

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

def delete_data(request, file_id):
    database_followup = file.objects.get(pk=file_id)
    database_followup.delete()
    return redirect('output_database')


def update_database(request, file_id):
    database_followup = file.objects.get(pk=file_id)
    form = fileForm(request.POST or None, request.FILES or None,
                    instance=database_followup)
    if form.is_valid():
        form.save()
        return redirect('output_database')
    return render(request, 'base/update_database.html', {'database_followup': database_followup,
                                                         'form': form})


def database(request):
    output_database = file.objects.all().order_by('nameOfFile')

    # Set up Pagination
    p = Paginator(file.objects.all().order_by('nameOfFile'), 10)
    page = request.GET.get('page')
    pages = p.get_page(page)
    nums = "a" * pages.paginator.num_pages

    return render(request, 'base/database.html',
                  {'output_database': output_database,
                   'pages': pages, 'nums': nums})


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
        form = fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_forms?submitted=True')
    else:
        form = fileForm
        if 'submitted' in request.GET:
            submitted = True

    form = fileForm
    return render(request, 'base/add_forms.html', {'form': form, 'submitted': submitted})

# Generate text file


def download_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=database.txt'

    writer = csv.writer(response)
    # Designate the model
    downloads = file.objects.all()
    # Create blank list
    # list = []
    # Loop through and output
    # for download in downloads:
    #     list.append(
    #         f'{download.id}\n{download.nameOfFile}\n{download.nameOfLectures}\n{download.fields}\n{download.file_upload}\n{download.usedFor}\n{download.difficultyLevel}\n{download.comment}\n{download.sourceOfProblem}\n{download.author}\n{download.typeOfProblem}\n{download.intendedLearningOutcome}\n{download.purposeOfFile}\n{download.grading}\n')
    writer.writerow(['id', 'nameOfFile', 'nameOfLectures',
                    'fields', 'file_upload', 'usedFor', 'difficultyLevel', 'comment', 'sourceOfProblem', 'author', 'typeOfProblem', 'intendedLearningOutcome', 'purposeOfFile', 'grading'])
    for download in downloads:
        writer.writerow(
            [download.id, download.nameOfFile, download.nameOfLectures, download.fields, download.file_upload, download.usedFor, download.difficultyLevel, download.comment, download.sourceOfProblem, download.author, download.typeOfProblem, download.intendedLearningOutcome, download.purposeOfFile, download.grading])
    # Write to the text file
    # response.writelines(list)
    return response


# Generate csv file

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=database.csv'
    # Create a csv writer
    writer = csv.writer(response)
    # Designate the model
    downloads = file.objects.all()
    # Add column headings to the csv file
    writer.writerow(['id', 'nameOfFile', 'nameOfLectures',
                    'fields', 'file_upload', 'usedFor', 'difficultyLevel', 'comment', 'sourceOfProblem', 'author', 'typeOfProblem', 'intendedLearningOutcome', 'purposeOfFile', 'grading'])
    # Loop through and output
    for download in downloads:
        writer.writerow(
            [download.id, download.nameOfFile, download.nameOfLectures, download.fields, download.file_upload, download.usedFor, download.difficultyLevel, download.comment, download.sourceOfProblem, download.author, download.typeOfProblem, download.intendedLearningOutcome, download.purposeOfFile, download.grading])
    return response


# Generate pdf file

def download_pdf(request):
    # create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Designate The Model
    downloads = file.objects.all()
    # Create blank list
    lines = []

    for download in downloads:
        lines.append(download.id)
        lines.append(download.nameOfFile)
        lines.append(download.nameOfLectures)
        lines.append(download.fields)
        lines.append(download.file_upload)
        lines.append(download.usedFor)
        lines.append(download.difficultyLevel)
        lines.append(download.comment)
        lines.append(download.sourceOfProblem)
        lines.append(download.author)
        lines.append(download.typeOfProblem)
        lines.append(download.intendedLearningOutcome)
        lines.append(download.purposeOfFile)
        lines.append(download.grading)

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='database.pdf')


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = file.objects.all()
    name_of_file = request.GET.get('name_of_file')
    name_of_lecture = request.GET.get('name_of_lecture')
    name_of_field = request.GET.get('name_of_field')
    file_used_for = request.GET.get('used_for')
    name_of_author = request.GET.get('name_of_author')
    type_of_problem = request.GET.get('type_of_problem')
    minimum_difficulty = request.GET.get('min_difficulty')
    maximum_difficulty = request.GET.get('max_difficulty')

    if is_valid_queryparam(name_of_file):
        qs = qs.filter(nameOfFile__icontains=name_of_file)

    if is_valid_queryparam(name_of_lecture):
        qs = qs.filter(nameOfLectures__icontains=name_of_lecture)

    if is_valid_queryparam(name_of_field):
        qs = qs.filter(fields__icontains=name_of_field)

    if is_valid_queryparam(file_used_for):
        qs = qs.filter(used_for__icontains=file_used_for)

    if is_valid_queryparam(name_of_author):
        qs = qs.filter(author__icontains=name_of_author)

    if is_valid_queryparam(type_of_problem):
        qs = qs.filter(typeOfProblem__icontains=type_of_problem)

    if is_valid_queryparam(minimum_difficulty):
        qs = qs.filter(difficultyLevel__gte=minimum_difficulty)

    if is_valid_queryparam(maximum_difficulty):
        qs = qs.filter(difficultyLevel__lt=maximum_difficulty)
    context = {
        'queryset': qs
    }
    return render(request, "base/filter.html", context)
