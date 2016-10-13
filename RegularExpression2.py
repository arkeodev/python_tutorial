# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import re

# A very intuitive example are XML or HTML tags. E.g. let's assume we have a file (called "tags.txt")
# with content like this:

# <composer>Wolfgang Amadeus Mozart</composer>
# <author>Samuel Beckett</author>
# <city>London</city>

# We want to rewrite this text automatically to
# composer: Wolfgang Amadeus Mozart
# author: Samuel Beckett
# city: London

fh = open("tags.txt")
for i in fh:
     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
     print(res.group(1) + ": " + res.group(2))

# Another example for back references. The task is to rewrite this example in the following way:
# Allison Neu 555-8396
# C. Montgomery Burns
# Lionel Putz 555-5299
# Homer Jay Simpson 555-7334

l = ["555-8396 Neu, Allison",
     "Burns, C. Montgomery",
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))

# A third example for capturing groups to assign them descriptive names instead of automatic numbers
s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
# '13'
print(x.group('minutes'))
# '47'
print(x.group("seconds"))
# '03'
print(x.start('minutes'))
# 14
print(x.end('minutes'))
# 16
print(x.span('seconds'))
# (17, 19)

# The last example: Our task is to create a list with the top 19 cities, with the city names accompanied by the postal code

# First file:
# 68309,"Mannheim",8222,"Mannheim",8,"Baden-Wrttemberg"
# 68519,"Viernheim",6431,"Bergstraße",6,"Hessen"
# 68526,"Ladenburg",8226,"Rhein-Neckar-Kreis",8,"Baden-Württemberg"
# 68535,"Edingen-Neckarhausen",8226,"Rhein-Neckar-Kreis",8,"Baden-Württemberg"

# Second file:
# 1.  Berlin          3.382.169 Berlin
# 2.  Hamburg         1.715.392 Hamburg
# 3.  München         1.210.223 Bayern
# 4.  Köln              962.884 Nordrhein-Westfalen
# 5.  Frankfurt am Main 646.550 Hessen
# 6.  Essen             595.243 Nordrhein-Westfalen
# 7.  Dortmund          588.994 Nordrhein-Westfalen
# 8.  Stuttgart         583.874 Baden-Württemberg
# 9.  Düsseldorf        569.364 Nordrhein-Westfalen
# 10. Bremen            539.403 Bremen
# 11. Hannover          515.001 Niedersachsen
# 12. Duisburg          514.915 Nordrhein-Westfalen
# 13. Leipzig           493.208 Sachsen
# 14. Nürnberg          488.400 Bayern
# 15. Dresden           477.807 Sachsen
# 16. Bochum            391.147 Nordrhein-Westfalen
# 17. Wuppertal         366.434 Nordrhein-Westfalen
# 18. Bielefeld         321.758 Nordrhein-Westfalen
# 19. Mannheim          306.729 Baden-Württemberg

fh_post_codes = open("post_codes_germany.txt")
PLZ = {}
for line in fh_post_codes:
    (post_code, city, rest) = line.split(",",2)
    PLZ[city.strip("\"")] =  post_code


fh_largest_cities = open("largest_cities_germany.txt")

for line in fh_largest_cities:
    re_obj = re.search(r"^[0-9]{1,2}\.\s+([\wÄÖÜäöüß\s]+\w)\s+[0-9]",line)
    city = re_obj.group(1)
    print(city, PLZ[city])
