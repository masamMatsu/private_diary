from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = '内容を入力'


class Inquiry2Form(forms.Form):
    name = forms.CharField(label='氏名', max_length=30)
    adress = forms.CharField(label='住所', max_length=30)
    age = forms.IntegerField(label='年齢')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '氏名をここに入力してください。'

        self.fields['adress'].widget.attrs['class'] = 'form-control'
        self.fields['adress'].widget.attrs['placeholder'] = '住所をここに入力してください。'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['placeholder'] = '年齢をここに入力してください。'
