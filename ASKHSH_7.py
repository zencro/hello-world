import pyowm

#�������� ������� ��� �������� ��� OpenWeatherap
owm = pyowm.OWM('8b0969d0b1d137bec23f97ce69b14775')

#�������� ����������� ������� ��� ����������� ������ �� ������ ����������� ���������
while True:
    while True:
        try:
            lat = float(raw_input("����� ���������� ������ (latitude) ��� ����������: "))
            break
        except ValueError:
            print "������ �� ������ ������. ��������� ����..."
    if lat >= -90 and lat <=90:
        break
    else:
        print "�� ������������� ������ �� ����� ��� -90 �� +90. ��������� ����..."

while True:
    while True:
        try:
            lon = float(raw_input("����� ���������� ����� (longitude) ��� ����������: "))
            break
        except ValueError:
            print "������ �� ������ ������. ��������� ����..."
    if lon >= -90 and lon <=90:
        break
    else:
        print "�� ������������� ������ �� ����� ��� -90 �� +90. ��������� ����..."

#����������� �� �� OpenWeatherap �� ���� ��� ������������� ��� ����� � �������        
obs_list=owm.weather_around_coords(lat, lon)
obs = obs_list[0]

#�������� ���������� ��� ������������ �� �������������
location = obs.get_location()
location_name=location.get_name()
print "����������� �������� �������� ��� ��� �������: ",location_name

#�������� ����������� ��� ������� ��� ��������� �������� ��������
weather = obs.get_weather()
t=weather.get_reference_time(timeformat='iso')
temperature = weather.get_temperature('celsius')
general_condition=weather.get_status()
print "\n� ������� ��������� ����: ",t
print "�����������: ", temperature['temp'],
if temperature['temp']>20:
    print "nice"
elif temperature['temp']<5:
    print "brrrr..."
else:
    print
print "������ ������: ", general_condition,
if general_condition == 'rain':
    print " --  I'm singing in the rain!"
else:
    print


