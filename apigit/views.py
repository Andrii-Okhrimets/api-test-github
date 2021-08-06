from django.shortcuts import render
from django.core.exceptions import ValidationError
from .models import API_GIT
from .forms import ApigitForm
import requests


def apitest(request):

    url = 'https://api.github.com/users/{}'

    if (request.method == 'POST'):
        form = ApigitForm(request.POST)
        form.save()
    
    form = ApigitForm()

    many = API_GIT.objects.all()

    for login in many:
        res = requests.get(url.format(login.login)).json()
        res_2 = requests.get(url.format(login.login) + '/repos').json()
        info_res_2 = []
        
        try:
            res['name']
        except (TypeError, KeyError):
            info_res = {
                'login': login.login,
                'name': 'no such user exists'
            }
            
            git_info = {
                'repos': "Not iterable"
            }
            info_res_2.append(git_info)
        else:
            info_res = {
                'login': login.login,
                'name': res['name']
            }

            for i in res_2:
                git_info = {
                    'repos': i['name']
                }
                info_res_2.append(git_info)
        finally:
            contex = {'info': info_res_2, 'info_one': info_res, 'form': form}

    return render(request, 'apigit/index.html', contex)

