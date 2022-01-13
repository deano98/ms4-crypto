from django.shortcuts import render
from pycoingecko import CoinGeckoAPI

def markets(request):
    cg = CoinGeckoAPI()
    all_markets = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=10, page=1)
    return render(request, 'index.html', {'all_markets': all_markets})
