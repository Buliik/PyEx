from django import forms

class RazeSearchForm(forms.Form):
    from_raze = forms.FloatField(label="from")
    to_raze = forms.FloatField(label="to")


class RokSearchForm(forms.Form):
    from_rok = forms.FloatField(label="from")
    to_rok = forms.FloatField(label="to")


class VzdalenostSearchForm(forms.Form):
    from_vzdalenost = forms.FloatField(label="from")
    to_vzdalenost = forms.FloatField(label="to")


class ZamDateSearchForm(forms.Form):
    from_date = forms.DateField(label="from", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])
    to_date = forms.DateField(label="to", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])


class ZakDateSearchForm(forms.Form):
    from_date = forms.DateField(label="from", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])
    to_date = forms.DateField(label="to", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'])


class StrDateSearchForm(forms.Form):
    from_date = forms.DateTimeField(label="from")
    to_date = forms.DateTimeField(label="to")
