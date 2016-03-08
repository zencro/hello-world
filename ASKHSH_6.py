import urllib2
import datetime

#Ζητείται η ημερομηνία στην μορφή ηη-μμ-χχχχ

date_text=raw_input("Enter date to retrieve results for KINO ")

#Έλεγχος αν η ημερομηνία είναι σωστή. Αν δεν είναι ζητείται νέα
while True:
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        break
    except ValueError:
        date_text=raw_input("Enter correct format date (DD-MM-YYYY) ")

#Λήψη αποτελεσμάτων ΚΙΝΟ για την συγκεκριμένη ημερομηνία
        
req = urllib2.Request('http://applications.opap.gr/DrawsRestServices/kino/drawDate/' + date_text + '.json')
response = urllib2.urlopen(req)
the_page = response.read()

#Αντικατάσταση των χαρακτήρων '[' και ']' με τον χαρακτήρα ','  
new_page=the_page.replace ("[",",")
new_page1=new_page.replace ("]",",")

#Δημιουργία λίστας από το περιεχόμενο του new_page1 
numbers=new_page1.split(',')



# Το s θα περιέχει το πλήθος των εμφανίσεω κάθε αριθμού. Στην αρχή κάθε στοιχείο του γίνεται μηδέν
s=[]
for i in range (81):
    s.append(0)

#Το new_num θα περιέχει όποια περιεχόμενα της λίστας numbers είναι μόνο αριθμητικά
new_num=[]    
for i in range (len(numbers)):
    if numbers[i]<"A" and numbers[i]>"0":
       new_num.append(numbers[i])


#Για κάθε αριθμό της λίστας new_num αυξάνεται το αντίστοιχο στοιχείο της s
for i in range (len(new_num)):
    x=int(new_num[i])
    s[x]=s[x]+1

#Εμφάνιση αποτελεσμάτων
print ("KINO NUMBER      NUMBER OF DRAWS")
print ("--------------------------------")
for i in range (1,81):
    print repr(i).rjust(5),repr(s[i]).rjust(20)
