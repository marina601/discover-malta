

def bag_content(request):

    bag_items = []
    total_price = 0
    total_tickets = 0
     
    context = {
        'bag_items': bag_items,
        'total_price': total_price,
        'total_tickets': total_tickets,
    }

    return context
