# slicing = create a substring by extracting elements of another string
#           indexing[] or slice()
#            [start:stop:step]

#name = "Harry Houndonougbo"

#first_name = name[:5]          #   [0:3]
#last_name = name[6:]           #   [4:end]
#funky_name = name[::2]         #   [0:end:2]
#reversed_name = name[::-1]     #   [0:end:-1]

#print(reversed_name)*

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])