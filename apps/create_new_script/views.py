from django.shortcuts import render
from django.views import View
from apps.create_new_script import forms
import os
import subprocess
# Create your views here.

class NewScriptView(View):

    def get(self, request):
        context = {'form': forms.GetProductDetailsForm()}
        template = 'create_new_script/new_script.html'
        return render(request, template, context)
    
class OutputScriptView(View):

    def post(self, request):
        if request.method == 'POST' and request.FILES['script']:
            file = request.FILES['script']
            file_name = file.name
            form = request.POST
            # try:
            #     os.mkdir(os.path.join(settings.MEDIA_ROOT, folder))
            # except:
            #     pass
            path = '/home/localuser/Datacube/NE-GeoCloud/Scripts/'+file_name
            dest = open(path, 'wb+')

            for chunk in file.chunks():
                dest.write(chunk)
            dest.close()

            out, err = runFile(file_name)
            #result = out.split('\n')
            context = {'file': file,
            'form': form,
            'out': out,
            'err': err}
            template = 'create_new_script/output.html'  
            return render(request, template, context)
        else:
            return HttpResponseBadRequest('Only POST requests are allowed')
    
def runFile(file_name):
    cmd = 'python Scripts/' + file_name
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    # for lin in result:
    #     if not lin.startswith('#'):
    #         print(lin)
    return out, err