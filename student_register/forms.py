from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','stud_id','contact_number','course')
        labels = {'fullname':'Full Name',
        'stud_id':'Student ID',
        'contact_number':'Contact Number',
        'course':'Course'
        }
    
    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].empty_label="Select"