from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

# Create your views here.

def index(request):
    """Basic index view"""
    return HttpResponse("Welcome to the Library!")

def example_view(request):
    """Example view demonstrating ExampleForm usage"""
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form
            example_data = form.cleaned_data['example_field']
            return HttpResponse(f"Form submitted successfully: {example_data}")
    else:
        form = ExampleForm()
    
    # Simple HTML response with form
    html = f'''
    <html>
    <body>
        <h1>Example Form</h1>
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="dummy">
            {form.as_p()}
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''
    return HttpResponse(html)
