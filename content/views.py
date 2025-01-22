from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Content
from .serializers import ContentSerializer, AdminContentSerializer

class AuthorContentListCreateView(generics.ListCreateAPIView):
     serializer_class = ContentSerializer
     permission_classes = [permissions.IsAuthenticated]
     def get_queryset(self):
        return Content.objects.filter(author=self.request.user)
     def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AuthorContentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Content.objects.filter(author=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       self.perform_destroy(instance)
       return Response({"message": "Content deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class AdminContentListCreateView(generics.ListCreateAPIView):
      serializer_class = AdminContentSerializer
      permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
      queryset = Content.objects.all()
    

class AdminContentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdminContentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Content.objects.all()

    def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       self.perform_destroy(instance)
       return Response({"message": "Content deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class ContentSearchView(generics.ListAPIView):
   serializer_class = ContentSerializer
   permission_classes = [permissions.IsAuthenticated]

   def get_queryset(self):
       query = self.request.query_params.get('q', None)
       if query:
          return Content.objects.filter(
              Q(title__icontains=query) |
              Q(body__icontains=query) |
              Q(summary__icontains=query) |
              Q(categories__icontains=query)
            )
       return Content.objects.none()