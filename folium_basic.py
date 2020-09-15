from flask import Flask, render_template, Markup
import folium

app=Flask(__name__)

@app.route('/')
def index():
    start_coords = (37.4449168, 127.1388684) # 성남 경도, 위도
    map = folium.Map(location=start_coords, zoom_start=14)

    # 마커 생성 - 좌표, popup, tooltip
    m1 = folium.Marker([37.4449168, 127.1388684],popup='기본',tooltip='click me')
    m2 = folium.Marker([37.4449168, 127.1378684],popup='<b>굵게</b>',tooltip='click me')

    # 맵에 마커를 적용
    m1.add_to(map)
    m2.add_to(map)

    # return map._repr_html_()
    map_data = map.get_root().render()
    map_data = Markup(map_data)
    return render_template('map.html',map_data=map_data)

if __name__ == "__main__":
    app.run(debug=True)