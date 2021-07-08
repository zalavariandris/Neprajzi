
import re

# cells = [
#     "42936-43059 (R10583-R10583) Rajzgyűjtemény, 43060 ? gyűjtemény, 43061-43089 Állattartás gyűjtemény, 43090-43100 (F4512-F4522) Fényképgyűjtemény"
#     ]



# patterns = [
# 	"\d+?-\d+? \([F\d\s]+?\) Fényképgyűjtemény",
# 	"\d+?-\d+? \([R\d\s]+?\) Rajzgyűjtemény"
# ]

# import re

# pattern = re.compile("\d+-\d+ \([R\d+-R\d+]+?\) Fényképgyűjtemény|\d+-\d+ \([R\d+-R\d+]+?\) Rajzgyűjtemény")

# for f in pattern.findall(cells[0]):
# 	print(f)


cell = "[...], 2212-2215 Törlés 49/897, [...], [...], [...], 2254-2255 Törlés 49/897, [...], "
cell2 = "[...], , [...], [...], [...],, [...], "

res = re.compile(".*[a-zA-Z].*").match(cell2)
print(res)