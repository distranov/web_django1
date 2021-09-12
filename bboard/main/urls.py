from django.urls import path
from .views import index, other_page, BBLoginView, profile, BBLogOutView, ChangeUserInfoView, BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate, DeleteUserView, by_rubric

app_name = 'main'
urlpatterns = [
    path('<int:pk>/', by_rubric, name = 'by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/logout/', BBLogOutView.as_view(),  name='logout'),
]
