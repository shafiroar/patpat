from django.shortcuts import render

# Create your views here.
def show_main(request):
    product = [
        {'product': 'Whiskas Kitten Food',
        'price': 53000,
        'description': 'Premium cat food with essential nutrients',
        'pet' :'Cat',
        'image_url': 'https://www.petworld.ie/wp-content/uploads/2016/03/whiskas-meaty-meals-in-gravy-petworld.ie_.webp'},


        {'product': 'Whiskas Cat Food',
        'price': 36000,
        'description': 'Delicious cat food to keep your cat healthy.',
        'pet' :'Cat',
         'image_url': 'https://www.justdogsstore.com/wp-content/uploads/2021/07/61daAb0Hv2L._SL1000_.jpg'},

        {'product': 'Whiskas Cat Milk',
        'price': 24000,
        'description': 'Cat milk for your growing canine companion',
        'pet' :'Cat',
        'image_url': 'https://i0.wp.com/www.petmania.ie/wp-content/uploads/2021/11/54991.jpg?fit=600%2C600&ssl=1'},

        {'product': 'Iams Dog Food',
        'price': 45000,
        'description': 'Nutritious dog food for active and playful dogs.',
        'pet': 'Dog',
         'image_url': 'https://www.iams.com/cdn-cgi/image/width=600,height=600,f=auto,quality=90/sites/g/files/fnmzdf3396/files/migrate-product-files/images/umdk8risrxj5a1vsuffs.png'},

        {'product': 'Nature Science Diet Puppy Food',
        'price': 55000,
        'description': 'Specially formulated puppy food for optimal growth.',
        'pet': 'Dog',
         'image_url': 'https://cdn11.bigcommerce.com/s-lmdkge2gql/images/stencil/1280x1280/products/3790/4460/Nature%20Diet%20Grain%20Free%20Puppy__55984.1651786273.jpg?c=1'},

        {'product': 'Lucy Adult Dog Food',
        'price': 38000,
        'description': 'A balanced diet for adult dogs for overall health.',
        'pet': 'Dog',
         'image_url': 'https://www.lucypetproducts.com/wp-content/uploads/2019/07/ChBR_25lb-500x500.jpg.webp'}
    ]

    context = {
        'product' : product,
    }

    return render(request, "main.html", context)

