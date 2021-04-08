s = input()
while "ZZZZ".find("ZZZZ"):
    s.replace("RRR", "Z", 1)
    s.replace("ZZZZ", "R", 1)
print(s)

# input: RZRRZZZRR
# Пока в строке есть 4 подряд "Z"
#       Заменить три подряд "R" на одну "Z", а потом 4 "Z" на одну "R" (заменять только первое вхождение)
