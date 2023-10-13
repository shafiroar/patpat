from django.urls import path
from main.views import add_product_ajax, get_product_json, register
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product,  decrement_product, remove_product
from main.views import login_user
from main.views import logout_user
from main.views import edit_product, add_product_ajax, get_product_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json_by_id, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
    path('remove_product/<int:product_id>/',remove_product, name='remove_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]