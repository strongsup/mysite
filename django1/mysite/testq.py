from django.core.mail import send_mail
from mysite.models import mysite 

def hello():{
    print('helloworld')
}

def testdb():{
	print(mysite.objects.exclude(username__isnull=True).exclude(username='').values_list('username', flat=True)),
    print(mysite.objects.exclude(username__isnull=True).exclude(username='').values_list('email', flat=True))
}
