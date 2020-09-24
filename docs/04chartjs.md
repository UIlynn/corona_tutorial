# **개요**
- 다양한 차트를 지원하는 라이브러리
- js 라이브러리
- `<canvas>` 요소에 차트를 렌더링(표기 및 생성)한다

# 튜토리얼 1단계
- `<canvas>`요소를 생성
```html
<canvas id="myChart"></canvas>
```

# 튜토리얼 2단계
- 라이브러리를 참조
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
```

# 튜토리얼 3단계
- 생성한 캔버스 객체를 찾고 저장
- 캔버스 객체에 차트 객체를 생성하여 적용
```js
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // 생성하려는 타입
    type: 'line',

    // 데이터 집합(data set)
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});
```