"""
Post모델
    author = User와 연결
    title
    content
    created_date
        DateTimeField사용
    modified_date
        DateTimeField사용

Comment모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User모델
    name
    created_date
    modified_date
"""

from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User', on_delete=models.CASCADE)  # User클래스가 아래에 있기 때문에 문자열 표시를 해 줘야 한다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 이 Post에 좋아요를 누른사람들
    like_user = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_posts',
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name=None
    )

    def __str__(self):
        return self.title


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=100)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_user'


"""
PostLike
    post = Post
    user = User
    created_date
    
Tag
    title
    
Post모델
    like_users = User와 MTM으로 연결, Intermediate model로 PostLike모델을 사용
    tags = MTM으로 Tag와 연결
    
    def like_post(self, user):
        return '해당 user의 PostLike를 생성 이 후 생성 객체를 리턴'
    
    def add_tag(self, tag_name):
        return '해당 tag_name의 Tag를 생성 또는 기존항목 가져와서 Post에 추가 이후 Tag리턴'

"""
