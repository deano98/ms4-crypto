import requests
from django.utils.text import slugify
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
from .forms import PostForm
from .models import Post, Coins


def markets(request):
    '''
    Display the current price data for the top 12 cryptocurrencies
    ranked by market cap

    **Context**

    ``all_markets``
            object containing the price data

    **Template:**

    :template: `index.html`

    '''
    c_g = CoinGeckoAPI()
    all_markets = c_g.get_coins_markets(order='market_cap_desc',
                                        vs_currency='usd', per_page=12, page=1)
    return render(request, 'index.html', {'all_markets': all_markets})


def coin_posts(request, id):
    '''
    GET: Display all posts from the Post model for a particular coin,
    update Coins model with latest data from API.

    POST: Update the Post model with data submitted from a user using
    the PostForm.

    **Context**

    ``post``
        An instance of :model: `Post`
    ``coin_display``
        An instance of :model: `Coins`
    ``post_form``
        Form to create a new post
    ``request_user``
        The user who made the request, saved as a string

    **Template:**

    :template: `coins.html`

    '''
    if request.method == 'GET':
        coin_display = {}
        post = Post.objects.filter(coin_name=id)
        api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=%s&order=market_cap_desc&per_page=100&page=1&sparkline=false' % id
        response = requests.get(api)
        request_user = str(request.user)

        data = response.json()
        coin = data[0]

        coin_data = Coins(
            coin_id=coin['id'],
            coin_name=coin['name'],
            coin_price=coin['current_price'],
            market_cap=coin['market_cap'],
            rank=coin['market_cap_rank'],
            price_change=coin['price_change_24h'],
            image_url=coin['image']
        )
        coin_data.save()
        coin_display = Coins.objects.filter(coin_id=id)

        return render(request, 'coins.html', {
            'post': post,
            'coin_display': coin_display,
            'post_form': PostForm(),
            'request_user': request_user,
            },
        )

    if request.method == 'POST':
        post = Post.objects.filter(coin_name=id)
        post_form = PostForm(data=request.POST)
        coin_display = Coins.objects.filter(coin_id=id)
        request_user = str(request.user)

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
        'request_user': request_user,
        },
    )


def post_edit(request, slug, coin_id):
    '''
    Allows a user to edit their own posts

    **Template**

    :template: `coins.html`

    '''
    obj = Post.objects.get(slug=slug)
    if str(request.user) == obj.user:
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=obj)
            if post_form.is_valid():
                post_form.save()
        else:
            post_form = PostForm()

    return HttpResponseRedirect(reverse('coin_posts', args=[coin_id]))


def post_delete(request, slug, id):
    '''
    Allows a user to delete their own posts

    **Template**

    :template: `coins.html`

    '''
    obj = Post.objects.get(slug=slug)
    if str(request.user) == obj.user:
        Post.objects.filter(slug=slug).delete()

    return HttpResponseRedirect(reverse('coin_posts', args=[id]))


def post_upvote(request, id):
    '''
    If a user clicks upvote on a post, checks the Post model
    to see if user has already voted or not, model is updated
    accordingly

    **Context**

    ``post_id``
        The primary key of the corresponding post
    ``up_count``
        The up vote count of the corresponding post
    ``down_count``
        The down vote count of the corresponding post

    **Template:**

    :template: `coins.html`

    '''
    if request.method == 'POST':
        post_id = request.POST['postid']
        post = Post.objects.get(pk=id)

        if post.up_votes.filter(id=request.user.id).exists():
            post.up_votes.remove(request.user)
        elif post.down_votes.filter(id=request.user.id).exists():
            post.down_votes.remove(request.user)
            post.up_votes.add(request.user)
        else:
            post.up_votes.add(request.user)

        up_count = post.up_votes.count()
        down_count = post.down_votes.count()

        return JsonResponse({
            'post_id': post_id,
            'up_count': up_count,
            'down_count': down_count,
            })


def post_downvote(request, id):
    '''
    If a user clicks downvote on a post, checks the Post model
    to see if user has already voted or not, model is updated
    accordingly

    **Context**

    ``post_id``
        The primary key of the corresponding post
    ``up_count``
        The up vote count of the corresponding post
    ``down_count``
        The down vote count of the corresponding post

    **Template:**

    :template: `coins.html`

    '''

    if request.method == 'POST':
        post_id = request.POST['postid']
        post = Post.objects.get(pk=id)

        if post.down_votes.filter(id=request.user.id).exists():
            post.down_votes.remove(request.user)
        elif post.up_votes.filter(id=request.user.id).exists():
            post.up_votes.remove(request.user)
            post.down_votes.add(request.user)
        else:
            post.down_votes.add(request.user)

        up_count = post.up_votes.count()
        down_count = post.down_votes.count()

        return JsonResponse({
            'post_id': post_id,
            'up_count': up_count,
            'down_count': down_count,
            })
