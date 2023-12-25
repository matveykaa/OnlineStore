from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.paginator import Paginator

from shop.forms import ReviewForm, CommentForm
from shop.models import Product, Category, Comments
from cart.forms import QuantityForm
from .tasks import delivery
from django.http import HttpResponse
from django.template.loader import render_to_string


def paginat(request, list_objects):
    p = Paginator(list_objects, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj


def home_page(request):
    products = Product.objects.all()
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def product_detail(request, slug):
    form = QuantityForm()
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).all()[:5]

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.product = product
            new_comment.save()
            # Redirect to the same page after comment submission
            return redirect('shop:product_detail', slug=slug)
    else:
        comment_form = CommentForm()

    context = {'title': product.title, 'product': product, 'form': form, 'favorites': 'favorites',
               'related_products': related_products, 'comment_form': comment_form}

    if request.user.likes.filter(id=product.id).first():
        context['favorites'] = 'remove'

    context['comment_form'] = comment_form

    return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.add(product)
    return redirect('shop:product_detail', slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.remove(product)
    return redirect('shop:favorites')


@login_required
def favorites(request):
    products = request.user.likes.all()
    context = {'title': 'Favorites', 'products': products}
    return render(request, 'favorites.html', context)


def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query).all()
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def filter_by_category(request, slug):
    """when user clicks on parent category
	we want to show all products in its sub-categories too
	"""
    result = []
    category = Category.objects.filter(slug=slug).first()
    [result.append(product) \
     for product in Product.objects.filter(category=category.id).all()]
    # check if category is parent then get all sub-categories
    if not category.is_sub:
        sub_categories = category.sub_categories.all()
        # get all sub-categories products
        for category in sub_categories:
            [result.append(product) \
             for product in Product.objects.filter(category=category).all()]
    context = {'products': paginat(request, result)}
    return render(request, 'home_page.html', context)


from django.shortcuts import render


@login_required
@require_http_methods(['GET', 'POST'])
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user_email = request.user.email
            review_text = form.cleaned_data['review_text'] + " -- FROM --\n" + user_email
            delivery.delay(review_text, user_email)
            messages.success(request, 'Thank you for your review', 'success')
            return redirect('shop:home_page')
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'form': form})
