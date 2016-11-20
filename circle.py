print "what would you like to do?"
print "find cirumference"
print "find area"
print "find diameter"
print "find radius"
option = raw_input("enter 1 2 3 or 4 ")
if option == "1":
	d = raw_input("enter radius of circle in cm ")
	d = float(d)
	result = 2 * 3.14 * d
	print "the circumference is %s" % result
elif option == "2":
	a = raw_input("enter radius of circle in cm ")
	a = float(a)
	result = 3.14 * a * a
	print "the area is %s" % result
elif option == "3":
        r = raw_input("enter radius ")
        r = float(r)
        result = r * 2
        print "diameter is %s" % result
elif option == "4":
        m = raw_input("enter diameter ")
        m = float(m)
        result = m / 2
        print "radius is %s" % result
        
	

