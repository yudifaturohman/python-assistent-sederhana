try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
a = input("Apa yang di cari : ")
query = a
  
for j in search(query, tld="com", num=10, stop=5, pause=0): 
    print(j) 
