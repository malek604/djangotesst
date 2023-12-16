from django.shortcuts import render, get_object_or_404
from .models import Accessory
from .forms import InputForm
# View for the home page that displays a list of all accessories
def home(request):
    #pylint:disable=no-member
    accessories = Accessory.objects.all() # دریافت تمام لوازم جانبی
    return render(request, 'accessories/home.html', {'accessories': accessories})

# Detail view for an accessory based on its slug
def accessory_detail(request, slug):
    accessory = get_object_or_404(Accessory, slug=slug)  # دریافت لوازم جانبی بوسیله slug
    return render(request, 'accessories/accessory_detail.html', {'accessory': accessory})

# views.py
def my_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['number']
            mystr=form.cleaned_data['string']
            result = double_number(user_input)
            context = {'result': result, 'mystr': mystr}
            return render(request, 'result.html', context)
    else:
        form = InputForm()
    return render(request, 'input_form.html', {'form': form})

def double_number(n):
    return n * 2
