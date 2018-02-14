from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from goat_website.settings import STATIC_DIR
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from goat_app.models import Daily_Image, Subscriber
import os

class Command(BaseCommand):

    help = 'Sends an email to each subscriber on the list'

    template = get_template('email.html')
    context = {'user': 'user', 'other_info': 'info'}
    content = template.render(context)
    # if not user.email:
    #     raise BadHeaderError('No email address given for {0}'.format(user))
    emailList = list(Subscriber.objects.all().only('email').values_list('email', flat=True))
    msg = EmailMultiAlternatives('GOTD', content, 'bruvajohn@gmail.com', to=emailList)
    msg.attach_alternative(content, "text/html")
    image_path = Daily_Image.objects.latest('first_published_date').image_path.url

    image = MIMEImage(open(os.path.join(STATIC_DIR, image_path), 'rb').read())
    image.add_header('Content-ID', '<{}>'.format('gotd.jpg'))
    msg.content_subtype = 'html'
    msg.mixed_subtype = 'related'
    msg.attach(image)
    msg.send()


    # print(send_mail('Subject here', message, settings.EMAIL_HOST_USER,
    # ['bruvajohn@gmail.com'], fail_silently=False, html_message=message))
