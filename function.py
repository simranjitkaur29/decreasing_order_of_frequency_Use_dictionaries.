# Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
def most_frequent(string):
    a=dict()
    for key in string:
        if key not in a:
            a[key]=1
        else:
            a[key]+=1

    return a
s=input("enter : ")
print(most_frequent(s))
