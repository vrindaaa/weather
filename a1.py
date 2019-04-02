#Vrinda Narayan
#Roll Number:2018120
#Section: A
#Group: 8
from urllib.request import *
from urllib.request import HTTPError
from datetime import *

# function to get weather response
def weather_response(location, API_key):
        x='http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
        y=Request(x)
        try:
                f=urlopen(y)
                t=(f.read())
        #instead of making a seperate case for invalid API key I have made it same as the case when location is invalid
        #hence I have grouped all of the errors together        
        except HTTPError:
                t='{"cod":"404","message":"city not found"}'
        return t
#function to check for valid response
#returns True when error otherwise False
def has_error(location,json):
        json=str(json)
        x=json.find('name')
        y=len(location)
        if json=='{"cod":"404","message":"city not found"}':
                return True 
        elif json[x+7:x+7+y]!=location:
                return True
        else:
                return False

# function to get attributes on nth day
def get_temperature (json, n=0, t='3:00'):
        if t!='3:00' and t!='6:00' and t!='9:00' and t!='12:00' and t!='15:00' and t!='18:00' and t!='21:00':
                temp='Error'
                print('1')
                print(t)
        elif n<0 or n>4:
                temp='Error'
                print('2')
        else:
                if t=='3:00' or t=='6:00' or t=='9:00':
                        t='0'+t
                json=str(json)
                current_date=date.today()
                n=int(n)
                nday=timedelta(n)
                nth_day=current_date+nday
                x=str(nth_day)
                y=x+' '+t
                z=json.find(y)
                a=json.find('temp',z-362)
                if a==-1:
                        temp='Error'
                else:
                        start=json.find(':',a)
                        end=json.find(',',a)
                        temp=json[start+1:end]
        return temp

def get_humidity(json, n=0, t='3:00'):
        if t!='3:00' and t!='6:00' and t!='9:00' and t!='12:00' and t!='15:00' and t!='18:00' and t!='21:00':
                humidity='Error'
        elif n<0 or n>4:
                humidity='Error'
        else:
                if t=='3:00' or t=='6:00' or t=='9:00':
                        t='0'+t
                json=str(json)
                current_date=date.today()
                n=int(n)
                nday=timedelta(n)
                nth_day=current_date+nday
                x=str(nth_day)
                y=x+' '+t
                z=json.find(y)
                a=json.find('humidity',z-282)
                if a==-1:
                        humidity='Error'
                        return humidity
                else:
                        start=json.find(':',a)
                        end=json.find(',',a)
                        humidity=json[start+1:end]
                        humidity=int(humidity)
        return humidity

def get_pressure(json, n=0, t='3:00'):
        if t!='3:00' and t!='6:00' and t!='9:00' and t!='12:00' and t!='15:00' and t!='18:00' and t!='21:00':
                pressure='Error'
        elif n<0 or n>4:
                pressure='Error'
        else:
                if t=='3:00' or t=='6:00' or t=='9:00':
                        t='0'+t
                json=str(json)
                current_date=date.today()
                n=int(n)
                nday=timedelta(n)
                nth_day=current_date+nday
                x=str(nth_day)
                y=x+' '+t
                z=json.find(y)
                a=json.find('pressure',z-332)
                if a==-1:
                        pressure='Error'
                else:
                        start=json.find(':',a)
                        end=json.find(',',a)
                        pressure=json[start+1:end]
                        pressure=float(pressure)
        return pressure

def get_wind(json, n=0, t='3:00'):
        if t!='3:00' and t!='6:00' and t!='9:00' and t!='12:00' and t!='15:00' and t!='18:00' and t!='21:00':
                wind='Error'
        elif n<0 or n>4:
                wind='Error'
        else:
                if t=='3:00' or t=='6:00' or t=='9:00':
                        t='0'+t
                json=str(json)
                current_date=date.today()
                n=int(n)
                nday=timedelta(n)
                nth_day=current_date+nday
                x=str(nth_day)
                y=x+' '+t
                z=json.find(y)
                a=json.find('wind',z-200)
                if a==-1:
                        wind='Error'
                else:
                        start=json.find('{',a)
                        end=json.find('}',a)
                        wind=json[start:end+1]
        return wind

def get_sealevel(json, n=0, t='3:00'):
        if t!='3:00' and t!='6:00' and t!='9:00' and t!='12:00' and t!='15:00' and t!='18:00' and t!='21:00':
                sea_level='Error'
        elif n<0 or n>4:
                sea_level='Error'
        else:
                if t=='3:00' or t=='6:00' or t=='9:00':
                        t='0'+t
                json=str(json)
                current_date=date.today()
                n=int(n)
                nday=timedelta(n)
                nth_day=current_date+nday
                x=str(nth_day)
                y=x+' '+t
                z=json.find(y)
                a=json.find('sea_level',z-362)
                if a==-1:
                        sea_level='Error'
                else:
                        start=json.find(':',a)
                        end=json.find(',',a)
                        sea_level=json[start+1:end]
                        sea_level=float(sea_level)
        return sea_level
 
