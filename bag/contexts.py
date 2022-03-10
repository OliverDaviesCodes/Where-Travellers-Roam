from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Return shopping bag information into a dictionary
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    if total < settings.DISCOUNT_THRESHOLD:
        discount_threshold_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        discount_threshold_delta = 0

    if total > settings.DISCOUNT_THRESHOLD:
        grand_total = total - settings.DISCOUNT_AMOUNT
        discounted = True
    else:
        discounted = False
        grand_total = total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "discount_threshold_delta": discount_threshold_delta,
        "discount": settings.DISCOUNT_AMOUNT if discounted else 0,
        "grand_total": grand_total,
    }

    return context
