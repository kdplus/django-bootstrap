from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['15058617922@163.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
			initial={'subject':'I Love Your Site'}
		)
    return render(request, 'contact_form.html', {'form': form})