from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify, name='verify'),
    path('home/', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('reset_profile/', views.reset_profile, name='reset_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setting/', views.setting, name='setting'),
    path('transaction/', views.transaction, name='transaction'),
    path('bank/', views.bank, name='bank'),
    path('crypto/', views.crypto, name='crypto'),
    path('paypal/', views.paypal, name='paypal'),
    path('skrill/', views.skrill, name='skrill'),
    path('pending/', views.pending, name='pending'),
    path('Upgrade_Account/', views.Upgrade_Account, name='Upgrade_Account'),
    path('imf/', views.imf, name='imf'),
    path('G_pay/', views.G_pay, name='G_pay'),
    path('payoneer/', views.payoneer, name='payoneer'),
    path('western_union/', views.western_union, name='western_union'),
    path('trust_wise/', views.trust_wise, name='trust_wise'),
    path('linking_view/', views.linking_view, name='linking_view'),
    path('LogoutPage/', views.LogoutPage, name='logout'),
]
