from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
from .forms import PostForm
from .models import Post, Comment, Coins
import requests

def markets(request):
    cg = CoinGeckoAPI()
    all_markets = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=10, page=1)
    return render(request, 'index.html', {'all_markets': all_markets})

def coin_posts(request, id):
    if request.method == 'GET':
        coin_display = {}
        post = Post.objects.filter(coin=id)
        api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=%s&order=market_cap_desc&per_page=100&page=1&sparkline=false' % id
        response = requests.get(api)

        data = response.json()
        coin = data[0]        

        coin_data = Coins(
            coin_id = coin['id'],
            coin_name = coin['name'],
            coin_price = coin['current_price'],
            market_cap = coin['market_cap'],
            rank = coin['market_cap_rank'],
            price_change = coin['price_change_24h'],
            image_url = coin['image']
        )
        coin_data.save()
        coin_display = Coins.objects.filter(coin_id=id)

        return render(request, 'coins.html', { 
            'post': post,
            'coin_display': coin_display,
            },
        )