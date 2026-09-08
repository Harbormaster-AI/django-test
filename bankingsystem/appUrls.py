"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('Bank/', include('bankingsystem.urls.BankUrls')),
    path('Branch/', include('bankingsystem.urls.BranchUrls')),
    path('ATM/', include('bankingsystem.urls.ATMUrls')),
    path('Customer/', include('bankingsystem.urls.CustomerUrls')),
    path('KycProfile/', include('bankingsystem.urls.KycProfileUrls')),
    path('IdentityDocument/', include('bankingsystem.urls.IdentityDocumentUrls')),
    path('RiskAssessment/', include('bankingsystem.urls.RiskAssessmentUrls')),
    path('ScreeningResult/', include('bankingsystem.urls.ScreeningResultUrls')),
    path('BankingProduct/', include('bankingsystem.urls.BankingProductUrls')),
    path('Account/', include('bankingsystem.urls.AccountUrls')),
    path('AccountStatement/', include('bankingsystem.urls.AccountStatementUrls')),
    path('Transaction/', include('bankingsystem.urls.TransactionUrls')),
    path('ExternalAccount/', include('bankingsystem.urls.ExternalAccountUrls')),
    path('FundsTransfer/', include('bankingsystem.urls.FundsTransferUrls')),
    path('StandingInstruction/', include('bankingsystem.urls.StandingInstructionUrls')),
    path('PaymentCard/', include('bankingsystem.urls.PaymentCardUrls')),
    path('LoanAccount/', include('bankingsystem.urls.LoanAccountUrls')),
    path('RepaymentSchedule/', include('bankingsystem.urls.RepaymentScheduleUrls')),
    path('LoanPayment/', include('bankingsystem.urls.LoanPaymentUrls')),
    path('Collateral/', include('bankingsystem.urls.CollateralUrls')),
    path('FeeCharge/', include('bankingsystem.urls.FeeChargeUrls')),
    path('ExchangeRate/', include('bankingsystem.urls.ExchangeRateUrls')),
    path('FXTrade/', include('bankingsystem.urls.FXTradeUrls')),
    path('Dispute/', include('bankingsystem.urls.DisputeUrls')),
    path('Consent/', include('bankingsystem.urls.ConsentUrls')),
    path('ThirdPartyProvider/', include('bankingsystem.urls.ThirdPartyProviderUrls')),
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
]