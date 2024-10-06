from django.urls import path
# from apps.users.api.api import UserAPIView
# from apps.users.api.api import user_api_view, user_detail_api_view


urlpatterns = [
    # path('usuario/', UserAPIView.as_view(), name='usuario_api'),  # User API endpoint
    path('usuario/', user_api_view, name='usuario_api'),  # User API endpoint
    path('usuario/<int:pk>/', user_detail_api_view, name='usuario_detail_api'),  
]
    