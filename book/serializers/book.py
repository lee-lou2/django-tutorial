import logging

from rest_framework import serializers

from book.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    """도서 시리얼라이저"""

    def __init__(self, *args, **kwargs):
        logging.info("BookSerializer > __init__")
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        """데이터 전처리"""
        logging.info("[Start] BookSerializer > to_internal_value")
        value = super().to_internal_value(data)
        logging.info("[End] BookSerializer > to_internal_value")
        return value

    def validate(self, attrs):
        """필드별 유효성 검사"""
        logging.info("[Start] BookSerializer > validate")
        data = super().validate(attrs)
        logging.info("[End] BookSerializer > validate")
        return data

    def validate_title(self, attr):
        """특정 필드 유효성 검사"""
        logging.info("BookSerializer > validate_title")
        return attr

    def to_representation(self, instance):
        """데이터 반환"""
        logging.info("[Start] BookSerializer > to_representation")
        resp = super().to_representation(instance)
        logging.info("[End] BookSerializer > to_representation")
        return resp

    def create(self, validated_data):
        """데이터 생성"""
        logging.info("[Start] BookSerializer > create")
        data = super().create(validated_data)
        logging.info("[End] BookSerializer > create")
        return data

    def update(self, instance, validated_data):
        """데이터 수정"""
        logging.info("[Start] BookSerializer > update")
        data = super().update(instance, validated_data)
        logging.info("[End] BookSerializer > update")
        return data

    def save(self, **kwargs):
        """데이터 생성/수정"""
        logging.info("[Start] BookSerializer > save")
        data = super().save()
        logging.info("[End] BookSerializer > save")
        return data

    class Meta:
        model = Book
        fields = "__all__"
