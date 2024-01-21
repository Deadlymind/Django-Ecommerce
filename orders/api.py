from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import datetime

from .serializers import CartSerializer, CartDetailSerializer, OrderDetailSerializer, OrderSerializer
from .models import Order, OrderDetail, Cart, CartDetail, Coupon
from products.models import Product
from settings.models import DeliveryFee


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()

        user = User.objects.get(username=self.kwargs['username'])

        queryset = queryset.filter(user=user)

        return queryset

    # def list(self,request,*args, **kwargs):
    #     queryset = super(OrderListAPI, self).get_queryset()

    #     user = User.objects.get(username=self.kwargs['username'])

    #     queryset = queryset.filter(user=user)
    #     data = OrderSerializer(queryset, many=True).data

    #     return Response({'orders':data})


class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    


class ApplyCouponAPI(generics.GenericAPIView):
    
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])            #url
        coupon = get_object_or_404(Coupon, code=request.data['coupon_code']) #request body
        delivery_fee = DeliveryFee.objects.last().fee
        cart = Cart.objects.get(user=user,status='Inprogress')

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = cart.cart_total / 100*coupon.discount
                sub_total = cart.cart_total - coupon_value

                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()

                coupon.quantity -= 1
                coupon.save()

                return Response({'message': "Coupon was applied successfully" })
            
            else:
                return Response({'message': "Coupon is invalid or expired" })
        
        return Response({'message':'Coupon not found'}) 

# class ApplyCouponAPI(generics.GenericAPIView):
    
#     def post(self, request, *args, **kwargs):
#         # Assuming the 'username' is part of the URL kwargs
#         user = User.objects.get(username=self.kwargs['username'])

        # # Check if 'coupon_code' is in the request data
        # if 'coupon_code' in request.data:
        #     coupon_code = request.data['coupon_code']
        #     coupon = get_object_or_404(Coupon, code=coupon_code)

#             delivery_fee = DeliveryFee.objects.last().fee
#             cart = Cart.objects.get(user=user, status='Inprogress')

#             if coupon and coupon.quantity > 0:
#                 today_date = datetime.datetime.today().date()

#                 if today_date >= coupon.start_date and today_date <= coupon.end_date:
#                     coupon_value = cart.cart_total / 100 * coupon.discount
#                     sub_total = cart.cart_total - coupon_value

#                     cart.coupon = coupon
#                     cart.total_with_coupon = sub_total
#                     cart.save()

#                     coupon.quantity -= 1
#                     coupon.save()

#                     return Response({'message': "Coupon was applied successfully" })
                
#                 else:
#                     return Response({'message': "Coupon is invalid or expired" })
            
#             else:
#                 return Response({'message': 'Coupon not found'})

#         else:
#             return Response({'message': 'Coupon code not provided in the request data'})


# class ApplyCouponAPI(generics.GenericAPIView):
    
#     def post(self, request, *args, **kwargs):
#         user = User.objects.get(username=self.kwargs['username'])  # Assuming 'username' is part of the URL
#         coupon_code = request.data.get('coupon_code', None)  # Use get to avoid KeyError

#         if not coupon_code:
#             return Response({'message': 'Coupon code not provided in the request data'})

#         coupon = get_object_or_404(Coupon, code=coupon_code)
#         delivery_fee = DeliveryFee.objects.last().fee
#         cart = Cart.objects.get(user=user, status='Inprogress')

#         if coupon and coupon.quantity > 0:
#             today_date = datetime.today().date()

#             if today_date >= coupon.start_date and today_date <= coupon.end_date:
#                 coupon_value = cart.cart_total / 100 * coupon.discount
#                 sub_total = cart.cart_total - coupon_value

#                 cart.coupon = coupon
#                 cart.total_with_coupon = sub_total
#                 cart.save()

#                 coupon.quantity -= 1
#                 coupon.save()

#                 return Response({'message': "Coupon was applied successfully" })
            
#             else:
#                 return Response({'message': "Coupon is invalid or expired" })
        
#         return Response({'message': 'Coupon not found'})



