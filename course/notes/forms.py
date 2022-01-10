from django import forms

SECTION_TITLES = (
    ("Web", "Web Frameworks"),
    ("Django", "Setting up Django"),
    ("mapping", "URL Mapping"),
)


class SearchForm(forms.Form):
    term_of_search = forms.CharField()
    section = forms.ChoiceField(choices=SECTION_TITLES)
