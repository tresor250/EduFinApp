from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Testing, Transaction, Budget, Category
from core.serializers import TestingSerializer, TransactionSerializer, BudgetSerializer, CategorySerializer


# --- Existing views from Lab 1 ---

def testing_view(request):
    data = Testing.objects.all()
    serializer = TestingSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


# --- New CRUD views ---

class TransactionListView(APIView):
    """
    GET  /api/transactions/     -> List all transactions
    POST /api/transactions/     -> Create a new transaction
    """

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailView(APIView):
    """
    GET    /api/transactions/<id>/  -> Retrieve a single transaction
    PUT    /api/transactions/<id>/  -> Update a transaction
    DELETE /api/transactions/<id>/  -> Delete a transaction
    """

    def get_object(self, id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        transaction = self.get_object(id)
        if transaction is None:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BudgetListView(APIView):
    """
    GET  /api/budgets/     -> List all budgets
    POST /api/budgets/     -> Create a new budget
    """

    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(APIView):
    """
    GET  /api/categories/     -> List all categories
    POST /api/categories/     -> Create a new category
    """

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    """
    GET    /api/categories/<id>/  -> Retrieve a single category
    PUT    /api/categories/<id>/  -> Update a category
    DELETE /api/categories/<id>/  -> Delete a category
    """

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        if category is None:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
