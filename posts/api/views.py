from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView, 
	UpdateAPIView, 
	DestroyAPIView, 
	CreateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)



from posts.models import Post

from django.db.models import Q

from .serializers import ( 
	PostDetailSerializer, 
	PostListSerializer, 
	PostCreateUpdateSerializer
	)



class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	#permission_classes = [IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	permission_classes = [AllowAny]


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	permission_classes = [IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	permission_classes = [IsOwnerOrReadOnly]


class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	permission_classes = [AllowAny]
	search_fields = ['title', 'content', 'user__first_name']
	pagination_class = PostPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all() #filter.(user=self.request.user)
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(title__icontains=query)|
					Q(content__icontains=query)|
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list



