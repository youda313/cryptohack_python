import os
import re

listFiles = "; ".join(os.listdir())   #transforming a list into a string
print(listFiles)

pattern = 'fileName'
if re.search(pattern, listFiles):
   print ("Pattern found")
else:
   print ("Pattern not found")

