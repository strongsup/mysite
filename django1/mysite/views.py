#create your views here.
from mysite.models import mysite
from .serializers import mysiteSerializer
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from .search import Filter
#from .forms import UserRegistrationForm
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from reportlab.pdfgen import canvas
from .models import Report
import io

#Create your views here.
class mysiteViewSet(Filter,viewsets.ModelViewSet):
    queryset = mysite.objects.all()
    serializer_class = mysiteSerializer
    permission_classes = (IsAuthenticated,)
    # 設置篩選器
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

def home_view(request):
    return render(request, 'registration/home.html')


def login_user(request):
    return render(request, 'registration/login.html')


def login_home_view(request):
    return render(request, 'registration/login_home.html')   
        
def register_user(request):
    if request.method == 'POST':
        # 獲取表單數據
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # 檢查使用者名稱是否已存在
        if mysite.objects.filter(username=username).exists():
            # 處理已存在的使用者名稱錯誤
            # 返回一個錯誤訊息，或者重新導向到註冊頁面並顯示錯誤訊息
            return render(request, 'registration/register.html', {'error': '使用者名稱已存在'})

        if mysite.objects.filter(email=email).exists():
            # 處理已存在的使用者名稱錯誤
            # 返回一個錯誤訊息，或者重新導向到註冊頁面並顯示錯誤訊息
            return render(request, 'registration/register.html', {'error': '信箱已被使用'})

        # 將表單數據保存到資料庫
        new_user = mysite(username=username, email=email, password=password)
        
        # 在這裡可以進行進一步的檢查或處理

        # 保存到資料庫
        new_user.save()

        # 在這裡可以發送歡迎郵件或其他後續處理
        send_welcome_email(new_user.email)

        return redirect('success')  # 定向到成功頁面或其他頁面
    else:
        return render(request, 'registration/register.html')

def success_view(request):
    # 在這裡處理成功註冊後的行為
    return render(request, 'registration/success.html')

from django.core.mail import send_mail

# 發送歡迎郵件的功能
def send_welcome_email(user_email):
    # 寄送歡迎郵件
    send_mail(
        '歡迎加入我們！',  # 郵件標題
        '感謝您的註冊，歡迎加入我們的網站！',  # 郵件內容
        '41041118@gm.nfu.edu.tw',  # 寄件人郵件地址
        [user_email],  # 收件人郵件地址（這裡使用註冊的新用戶郵件地址）
        fail_silently=False,
    )
    
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="user_data.pdf"'

    # 创建一个 PDF 文档
    p = canvas.Canvas(response)

    # 获取数据库中的数据
    user_data = mysite.objects.all()  # 假设 YourModel 是您的模型类

    # 在 PDF 中写入数据库信息
    y = 800  # 设置初始纵坐标
    for user in user_data:
        p.drawString(100, y, f'Username: {user.username}')
        p.drawString(100, y - 20, f'Email: {user.email}')
        p.drawString(100, y - 40, f'Password: {user.password}')
        y -= 60  # 调整纵坐标以放置下一个用户信息

    # 关闭 PDF 文档并返回响应
    p.showPage()
    p.save()
    return response
