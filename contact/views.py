from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def contact(request):
    """ A view to return the contact page and contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Enquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            """ To prevent extra headers being added """
            try:
                send_mail(subject, message, 'info@homelearning.com', ['info@homelearning.com'])
                messages.success(request, f'Your enquiry has been sent! \
                    We will aim to get back to you within 48 hours.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')


    form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})


