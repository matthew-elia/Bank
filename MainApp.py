import loginapp
import json
# from PkiUtil import PkiUtil
from SiteApp import SiteApp
from AccountApp import AccountApp
from HoldingApp import HoldingApp
from TransactionApp import TransactionApp
from AddSiteAccount import AddSiteAccount
from PortfolioAssetSummaryApp import PortfolioAssetSummaryApp
from HoldingAssetClassificationApp import HoldingAssetClassificationApp
from InvestmentPlanApp import InvestmentPlanApp
from AddProviderAccount import AddProviderAccount

def loop():
    print ('-----------------------------------------------')
    print ('YSL PFM/Aggregation')
    print ('-----------------------------------------------')
    print ('1. Site Search')
    print ('2. Add Provider Account (Non MFA')
    print ('3. Add Provider Account (MFA')
    #print ('4. Add Provider Account (Non MFA - With PKI Encryption')
    #print ('5. Add Provider Account (MFA - With PKI Encryption')
    print ('4. Add Provider Account (Non MFA - NEW')
    print ('5. Add Provider Account (MFA - NEW')
    print ('6. Accounts')
    print ('7. Holdings')
    print ('8. Transactions')
    print ('9. HoldingSummary')
    print ('10. Holding with Asset')
    print ('11. Investment Option')
    print ('0. Exit')
    print ('-----------------------------------------------')
    print ('Enter your choice:')
    print ('-----------------------------------------------')
    n = eval(input('enter the selection = '))
    if n == 0:
        print ('Exit')
    elif n == 1:
        searchString = eval(input("Enter the site you want to search : "))
        print (searchString)
        SiteApp.searchSite(searchString)
        site = eval(input("Enter the site Id : "))
        SiteApp.getSiteLoginForm(site)
        print((('Login Form:- '),SiteApp.siteResponse))
        loop()
    elif n == 2:
        print ("Adding site with Dag Site ID: 16441")
        site = '16441'  #Sample code for Non MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "DBmet1.site16441.1"
        sitePassword = "site16441.1"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = siteUserName
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = sitePassword
        provider = json.dumps(parsed_json)
        AddSiteAccount.addSiteAccount(provider)
        isPkiRequired = 0  #Setting to 0, coz PKI encryption is not required for this flow
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
        loop()
    elif n == 3:
        print ("Adding site with Dag Site ID: 16442")
        site = '16442'  #sample code for MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "Deepak3030.site16442.1"
        sitePassword = "site16442.1"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = siteUserName
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = sitePassword
        provider = json.dumps(parsed_json)
        AddSiteAccount.addSiteAccount(provider)
        isPkiRequired = 0  #Setting to 0, coz PKI encryption is not required for this flow
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
        loop()
    elif n == 41:
        print ("Adding site (PKI Encryption) with Dag Site ID: 16441")
        site = '16441'  #Sample code for Non MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "DBmet1.site16441.1"
        sitePassword = "site16441.1"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = PkiUtil.encryptPKI(siteUserName)
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = PkiUtil.encryptPKI(sitePassword)
        provider = json.dumps(parsed_json)
        AddSiteAccount.addSiteAccount(provider)
        isPkiRequired = 1  #Setting to 1, coz PKI encryption is required for this flow
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
        loop()
    elif n == 51:
        print ("Adding site (PKI Encryption) with Dag Site ID: 16442")
        site = '16442'  #sample code for MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "Deepak3030.site16442.1"
        sitePassword = "site16442.1"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = PkiUtil.encryptPKI(siteUserName)
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = PkiUtil.encryptPKI(sitePassword)
        provider = json.dumps(parsed_json)
        AddSiteAccount.addSiteAccount(provider)
        isPkiRequired = 1  #Setting to 1, coz PKI encryption is required for this flow
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
        loop()
    elif n == 4:
        print ("Adding provider account with Dag Site ID: 16441")
        site = '16441'  #Sample code for Non MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "DAPI.site16441.20"
        sitePassword = "site16441.20"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = siteUserName
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = sitePassword
        provider = json.dumps(parsed_json)
        AddProviderAccount.addProviderAccount(provider)
        isPkiRequired = 0  #Setting to 0, coz PKI encryption is not required for this flow
        AddProviderAccount.getProviderAccountDetails(AddProviderAccount.providerAccountId, isPkiRequired)
        loop()
    elif n == 5:
        print ("Adding provider account with Dag Site ID: 16442")
        site = '16442'  #sample code for MFA account addition
        SiteApp.getSiteLoginForm(site)
        provider1 = SiteApp.siteResponse
        parsed_json = json.loads(provider1)
        siteUserName = "DAPI.site16442.1"
        sitePassword = "site16442.1"
        parsed_json['provider'][0]['loginForm']['row'][0]['field'][0]['value'] = siteUserName
        parsed_json['provider'][0]['loginForm']['row'][1]['field'][0]['value'] = sitePassword
        provider = json.dumps(parsed_json)
        AddProviderAccount.addProviderAccount(provider)
        isPkiRequired = 0  #Setting to 0, coz PKI encryption is not required for this flow
        AddProviderAccount.getProviderAccountDetails(AddProviderAccount.providerAccountId, isPkiRequired)
        loop()	
    elif n == 6:
        AccountApp.getAccounts()
        loop()
    elif n == 7:
        HoldingApp.getHoldings()
        loop()
    elif n == 8:
        TransactionApp.getTransactions()
        loop()
    elif n == 9:
        print ("Holding summary with details")
        PortfolioAssetSummaryApp.getAssetSummary()
        loop()
    elif n == 10:
        print ("Holdings along with asset classification")
        HoldingAssetClassificationApp.getAssetClassificationHoldings()
        loop()
    elif n == 11:
        print ("Accounts with investment options")
        InvestmentPlanApp.getInvestmentOptions()
        loop()
    else:
        print ("exit")
loop()
