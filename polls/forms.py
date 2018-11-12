from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,required=True,min_length=6,
                               label='账号')
    password = forms.CharField(max_length=20,required=True,min_length=6,
                               label='密码',widget=forms.PasswordInput())


class CommentForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    is_true = forms.BooleanField(widget=forms.TextInput(attrs=dict(rows=5,cols=5)))
    comment = forms.CharField(widget=forms.Textarea(attrs=dict(rows=3,cols=20)))
    sel = forms.ChoiceField(choices=(('请选择', 1),  ('选吧', 2),('qq',3)))
    email = forms.EmailField()
    number = forms.IntegerField(max_value=10,min_value=6)
    date = forms.CharField(widget=forms.DateInput())
    datatime = forms.CharField(widget=forms.DateTimeInput())
    time = forms.CharField(widget=forms.TimeInput())
    hobby = forms.CharField(widget=forms.CheckboxInput())
    sex = forms.CharField(widget=forms.Select(choices=(('','请选择'),('1','男'),('0','女'))))
    is_sad = forms.CharField(widget=forms.NullBooleanSelect())
    file = forms.FileField(required=False,allow_empty_file=True)


birth_year_choices = ('1995', '1996', '1997')
colors_choices = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black')
    )

class SimpleForm(forms.Form):
    colors = forms.MultipleChoiceField(required=False,
                                       widget=forms.CheckboxSelectMultiple(),
                                       choices=colors_choices)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=birth_year_choices))



