import re

txt = "The rain in Spain and it's a cold cold rain"

foundVal = re.search("rain", txt)

print(foundVal)

print(foundVal.span)