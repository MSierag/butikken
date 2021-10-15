from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view that renders the checkout page """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':
            'pk_test_51JkoIXBbV7VdQTQg3W3CrrUhR4SQqMZn0Gr7BiprXFAXxMIIG92'
            'pMpT4kKgOBxtSfZ6l1CzGJ4iIhyBov5ER3xV0005J3zj3cL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
