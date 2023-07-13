import re

pattern=re.compile(r'[$].{0,3}.[0-9]{0,2}|\b\w*[0-9]\w*\w*[Gg]\w*\w*[Bb]\w*\b|\b\w*[0-9]\w*\w*[Gg]\w*[Hh]\w*[Zz]\w*\b')
text='I want to buy a system with 6Gigahertz CPU 500Gb ssd and below $100.'
print(pattern.search(text))
#regex for phone number
#\b\w*[+91]|0832|[-]\w*.\w*[0-9]{10}\w*\b
#\b\w*(\+|91|0832)\s?[-]?[0-9]{0,10}\w*\b|\b\w*[-][0-9]{0,10}\w*\b
#\b\w*(\+|91|0832)\s?[0-9]{0,10}\w*\b|\b\w*[-][0-9]{0,10}\w*\b|\b\w*(\+|91|0832)[0-9]*[-]*[0-9]\w*\b
#\b\w*(\+|91|0832)\s*[0-9]{0,10}\w*\b|\b\w*[0-9]{0,10}(\-)[0-9]{0,10}\w*\b