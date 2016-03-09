#exw xrhsimopoihsei greeklish giati ta ellhnika den emfanizontan sto github


import pyowm


owm = pyowm.OWM('8b0969d0b1d137bec23f97ce69b14775')


while True:
    while True:
        try:
            lat = float(raw_input("Dwste Gewgrafiko Platos (latitude) ths topothesias: "))
            break
        except ValueError:
            print "Prepei na dwsete arithmo. Dokimaste pali..."
    if lat >= -90 and lat <=90:
        break
    else:
        print "Oi syntetagmenes prepei na einai apo -90 ews +90. Dokimaste pali..."

while True:
    while True:
        try:
            lon = float(raw_input("Dwste Gewgrafiko Mhkos (longitude) ths topothesias : "))
            break
        except ValueError:
            print "Prepei na dwsete arithmo. Dokimaste pali..."
    if lon >= -90 and lon <=90:
        break
    else:
        print "Oi syntetagmenes prepei na einai apo -90 ews +90. Dokimaste pali..."

        
obs_list=owm.weather_around_coords(lat, lon)
obs = obs_list[0]


location = obs.get_location()
location_name=location.get_name()
print "Plhrofories kairikwn synthikwn gia thn perioxh: ",location_name


weather = obs.get_weather()
t=weather.get_reference_time(timeformat='iso')
temperature = weather.get_temperature('celsius')
general_condition=weather.get_status()
print "\nH parousa katastash stis: ",t
print "Thermokrasia: ", temperature['temp'],
if temperature['temp']>20:
    print "nice"
elif temperature['temp']<5:
    print "brrrr..."
else:
    print
print "Genikh Eikona: ", general_condition,
if general_condition == 'rain':
    print " --  I'm singing in the rain!"
else:
    print


