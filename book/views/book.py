import logging

from rest_framework import viewsets, permissions, pagination

from book.models.book import Book
from book.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """도서 관리"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = pagination.PageNumberPagination
    lookup_field = "pk"

    def get_queryset(self):
        """쿼리셋 조회"""
        logging.info("[Start] BookViewSet > get_queryset")
        queryset = super().get_queryset()
        logging.info("[End] BookViewSet > get_queryset")
        return queryset

    def get_object(self):
        """객체 조회"""
        logging.info("[Start] BookViewSet > get_object")
        _object = super().get_object()
        logging.info("[End] BookViewSet > get_object")
        return _object

    def get_permissions(self):
        """퍼미션 조회"""
        logging.info("[Start] BookViewSet > get_permissions")
        _permissions = super().get_permissions()
        logging.info("[End] BookViewSet > get_permissions")
        return _permissions

    def get_serializer(self, *args, **kwargs):
        """시리얼 라이저 조회"""
        logging.info("[Start] BookViewSet > get_serializer")
        serializer = super().get_serializer(*args, **kwargs)
        logging.info("[End] BookViewSet > get_serializer")
        return serializer

    def get_serializer_class(self):
        """시리얼 라이저 클래스 조회"""
        logging.info("[Start] BookViewSet > get_serializer_class")
        serializer_class = super().get_serializer_class()
        logging.info("[End] BookViewSet > get_serializer_class")
        return serializer_class

    def get_serializer_context(self):
        """시리얼 라이저 Context 조회"""
        logging.info("[Start] BookViewSet > get_serializer_context")
        serializer_context = super().get_serializer_context()
        logging.info("[End] BookViewSet > get_serializer_context")
        return serializer_context

    def get_exception_handler(self):
        """오류 핸들러 클래스 조회"""
        logging.info("[Start] BookViewSet > get_exception_handler")
        handler = super().get_exception_handler()
        logging.info("[End] BookViewSet > get_exception_handler")
        return handler

    def handle_exception(self, exc):
        """오류 핸들링"""
        logging.info("[Start] BookViewSet > handle_exception")
        exception = super().handle_exception(exc)
        logging.info("[End] BookViewSet > handle_exception")
        return exception

    def create(self, request, *args, **kwargs):
        """데이터 생성"""
        logging.info("[Start] BookViewSet > create")
        resp = super().create(request, *args, **kwargs)
        logging.info("[End] BookViewSet > create")
        return resp

    def update(self, request, *args, **kwargs):
        """데이터 업데이트 - 전체"""
        logging.info("[Start] BookViewSet > update")
        resp = super().update(request, *args, **kwargs)
        logging.info("[End] BookViewSet > update")
        return resp

    def partial_update(self, request, *args, **kwargs):
        """데이터 업데이트 - 부분"""
        logging.info("[Start] BookViewSet > partial_update")
        resp = super().partial_update(request, *args, **kwargs)
        logging.info("[End] BookViewSet > partial_update")
        return resp

    def retrieve(self, request, *args, **kwargs):
        """데이터 상세 조회"""
        logging.info("[Start] BookViewSet > retrieve")
        resp = super().retrieve(request, *args, **kwargs)
        logging.info("[End] BookViewSet > retrieve")
        return resp

    def destroy(self, request, *args, **kwargs):
        """데이터 삭제"""
        logging.info("[Start] BookViewSet > destroy")
        resp = super().destroy(request, *args, **kwargs)
        logging.info("[End] BookViewSet > destroy")
        return resp
