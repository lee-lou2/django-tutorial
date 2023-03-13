from django.db import models


"""
[ 모델 구조 ]

Book : 도서
NewBook : 도서(신규) - 사례를 위해 생성
NewBookV2 : 도서(신규2) - 사례를 위해 생성

User : 사용자(최소 단위)
UserProfile : 사용자 프로필
Author : 작가(사용자 기반)

Post : 포스트
PostLike : 포스트 좋아요
"""


class Book(models.Model):
    """도서"""
    title = models.CharField(help_text="제목", max_length=100)

    class Meta:
        db_table = "book"


class NewBook(models.Model):
    """잘못된 사례 : 신규 도서"""
    title = models.CharField(help_text="제목", max_length=100)

    class Meta:
        db_table = "new_book"


class NewBookV2(models.Model):
    """잘못된 사례 : 신규 도서 V2"""
    name = models.CharField(help_text="제목", max_length=100)

    class Meta:
        db_table = "new_book_v2"


class UserQuerySet(models.QuerySet):
    """사용자 쿼리셋"""
    def only_author(self):
        return self.exclude(author=None)


class UserManager(models.Manager):
    """사용자 관리"""
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def only_author(self):
        return self.get_queryset().only_author()

    def exclude_author(self):
        return self.filter(author=None)


class User(models.Model):
    """사용자"""
    email = models.EmailField(help_text="이메일 주소", primary_key=True)

    def get_posts(self, title: str = "", content: str = ""):
        """작성한 모든 포스트 조회"""
        return self.post_set.filter(
            title__icontains=title,
            content__icontains=content
        )

    # 매니저 오버라이딩
    objects = UserManager()

    class Meta:
        db_table = "user"


class UserProfile(models.Model):
    """사용자 프로필"""
    user = models.OneToOneField(
        help_text="사용자",
        to=User,
        on_delete=models.CASCADE,
        related_name="r_profile"
    )
    name = models.CharField(help_text="이름", max_length=50)

    class Meta:
        db_table = "user_profile"


class Author(models.Model):
    """작가"""
    user = models.OneToOneField(help_text="사용자", to=User, on_delete=models.CASCADE)
    books = models.ManyToManyField(help_text="도서들", to=Book)

    class Meta:
        db_table = "author"


class Post(models.Model):
    """포스트"""
    user = models.ForeignKey(help_text="사용자", to=User, on_delete=models.CASCADE)
    title = models.CharField(help_text="제목", max_length=50)
    content = models.TextField(help_text="내용")
    likes = models.ManyToManyField(help_text="좋아요", to=User, through="PostLike", related_name="r_post_likes")

    class Meta:
        db_table = "post"


class PostLike(models.Model):
    """포스트 좋아요"""
    user = models.ForeignKey(help_text="사용자", to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(help_text="포스트", to=Post, on_delete=models.CASCADE)
    created = models.DateTimeField(help_text="생성일시", auto_now_add=True)

    class Meta:
        db_table = "post_like"
