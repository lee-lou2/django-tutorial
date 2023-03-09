import random

from book.models import Book, Author, User, UserProfile, Post, PostLike, NewBook, NewBookV2


def 더미_데이터_생성():
    # 사용자-작가 생성
    users = []
    authors = []
    for i in range(1000):
        user = User.objects.create(email=f"test_email_{i}@test.com")
        users.append(user)
        UserProfile.objects.create(user=user, name=f"test_name_{i}")
        if random.choice([True, False]):
            author = Author.objects.create(user=user)
            authors.append(author)
    # 도서 생성
    book_list = [Book(title=f"test_book_{i}") for i in range(5000)]
    books = Book.objects.bulk_create(book_list)
    # 작가 - 도서 매칭
    for author in authors:
        author.books.add(*random.choices(books, k=random.randint(1, 5)))
    # 포스트 생성
    for i in range(300):
        post = Post.objects.create(
            user=random.choices(users)[0],
            title=f"test_post_{i}",
            content=f"test_content_{i}"
        )
        for _ in range(random.randint(1, 10)):
            PostLike.objects.create(
                user=random.choices(users)[0],
                post=post
            )
    # 신규 도서 생성
    [NewBook.objects.create(title=f"test_new_book_{i}") for i in range(1000)]
    [NewBookV2.objects.create(name=f"test_new_book_v2_{i}") for i in range(1000)]
