from .models import Cart, CartDetail


def get_cart_data(request):
    if request.user.is_authenticated:
        # get or create a cart for the authenticated user with status 'Inprogress'
        cart, created = Cart.objects.get_or_create(user=request.user, status='Inprogress')
        
        # retrieve cart details associated with the cart
        cart_detail = CartDetail.objects.filter(cart=cart)

        # return a dictionary containing cart-related data
        return {'cart_data': cart, 'cart_detail_data': cart_detail}
    
    else:
        # if the user is not authenticated, return an empty dictionary
        return {}
 