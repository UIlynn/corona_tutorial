import requests
from bs4 import BeautifulSoup

def get_corona_summary():
    url = "https://search.naver.com/search.naver?query=코로나"

    # 페이지 소스코드 요청 -> 응답데이터를 확인
    res = requests.get(url)

    # 구문 분석 bs4
    soup = BeautifulSoup(res.text,'lxml')

    # 추출하기-> css selector, .select   .select_one
    divs = soup.select('.status_info')

    # 리스트로 추출하는 방법
    persons = divs[0].select('.info_num')
    # case1 for문으로
    results = []
    for p in persons:
        results.append(p.text)
    # print(results)

    # case2 list comprehension으로
    results = [p.text for p in persons]
    # print(results)

    # 국내 영역 - 딕셔너리로 추출하는 방법
    lis = divs[0].select('li') # [li, li,li,li]

    # 데이터 추출 key:value
    results = {}
    for li in lis:
        key = li.select_one('.info_title').text # '확진환자'
        value = li.select_one('.info_num').text.replace(',','') # '19,737'
        value = int(value)
        results[key] = value # 없으면 생성
    # print(results)
    return results

# 테스트 코드
if __name__ == "__main__":
    print(get_corona_summary())