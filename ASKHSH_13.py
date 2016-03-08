from PIL import Image

#Εισαγωγή ονόματος αρχείου που περιέχει την εικόνα
image_name=raw_input("Enter filename of an image ")

#Έλεγχος αν το αρχείο υπάρχει
while True:
    try:
        img = Image.open(image_name) 
        break
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        image_name=raw_input("Please enter correct filename of an image ")

#Οταν δοθεί αρχείο που υπάρχει φορτώνεται η εικόνα
picture = img.load()


#Μεταφορά των Pixels της εικόνας στο pixels
pixels=[]

for i in range (img.size[0]):
    for j in range (img.size[1]):
        pixels.append(picture[i,j])

#Μετατροπή του αριθμού χρώματος από 3 αριθμούς σε έναν μοανδικό αριθμό για κάθε pixel
colors=[]
for i in range (len(pixels)):
    x= pixels[i][0]
    x= x << 8
    x= x | pixels[i][1]
    x= x << 8
    x= x | pixels[i][2]
    colors.append(x)

#Ταξινόμηση των αριθμών χρώματος
colors.sort()

#Κάθε διαφορετικό χρώμα καταχωρειται στη λίστα paleta, ενώ το πλήθος των εμφανίσεων
#του χρώματος στην εικόνα καταχωρειται στην col_count
count=1
paleta=[]
col_count=[]

for i in range (1, len(colors)):
    if colors[i] == colors[i-1]:
        count +=1
    else:
        paleta.append(colors[i-1])
        col_count.append(count)              
        count=1
        
if colors[len(colors)-1] == colors[len(colors)-2]:
        paleta.append(len(colors)-1)
        col_count.append(count)              

#Δημιουργία tuple από τις λίστες colors και col_count        
zipped=zip(paleta,col_count)

#Ταξινόμηση της tuple με κλειδί το δευτερο πεδίο (αριθμό εμφανισης χρώματος
zipped.sort(key=lambda tup: tup[1], reverse=True) 

#Εμφάνιση σε δεκαεξαδική μορφή των 5 χρωμάτων με την μεγαλύτερη συχνότητα
#εμφάνισης στην εικόνα και δίπλα ο αριθμός των εμφανίσεων
for i in range(5):
    print hex(zipped[i][0]), zipped[i][1]

#Εμφάνιση της χρωματικής παλέτας
from turtle import *
up()
backward(100)
down()
for j in range(5):
    st=hex(zipped[j][0])
    if len(st)==8:
        st1='#'+st[2:]
    elif len(st)==7:
        st1='#0'+st[2:]
    elif len(st)==6:
        st1='#00'+st[2:]
    elif len(st)==5:
        st1='#000'+st[2:]
    elif len(st)==4:
        st1='#0000'+st[2:]
    elif len(st)==3:
        st1='#00000'+st[2:]
    elif len(st)==2:
        st1='#000000'+st[2:]
        
    color(st1)
    begin_fill()
    for i in range (4):
        forward(50)
        left(90)
    forward(50)
end_fill()
done()

