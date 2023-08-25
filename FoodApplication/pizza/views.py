from django.shortcuts import render, redirect
from .forms import PizzaForm
from django.contrib import messages

# Create your views here.

def home_page(request):
    return render(request, 'pizza/home.html')

def order_page(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizz is on its way!' %(filled_form.cleaned_data['size'],
                                                                                 filled_form.cleaned_data['topping1'],
                                                                                  filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform':new_form, 'note':note}) 
            # filled_form.save()
            # messages.success(request, 'Your Order is Successfully..!')

    
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form})