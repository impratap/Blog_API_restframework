from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# when we use views for url, not viewset for router
'''

urlpatterns=[
    path('user/',UserList.as_view()),
    path('user/<int:pk>/',UserDetail.as_view()),
    path('<int:pk>/',PostDetail.as_view()),
    path('',PostList.as_view()),
]'''

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)

urlpatterns = router.urls