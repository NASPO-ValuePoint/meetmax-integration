#Map Industries to Integers

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
