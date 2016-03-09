from PIL import Image


image_name=raw_input("Enter filename of an image ")


while True:
    try:
        img = Image.open(image_name) 
        break
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        image_name=raw_input("Please enter correct filename of an image ")


picture = img.load()



pixels=[]

for i in range (img.size[0]):
    for j in range (img.size[1]):
        pixels.append(picture[i,j])


colors=[]
for i in range (len(pixels)):
    x= pixels[i][0]
    x= x << 8
    x= x | pixels[i][1]
    x= x << 8
    x= x | pixels[i][2]
    colors.append(x)


colors.sort()



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

       
zipped=zip(paleta,col_count)


zipped.sort(key=lambda tup: tup[1], reverse=True) 



for i in range(5):
    print hex(zipped[i][0]), zipped[i][1]


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

