# **Jinja2 Template 표현식 개요**
- 템플릿(HTML)은 기본적으로 그냥 보여지는 역할을 수행함
- 프로그래밍적 연산 등이 필요한 경우에 아래 기호들이 쓰인다. 

# **표현식(기본)**
- {%  : block start string : 프로그래밍 영역 시작 기호
- %}  : block end string : 프로그래밍 영역 끝 기호
- {{ : variable start string : 변수 출력 시작 기호
- }} : variable end string : 변수 출력 끝 기호
- {# : comment start string : 주석 시작 기호
- }# : comment end string : 주석 끝 기호

# **예제 1 - 반복문**
```html
    {% for i in range(10) %}
        양산하고 싶은 html
    {% endfor %}
```


```html
숫자 출력 : {% for i in range(10) %} {{i}} {% endfor %}
```
- 반복문 시작을 위해 {% for ... %} 가 작성되었다.
- 반복문 끝을 위해 {% endfor %} 가 작성되었다.
- 변수 출력을 위해 {{변수명}} 이 사용되었다.

# **예제 2 - 조건문**
```html
<div>
    {% if x > 3 %}
        3이상
    {% else %}
        3미만
    {% endif %}
</div>
```

# **예제 3 - 변수, 리스트, 딕셔너리 가져올 때**
- javascript와 유사하다
```html
{변수명}
{변수명[0]}
{변수명[key]}
{변수명.key}
```

# **내장필터 sum**
- `{{[3,6,9,12]|sum}}` => 30
- `{{[{'id':'id1', 'points':5}, {'id':'id2', 'points':7}|sum(attribute='points')}}  => 12`
- `{{corona_data.values()|sum}}`


# **내장필터 float, int**
- `{{3|float}}` -> 3.0
- `{{3.14|int}}` -> 3

# **내장필터 length**
- `{{[1,2,3,4,5,6]|length}}` -> 6

# **예제 4 - 평균 구하기**
```html
{{[1,2,3,4,5]|sum / [1,2,3,4,5]|length}}
```

```html
{% set list_data = [1,2,3,4,5] %}
{{list_data|sum / list_data|length}}
```

# **페이지 상속**
- 베이스 html을 만들어두고 재활용 하는 방법

### **base.html**
- 기본적인 구조를 짜놓는다.
- 나중에 다른 요소가 들어갈 구멍을 뚫어놓는다.
- 구멍은 `{% block 구멍이름 %} {% endblock %}` 로 정의
```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>
```

### **children.html**
- `{% extends "base.html" %}` : base가 될 레이아웃을 참조
- `{% block 구멍이름 %}` 채워넣을 내용 {% endblock %}
- `{{super()}}` : base의 html을 사용(렌더링)하고싶을 때 사용
```html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}
```

