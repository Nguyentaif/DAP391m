import requests
import pandas as pd
import time

# Danh sách tỉnh
locations = [
    {"name": "Hà Nội", "lat": 21.0285, "lon": 105.8542},
    {"name": "Hồ Chí Minh", "lat": 10.7769, "lon": 106.7009},
    {"name": "Đà Nẵng", "lat": 16.0544, "lon": 108.2022},
    {"name": "Hải Phòng",             "lat": 20.8449, "lon": 106.6881},
    {"name": "Cần Thơ",               "lat": 10.0452, "lon": 105.7469},
    {"name": "An Giang",              "lat": 10.5790, "lon": 105.4310},
    {"name": "Bà Rịa–Vũng Tàu",        "lat": 10.3530, "lon": 107.0846},
    {"name": "Bắc Giang",             "lat": 21.2768, "lon": 106.1941},
    {"name": "Bắc Kạn",               "lat": 22.1975, "lon": 105.8344},
    {"name": "Bạc Liêu",              "lat": 9.2516,  "lon": 105.5136},
    {"name": "Bắc Ninh",              "lat": 21.1358, "lon": 106.0519},
    {"name": "Bến Tre",               "lat": 10.2360, "lon": 106.3774},
    {"name": "Bình Định",             "lat": 13.7793, "lon": 109.2238},
    {"name": "Bình Dương",            "lat": 11.0535, "lon": 106.6578},
    {"name": "Bình Phước",            "lat": 11.6921, "lon": 106.8023},
    {"name": "Bình Thuận",            "lat": 10.9340, "lon": 107.8220},
    {"name": "Cà Mau",                "lat": 9.1765,  "lon": 105.1534},
    {"name": "Cao Bằng",              "lat": 22.6680, "lon": 106.2479},
    {"name": "Đắk Lắk",               "lat": 12.6667, "lon": 108.0500},
    {"name": "Đắk Nông",              "lat": 12.2500, "lon": 107.5000},
    {"name": "Điện Biên",             "lat": 21.3861, "lon": 103.0231},
    {"name": "Đồng Nai",              "lat": 10.8231, "lon": 106.3397},
    {"name": "Đồng Tháp",             "lat": 10.6494, "lon": 105.1000},
    {"name": "Gia Lai",               "lat": 13.8236, "lon": 108.0007},
    {"name": "Hà Giang",              "lat": 22.7583, "lon": 104.9937},
    {"name": "Hà Nam",                "lat": 20.5833, "lon": 105.9167},
    {"name": "Hà Tĩnh",               "lat": 18.3452, "lon": 105.9054},
    {"name": "Hải Dương",             "lat": 20.9467, "lon": 106.3333},
    {"name": "Hậu Giang",             "lat": 9.7833,  "lon": 105.4833},
    {"name": "Hòa Bình",              "lat": 20.8125, "lon": 105.3396},
    {"name": "Hưng Yên",              "lat": 20.8176, "lon": 106.0861},
    {"name": "Khánh Hòa",             "lat": 12.2672, "lon": 109.1890},
    {"name": "Kiên Giang",            "lat": 9.8249,  "lon": 105.1259},
    {"name": "Kon Tum",               "lat": 14.3657, "lon": 107.3613},
    {"name": "Lai Châu",              "lat": 22.4492, "lon": 103.9416},
    {"name": "Lâm Đồng",              "lat": 11.9340, "lon": 108.4386},
    {"name": "Lạng Sơn",              "lat": 21.8534, "lon": 106.7591},
    {"name": "Lào Cai",               "lat": 22.4850, "lon": 103.9960},
    {"name": "Long An",               "lat": 10.7200, "lon": 106.2465},
    {"name": "Nam Định",              "lat": 20.4210, "lon": 106.1640},
    {"name": "Nghệ An",               "lat": 19.1962, "lon": 105.5515},
    {"name": "Ninh Bình",             "lat": 20.2500, "lon": 105.9760},
    {"name": "Ninh Thuận",            "lat": 11.5650, "lon": 108.9889},
    {"name": "Phú Thọ",               "lat": 21.3297, "lon": 105.2786},
    {"name": "Phú Yên",               "lat": 13.0986, "lon": 109.3201},
    {"name": "Quảng Bình",            "lat": 17.5620, "lon": 106.5886},
    {"name": "Quảng Nam",             "lat": 15.5693, "lon": 108.5226},
    {"name": "Quảng Ngãi",            "lat": 15.1169, "lon": 108.7910},
    {"name": "Quảng Ninh",            "lat": 20.9545, "lon": 107.0558},
    {"name": "Quảng Trị",             "lat": 16.7464, "lon": 107.1810},
    {"name": "Sóc Trăng",             "lat": 9.6017,  "lon": 105.9730},
    {"name": "Sơn La",                "lat": 21.3250, "lon": 103.9092},
    {"name": "Tây Ninh",              "lat": 11.3173, "lon": 106.1198},
    {"name": "Thái Bình",             "lat": 20.4438, "lon": 106.3342},
    {"name": "Thái Nguyên",           "lat": 21.5982, "lon": 105.8482},
    {"name": "Thanh Hóa",             "lat": 19.8076, "lon": 105.7660},
    {"name": "Thừa Thiên Huế",        "lat": 16.4623, "lon": 107.5909},
    {"name": "Tiền Giang",            "lat": 10.3500, "lon": 106.3525},
    {"name": "Trà Vinh",              "lat": 9.9333,  "lon": 106.3500},
    {"name": "Tuyên Quang",           "lat": 21.8233, "lon": 105.2179},
    {"name": "Vĩnh Long",             "lat": 10.2479, "lon": 105.9719},
    {"name": "Vĩnh Phúc",             "lat": 21.3082, "lon": 105.5945},
    {"name": "Yên Bái",               "lat": 21.7167, "lon": 104.8667},
]

start_date = "2016-01-01"
end_date = "2023-01-01"

all_data = []

for loc in locations:
    print(f"Lấy dữ liệu cho {loc['name']}...")

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={loc['lat']}&longitude={loc['lon']}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,"
        f"windspeed_10m_max,winddirection_10m_dominant,"
        f"precipitation_sum,relative_humidity_2m_max,"
        f"cloudcover_mean,surface_pressure_mean"
        f"&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        daily = data["daily"]

        for i in range(len(daily["time"])):
            all_data.append({
                "location": loc["name"],
                "date": daily["time"][i],
                "temp_max": daily["temperature_2m_max"][i],
                "temp_min": daily["temperature_2m_min"][i],
                "wind_speed": daily["windspeed_10m_max"][i],
                "wind_dir": daily["winddirection_10m_dominant"][i],
                "rain": daily["precipitation_sum"][i],
                "humidity": daily["relative_humidity_2m_max"][i],
                "cloud_cover": daily["cloudcover_mean"][i],
                "pressure": daily["surface_pressure_mean"][i]
            })
    else:
        print(f" Không lấy được dữ liệu cho {loc['name']}: {response.status_code}")

    time.sleep(20)

# Chuyển sang DataFrame và lưu
df = pd.DataFrame(all_data)
df.to_csv("weather_vietnam_63_tinh.csv", index=False)
print("✅ Dữ liệu đã lưu vào 'weather_vietnam_63_tinh.csv'")
