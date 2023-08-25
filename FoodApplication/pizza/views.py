from django.shortcuts import render, redirect
from .forms import PizzaForm, MultiplePizzaForms
from django.contrib import messages
from django.forms import formset_factory
# Create your views here.

def home_page(request):
    return render(request, 'pizza/home.html')

def order_page(request):
    multiple_form = MultiplePizzaForms()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizz is on its way!' %(filled_form.cleaned_data['size'],
                                                                                 filled_form.cleaned_data['topping1'],
                                                                                  filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform':new_form, 'note':note, 'multiple_form':multiple_form}) 
            # filled_form.save()
            # messages.success(request, 'Your Order is Successfully..!')

    
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form, 'multiple_form':multiple_form})
    

def pizzas_page(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForms(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Order save'
        else:
            note = 'Order is not created..please try again...!'
        return render(request, 'pizza/pizzas.html', {'note':note, 'formset':formset})
    
    
