import requests
from datetime import datetime
import xmltodict


def get_current_date():
    current_date = datetime.now().date()
    return current_date.strftime("%Y%m%d")


def get_current_hour():
    now = datetime.now()
    return datetime.now().strftime("%H%M")


int_to_weather = {
    "0": "맑음",
    "1": "비",
    "2": "비/눈",
    "3": "눈",
    "5": "빗방울",
    "6": "빗방울눈날림",
    "7": "눈날림"
}


def forecast(params):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'  # 초단기예보

    # 값 요청 (웹 브라우저 서버에서 요청 - url주소와 파라미터)
    res = requests.get(url, params)

    # XML -> 딕셔너리
    xml_data = res.text
    dict_data = xmltodict.parse(xml_data)

    for item in dict_data['response']['body']['items']['item']:
        if item['category'] == 'T1H':
            temp = item['obsrValue']
        # 강수형태: 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
        if item['category'] == 'PTY':
            sky = item['obsrValue']
        if item['category'] == 'REH':
            hum = item['obsrValue']
        if item['category'] == 'RN1':
            pre = item['obsrValue']

    sky = int_to_weather[sky]

    return temp, sky, hum, pre

if __name__ == '__main__':
    keys = 'c0Z8qEc0Rax20wIbXMOeCf2LC1w+/1AL88PovrnVShPGHMniU9jLTDNf6Z5exxcZcB3gnFQQxyK/5nhseqE7qA=='
    params ={'serviceKey' : keys,
             'pageNo' : '1',
             'numOfRows' : '10',
             'dataType' : 'XML',
             'base_date' : get_current_date(),
             'base_time' : get_current_hour(),
             'nx' : '67',
             'ny' : '100' }
    print(forecast(params))