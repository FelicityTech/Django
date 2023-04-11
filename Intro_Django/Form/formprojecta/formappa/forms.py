from django import forms

class CreateStudentForm(forms.Form):
    name = models.CharField(label='Student name',max_length=100)

<form>
<label for='name'>Student Name:</label>
<input id='name' type='text' name='name' maxlength='100' required>
<button>
</form>