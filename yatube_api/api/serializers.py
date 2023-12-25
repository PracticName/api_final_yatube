from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    def validate_following(self, value):
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=value
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя')
        return value

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя'
            )
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        '''validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Пользователь не может подписаться сам на себя'
            )
        ]'''

    '''def validate(self, data):
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=data['following']
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя')
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя'
            )
        return data'''
