import os
from django.core.mail import EmailMessage
from mysite.models import mysite  # 將 'your_app' 替換為實際的應用程式名稱

def send_emails():
    # 取得所有非空的使用者郵件地址
    users_with_emails = mysite.objects.exclude(username__isnull=True).exclude(username='').values_list('email', flat=True)
    
    # 要附加的檔案路徑
    file_path = '/home/vboxuser/Downloads/test.pdf'

    # 逐個使用者發送郵件並附加檔案
    for user_email in users_with_emails:
        email = EmailMessage(
            '測試主旨',  # 替換為您的郵件主旨
            '測試內容',  # 替換為您的郵件內容
            '41041118@gm.nfu.edu.tw',  # 替換為寄件者的郵件地址
            [user_email],  # 使用者郵件地址列表
            reply_to=['41041118@gm.nfu.edu.tw'],  # 回覆地址
        )
        # 附加檔案
        with open(file_path, 'rb') as file:
            email.attach('test.pdf', file.read(), 'application/pdf')
        
        # 發送郵件
        email.send(fail_silently=False)

if __name__ == "__main__":
    send_emails()
#test