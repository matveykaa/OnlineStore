from cart.utils.cart import Cart
from shop.models import Category
from accounts.models import User


def return_cart(request):
    cart = len(list(Cart(request)))
    return {'cart_count': cart}


def return_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def user_image(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return {'user_image': user.image.url}
    return {}
