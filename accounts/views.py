from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect

from .forms import SignupForm, UserActivateForm
from .models import Porfile

from products.models import Product, Brand, Review
from orders.models import Order, OrderDetail
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone

# Create your views here.

def signup(request):
    pass
    """
    -- create new user --
    -- send email code --
    -- redirect to activate --
    """
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=False)
            user.is_active = False
            form.save() # trigger signal --> create profile --> send code
            profile = Porfile.objects.get(user__username=username)
            # send email code
            send_mail(
                "Activate your account",
                f"Welcome {username}\n Use this code {profile.code} to activate your account",
                "oussamaayari2014@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_activate(request, username):
    """
    -- activate user --
    -- redirect to login --
    """
    profile = Porfile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                profile.save()

                return redirect('/accounts/login')

    else:
        form = UserActivateForm()
    return render(request, 'accounts/activate.html', {'form': form})






def dashboard(request):
    users = User.objects.all().count()
    products = Product.objects.all().count()
    orders = Order.objects.all().count()
    brands = Brand.objects.all().count()
    reviews = Review.objects.all().count()

    new_products = Product.objects.filter(flag='New').count()
    sale_products = Product.objects.filter(flag='sale').count()
    feature_products = Product.objects.filter(flag='Feature').count()

    # Retrieve sales data for the last six months
    sales_data = OrderDetail.objects.filter(order__status='Delivered').annotate(month=TruncMonth('order__order_time')).values('month').annotate(total_amount=Sum('total')).order_by('-month')[:6]

    # Extract labels and data for the sales trend chart
    sales_labels = [entry['month'].strftime('%b %Y') for entry in sales_data]
    sales_amounts = [entry['total_amount'] for entry in sales_data]

    return render(request, 'accounts/dashboard.html', {
        'users': users,
        'products': products,
        'orders': orders,
        'brands': brands,
        'reviews': reviews,
        'new_products': new_products,
        'sale_products': sale_products,
        'feature_products': feature_products,
        'sales_labels': sales_labels,
        'sales_amounts': sales_amounts,
    })

# def dashboard(request):
#     # Product-related statistics
#     total_products = Product.objects.all().count()
#     new_products = Product.objects.filter(flag='New').count()
#     sale_products = Product.objects.filter(flag='sale').count()
#     feature_products = Product.objects.filter(flag='Feature').count()

#     # Order-related statistics
#     total_orders = Order.objects.all().count()
#     total_order_amount = Order.objects.aggregate(Sum('total'))['total__sum']

#     # User-related statistics
#     total_users = User.objects.all().count()

#     # Review-related statistics
#     total_reviews = Review.objects.all().count()

#     # Sample data for charts (replace with your actual data)
#     sales_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
#     sales_amounts = [100, 150, 200, 180, 250, 300]

#     # Sample data for recent orders and notifications (replace with your actual data)
#     recent_orders = OrderDetail.objects.filter(order__status='Delivered')[:5]
#     notifications = ['New User Registered', 'Product Out of Stock']

#     # Sample data for user activity log (replace with your actual data)
#     user_activity_log = [{'user': User.objects.first(), 'timestamp': timezone.now()}]

#     return render(request, 'accounts/dashboard.html', {
#         'total_products': total_products,
#         'new_products': new_products,
#         'sale_products': sale_products,
#         'feature_products': feature_products,
#         'total_orders': total_orders,
#         'total_order_amount': total_order_amount,
#         'total_users': total_users,
#         'total_reviews': total_reviews,
#         'sales_labels': sales_labels,
#         'sales_amounts': sales_amounts,
#         'recent_orders': recent_orders,
#         'notifications': notifications,
#         'user_activity_log': user_activity_log,
#     })