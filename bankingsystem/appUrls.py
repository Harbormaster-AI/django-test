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
    path('Bank/', include('bankingSystem.urls.BankUrls')),
    path('Branch/', include('bankingSystem.urls.BranchUrls')),
    path('ATM/', include('bankingSystem.urls.ATMUrls')),
    path('Customer/', include('bankingSystem.urls.CustomerUrls')),
    path('KycProfile/', include('bankingSystem.urls.KycProfileUrls')),
    path('IdentityDocument/', include('bankingSystem.urls.IdentityDocumentUrls')),
    path('RiskAssessment/', include('bankingSystem.urls.RiskAssessmentUrls')),
    path('ScreeningResult/', include('bankingSystem.urls.ScreeningResultUrls')),
    path('BankingProduct/', include('bankingSystem.urls.BankingProductUrls')),
    path('Account/', include('bankingSystem.urls.AccountUrls')),
    path('AccountStatement/', include('bankingSystem.urls.AccountStatementUrls')),
    path('Transaction/', include('bankingSystem.urls.TransactionUrls')),
    path('ExternalAccount/', include('bankingSystem.urls.ExternalAccountUrls')),
    path('FundsTransfer/', include('bankingSystem.urls.FundsTransferUrls')),
    path('StandingInstruction/', include('bankingSystem.urls.StandingInstructionUrls')),
    path('PaymentCard/', include('bankingSystem.urls.PaymentCardUrls')),
    path('LoanAccount/', include('bankingSystem.urls.LoanAccountUrls')),
    path('RepaymentSchedule/', include('bankingSystem.urls.RepaymentScheduleUrls')),
    path('LoanPayment/', include('bankingSystem.urls.LoanPaymentUrls')),
    path('Collateral/', include('bankingSystem.urls.CollateralUrls')),
    path('FeeCharge/', include('bankingSystem.urls.FeeChargeUrls')),
    path('ExchangeRate/', include('bankingSystem.urls.ExchangeRateUrls')),
    path('FXTrade/', include('bankingSystem.urls.FXTradeUrls')),
    path('Dispute/', include('bankingSystem.urls.DisputeUrls')),
    path('Consent/', include('bankingSystem.urls.ConsentUrls')),
    path('ThirdPartyProvider/', include('bankingSystem.urls.ThirdPartyProviderUrls')),
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
]