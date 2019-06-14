from django.shortcuts import render
from django.views import View
from apps.create_new_script import forms
# Create your views here.


class NewScriptView(View):

    def get(self, request):
        context = {'form': forms.GetProductDetailsForm()}
        template = 'create_new_script/new_script.html'
        return render(request, template, context)
