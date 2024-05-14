from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexpage,name="index"),
    path('about.html',views.aboutuspage,name="about"),
    path('login',views.signupapge,name="signup"),
    path('registerdata', views.registerdata, name="registerdata"),
    path('logindata', views.logindata, name="logindata"),
    path('logout', views.logout, name="logout"),
    path('contact.html',views.contactuspage,name="contact"),
    path('contactdata', views.contactdata, name="contactdata"),
    path('shop.html',views.servicespage,name="service"),
    path('addproduct', views.addproductpage, name="addproduct"),
    path('addproductdata', views.addproductdata, name="addproductdata"),
    # path('shop-details.html/<int:id>', views.shopdetailsingle, name="single"),
    path('inquiry', views.inquiry, name="inquiry"),
    path('inquirydata', views.inquirydata, name="inquirydata"),
    path('feadbackdata', views.feadbackdata, name="feadbackdata"),
    path('searchdata', views.searchdata, name="searchdata"),
    path('changepassword.html',views.changepasswordpage,name="changepassword.html"),
    path('change_password',views.change_password, name='change_password'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('forgotpwd', views.forgotpwd, name='forgotpwd'),
    path("category.html" , views.catergory, name="category.html"),
    path("products.html", views.products, name="products.html"),
    path("profile.html", views.profile, name="profile.html"),
    path("product-details.html", views.productDetails, name="product-details.html")
]