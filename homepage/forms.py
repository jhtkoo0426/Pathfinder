from django import forms


class SearchStationForm(forms.Form):
    start_station = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Start Station",
                "class": "test-class"
            }
        )
    )

    end_station = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "End Station",
                "class": "test-class"
            }
        )
    )