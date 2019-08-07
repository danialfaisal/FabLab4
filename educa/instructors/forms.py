from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Lesson


ModuleFormSet = inlineformset_factory(Course,
                                      Lesson,
                                      fields=['title', 'course', 'duration', 'video_url'],
                                      extra=2,
                                      can_delete=True)

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)