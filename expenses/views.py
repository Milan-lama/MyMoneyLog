from rest_framework import viewsets, permissions,status
from rest_framework.response import Response
from .models import ExpenseIncome
from .serializers import ExpenseIncomeListSerializer, ExpenseIncomeSerializer

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ExpenseIncome.objects.all().order_by('-created_at')
        return ExpenseIncome.objects.filter(user=user).order_by('-created_at')

    # Get the serializer class based on the action
    def get_serializer_class(self):
        if self.action == 'list':
            return ExpenseIncomeListSerializer
        return ExpenseIncomeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Record deleted successfully"}, status=status.HTTP_200_OK)