#Map Industries to Integers
import re
import numpy as np

def industry_number(text):
  options = ["Agricultural Equipment",
  "Automotive/Fleet",
  "Construction Equipment and Supplies Cooperative Purchasing",
  "Equipment Rental and Leasing",
  "Healthcare Supplies",
  "Heavy Machinery",
  "Industrial and Construction",
  "IT Hardware and Software",
  "IT Services",
  "Laboratory Services",
  "Material Goods",
  "Maintenance, Repair and Operations",
  "Mobile Technology",
  "Procurement Services",
  "Professional Services",
  "Sustainable Products",
  "Telecommunications",
  "Other"
  ]

  index = options.index(text)
  return index + 1

#Clean Categories/Industries field so its accepted by meetmax api
#Separate each category by newline and then split into a list of strings
# def cleancol(input):
#     if input:
#       output = re.sub(r', (?![^(]*\))', '\n', input)
#       out = output.split('\n')
#       print(out[-1])
#       if 'OTHER:' in out[-1]:
#         other_category = ''.join(out[-1].split('OTHER: ', 1))
#         out[-1] = 'Other'
#       else:
#         other_category = None
#     else:
#       out = None
#       other_category = None
#     return out, other_category


def cleancol(input):
  if input:
    output = re.sub(r', (?![^(]*\))', '\n', input)
    out = output.split('\n')
    #print(out)
    for i, x in enumerate(out):
      #print(x)
      if 'OTHER:' in x:
        temp = ', '.join(out[i:len(out)])
        other_category = temp.split('OTHER: ')[1]
        category = out[0:i]
        category.append('Other')
        #print(other_category)
        break
      else:
        other_category = None
      category = out
  else:
    category = None
    other_category = None
  return category, other_category



#input = 'Facilities MRO, OTHER: Metalworking'
#input = ''
input = 'Office Equipment/Supplies/Service (Copiers, Paper, Furniture, Mailroom, etc.), OTHER: Managed Print Services, Document Solutions'
#print(cleancol(input))
