import re


# Clean Categories/Industries field so its accepted by meetmax api
# Separate each category by newline and then split into a list of strings
def cleancol(input):
    if input:
        output = re.sub(r', (?![^(]*\))', '\n', input)
        out = output.split('\n')
        # print(out)
        for i, x in enumerate(out):
            # print(x)
            if 'OTHER:' in x:
                temp = ', '.join(out[i:len(out)])
                other_category = temp.split('OTHER: ')[1]
                category = out[0:i]
                category.append('Other')
                # print(other_category)
                break
            else:
                other_category = None
            category = out
    else:
        category = None
        other_category = None
    return category, other_category

# input = 'Facilities MRO, OTHER: Metalworking'
# input = ''
# input = 'Technology - Hardware/Software, OTHER: Procurement Solutions'
# input = 'Consulting/Professional Services, Technology - Hardware/Software, OTHER: Cloud, as a Service IT'
# print(cleancol(input)[0])
# print(cleancol(input)[1])
