from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseIncomeViewSet, basename='expenses')

urlpatterns = router.urls
