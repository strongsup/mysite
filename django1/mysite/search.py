from rest_framework import filters
from .models import mysite 

class Filter:
    def get_queryset(self):
        queryset = super().get_queryset()

        # 模糊搜索
        username_search = self.request.query_params.get('username_search', None)
        email_search = self.request.query_params.get('email_search', None)
        email_search_username = self.request.query_params.get('email_search_username', None)

        if username_search:
            queryset = queryset.filter(username__icontains=username_search)
        if email_search:
            queryset = queryset.filter(email__icontains=email_search)
        if email_search_username:
            queryset = queryset.filter(email__icontains=email_search_username).values('username')

        return queryset
