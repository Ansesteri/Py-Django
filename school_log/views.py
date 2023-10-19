from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SchoolMessageForm
from .models import SchoolMessage, Subject

class SchoolMessageCreateView(CreateView):
   template_name = 'school_log/create1.html'
   form_class = SchoolMessageForm
   success_url = reverse_lazy('index')

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["subjects"] = Subject.objects.all()
      return context
   

def index(request):
   posts = SchoolMessage.objects.all()
   subjects = Subject.objects.all()
   context = {
      'posts': posts,
      'subjects': subjects
   }
   return render(request, 'school_log/index1.html', context)


def subject(request, subject_id):
   posts = SchoolMessage.objects.filter(subject = subject_id)
   rubrics = Subject.objects.all()
   current_rubric = Subject.objects.get(pk=subject_id)
   return render(request, 'school_log/subject.html', locals())