from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.index, name="index"),

    path('about_us/', views.aboutUs, name="about_us"),

    path('post/<str:slug>/', views.post_detail, name="post_detail_url"),
    path('articles/', views.articles, name="articles"),

    path('courses/', views.courses, name="courses"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/reset_password/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password/password_reset_done.html"),
         name="password_reset_complete"),

    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

]
