from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowView, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/follow/', FollowView.as_view()),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
