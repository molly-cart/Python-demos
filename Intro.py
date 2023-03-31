course = 'Doggie Pay Care 24/7'
print(course.upper())
print(course)
print(course.replace('Pay', 'Day '))

bolo = 'Be on the lookout for white male'
print(bolo.upper())
print(bolo.lower())

print(bolo.find('male'))
print('beige' in bolo)

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1


weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
