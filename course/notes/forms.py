from django import forms

SECTION_TITLES = (
    ("any", "--Any--"),
    ("Web Frameworks", "Web Frameworks"),
    ("URL Mapping", "URL Mapping"),
    ("Setting up Django", "Setting up Django"),
)


class SearchForm(forms.Form):
    term_of_search = forms.CharField()
    section = forms.ChoiceField(choices=SECTION_TITLES, required=False)
