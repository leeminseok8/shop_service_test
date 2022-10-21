# Shop Service
태그, 옵션 등록이 가능한 상품의 백엔드 API를 제공합니다.

---
## 목차
1. [사용법](#사용법)
2. [사용 기술 스택](#사용-기술-스택)
3. [MVP Service](#MVP-Service)
4. [API 명세서](#API-명세서)
5. [요구사항 및 기능 명세서](#요구사항-및-기능-명세서)

<br>

---

## 사용법
> 명령어를 순서대로 입력하세요.

<br>

### 1) 프로젝트 로컬 환경 설치
```
> git clone https://github.com/leeminseok8/investment_data_service.git

> cd shop_service_test
```

### 2) 가상 환경 설치
> pipenv를 사용하였습니다.
```
프로젝트 최상위 디렉토리(Pipfile 레벨)에서 실행
> pwd
~/.../shop_service_test


pipenv가 존재하지 않은 경우
> pip install pipenv

> pipenv shell


pipenv가 존재하는 경우
> pipenv shell
```

### 3) DB 생성
```
프로젝트 최상위 디렉토리(manage.py 레벨)에서 실행
> pwd
~/.../shop_service_test

> python manage.py makemigrations

> python manage.py migrate
```

### 4) 로컬(개발용) 서버 실행
```
프로젝트 최상위 디렉토리(manage.py 레벨)에서 실행
> pwd
~/.../shop_service_test

> python manage.py runserver
```

### Document

Postman Export file
- 프로젝트 최상위 디렉토리의 "Shop.postman_collection" 파일입니다.

Swagger
- 서버 실행 후 <a href="http://127.0.0.1:8000/doc/">http://127.0.0.1:8000/doc/</a> 에 접속하세요.



<br>

---

## 사용 기술 스택
- Back-end : Python, Django, DjangoRestFramework

- DataBase : MySQL

- Formater : Black

- Document : Swagger, Postman

<br>

---

## MVP Service

### 상품
- 생성
    - 상품 및 옵션을 생성합니다.
    - 기존 존재하는 태그는 연결, 신규 태그는 생성 후 연결합니다.
- 조회
    - 전체 상품 또는 특정 상품을 조회합니다.
- 수정
    - 특정 상품의 내용을 수정합니다.
    - 태그 및 옵션을 생성, 수정, 삭제할 수 있습니다.
- 삭제
    - 특정 상품을 삭제합니다.

<br>

---

## API 명세서
| Domain | endpoint | Method | 기능 | 권한 |
| --- | --- | --- | --- | --- |
| **Product** |products/ | POST | 상품 생성 | - |
|  | shop/products/ | GET | 전체 상품 조회 | - |
|  | shop/products/id | GET | 특정 상품 조회 | - |
|  | shop/products/id | PATCH | 상품 수정 | - |
|  | shop/products/id | DELETE | 상품 삭제 | - |
| **Swagger** | doc/ | - | API 문서 | - |
|  | swagger | - | Swagger UI | - |

<br>

---

## 요구사항 및 기능 명세서

### Django Rest Framework

- WritableNestedModelSerializer
<img width="1208" alt="스크린샷 2022-10-20 오후 6 53 16" src="https://user-images.githubusercontent.com/93478318/196917389-cf769947-ed2f-4ff1-92e1-d338502a3229.png">
    - WritableNestedModelSerializer를 사용하여 중첩구조 데이터를 오버라이드 없이 한 번의 요청으로 처리하였습니다.

- 문서화
    - drf-yasg를 사용한 문서화를 작성하였습니다.
        - 문서는 **/doc/** 에서 확인하실 수 있습니다.
    - Postman Export를 제출하였습니다.
        - 파일 이름은 **Shop.postman_collection** 입니다.

<br>

### Django
- ORM 쿼리 최적화
    - 최적화 전
    <img width="1185" alt="스크린샷 2022-10-18 오후 11 30 57" src="https://user-images.githubusercontent.com/93478318/196922245-9a7dd8af-5004-4f77-b368-ab3e53edcfd2.png">
    전체 상품 조회 시 쿼리입니다. 상품이 2개일 경우 총 5번의 쿼리를 호출합니다.

    - 최적화 후
    <img width="1195" alt="스크린샷 2022-10-18 오후 11 31 50" src="https://user-images.githubusercontent.com/93478318/196922160-830ac01b-9ff4-4149-afb4-fc9d0476176d.png">
    같은 요청 시 쿼리입니다. 상품이 2개일 경우 3번의 쿼리를 호출합니다. 상품 개수 당 2번의 쿼리를 줄였습니다.

<br>

### Docker(서버 접근 에러)
- Dockerfile, docker-compose.yml를 사용하여 이미지 생성과 컨테이너를 띄웠으나 서버 접근 에러가 발생하여 develop 브랜치까지만 푸시하였습니다.

<br>

### 커밋 컨벤션
- Feat: 기능 추가
- Modify: 코드 수정
- etc: 기능 외 기타 코드