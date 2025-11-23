# Summary

* [3분 Django DRF: 쉽고 빠른 실무 가이드](README.md)

## 1. 강의 소개

* [3분 Django DRF: 쉽고 빠른 실무 가이드](contents/1-1.md)
* [Django REST Framework를 선택해야 하는 이유](contents/1-2.md)

## 2. 프로젝트 설정

* [개발/테스트/운영 환경을 분리하는 settings.py 설계 전략](contents/2-1.md)
* [django-environ으로 민감 정보와 환경변수 안전하게 관리하기](contents/2-2.md)
* [AWS Parameter Store, Secrets Manager를 이용한 환경 변수 관리](contents/2-3.md)
* [structlog로 구축하는 실무형 구조화 로깅](contents/2-4.md)
* [CORS와 보안 관련 HTTP 헤더](contents/2-5.md)
* [프로젝트 시작부터 커스텀 유저 모델로 설계하는 이유와 방법](contents/2-6.md)
* [Django/DRF 메이저 버전 업그레이드 안전 가이드](contents/2-7.md)

## 3. 인증 및 권한

* [DRF 인증/권한 클래스의 전체적인 흐름](contents/3-1.md)
* [Simple JWT: Access Token, Refresh Token 기본 설정과 활용법](contents/3-2.md)
* [객체 레벨 권한(Object-level Permission) 직접 만들기](contents/3-3.md)
* [Django DRF: 외부 서비스를 위한 API Key 인증 방식 구현](contents/3-4.md)
* [DRF 기본 제공 권한 클래스 파헤치기](contents/3-5.md)
* [JWT, Session, API Key 인증을 한 번에 지원하기](contents/3-6.md)
* [효율적인 커스텀 JWTAuthentication Class 구현](contents/3-7.md)

## 4. Views & Viewsets

* [ViewSet의 내부 동작 흐름: Router부터 Response까지](contents/4-1.md)
* [APIView vs ViewSet, 실무에서 사용하는 명확한 기준](contents/4-2.md)
* [GenericViewSet과 Mixin 조합으로 나만의 CRUD 로직 만들기](contents/4-3.md)
* [@action 데코레이터로 특정 로직을 위한 깔끔한 엔드포인트 추가하기](contents/4-4.md)
* [get_serializer_class: 요청별로 다른 Serializer 동적 반환하기](contents/4-5.md)
* [perform_create: request.user와 같은 추가 정보 주입하기](contents/4-6.md)
* [pk 대신 slug나 uuid로 객체를 조회하는 get_object 커스텀](contents/4-7.md)
* [get_permissions: HTTP 메서드별로 다른 권한 클래스 적용하기](contents/4-8.md)

## 5. Serializers

* [Serializer의 내부 동작 흐름: 데이터 입력부터 출력까지](contents/5-1.md)
* [읽기/쓰기/업데이트 전용 필드 분리로 API 안정성 높이기](contents/5-2.md)
* [SerializerMethodField의 성능 함정과 캐싱으로 해결하기](contents/5-3.md)
* [Writable Nested Serializer로 중첩된 객체 한 번에 생성/수정하기](contents/5-4.md)
* [to_representation vs to_internal_value 오버라이드 기준](contents/5-5.md)
* [Serializer의 context를 활용하여 View의 정보 전달하기](contents/5-6.md)
* [ListSerializer 커스텀으로 bulk_create/update 구현](contents/5-7.md)
* [source 속성 활용: 관계 데이터 조회 및 모델의 property](contents/5-8.md)
* [의외로 잘 모르지만 유용한 HiddenField](contents/5-9.md)

## 6. API 기능 구현

* [Views & Viewsets 주요 함수 및 활용](contents/6-1.md)
* [Serializer 주요 함수 및 활용](contents/6-2.md)
* [무한 스크롤을 위한 CursorPagination과 OffsetPagination의 차이](contents/6-3.md)
* [django-filter 라이브러리로 강력한 필터링 기능 손쉽게 추가하기](contents/6-4.md)
* [사용자가 원하는 필드로 정렬하기 (OrderingFilter 커스텀)](contents/6-5.md)
* [사용자 등급별/IP별 요청량을 제어하는 Throttling 정책 설계](contents/6-6.md)
* [API 버저닝(Versioning) 전략](contents/6-7.md)
* [대용량 파일 업로드 처리와 S3 연동, 그리고 보안 고려사항](contents/6-8.md)
* [Content Negotiation으로 JSON, XML, CSV 등 다양한 포맷 응답하기](contents/6-9.md)
* [Django Channels를 이용한 WebSocket 실시간 통신 연동 기초](contents/6-10.md)

## 7. Models(ORM)

