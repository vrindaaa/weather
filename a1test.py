#Vrinda Narayan
#Roll No:2018120
#Section A Group 8
import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel
from var import x


# TEST cases should cover the different boundary cases.
#as all of the data is real time hence it's value changes because of which our test cases may not be satisfied
#hence depending on when we check our functions the test cases may or may not be satisfied
class testpoint(unittest.TestCase):
	
        def test_weather_response(self):
                #as the data is changing everyday this test case might show error even if it is working fine
                #this is because it is real time data and depends on when it is being tested
                self.assertEqual(weather_response("Delhi","35c741a17a5f67491326f9fafae2bc51"),x)
                #location exists but first letter is not capital
                self.assertEqual(weather_response("delhi","35c741a17a5f67491326f9fafae2bc51"),x)
                #test case when API key is invalid
                self.assertEqual(weather_response("Delhi","uhdeudiw"),'{"cod":"404","message":"city not found"}')
                #test case when location doesn't exist
                self.assertEqual(weather_response("xyz","35c741a17a5f67491326f9fafae2bc51"),'{"cod":"404","message":"city not found"}')
        def test_has_error(self):
                #test case when location does not exist
                self.assertTrue(has_error('xyz','{"cod":"404","message":"city not found"}'))
		#location exists and is correct
                self.assertFalse(has_error('Delhi',x))
                #location exists but first letter is not capital, hence the location doesn't match
                self.assertTrue(has_error('delhi',x))
                #location exists and is correct : 2
                self.assertFalse(has_error('London','{"cod":"200","message":0.0383,"cnt":40,"list":[{"dt":1535965200,"main":{"temp":296.47,"temp_min":291.644,"temp_max":296.47,"pressure":1027.83,"sea_level":1035.28,"grnd_level":1027.83,"humidity":63,"temp_kf":4.83},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":44},"wind":{"speed":1.16,"deg":46.0033},"sys":{"pod":"d"},"dt_txt":"2018-09-03 09:00:00"},{"dt":1535976000,"main":{"temp":298.38,"temp_min":294.765,"temp_max":298.38,"pressure":1026.69,"sea_level":1034.16,"grnd_level":1026.69,"humidity":51,"temp_kf":3.62},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":56},"wind":{"speed":1.76,"deg":44.0035},"sys":{"pod":"d"},"dt_txt":"2018-09-03 12:00:00"},{"dt":1535986800,"main":{"temp":297.85,"temp_min":295.433,"temp_max":297.85,"pressure":1025.81,"sea_level":1033.28,"grnd_level":1025.81,"humidity":44,"temp_kf":2.41},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":76},"wind":{"speed":1.76,"deg":23.0021},"sys":{"pod":"d"},"dt_txt":"2018-09-03 15:00:00"},{"dt":1535997600,"main":{"temp":295.26,"temp_min":294.049,"temp_max":295.26,"pressure":1025.59,"sea_level":1033.06,"grnd_level":1025.59,"humidity":44,"temp_kf":1.21},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":1.41,"deg":13.5003},"sys":{"pod":"d"},"dt_txt":"2018-09-03 18:00:00"},{"dt":1536008400,"main":{"temp":287.034,"temp_min":287.034,"temp_max":287.034,"pressure":1026.34,"sea_level":1034.05,"grnd_level":1026.34,"humidity":76,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.71,"deg":50.0007},"sys":{"pod":"n"},"dt_txt":"2018-09-03 21:00:00"},{"dt":1536019200,"main":{"temp":283.166,"temp_min":283.166,"temp_max":283.166,"pressure":1026.54,"sea_level":1034.15,"grnd_level":1026.54,"humidity":96,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.06,"deg":65.5005},"sys":{"pod":"n"},"dt_txt":"2018-09-04 00:00:00"},{"dt":1536030000,"main":{"temp":281.223,"temp_min":281.223,"temp_max":281.223,"pressure":1026.49,"sea_level":1034.19,"grnd_level":1026.49,"humidity":92,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.87,"deg":348.004},"sys":{"pod":"n"},"dt_txt":"2018-09-04 03:00:00"},{"dt":1536040800,"main":{"temp":282.592,"temp_min":282.592,"temp_max":282.592,"pressure":1026.99,"sea_level":1034.63,"grnd_level":1026.99,"humidity":99,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":2.65,"deg":0.501343},"sys":{"pod":"d"},"dt_txt":"2018-09-04 06:00:00"},{"dt":1536051600,"main":{"temp":288.6,"temp_min":288.6,"temp_max":288.6,"pressure":1027.08,"sea_level":1034.5,"grnd_level":1027.08,"humidity":82,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":0},"wind":{"speed":2.96,"deg":6.50018},"rain":{"3h":0.055},"sys":{"pod":"d"},"dt_txt":"2018-09-04 09:00:00"},{"dt":1536062400,"main":{"temp":294.46,"temp_min":294.46,"temp_max":294.46,"pressure":1026.06,"sea_level":1033.57,"grnd_level":1026.06,"humidity":56,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.71,"deg":9.50546},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-04 12:00:00"},{"dt":1536073200,"main":{"temp":295.916,"temp_min":295.916,"temp_max":295.916,"pressure":1025.34,"sea_level":1032.77,"grnd_level":1025.34,"humidity":49,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":4.3,"deg":19.5029},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-04 15:00:00"},{"dt":1536084000,"main":{"temp":293.89,"temp_min":293.89,"temp_max":293.89,"pressure":1025.57,"sea_level":1033.06,"grnd_level":1025.57,"humidity":49,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.15,"deg":19.5049},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-04 18:00:00"},{"dt":1536094800,"main":{"temp":289.48,"temp_min":289.48,"temp_max":289.48,"pressure":1027,"sea_level":1034.53,"grnd_level":1027,"humidity":67,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.11,"deg":16.0013},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-04 21:00:00"},{"dt":1536105600,"main":{"temp":286.861,"temp_min":286.861,"temp_max":286.861,"pressure":1027.21,"sea_level":1034.74,"grnd_level":1027.21,"humidity":86,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":24},"wind":{"speed":3.91,"deg":4.5},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-05 00:00:00"},{"dt":1536116400,"main":{"temp":286.544,"temp_min":286.544,"temp_max":286.544,"pressure":1026.73,"sea_level":1034.29,"grnd_level":1026.73,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":76},"wind":{"speed":4.33,"deg":1.50522},"rain":{"3h":0.195},"sys":{"pod":"n"},"dt_txt":"2018-09-05 03:00:00"},{"dt":1536127200,"main":{"temp":286.658,"temp_min":286.658,"temp_max":286.658,"pressure":1026.67,"sea_level":1034.27,"grnd_level":1026.67,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":68},"wind":{"speed":4.36,"deg":1.00159},"rain":{"3h":0.2},"sys":{"pod":"d"},"dt_txt":"2018-09-05 06:00:00"},{"dt":1536138000,"main":{"temp":289.694,"temp_min":289.694,"temp_max":289.694,"pressure":1026.61,"sea_level":1034.11,"grnd_level":1026.61,"humidity":79,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":4.47,"deg":7.00256},"rain":{"3h":0.16},"sys":{"pod":"d"},"dt_txt":"2018-09-05 09:00:00"},{"dt":1536148800,"main":{"temp":292.42,"temp_min":292.42,"temp_max":292.42,"pressure":1025.66,"sea_level":1033.06,"grnd_level":1025.66,"humidity":67,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":4.41,"deg":15.5088},"rain":{"3h":0.07},"sys":{"pod":"d"},"dt_txt":"2018-09-05 12:00:00"},{"dt":1536159600,"main":{"temp":293.831,"temp_min":293.831,"temp_max":293.831,"pressure":1024.39,"sea_level":1031.83,"grnd_level":1024.39,"humidity":61,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":56},"wind":{"speed":4.65,"deg":16.0004},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-05 15:00:00"},{"dt":1536170400,"main":{"temp":292.466,"temp_min":292.466,"temp_max":292.466,"pressure":1024.11,"sea_level":1031.57,"grnd_level":1024.11,"humidity":60,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":4.51,"deg":15.0039},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-05 18:00:00"},{"dt":1536181200,"main":{"temp":288.865,"temp_min":288.865,"temp_max":288.865,"pressure":1024.59,"sea_level":1032.02,"grnd_level":1024.59,"humidity":75,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":3.66,"deg":9.00311},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-05 21:00:00"},{"dt":1536192000,"main":{"temp":286.425,"temp_min":286.425,"temp_max":286.425,"pressure":1024.12,"sea_level":1031.65,"grnd_level":1024.12,"humidity":88,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":64},"wind":{"speed":3.22,"deg":3.00052},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-06 00:00:00"},{"dt":1536202800,"main":{"temp":284.457,"temp_min":284.457,"temp_max":284.457,"pressure":1023.19,"sea_level":1030.69,"grnd_level":1023.19,"humidity":98,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.86,"deg":339.009},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-06 03:00:00"},{"dt":1536213600,"main":{"temp":282.946,"temp_min":282.946,"temp_max":282.946,"pressure":1022.57,"sea_level":1030.22,"grnd_level":1022.57,"humidity":100,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.57,"deg":316.005},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-06 06:00:00"},{"dt":1536224400,"main":{"temp":289.08,"temp_min":289.08,"temp_max":289.08,"pressure":1021.98,"sea_level":1029.45,"grnd_level":1021.98,"humidity":73,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.21,"deg":310.504},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-06 09:00:00"},{"dt":1536235200,"main":{"temp":292.311,"temp_min":292.311,"temp_max":292.311,"pressure":1020.31,"sea_level":1027.65,"grnd_level":1020.31,"humidity":60,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.01,"deg":290.502},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-06 12:00:00"},{"dt":1536246000,"main":{"temp":291.027,"temp_min":291.027,"temp_max":291.027,"pressure":1018.74,"sea_level":1026.09,"grnd_level":1018.74,"humidity":65,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":100},"wind":{"speed":4.81,"deg":296.005},"rain":{"3h":0.15},"sys":{"pod":"d"},"dt_txt":"2018-09-06 15:00:00"},{"dt":1536256800,"main":{"temp":289.723,"temp_min":289.723,"temp_max":289.723,"pressure":1017.95,"sea_level":1025.39,"grnd_level":1017.95,"humidity":57,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":56},"wind":{"speed":4.67,"deg":302.5},"rain":{"3h":0.08},"sys":{"pod":"d"},"dt_txt":"2018-09-06 18:00:00"},{"dt":1536267600,"main":{"temp":286.001,"temp_min":286.001,"temp_max":286.001,"pressure":1018.87,"sea_level":1026.38,"grnd_level":1018.87,"humidity":61,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":4.35,"deg":314.503},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-06 21:00:00"},{"dt":1536278400,"main":{"temp":283.04,"temp_min":283.04,"temp_max":283.04,"pressure":1019.25,"sea_level":1026.71,"grnd_level":1019.25,"humidity":76,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.76,"deg":300.002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 00:00:00"},{"dt":1536289200,"main":{"temp":281.563,"temp_min":281.563,"temp_max":281.563,"pressure":1018.81,"sea_level":1026.47,"grnd_level":1018.81,"humidity":87,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.97,"deg":286.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 03:00:00"},{"dt":1536300000,"main":{"temp":280.939,"temp_min":280.939,"temp_max":280.939,"pressure":1019.08,"sea_level":1026.74,"grnd_level":1019.08,"humidity":88,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.87,"deg":278.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 06:00:00"},{"dt":1536310800,"main":{"temp":286.548,"temp_min":286.548,"temp_max":286.548,"pressure":1019.22,"sea_level":1026.74,"grnd_level":1019.22,"humidity":65,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.26,"deg":268.005},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 09:00:00"},{"dt":1536321600,"main":{"temp":289.845,"temp_min":289.845,"temp_max":289.845,"pressure":1018.53,"sea_level":1025.86,"grnd_level":1018.53,"humidity":56,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":44},"wind":{"speed":5.67,"deg":256.003},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 12:00:00"},{"dt":1536332400,"main":{"temp":290.487,"temp_min":290.487,"temp_max":290.487,"pressure":1017.57,"sea_level":1025.09,"grnd_level":1017.57,"humidity":51,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":76},"wind":{"speed":6.58,"deg":252},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 15:00:00"},{"dt":1536343200,"main":{"temp":288.82,"temp_min":288.82,"temp_max":288.82,"pressure":1017.57,"sea_level":1025.08,"grnd_level":1017.57,"humidity":50,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":88},"wind":{"speed":5.92,"deg":261.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 18:00:00"},{"dt":1536354000,"main":{"temp":286.992,"temp_min":286.992,"temp_max":286.992,"pressure":1018.05,"sea_level":1025.57,"grnd_level":1018.05,"humidity":60,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":32},"wind":{"speed":5.12,"deg":255.006},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 21:00:00"},{"dt":1536364800,"main":{"temp":285.96,"temp_min":285.96,"temp_max":285.96,"pressure":1017.61,"sea_level":1025.23,"grnd_level":1017.61,"humidity":73,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":5.28,"deg":245.501},"rain":{"3h":0.16},"sys":{"pod":"n"},"dt_txt":"2018-09-08 00:00:00"},{"dt":1536375600,"main":{"temp":285.412,"temp_min":285.412,"temp_max":285.412,"pressure":1016.71,"sea_level":1024.25,"grnd_level":1016.71,"humidity":82,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":88},"wind":{"speed":5.11,"deg":240.003},"rain":{"3h":0.34},"sys":{"pod":"n"},"dt_txt":"2018-09-08 03:00:00"},{"dt":1536386400,"main":{"temp":285.885,"temp_min":285.885,"temp_max":285.885,"pressure":1016.36,"sea_level":1023.88,"grnd_level":1016.36,"humidity":71,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":32},"wind":{"speed":5.07,"deg":253.001},"rain":{"3h":0.01},"sys":{"pod":"d"},"dt_txt":"2018-09-08 06:00:00"}],"city":{"id":2643743,"name":"London","coord":{"lat":51.5073,"lon":-0.1277},"country":"GB","population":1000000}}'))
                #location is london but data is given of delhi as json string
                self.assertTrue(has_error('london','{"cod":"200","message":0.0026,"cnt":37,"list":[{"dt":1535965200,"main":{"temp":302.17,"temp_min":300.144,"temp_max":302.17,"pressure":990.55,"sea_level":1014.89,"grnd_level":990.55,"humidity":100,"temp_kf":2.03},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":68},"wind":{"speed":2.56,"deg":39.5006},"rain":{"3h":2.97},"sys":{"pod":"d"},"dt_txt":"2018-09-03 09:00:00"},{"dt":1535976000,"main":{"temp":302.37,"temp_min":301.02,"temp_max":302.37,"pressure":990.19,"sea_level":1014.46,"grnd_level":990.19,"humidity":91,"temp_kf":1.35},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":2.42,"deg":62.5029},"rain":{"3h":0.009999999999998},"sys":{"pod":"d"},"dt_txt":"2018-09-03 12:00:00"},{"dt":1535986800,"main":{"temp":300.12,"temp_min":299.444,"temp_max":300.12,"pressure":991.25,"sea_level":1015.65,"grnd_level":991.25,"humidity":93,"temp_kf":0.68},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":48},"wind":{"speed":1.51,"deg":54.5002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-03 15:00:00"},{"dt":1535997600,"main":{"temp":297.96,"temp_min":297.96,"temp_max":297.96,"pressure":991.56,"sea_level":1016.01,"grnd_level":991.56,"humidity":96,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":1.32,"deg":8.50287},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-03 18:00:00"},{"dt":1536008400,"main":{"temp":296.949,"temp_min":296.949,"temp_max":296.949,"pressure":991.19,"sea_level":1015.72,"grnd_level":991.19,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":80},"wind":{"speed":1.22,"deg":36.5095},"rain":{"3h":0.325},"sys":{"pod":"n"},"dt_txt":"2018-09-03 21:00:00"},{"dt":1536019200,"main":{"temp":296.22,"temp_min":296.22,"temp_max":296.22,"pressure":991.71,"sea_level":1016.18,"grnd_level":991.71,"humidity":98,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"clouds":{"all":88},"wind":{"speed":2.28,"deg":144.004},"rain":{"3h":4.24},"sys":{"pod":"n"},"dt_txt":"2018-09-04 00:00:00"},{"dt":1536030000,"main":{"temp":297.258,"temp_min":297.258,"temp_max":297.258,"pressure":992.91,"sea_level":1017.42,"grnd_level":992.91,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":1.77,"deg":162.503},"rain":{"3h":0.51},"sys":{"pod":"d"},"dt_txt":"2018-09-04 03:00:00"},{"dt":1536040800,"main":{"temp":299.114,"temp_min":299.114,"temp_max":299.114,"pressure":993.33,"sea_level":1017.75,"grnd_level":993.33,"humidity":99,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":2.67,"deg":63.5009},"rain":{"3h":0.23},"sys":{"pod":"d"},"dt_txt":"2018-09-04 06:00:00"},{"dt":1536051600,"main":{"temp":300.521,"temp_min":300.521,"temp_max":300.521,"pressure":991.75,"sea_level":1016,"grnd_level":991.75,"humidity":98,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":64},"wind":{"speed":2.66,"deg":58.5057},"rain":{"3h":0.040000000000003},"sys":{"pod":"d"},"dt_txt":"2018-09-04 09:00:00"},{"dt":1536062400,"main":{"temp":300.635,"temp_min":300.635,"temp_max":300.635,"pressure":990.82,"sea_level":1015.21,"grnd_level":990.82,"humidity":89,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":1.96,"deg":41.5062},"rain":{"3h":0.079999999999998},"sys":{"pod":"d"},"dt_txt":"2018-09-04 12:00:00"},{"dt":1536073200,"main":{"temp":299.159,"temp_min":299.159,"temp_max":299.159,"pressure":992.36,"sea_level":1016.78,"grnd_level":992.36,"humidity":93,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":56},"wind":{"speed":1.33,"deg":39.505},"rain":{"3h":0.07},"sys":{"pod":"n"},"dt_txt":"2018-09-04 15:00:00"},{"dt":1536084000,"main":{"temp":298.167,"temp_min":298.167,"temp_max":298.167,"pressure":992.48,"sea_level":1016.95,"grnd_level":992.48,"humidity":95,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.41,"deg":345.002},"rain":{"3h":0.02},"sys":{"pod":"n"},"dt_txt":"2018-09-04 18:00:00"},{"dt":1536094800,"main":{"temp":297.563,"temp_min":297.563,"temp_max":297.563,"pressure":991.22,"sea_level":1015.7,"grnd_level":991.22,"humidity":94,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02n"}],"clouds":{"all":8},"wind":{"speed":1.81,"deg":352.503},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-04 21:00:00"},{"dt":1536105600,"main":{"temp":297.206,"temp_min":297.206,"temp_max":297.206,"pressure":991.07,"sea_level":1015.66,"grnd_level":991.07,"humidity":94,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":24},"wind":{"speed":2.51,"deg":1.50064},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-05 00:00:00"},{"dt":1536116400,"main":{"temp":298.345,"temp_min":298.345,"temp_max":298.345,"pressure":992.75,"sea_level":1017.15,"grnd_level":992.75,"humidity":100,"temp_kf":0},"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":3.32,"deg":64.5047},"rain":{"3h":3.83},"sys":{"pod":"d"},"dt_txt":"2018-09-05 03:00:00"},{"dt":1536127200,"main":{"temp":301.155,"temp_min":301.155,"temp_max":301.155,"pressure":992.85,"sea_level":1017.25,"grnd_level":992.85,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":64},"wind":{"speed":3.51,"deg":75.0036},"rain":{"3h":1.11},"sys":{"pod":"d"},"dt_txt":"2018-09-05 06:00:00"},{"dt":1536138000,"main":{"temp":302.574,"temp_min":302.574,"temp_max":302.574,"pressure":991.05,"sea_level":1015.42,"grnd_level":991.05,"humidity":90,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":88},"wind":{"speed":3.01,"deg":115},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-05 09:00:00"},{"dt":1536148800,"main":{"temp":301.152,"temp_min":301.152,"temp_max":301.152,"pressure":990.79,"sea_level":1015,"grnd_level":990.79,"humidity":91,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":2.11,"deg":130.002},"rain":{"3h":0.23},"sys":{"pod":"d"},"dt_txt":"2018-09-05 12:00:00"},{"dt":1536159600,"main":{"temp":299.6,"temp_min":299.6,"temp_max":299.6,"pressure":992.26,"sea_level":1016.75,"grnd_level":992.26,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.32,"deg":94.5002},"rain":{"3h":0.14},"sys":{"pod":"n"},"dt_txt":"2018-09-05 15:00:00"},{"dt":1536170400,"main":{"temp":298.591,"temp_min":298.591,"temp_max":298.591,"pressure":992.6,"sea_level":1017.17,"grnd_level":992.6,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":48},"wind":{"speed":1.86,"deg":100.502},"rain":{"3h":0.020000000000003},"sys":{"pod":"n"},"dt_txt":"2018-09-05 18:00:00"},{"dt":1536181200,"main":{"temp":297.249,"temp_min":297.249,"temp_max":297.249,"pressure":991.83,"sea_level":1016.34,"grnd_level":991.83,"humidity":95,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":1.33,"deg":74.5024},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-05 21:00:00"},{"dt":1536192000,"main":{"temp":297.738,"temp_min":297.738,"temp_max":297.738,"pressure":991.67,"sea_level":1016.23,"grnd_level":991.67,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.37,"deg":46.0051},"rain":{"3h":0.07},"sys":{"pod":"n"},"dt_txt":"2018-09-06 00:00:00"},{"dt":1536202800,"main":{"temp":299.587,"temp_min":299.587,"temp_max":299.587,"pressure":992.82,"sea_level":1017.23,"grnd_level":992.82,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":2.2,"deg":85.0021},"rain":{"3h":0.079999999999998},"sys":{"pod":"d"},"dt_txt":"2018-09-06 03:00:00"},{"dt":1536213600,"main":{"temp":301.41,"temp_min":301.41,"temp_max":301.41,"pressure":993.24,"sea_level":1017.58,"grnd_level":993.24,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":2.68,"deg":137.504},"rain":{"3h":0.17},"sys":{"pod":"d"},"dt_txt":"2018-09-06 06:00:00"},{"dt":1536224400,"main":{"temp":302.218,"temp_min":302.218,"temp_max":302.218,"pressure":991.55,"sea_level":1015.84,"grnd_level":991.55,"humidity":95,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":36},"wind":{"speed":2.27,"deg":149.5},"rain":{"3h":0.12},"sys":{"pod":"d"},"dt_txt":"2018-09-06 09:00:00"},{"dt":1536235200,"main":{"temp":302.635,"temp_min":302.635,"temp_max":302.635,"pressure":991.19,"sea_level":1015.53,"grnd_level":991.19,"humidity":84,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":68},"wind":{"speed":1.97,"deg":119.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-06 12:00:00"},{"dt":1536246000,"main":{"temp":300.209,"temp_min":300.209,"temp_max":300.209,"pressure":992.56,"sea_level":1017.05,"grnd_level":992.56,"humidity":91,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.75,"deg":139.5},"rain":{"3h":0.1},"sys":{"pod":"n"},"dt_txt":"2018-09-06 15:00:00"},{"dt":1536256800,"main":{"temp":298.315,"temp_min":298.315,"temp_max":298.315,"pressure":993.4,"sea_level":1017.76,"grnd_level":993.4,"humidity":98,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":68},"wind":{"speed":1.87,"deg":217.501},"rain":{"3h":0.07},"sys":{"pod":"n"},"dt_txt":"2018-09-06 18:00:00"},{"dt":1536267600,"main":{"temp":297.378,"temp_min":297.378,"temp_max":297.378,"pressure":992.73,"sea_level":1017.24,"grnd_level":992.73,"humidity":98,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":1.52,"deg":269.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-06 21:00:00"},{"dt":1536278400,"main":{"temp":296.396,"temp_min":296.396,"temp_max":296.396,"pressure":992.72,"sea_level":1017.25,"grnd_level":992.72,"humidity":97,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":1.11,"deg":67.5011},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 00:00:00"},{"dt":1536289200,"main":{"temp":300.027,"temp_min":300.027,"temp_max":300.027,"pressure":993.96,"sea_level":1018.45,"grnd_level":993.96,"humidity":100,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":1.98,"deg":122.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 03:00:00"},{"dt":1536300000,"main":{"temp":303.237,"temp_min":303.237,"temp_max":303.237,"pressure":994.2,"sea_level":1018.56,"grnd_level":994.2,"humidity":92,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":48},"wind":{"speed":2.1,"deg":136.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 06:00:00"},{"dt":1536310800,"main":{"temp":304.053,"temp_min":304.053,"temp_max":304.053,"pressure":992.33,"sea_level":1016.55,"grnd_level":992.33,"humidity":84,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":76},"wind":{"speed":2.86,"deg":148},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 09:00:00"},{"dt":1536321600,"main":{"temp":303.439,"temp_min":303.439,"temp_max":303.439,"pressure":992.12,"sea_level":1016.35,"grnd_level":992.12,"humidity":79,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":76},"wind":{"speed":2.06,"deg":146},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-09-07 12:00:00"},{"dt":1536332400,"main":{"temp":301.492,"temp_min":301.492,"temp_max":301.492,"pressure":993.64,"sea_level":1018.05,"grnd_level":993.64,"humidity":81,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":68},"wind":{"speed":1.86,"deg":137.504},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 15:00:00"},{"dt":1536343200,"main":{"temp":299.375,"temp_min":299.375,"temp_max":299.375,"pressure":994.1,"sea_level":1018.59,"grnd_level":994.1,"humidity":93,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":80},"wind":{"speed":1.96,"deg":183.501},"rain":{"3h":1.51},"sys":{"pod":"n"},"dt_txt":"2018-09-07 18:00:00"},{"dt":1536354000,"main":{"temp":297.623,"temp_min":297.623,"temp_max":297.623,"pressure":993.18,"sea_level":1017.68,"grnd_level":993.18,"humidity":95,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.31,"deg":160.506},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-09-07 21:00:00"}],"city":{"id":1273294,"name":"Delhi","coord":{"lat":28.6517,"lon":77.2219},"country":"IN","population":10927986}}'))
        def test_get_temperature(self):
                #case to only input json string and default values of n and t
                #x is json string for delhi in real time
                #to avoid error as the time for 3:00 may not exist for current day we calculate it for the next day
                #the value of delta is taken as 10 to avoid error as it is real time data
                #as this data is real time data, when we are checking the temperature the temperature value for 3:00 mightnot be on the string example if we are checking it at 12:00 hence there might be error even if the function works
                #t=float(get_temperature(x))
                #self.assertAlmostEqual(t,300, delta=10)
                t=float(get_temperature(x,1))
                self.assertAlmostEqual(t,302,delta=10)
                t=float(get_temperature(x,t='21:00'))
                self.assertAlmostEqual(t,300,delta=10)
                #case when location doesn't exist
                self.assertEqual(get_temperature('{"cod":"404","message":"city not found"}',2), 'Error')
                #when location exists but the time entered is not in correct format
                self.assertEqual(get_temperature(x,2,'7:00'), 'Error')
                #when location exists but date is not in correct format
                self.assertEqual(get_temperature(x,7, '3:00'), 'Error')
                #case to check if it is returning the correct temperature
                #as this data is real time this case may not be satisfied because of the values changing with time
                t=float(get_temperature(x,2, '6:00'))
                self.assertAlmostEqual(t,301.155, delta=10)
        def test_get_humidity(self):
                #self.assertAlmostEqual(get_humidity(x),97,delta=5)
                #this might show error as when we're checking for today the data of 3:00 might not exist anymore
                self.assertAlmostEqual(get_humidity(x,1), 100, delta=5)
                self.assertAlmostEqual(get_humidity(x,t='21:00'), 96, delta=5)
                #case when location doesn't exist
                self.assertEqual(get_humidity('{"cod":"404","message":"city not found"}',2), 'Error')
                #when location exists but the time entered is not in correct format
                self.assertEqual(get_humidity(x,2,'7:00'), 'Error')
                #when location exists but date is not in correct format
                self.assertEqual(get_humidity(x,7, '3:00'), 'Error')
                #when both date and time are correct
                self.assertAlmostEqual(get_humidity(x,3,'15:00'),76, delta=10)
        def test_get_pressure(self):
                #self.assertAlmostEqual(get_pressure(x),990,delta=5)
                #this might show error as when we're checking for today the data of 3:00 might not exist anymore
                self.assertAlmostEqual(get_pressure(x,1),992,delta=5)
                self.assertAlmostEqual(get_pressure(x,t='21:00'),991, delta=5)
                #case when location doesn't exist
                self.assertEqual(get_pressure('{"cod":"404","message":"city not found"}',2), 'Error')
                #when location exists but the time entered is not in correct format
                self.assertEqual(get_pressure(x,2,'7:00'), 'Error')
                #when location exists but date is not in correct format
                self.assertEqual(get_pressure(x,7, '3:00'), 'Error')
                self.assertAlmostEqual(get_pressure(x,3,'9:00'),992, delta=10)
        def test_get_wind(self):
                #self.assertEqual(get_wind(x),'{"speed":1.92,"deg":97.0044}')
                #this might show error as when we're checking for today the data of 3:00 might not exist anymore
                self.assertEqual(get_wind(x,1),'{"speed":2.06,"deg":284.001}')
                self.assertEqual(get_wind(x,t='21:00'),'{"speed":1.76,"deg":217.001}')
                #case when location doesn't exist
                self.assertEqual(get_wind('{"cod":"404","message":"city not found"}',2), 'Error')
                #when location exists but the time entered is not in correct format
                self.assertEqual(get_wind(x,2,'7:00'), 'Error')
                #when location exists but date is not in correct format
                self.assertEqual(get_wind(x,7, '3:00'), 'Error')
                #both date and time are in correct format
                self.assertEqual(get_wind(x,3,'9:00'),'{"speed":3.6,"deg":108}')
        def test_get_sealevel(self):
                #self.assertAlmostEqual(get_sealevel(x),1015,delta=5)
                #this might show error as when we're checking for today the data of 3:00 might not exist anymore
                self.assertAlmostEqual(get_sealevel(x,1),1015,delta=5)
                self.assertAlmostEqual(get_sealevel(x,t='21:00'),1015, delta=5)
                #case when location doesn't exist
                self.assertEqual(get_sealevel('{"cod":"404","message":"city not found"}',2), 'Error')
                #when location exists but the time entered is not in correct format
                self.assertEqual(get_sealevel(x,2,'7:00'), 'Error')
                #when location exists but date is not in correct format
                self.assertEqual(get_sealevel(x,7, '3:00'), 'Error')
                #both date and time are in correct format
                self.assertAlmostEqual(get_sealevel(x,2,'18:00'),1015,delta=5)
	
if __name__=='__main__':
	unittest.main()
