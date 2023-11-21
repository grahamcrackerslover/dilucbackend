from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Review
from reviews.serializers import ReviewSerializer
from shop.models import Purchase
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def add_review(request):
    review_code = request.data.get('code_used')
    try:
        purchase = Purchase.objects.get(review_code=review_code)
    except Purchase.DoesNotExist:
        return Response({"error": "Invalid review code"}, status=400)

    review_data = request.data.copy()
    # review_data['item'] = purchase.item.id
    review_serializer = ReviewSerializer(data=review_data)
    if Review.objects.filter(code_used=review_data['code_used']).exists():
        return Response({"error": "Review code already used"}, status=400)

    if review_serializer.is_valid():
        review_serializer.save()
        return Response(review_serializer.data, status=201)
    return Response(review_serializer.errors, status=400)


@api_view(['GET'])
def list_reviews(request):
    # Запрос будет отправляться в формате /api/reviews/?page=x
    page_number = int(request.query_params.get('page', 1))
    page_size = 5
    start = (page_number - 1) * page_size
    end = start + page_size

    count = Review.objects.count()
    queryset = Review.objects.order_by('-created_at')[start:end]
    # Проверить есть ли отзывы на следующей странице
    has_next = Review.objects.order_by('-created_at')[end:end + page_size].exists()

    # Проверяем есть ли отзывы (надо будет заменить на какой-то код, чтобы
    # фронтенд понимал, есть ли еще отзывы и убирал кнопку
    if not queryset:
        return Response({"error": "No reviews found"}, status=200)

    serializer = ReviewSerializer(queryset, many=True)

    return Response({
        "reviews": serializer.data, "page": page_number, "has_next": has_next, "count": count}
    )


@api_view(['GET'])
def reviews_stats(request):
    # Get the count of positive and negative reviews
    positive_reviews = Review.objects.filter(is_positive=True).count()
    negative_reviews = Review.objects.filter(is_positive=False).count()

    return Response({
            "positive_reviews": positive_reviews,
            "negative_reviews": negative_reviews
        }
    )