* [select_related, prefetch_related 실전 패턴과 실수 피하기](contents/7-1.md)
* [Prefetch 객체와 Subquery로 복잡한 N+1 문제 해결하기](contents/7-2.md)
* [F 객체와 Q 객체를 활용한 고급 동적 쿼리 작성법](contents/7-3.md)
* [annotate와 aggregate로 DB 레벨에서 데이터 분석/통계내기](contents/7-4.md)
* [bulk_create와 bulk_update로 대량 데이터 효율적으로 처리하기](contents/7-5.md)
* [Manager와 QuerySet을 커스텀하여 재사용 가능한 쿼리 만들기](contents/7-6.md)
* [on_delete 옵션 완벽 정복](contents/7-7.md)
* [DB Index, 언제 어떻게 추가해야 쿼리 속도가 빨라질까?](contents/7-8.md)

## 8. API 문서화

* [API 문서화: drf-spectacular로 OpenAPI 3.0(Swagger) 문서 자동 생성하기](contents/8-1.md)
* [@extend_schema를 활용해 자동화가 어려운 API까지 완벽하게 문서화](contents/8-2.md)
* [Serializer와 응답 예시를 명확하게 문서화하는 팁](contents/8-3.md)
* [API 문서에 인증 정보(API Key, Bearer Token) 포함하기](contents/8-4.md)
* [Enum과 TypedDict를 활용해 문서 가독성 높이기](contents/8-5.md)

## 9. 성능 최적화

* [django-debug-toolbar와 django-silk로 병목 지점 찾기](contents/9-1.md)
* [DRF 내장 캐싱을 활용한 API 응답 캐싱 전략](contents/9-2.md)
* [Redis를 활용한 저수준 캐시 API와 쿼리 결과 캐싱](contents/9-3.md)
* [느린 직렬화(Serialization) 과정 최적화하기](contents/9-4.md)
* [수만 건 데이터, StreamingHttpResponse로 메모리 문제 없이 응답](contents/9-5.md)
* [DB Connection Pooling으로 커넥션 부하 줄이기 (pgBouncer)](contents/9-6.md)
* [비동기 View (async def)를 활용한 I/O 바운드 작업 성능 향상](contents/9-7.md)
* [Gzip 압축 미들웨어로 API 응답 크기 줄이기](contents/9-8.md)
* [N+1 문제는 반드시 해결해야 할까?](contents/9-9.md)
* [ORM의 한계? Raw Query 사용 방법과 시점](contents/9-10.md)

## 10. 테스팅

* [APITestCase를 활용한 API 테스트 실무 패턴](contents/10-1.md)
* [factory-boy와 Faker로 실제 같은 테스트 데이터 대량 생성하기](contents/10-2.md)
* [Mock, Patch를 이용해 외부 API 의존성 테스트하기](contents/10-3.md)
* [시간에 따라 결과가 달라지는 로직 테스트하기 (freeze_gun)](contents/10-4.md)
* [테스트 DB 분리와 TransactionTestCase의 사용 시점](contents/10-5.md)
* [API 성능 테스트와 부하 테스트 (locust 활용)](contents/10-6.md)
* [테스트 커버리지 100%가 항상 좋은 것일까? (현실적인 목표 설정)](contents/10-7.md)
* [Pytest와 유용한 플러그인으로 Django 테스트 환경 개선하기](contents/10-8.md)

## 11. 배포 및 운영

* [Docker와 Docker Compose로 일관성 있는 환경 구축하기](contents/11-1.md)
* [Gunicorn/Uvicorn과 Nginx를 활용한 실서버 배포 아키텍처](contents/11-2.md)
* [CI/CD 파이프라인 구축 자동화 (GitHub Actions 기준)](contents/11-3.md)
* [Sentry 연동으로 실시간 에러 추적 및 알림 받기](contents/11-4.md)
* [Prometheus와 Grafana로 API 성능 지표 대시보드 만들기](contents/11-5.md)
* [무중단 배포 전략 (Blue-Green, Rolling 배포)](contents/11-6.md)

## 12. 유틸 및 실무 팁

* [무거운 작업은 비동기로! Celery와 Redis 연동하기](contents/12-1.md)
* [Django Signals, 꼭 필요할 때만 현명하게 사용하기](contents/12-2.md)
* [나만의 커스텀 미들웨어로 API 로깅과 모니터링 구현하기](contents/12-3.md)
* [실무에서 자주 만드는 커스텀 데코레이터 패턴](contents/12-4.md)
* [DRF 생산성을 높여주는 서드파티 라이브러리들](contents/12-5.md)
* [Django Admin 커스터마이징 꿀팁](contents/12-6.md)
* [DRF와 GraphQL(Graphene) 함께 사용하기](contents/12-7.md)

## 13. 마치며

* [강의 요약 및 클린 API 설계 원칙 되짚어보기](contents/13-1.md)
* [실무 개발자가 되기 위한 추가 학습 로드맵](contents/13-2.md)

