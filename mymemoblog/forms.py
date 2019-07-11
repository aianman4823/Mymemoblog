from django import forms



class SearchForm(forms.Form):

    keyword=forms.CharField(
        initial='',
        label='検索キーワード',
        required=False,#必須ではない
    )



BlogSearchFormSet=forms.formset_factory(SearchForm,extra=1)