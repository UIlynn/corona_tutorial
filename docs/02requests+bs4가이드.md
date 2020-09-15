# 가능한 페이지 인가?
- 크롤링을 하는 2가지 조합
    - requests + bs4 : 정적페이지(=내가 추출하려는 정보가 소스코드보기에 존재)
    - selenium (+bs4) : 동적페이지(=현재 크롬창이 보여주는 화면)

# 1단계 웹 요청 하고 응답데이터 받기

```python
import requests
url="주소"
res = requests.get()
print(res.text) # html 소스코드
```

- 웹 요청 get
- 웹 요청에 대한 응답이 res에 저장

# 2단계 웹 소스코드 구문분석하기
- bs4모듈의 BeautifulSoup
- 브라우저가 구조를 분석하는 역할을 대신 해준다.

```python
# 구문 분석 bs4
soup = BeautifulSoup(res.text,'lxml')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
```

# 리스트로 정리할까 딕셔너리로 정리할까?
- key : value형태여야한다면 딕셔너리. 예시 : 지역명:수치
- value의 나열형태라면 리스트. 예시 : 길거리 사람들 키를 조사

