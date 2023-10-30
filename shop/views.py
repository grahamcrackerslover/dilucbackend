from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item, Purchase
from .serializers import ItemSerializer, PurchaseSerializer


# Create your views here.
@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def buy_item(request):
    try:
        item_id = request.data['item_id']
        item = Item.objects.get(id=item_id)
        purchase = Purchase.objects.create(item=item)

        # TODO add verification and order completion
        return Response({'message': 'Покупка совершена успешно', 'review_code': purchase.review_code}, status=200)
    except Item.DoesNotExist or KeyError:
        return Response({'message': 'Что-то пошло не так. Обратитесь в поддержку'}, status=400)
