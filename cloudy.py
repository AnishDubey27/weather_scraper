from requests_html import HTMLSession

s = HTMLSession()

query = input("Enter location: ")
url = f'https://www.google.com/search?q=weather+{query}'

r= s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text  # type: ignore
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text  # type: ignore
precipitation = r.html.find('span#wob_pp', first=True).text  # type: ignore
humidity = r.html.find('span#wob_hm', first=True).text  # type: ignore
wind = r.html.find('span#wob_ws', first=True).text  # type: ignore
type = r.html.find('span#wob_dc', first=True).text  # type: ignore
print("Temperature of ",query," is ",temp, unit)
print(type)
print("Precipitation: ",precipitation)
print("Humidity: ",humidity)
print("Wind: ",wind)



 