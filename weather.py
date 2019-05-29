WEATHER_URL="http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
CITY_CODE="130010" # TOKYO

def get_weather_info():
    try:
        url = WEATHER_URL % CITY_CODE
        html = urllib.request.urlopen(url)
        html_json = json.loads(html.read().decode('utf-8'))
    except Exception as e:
        print ("Exception Error: ", e)
        sys.exit(1)
    return html_json


def set_weather_info(weather_json, day):
    max_temperature = None
    min_temperature = None
    try:
        date = weather_json['forecasts'][day]['date']
        weather = weather_json['forecasts'][day]['telop']
        max_temperature = weather_json['forecasts'][day]['temperature']['max']['celsius']
        min_temperature = weather_json['forecasts'][day]['temperature']['min']['celsius']
    except TypeError:
        # temperature data is None etc...
        pass
    msg = "%s\nweather: %s\nmin: %s\nmax: %s" % \
               (date, weather, min_temperature, max_temperature)
    return msg
