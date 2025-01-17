from django import forms


class SampleChoiceForm(forms.Form):
    text = forms.fields.ChoiceField(
        choices=(
            ('alice', '不思議の国のアリス'),
            ('constitution_of_japan', '日本国憲法'),
            ('dagon', 'ダゴン'),
            ('frankenstein', 'フランケンシュタイン'),
            ('lorem_ipsum', 'lorem'),
            ('lorem_ipsum_upper', 'lorem（大文字）'),
            ('pangram', 'パングラム'),
            ('rashomon', '羅生門'),
            ('sample', 'サンプルテキスト'),
        ),
        required=True,
        widget=forms.widgets.Select
    )
    count = forms.IntegerField
