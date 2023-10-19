from django.forms import ModelForm

from .models import SchoolMessage

class SchoolMessageForm(ModelForm):
   class Meta:
      model = SchoolMessage
      fields = ('title', 'content', 'mark', 'subject')
