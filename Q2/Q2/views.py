from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from contactform.models import Contact


def index(request):
    if request.method == 'POST':
        contact = Contact()
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        email = request.POST.get('e-mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.first_name = fname
        contact.last_name = lname
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        data = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        
        Hello {} {},
        
        {}
        
        From:{}
        '''.format(data['fname'], data['lname'], data['message'], data['email'])
        send_mail(data['subject'], message, '', ['saiprasannapandu17@gmail.com'])
        return render(request, 'contactform/Thank you.html', {})

    return render(request, 'contactform/index.html', {})
