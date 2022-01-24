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
def cleancol(input):
    if input:
      output = re.sub(r', (?![^(]*\))', '\n', input)
      out = output.split('\n')
    else:
      out = None
    return out

