from django.urls import path
from .views import AuthorContentListCreateView, AuthorContentRetrieveUpdateDeleteView, AdminContentListCreateView, AdminContentRetrieveUpdateDeleteView, ContentSearchView

urlpatterns = [
  path('author/', AuthorContentListCreateView.as_view(), name="author-content-list-create"),
  path('author/<int:pk>/', AuthorContentRetrieveUpdateDeleteView.as_view(), name='author-content-retrieve-update-delete'),
  path('admin/', AdminContentListCreateView.as_view(), name='admin-content-list-create'),
  path('admin/<int:pk>/', AdminContentRetrieveUpdateDeleteView.as_view(), name='admin-content-retrieve-update-delete'),
  path('search/', ContentSearchView.as_view(), name="content-search")
]