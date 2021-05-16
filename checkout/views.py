from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Irr8SKIoyyIjxEYYWZ2ioHEHvLRDsxt1KXrqvBroslJ7h6IK6Yarl9BidTlnW12Azea7ONcQNbfD0EVOybAWV6z00HhAm8rfU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
