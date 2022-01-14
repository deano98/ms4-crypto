from django.shortcuts import render, get_object_or_404, reverse
from pycoingecko import CoinGeckoAPI
from .forms import PostForm, CommentForm
from .models import Post, Comment, Coins
import requests
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def markets(request):
    cg = CoinGeckoAPI()
    all_markets = cg.get_coins_markets(order='market_cap_desc', vs_currency='usd', per_page=10, page=1)
    return render(request, 'index.html', {'all_markets': all_markets})

def coin_posts(request, id):
    if request.method == 'GET':
        coin_display = {}
        post = Post.objects.filter(coin_name=id)
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
            'post_form': PostForm(),
            },
        )

    if request.method == 'POST': 
        post = Post.objects.filter(coin_name=id)
        post_form = PostForm(data=request.POST)
        coin_display = Coins.objects.filter(coin_id=id)

        if post_form.is_valid():
            post_form.instance.coin_name = request.POST['coin_name']
            post_form.instance.user = request.user.username
            post_form.instance.slug = slugify(request.POST['title'])
            post_form.save()
        else:
            post_form = PostForm()


        return render(request, 'coins.html', { 
            'post': post,
            'coin_display': coin_display,
            'post_form': post_form,
            },
        )

def post_detail(request, slug):

    if request.method =='GET':
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.replies.order_by("-created_on")

        return render(request, 'coin_detail.html', { 
            'comments': comments,
            'post': post,
            'comment_form': CommentForm(),
            },
        )

    if request.method == 'POST':
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.replies.order_by("-created_on")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.user = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'coin_detail.html', { 
            'comments': comments,
            'post': post,
            'comment_form': comment_form,
            },
        )

def post_upvote(request, id):

    if request.method =='POST':
        post_id = request.POST['postid']
        post = Post.objects.get(pk = post_id)
        
        if post.up_votes.filter(id=request.user.id).exists():
            post.up_votes.remove(request.user)
        elif post.down_votes.filter(id=request.user.id).exists():
            post.down_votes.remove(request.user)
            post.up_votes.add(request.user)
        else:
            post.up_votes.add(request.user)

        up_count = post.up_votes.count()
        down_count = post.down_votes.count()
        count = up_count - down_count

        return JsonResponse({
            'post_id': post_id,
            'count': count,
            })

def post_downvote(request, id):

    if request.method =='POST':
        post_id = request.POST['postid']
        post = Post.objects.get(pk = post_id)
        
        if post.down_votes.filter(id=request.user.id).exists():
            post.down_votes.remove(request.user)
        elif post.up_votes.filter(id=request.user.id).exists():
            post.up_votes.remove(request.user)
            post.down_votes.add(request.user)
        else:
            post.down_votes.add(request.user)

        up_count = post.up_votes.count()
        down_count = post.down_votes.count()
        count = up_count - down_count

        return JsonResponse({
            'post_id': post_id,
            'count': count,
            })