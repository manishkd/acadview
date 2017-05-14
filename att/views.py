from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from att.forms import LoginForm
from .models import Subject, Student

def index(request):
    latest_subject_list = Subject.objects.order_by('-pub_date')[:5]
    context = {
        'latest_subject_list': latest_subject_list,
    }
    return render(request, 'att/index.html', context)

def detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'att/detail.html', {'subject': subject})

def results(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'att/results.html', {'subject': subject})


def votepresent(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    try:
        selected_choice = subject.student_set.get(pk=request.POST['student'])
    except (KeyError, Student.DoesNotExist):
        return render(request, 'att/detail.html', {
            'subject': subject,
            'error_message': "You didn't select a choice.",
        })
    else:
        if('incre' in request.POST):
            selected_choice.present +=1
            selected_choice.total +=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('att:detail', args=(subject.id,)))
        elif('decre' in request.POST):
            selected_choice.absent +=1
            selected_choice.total +=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('att:detail', args=(subject.id,)))
        elif('result' in request.POST):
            return HttpResponseRedirect(reverse('att:results', args=(subject.id,)))
    

def login(request):
    username= "not logged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username=MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
    return render(request,'loggedin.html',{"username":username})
