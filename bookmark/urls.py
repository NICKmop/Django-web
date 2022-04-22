from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # http://127.0.0.1:8000/bookmark/
    path('add/', BookmarkCreateView.as_view(), name='add'),  # http://127.0.0.1:8000/bookmark/add/
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),  # http://127.0.0.1:8000/bookmark/detail/1
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
]