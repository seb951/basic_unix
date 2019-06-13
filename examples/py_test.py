print("Hello from Python!")


my_number = 123

#string
my_string = str(my_number)
my_string = "this is not a string"

#integer
x = int("123")


#concat
string_two = "my homework!"
string_three = string_one + string_two

#slicing
my_string[0]
my_string[4:9]

#function on string
my_string.upper()

#options on strings
dir(my_string)
help(my_string.capitalize)


#float
float_string3 = "%f" % (1.237)

#dictionnaries
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})


###lists:
my_list3 = ["a", 1, "Python", 5]
my_list2 = ["a", "b", "c"]
m3 = my_list3 + my_list2
m4 = [4,24,1,2,3]
m4.sort()
m4

#slice list
m4[1:2]


###Tuples (immutable)
my_tuple = (1, 2, 3, 4, 5)

#dictionnaries (hash table: immutable)
my_dict = {"name":"Mike", "address":"123 Happy Way"}
my_other_dict = {"one":1, "two":2, "three":3}
my_dict["name"]
"name" in my_dict


#if
var1 = 1
var2 = 3
if var1 > var2:
    print("That's ok")
elif 1 <= var2 <= 5:
    print("I'd still pay that...")
else:
    print("ouin ouin")
        
        
#packages
pip install numpy
