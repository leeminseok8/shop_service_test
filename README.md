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

## 1. 사용법
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

### Postman Export & Swagger

Postman Export file
- 프로젝트 최상위 디렉토리의 "Shop.postman_collection" 파일입니다.

Swagger
- 서버 실행 후 <a href="http://127.0.0.1:8000/doc/">http://127.0.0.1:8000/doc/</a> 



<br>

---

## 2. 사용 기술 스택
- Back-end : Python, Django, DjangoRestFramework

- DataBase : MySQL

- Formater : Black

- Document : Swagger, Postman

<br>

---

## 3. MVP Service
> 중첩 구조의 데이터를 한 번의 요청으로 처리하도록 구현하였습니다.
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

## 4. API 명세서
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

## 5. 요구사항 및 기능 명세서

### Django Rest Framework

- WritableNestedModelSerializer
<img width="1208" alt="스크린샷 2022-10-20 오후 6 53 16" src="https://user-images.githubusercontent.com/93478318/196917389-cf769947-ed2f-4ff1-92e1-d338502a3229.png">
    - WritableNestedModelSerializer를 사용하여 별도의 오버라이드 없이 중첩구조 데이터의 create, update 요청을 처리하였습니다.

- 문서화
    - drf-yasg를 사용한 문서화를 작성하였습니다.
        - 문서는 **/doc/** 에서 확인하실 수 있습니다.
    - Postman Export를 제출하였습니다.
        - 파일 이름은 **Shop.postman_collection** 입니다.

### 투자 화면 조회
<img width="957" alt="스크린샷 2022-09-28 오후 6 36 11" src="https://user-images.githubusercontent.com/93478318/192745160-8a6eb188-ced0-472b-a2b3-81931fc9b9c7.png">

- 총 자산(total_asset)은 테이블 컬럼이 아닌 함수로 구현하여 return에 담아 응답하였습니다.

- 총 자산을 구현할 때 보유 종목(Stock 테이블)의 현금 컬럼을 어떻게 정의해야 하는지 고민했습니다. 현재는 보유 종목 테이블에 정의했지만, 이후 계좌(Account) 테이블 컬럼으로 마이그레이션할 예정입니다.
(**입금 시 현금으로 추가하여 자산을 계산해야 하기 때문**)

- 하루의 특정 시간( 예를 들어, 24시 ~ 24시 30분 )을 선정하여 한 번에 처리할 수 있도록 캐싱(redis)하는 방법으로 추가 구현을 예상하고 있습니다.

### 투자 상세 화면 조회
<img width="963" alt="스크린샷 2022-09-28 오후 6 35 39" src="https://user-images.githubusercontent.com/93478318/192745057-ee297af0-999e-4d92-b694-4a0367635ae7.png">

- 총 자산(total_asset)과 같이 총 수익(Total_proceed), 수익률(yeild)은 함수로 구현하였습니다.

### 보유 종목 화면 조회
<img width="965" alt="스크린샷 2022-09-28 오후 6 37 20" src="https://user-images.githubusercontent.com/93478318/192745399-13b0c17d-6e72-44e9-9839-34466254f1da.png">

- 로그인 유저 인증 후 참조하는(fk) 계좌의 보유 종목을 호출합니다.

### 입금 계좌 검증
<img width="964" alt="스크린샷 2022-09-28 오후 6 38 23" src="https://user-images.githubusercontent.com/93478318/192745653-7a751223-5a46-4716-8c70-f7ebb04b727a.png">

- 유저, 계좌 검증을 구현하였습니다.

- 기존 요청 예시값으로는 [유저 이름, 계좌 번호, 입금 금액]을 JSON으로 받았습니다. 하지만 이 경우, http method를 POST로 받아야 하여 테이블 컬럼이 중복되는 상황, 즉 정규화가 필요합니다. 이 부분에서 **역정규화하여 진행할 지 정규화하여 진행할 지 고민끝에 개명할 경우를 대비하여 정규화하여 진행하였습니다.**

### 계좌 자산 업데이트
<img width="961" alt="스크린샷 2022-09-28 오후 6 39 37" src="https://user-images.githubusercontent.com/93478318/192745904-ee349ae0-774e-437e-b9fc-ce3a5855c740.png">

- 검증 완료 후 검증된 데이터로 hashing하고 클라이언트에서 요청하면 DB의 데이터와 대조하여 실제 계좌를 업데이트합니다.

- [투자 화면 조회](#투자-화면-조회)의 총 자산을 구현할 때 고민한 것처럼 Stock 테이블의 현금 컬럼을 업데이트하는 방향으로 구현할 예정입니다. 총 자산뿐만 아닌 현금 자산과 함께 업데이트하도록 분석하였습니다.
