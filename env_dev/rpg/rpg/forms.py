from django import forms

class CharacterForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()#required=False)

#forms can be outputted in the following ways (HTML):
#NOTE: these never include the enclosing form, table, ul tags
##so that you can add additional content as you like
#print(form) #outputs as HTML table
#print(form.as_ul()) #outputs as HTML ul
#print(form.as_p()) #outputs as HTML paragraphs

#displaying HTML for an individual field:
#print(form["field"])

#When data is bound to a form, form.is_bound will be True
#form.cleaned_data converts input into python types (e.g. '1' -> 1)

#form.is_valid() to validate the data against its types
#form.errors has a JSON object of all the errors on the form
#form["field"].errors to access list of validation errors on that field
