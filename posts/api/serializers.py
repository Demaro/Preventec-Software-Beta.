from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
	)



from accounts.api.serializers import UserDetailSerializer


from posts.models import Post



class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
				'title',
				'content',
				'draft',
			
		]

post_detail_url = HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='slug',
		)

class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	comments = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
				'url',
				'id',
				'user',
				'title',
				'slug',
				'content',
				'publish',
				'image',
				'comments',
		]


	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image


class PostListSerializer(ModelSerializer):
	url = post_detail_url
	image = SerializerMethodField()
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
				'url',
				'user',
				'title',
				'slug',
				'content',
				'publish',
				'image',
		]

	def get_user(self, obj):
		return str(obj.user.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

