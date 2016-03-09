import urllib2
import datetime



date_text=raw_input("Enter date to retrieve results for KINO ")



while True:
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        break
    except ValueError:
        date_text=raw_input("Enter correct format date (DD-MM-YYYY) ")


        
req = urllib2.Request('http://applications.opap.gr/DrawsRestServices/kino/drawDate/' + date_text + '.json')
response = urllib2.urlopen(req)
the_page = response.read()


  
new_page=the_page.replace ("[",",")
new_page1=new_page.replace ("]",",")



numbers=new_page1.split(',')



s=[]
for i in range (81):
    s.append(0)



new_num=[]    
for i in range (len(numbers)):
    if numbers[i]<"A" and numbers[i]>"0":
       new_num.append(numbers[i])



for i in range (len(new_num)):
    x=int(new_num[i])
    s[x]=s[x]+1



print ("KINO NUMBER      NUMBER OF DRAWS")
print ("--------------------------------")
for i in range (1,81):
    print repr(i).rjust(5),repr(s[i]).rjust(20)
