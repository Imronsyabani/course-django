from django import forms

class CourseForm(forms.Form):
    title = forms.CharField(max_length=256,label="Title")
    date_from = forms.DateTimeField(label="Date From")
    date_to = forms.DateTimeField(label="Date To")
    second_date_from = forms.DateTimeField(label="Second Date From")
    second_date_to = forms.DateTimeField(label="Second Date To")
    description = forms.TextField(label="Description Course")
    address = forms.TextField(label="Address")
    kecamatan = forms.CharField(max_length=256,label="Kecamatan")
    kabupaten = forms.CharField(max_length=256,label="Kabupaten")
    provinsi = forms.CharField(max_length=256,label="Provinsi")
    contacts = forms.TextField(label="Contact Person")
    image = forms.BinaryField(label="Image")