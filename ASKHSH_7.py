import pyowm

#Εισαγωγή Κωδικού για πρόσβαση στο OpenWeatherap
owm = pyowm.OWM('8b0969d0b1d137bec23f97ce69b14775')

#Εισαγωγή Γεωγραφικού Πλάτους και Γεωγραφικού Μήκους με έλεγχο εγκυρότητας δεδομένων
while True:
    while True:
        try:
            lat = float(raw_input("Δώστε Γεωγραφικό Πλάτος (latitude) της τοποθεσίας: "))
            break
        except ValueError:
            print "Πρέπει να δώσετε Αριθμό. Δοκιμάστε πάλι..."
    if lat >= -90 and lat <=90:
        break
    else:
        print "Οι συντεταγμένες πρέπει να είναι από -90 ώς +90. Δοκιμάστε πάλι..."

while True:
    while True:
        try:
            lon = float(raw_input("Δώστε Γεωγραφικό Μήκος (longitude) της τοποθεσίας: "))
            break
        except ValueError:
            print "Πρέπει να δώσετε Αριθμό. Δοκιμάστε πάλι..."
    if lon >= -90 and lon <=90:
        break
    else:
        print "Οι συντεταγμένες πρέπει να είναι από -90 ώς +90. Δοκιμάστε πάλι..."

#Επικοινωνία με το OpenWeatherap με βάση τις συντεταγμένες που έδωσε ο χρήστης        
obs_list=owm.weather_around_coords(lat, lon)
obs = obs_list[0]

#Ανάκτηση τοποθεσίας που αντιστοιχούν οι συντεταγμένες
location = obs.get_location()
location_name=location.get_name()
print "Πληροφορίες καιρικών συνθηκών για την περιοχή: ",location_name

#Ανάκτηση πληροφοριών που αφορούν τις τρέχουσες καιρικές συνθήκες
weather = obs.get_weather()
t=weather.get_reference_time(timeformat='iso')
temperature = weather.get_temperature('celsius')
general_condition=weather.get_status()
print "\nΗ παρούσα κατάσταση στις: ",t
print "Θερμοκρασία: ", temperature['temp'],
if temperature['temp']>20:
    print "nice"
elif temperature['temp']<5:
    print "brrrr..."
else:
    print
print "Γενική εικόνα: ", general_condition,
if general_condition == 'rain':
    print " --  I'm singing in the rain!"
else:
    print


