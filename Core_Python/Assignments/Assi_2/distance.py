feet=int(input('enter distance in feet :'))
inches=int(input('enter the distance in inches'))

meter=feet*0.3048
centi=inches*2.54

total_meter=meter+ centi
meters=int(total_meter)
centimeters=(total_meter-meters)*100


print('dist in meters :',meters)
print('dist in centi',centimeters)