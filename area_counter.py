"""
This project will help you to calculate area of any circular or traiangular shape.
"""
print ('The Calculator is Starting.')
print ('Enter C for Circle or T for Triangle:')
dimension = input ("what types of area you want to calculate?")
if dimension == 'C' or dimension=='c': 
  radius=float( input( 'enter the radius:'))
  pi=3.1416
  area_of_circle=pi*radius*radius
  print ('the area of the circle is %s' %  area_of_circle)
elif dimension =="T" or dimension=="t":
  base =float( input('enter the value of base :'))
  height =float( input('enter the value of height: '))
  area_of_triangle=(base*height)/2
  print  ('the area of the traingle is %s' % area_of_triangle)
else:
  print ('you have entered and invalid shape.')
  
print ('the program is exiting. ')
