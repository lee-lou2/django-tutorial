from django.core.exceptions import FieldError, FieldDoesNotExist
from django.db import connection, OperationalError
from django.db.models import F, QuerySet, Count, Value, Subquery, OuterRef, CharField
from django.shortcuts import get_object_or_404
from django.test import TestCase

from book.models import Book, NewBook, NewBookV2, User, PostLike, UserProfile, Author
from core.logger import QueryLogger
from core.tests.dummy import 더미_데이터_생성


class TestORM(TestCase):
    def test_쿼리셋_조회(self):
        더미_데이터_생성()
        # 쿼리셋
        self.assertTrue(isinstance(
            Book.objects.all(),
            QuerySet
        ))
        # 쿼리셋
        self.assertTrue(isinstance(
            Book.objects.filter(title="test"),
            QuerySet
        ))
        # 객체
        self.assertFalse(isinstance(
            Book.objects.filter(title="test").first(),
            QuerySet
        ))

    def test_객체_조회(self):
        더미_데이터_생성()
        # 객체 조회
        obj1 = Book.objects.get(pk=1)
        obj2 = Book.objects.get(id=1)
        obj3 = get_object_or_404(Book, pk=1)
        obj4 = Book.objects.filter(id=1).first()
        obj5 = Book.objects.filter(id=1).last()
        obj6 = Book.objects.filter(title=obj1.title)[0]
        self.assertTrue(
            obj1 == obj2 == obj3 == obj4 == obj5 == obj6
        )

    def test_모델_매니저_사용(self):
        더미_데이터_생성()
        # 기본 함수
        user = User.objects.first()
        user.get_posts(title="test")

        # 매니저 활용
        self.assertEqual(
            User.objects.filter(author=None).count(),
            User.objects.exclude_author().count()
        )
        # 매니저의 한계
        with self.assertRaises(AttributeError):
            User.objects.filter(
                email__icontains="test"
            ).exclude_author().count()

        # 커스텀 쿼리셋 활용1
        self.assertEqual(
            # 일반 필터링과 쿼리셋 비교
            User.objects.exclude(author=None).count(),
            User.objects.only_author().count()
        )
        # 커스텀 쿼리셋 활용2
        self.assertEqual(
            # 일반 필터링과 쿼리셋 비교
            User.objects.filter(
                email__icontains="test"
            ).exclude(author=None).count(),
            User.objects.filter(
                email__icontains="test"
            ).only_author().only_author().count()  # <- 체인 형태로 활용 가능
        )

    def test_annotate_활용(self):
        더미_데이터_생성()

        # GroupBy 일반
        self.assertEqual(
            str(PostLike.objects.values("post").annotate(
                like_count=Count("post")
            ).query),
            (
                'SELECT '
                '"post_like"."post_id", '
                'COUNT("post_like"."post_id") AS "like_count" '
                'FROM "post_like" '
                'GROUP BY "post_like"."post_id"'
            )
        )
        self.assertEqual(
            PostLike.objects.values("post").annotate(
                like_count=Count("post")
            ).count(),
            PostLike.objects.values("post").distinct().count()
        )

        # GroupBy 잘못된 사례
        self.assertEqual(
            str(PostLike.objects.values("post").annotate(
                like_count=Count("post")
            ).values().query),
            (
                'SELECT '
                '"post_like"."id", '
                '"post_like"."user_id", '
                '"post_like"."post_id", '
                '"post_like"."created", '
                'COUNT("post_like"."post_id") AS "like_count" '
                'FROM "post_like" '
                'GROUP BY '
                '"post_like"."post_id", '
                '"post_like"."id", '
                '"post_like"."user_id", '
                '"post_like"."created"'
            )
        )
        # 전체 카운트와 같아짐
        self.assertEqual(
            PostLike.objects.values("post").annotate(
                like_count=Count("post")
            ).values().count(),
            PostLike.objects.count()
        )

        # 신규 컬럼 추가
        objs = PostLike.objects.values("post").annotate(
            additional_field=Value("test")
        )
        for obj in objs:
            self.assertEqual(obj.get("additional_field"), "test")
        self.assertEqual(
            str(objs.query),
            (
                'SELECT '
                '"post_like"."post_id", '
                'test AS "additional_field" '
                'FROM "post_like"'
            )
        )

        # Having
        self.assertEqual(
            str(PostLike.objects.values("post").annotate(
                like_count=Count("post")
            ).filter(like_count__lte=1).query),
            (
                'SELECT '
                '"post_like"."post_id", '
                'COUNT("post_like"."post_id") AS "like_count" '
                'FROM "post_like" '
                'GROUP BY "post_like"."post_id" '
                'HAVING COUNT("post_like"."post_id") <= 1'
            )
        )

    def test_aggregate_활용(self):
        더미_데이터_생성()

        # 전체 데이터 관리
        self.assertEqual(
            PostLike.objects.aggregate(Count("user")).get("user__count"),
            PostLike.objects.count()
        )
        self.assertEqual(
            type(PostLike.objects.aggregate(Count("user"))),
            dict
        )

    def test_ORM의_문제_n_plus_1(self):
        더미_데이터_생성()
        ql = QueryLogger(is_print=False)
        with connection.execute_wrapper(ql):
            resp = []

            # ----
            # 정참조
            # ----
            # 1. 해당 모델의 컬럼을 조회
            objs = UserProfile.objects.all()
            for obj in objs:
                resp.append(obj.name)

            # 2. n+1 이슈
            for obj in objs:
                resp.append(obj.user.email)

            # 3. 이슈 개선(select_related)
            for obj in objs.select_related("user"):
                resp.append(obj.user.email)

            # ---
            # 역참조
            # ---
            # 1. 해당 모델의 컬럼 조회
            objs = User.objects.all()
            for obj in objs:
                resp.append(obj.pk)

            # 2. n+1 이슈
            for obj in objs:
                resp.append(obj.r_profile.name)

            # 3. 이슈 개선
            for obj in objs.prefetch_related("r_profile"):
                resp.append(obj.r_profile.name)

    def test_서브_쿼리_활용(self):
        더미_데이터_생성()
        # 정상적인 사용 방법
        PostLike.objects.values("user").annotate(
            user_name=Subquery(
                UserProfile.objects.filter(user=OuterRef("user")).values("name"),
                output_field=CharField()
            )
        )
        # 서브쿼리에 반환되는 컬럼의 수가 1개 이상인 경우 오류 발생
        with self.assertRaises(OperationalError):
            print(PostLike.objects.values("user").annotate(
                user_name=Subquery(
                    UserProfile.objects.filter(user=OuterRef("user")),
                    output_field=CharField()
                )
            ))

    def test_로우_함수_활용(self):
        더미_데이터_생성()
        # 기본 조회
        users = UserProfile.objects.raw("SELECT * FROM user_profile")
        for user in users:
            self.assertTrue(isinstance(user, UserProfile))

        # 다른 테이블 데이터 조회
        ql = QueryLogger(is_print=False)
        with connection.execute_wrapper(ql):
            users = UserProfile.objects.raw("SELECT * FROM author")
            for user in users:
                # UserProfile 객체로 조회된다
                self.assertTrue(isinstance(user, UserProfile))
                # 단순히 pk 만 일치 시켜 데이터를 가져온다
                # => raw 는 데이터 전체를 가져오는게 아니라 pk 만 가져온다
                # => 심지어 모델에 포함된 데이터를 조회 할때도 n+1 이슈가 발생(매번 쿼리 호출)
                self.assertEqual(user.name, UserProfile.objects.get(pk=user.pk).name)

        # Primary Key 타입이 다른 경우 오류 발생
        with self.assertRaises(FieldDoesNotExist):
            users = UserProfile.objects.raw("SELECT * FROM user")
            for user in users:
                self.assertTrue(isinstance(user, UserProfile))

    def test_동일한_형태의_두_테이블_결합(self):
        더미_데이터_생성()
        books = Book.objects.all()
        new_books = NewBook.objects.all()
        all_book = books.union(new_books)

        self.assertEqual(all_book.count(), 6000)
        self.assertEqual(
            str(books.union(new_books).query),
            (
                'SELECT '
                '"book"."id", "book"."title" '
                'FROM "book" '
                'UNION SELECT '
                '"new_book"."id", "new_book"."title" '
                'FROM "new_book"'
            )
        )
        self.assertEqual(all_book.values("title").count(), 6000)

    def test_다른_형태의_두_테이블_결합(self):
        Book.objects.bulk_create([
            Book(title=f"test_{i}") for i in range(10)
        ])
        NewBookV2.objects.bulk_create([
            NewBookV2(name=f"test_v2_{i}") for i in range(10)
        ])
        # 가능한 명령
        all_book = Book.objects.all().union(NewBookV2.objects.all())
        for book in all_book:
            # 1. 모든 객체가 Book 모델로 변경된다
            self.assertTrue(isinstance(book, Book))
            # 2. name 필드가 자동으로 title 로 변경됐다
            # 어떻게? > 단순히 순서에 의해서!
            self.assertTrue(hasattr(book, "title"))
        with self.assertRaises(FieldError):
            # 3. name이 title 로 변경됐지만 values 명령어는 불가능
            self.assertEqual(all_book.values().count(), 20)
        # 쿼리 확인
        self.assertEqual(
            str(all_book.query),
            (
                'SELECT '
                '"book"."id", "book"."title" '
                'FROM "book" '
                'UNION SELECT '
                '"new_book_v2"."id", "new_book_v2"."name" '
                'FROM "new_book_v2"'
            )
        )

        # 그렇다면 어떻게?
        all_book = Book.objects.all().union(
            # 따로 컬럼을 변경해주는 작업이 필요
            NewBookV2.objects.all().values(
                "id", "name"
            ).annotate(
                title=F("name")
            ).values("id", "title")
        )
        # 활용 가능
        self.assertEqual(all_book.values().count(), 20)
        # 쿼리 확인
        self.assertEqual(
            str(all_book.query),
            (
                'SELECT '
                '"book"."id", "book"."title" '
                'FROM "book" '
                'UNION SELECT '
                '"new_book_v2"."id", "new_book_v2"."name" AS "title" '
                'FROM "new_book_v2"'
            )
        )
