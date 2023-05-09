from django.shortcuts import redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from django.core.paginator import Paginator

from mysite.models import Person
from mysite.forms import PersonForm

class StudentView(LoginRequiredMixin, CreateView):
    model = Person
    template_name = 'index.html'
    form_class = PersonForm

    def create_student(request, *args, **kwargs):
        f = PersonForm(request.POST or None)
        if request.method == 'POST':
            f = PersonForm(data=request.POST)
            if f.is_valid():
                stud_name = f.cleaned_data['name']
                stud_age = f.cleaned_data['age']
                stud_info = f.cleaned_data['info']
                f.save()
            return redirect('create_student')
        else:
            f = PersonForm()
        return render(request, "index.html", {'form': f})

def person_list(request):
    person = Person.objects.all()
    p = Paginator(person, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request, 'person_list.html', {'page_obj': page_obj})