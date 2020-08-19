from django import forms



class ProblemInputForm(forms.Form):
    number = forms.IntegerField(validators=[]) #TODO

    def is_integer_validator(self):
        data = self.cleaned_data['number']

        if type(data) is not int:
            raise forms.ValidationError('숫자만 입력해주세요.')
        return data