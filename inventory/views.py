from django.shortcuts import render

# Static data
ITEMS = [
    {'id': 1, 'name': 'Item 1', 'description': 'Description for item 1', 'quantity': 10, 'price': 15.00},
    {'id': 2, 'name': 'Item 2', 'description': 'Description for item 2', 'quantity': 5, 'price': 20.00},
    {'id': 3, 'name': 'Item 3', 'description': 'Description for item 3', 'quantity': 8, 'price': 25.00},
]

def item_list(request):
    return render(request, 'item_list.html', {'items': ITEMS})

def item_detail(request, item_id):
    item = next((item for item in ITEMS if item['id'] == item_id), None)
    if item is None:
        return render(request, '404.html')  # Optional: create a 404 page
    return render(request, 'item_detail.html', {'item': item})
