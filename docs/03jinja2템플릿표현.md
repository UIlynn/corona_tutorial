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

# **예시 1 반복문**
```html
숫자 출력 : {% for i in range(10) %} {{i}} {% endfor %}
```
- 반복문 시작을 위해 {% for ... %} 가 작성되었다.
- 반복문 끝을 위해 {% endfor %} 가 작성되었다.
- 변수 출력을 위해 {{변수명}} 이 사용되었다.

# **예시 2 조건문**
```html
<div>
    {% if x > 3 %}
        3이상
    {% else %}
        3미만
    {% endif %}
</div>
```

# **예시 3 변수, 리스트, 딕셔너리 가져올 때**
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

# **평균 구하기 예제**
```html
{{[1,2,3,4,5]|sum / [1,2,3,4,5]|length}}
```

```html
{% set list_data = [1,2,3,4,5] %}
{{list_data|sum / list_data|length}}
```