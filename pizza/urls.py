
from django.contrib import admin
from django.urls import path
from bakepizza.views import home, order, pizzas, edit_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This is for home page
    path('order/', order, name='order'),  # This is for ordering page
    path('pizzas', pizzas, name='pizzas'),
    path('order/<int:pk>', edit_order, name='edit_order'),
]

