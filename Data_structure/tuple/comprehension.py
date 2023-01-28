str_tuple = ("They", "all", "hate", "you", "Mando", "because", "you're", "a", "legend")

th = [x for x in str_tuple if "a" in x]
print(th)

sd = [x for x in str_tuple if "o" in x]
print(tuple(sd))
