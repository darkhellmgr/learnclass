from django import forms

from mainapp.models import School
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SchoolModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchoolModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        # self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

         # self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = School
        fields = '__all__'
