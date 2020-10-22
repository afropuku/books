from django import forms


# 書籍タイトル検索
class SearchForm(forms.Form):
    title = forms.CharField(label=("タイトル"), max_length=200, required=True)
