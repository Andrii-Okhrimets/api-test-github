from django.test import TestCase
from .models import API_GIT
from .forms import ApigitForm

class ApiGitModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        API_GIT.objects.create(login="Andrii")
    
    def test_login_labal(self):
        api_test = API_GIT.objects.get(id=1)
        field_label = api_test._meta.get_field('login').verbose_name
        self.assertEquals(field_label,'login')

    def test_login_max_length(self):
        api_test = API_GIT.objects.get(id=1)
        max_length = api_test._meta.get_field('login').max_length
        self.assertEquals(max_length, 100)


class ApiGitFormsTest(TestCase):

    def test_api_form_label(self):
        form = ApigitForm()
        self.assertFalse(form.fields['login'].label == None)

