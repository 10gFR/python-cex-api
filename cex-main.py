from cextrade import Cextrade

cex = Cextrade(api_user='YOUR USER NAME', api_key='YOUR API KEY', api_secret='YOUR API SECRET')

print cex.ticker()
print cex.account_balance()

