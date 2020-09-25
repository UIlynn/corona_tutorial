# postman 프로그램?
- GET, POST등 다양한 통신을 웹이 아닌 프로그램으로 통신시키는 프로그램
- https://www.postman.com/downloads/
- 나쁜 생각을 하면, 웹 트래픽 공격이나 데이터 변조 공격을 할 수 있다.

# 주로 사용할 HTTP 요청 메소드(또는 유형)
- GET : 리소스 취득. 주로 조회 목적으로 사용한다.
- POST : 내용 전송. 파일 전송. 데이터 제출용(주로 이 과정 이후 서버는 저장 프로세스를 진행)
- PUT : 업데이트. 내용 갱신 위주. 파일 전송 가능. POST는 없으면 새로운 데이터를 생성하나, PUT은 없으면 에러가 발생
- DELETE : 파일 삭제. 웹 리소스를 제거

# POSTMAN으로 GET 요청할 땐?
- url을 적고
- Params 항목을 작성한다
- GET요청은 URL주소로만 이루어지기 때문에 url이 자동으로 추가된다.

# POSTMAN으로 POST 요청할 땐?
- url을 적고
- Body 항목에서 form-data를 선택 후 작성한다
- POST 통신은 주로 form태그안의 데이터를 전송하는 용도로 쓰인다

# GET VS POST
- 네이버에서 검색을 하여 결과 조회를 한다. -> GET 통신
- GET통신은 원본 데이터를 수정시키지 않는다.
- 블로그 글쓰기를 사용하여 새로운 글을 업로드했다. -> POST 통신
- POST통신은 사용자가 데이터를 서버에 전송한다.
- 주로 데이터를 보내는 것은 저장 목적일 확률이 크기 때문이다.

# 간단한 GET 테스트
- https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
- 여기서 기상청 RSS 링크를 조회해보자