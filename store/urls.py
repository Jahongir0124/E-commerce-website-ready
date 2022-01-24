from . import views
from django.urls import path
urlpatterns=[
             path('',views.index,name='home'),
             # path('navbar/',views.products,name=''),
             # path('categories/',views.categories,name='categories'),
             # path('products/',views.products_1,name=''),
             path('categories/''<int:cat_id>/',views.products,name='products'),
             # path('categories/''<int:cat_id>/<int:pd_id>/',views.order,name='order'),
             path('box/',views.box,name='box'),
             # path('update_details/',views.update_details,name=''),
             # path('form/',views.form,name=''),
             # path('add_product/',views.add_product,name=''),
             # path('user/',views.user_form,name=''),
             path('login/',views.log_in,name='login'),
             path('order/''<int:pd_id>/',views.order,name='order'),
             path('register/',views.create_user,name='register'),
             # path('customer/', views.customer, name='login'),
             ]