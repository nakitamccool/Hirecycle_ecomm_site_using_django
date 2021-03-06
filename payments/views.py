from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from payments.forms import MakePaymentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from adverts.models import Advert
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required(login_url="/user/login?next=payments/buy_now")
def buy_now(request, id):
    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                advert = get_object_or_404(Advert, pk=id)
                customer = stripe.Charge.create(
                    amount= int(advert.daily_rental_rate * 100),
                    currency="EUR",
                    description=advert.item,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('advertlist'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = MakePaymentForm()
        advert = get_object_or_404(Advert, pk=id)

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'advert': advert}
    args.update(csrf(request))

    return render(request, 'pay.html', args)