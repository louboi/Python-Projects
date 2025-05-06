students = ["Louis", "James", "Daniel", "Taylor", "Harry", "Liam"]
length = len(students)
hash = [None] * (length)
hashtable = [None] * (length)
no = 0


def hashing(students, hash):
    x = 0
    y = 0
    for i in range(length):
        x = students[i]
        for j in range(len(x)):
            y += ord(x[j])
        hash[i] = (y % (length))

def table(students, hash, hashtable, no):
    for i in range(length):
        x = hash[i]
        try:
            if hashtable[x] == None:
                hashtable[x] = students[i]
            else:
                hashtable[x + 1] = students[i]
        except:
            no += 1

hashing(students, hash)
table(students, hash, hashtable, no)

print(students)
print(hash)
print(hashtable)
print(no)