from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages, auth
from django.core.mail import send_mail

# Create your views here.
def contact(request): 
  if request.method == 'POST':
    user_id = request.POST['user_id']
    listing = request.POST['listing']
    listing_id = request.POST['listing_id']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    realtor_email = request.POST['realtor_email']

    # Check if user made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

      if has_contacted:
        messages.error(request, 'You have already made an inquiry about this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

    contact.save()

    #Send mail
    # send_mail(
    #   'Property Listiing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'bcstith75@gmail.com',
    #   [realtor_email, 'bcstith@yahoo.com'],
    #   fail_silently=False
    # )

    messages.success(request, "Your inquiry has been sent")
    return redirect('/listings/'+listing_id)