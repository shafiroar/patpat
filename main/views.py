from django.shortcuts import render

# Create your views here.
def show_main(request):
    product = [
        {'product': 'Whiskas Kitten Food',
        'price': 53000,
        'description': 'Premium cat food with essential nutrients',
        'pet' :'Cat'},

        {'product': 'Royal Canin Cat Food',
        'price': 36000,
        'description': 'Delicious cat food to keep your cat healthy.',
        'pet' :'Cat'},

        {'product': 'Me-O Kitten Food',
        'price': 24000,
        'description': 'Kitten food for your growing canine companion',
        'pet' :'Cat'},

        {'product': 'Purina Dog Food',
        'price': 45000,
        'description': 'Nutritious dog food for active and playful dogs.',
        'pet': 'Dog'},

        {'product': 'Hills Science Diet Puppy Food',
        'price': 55000,
        'description': 'Specially formulated puppy food for optimal growth.',
        'pet': 'Dog'},

        {'product': 'Pedigree Adult Dog Food',
        'price': 38000,
        'description': 'A balanced diet for adult dogs for overall health.',
        'pet': 'Dog'},
    ]

    context = {
        'product' : product,
    }

    return render(request, "main.html", context)

