name = str(input())
name_list = name.split()
initials = f"{name_list[0][0]}.{name_list[1][0]}.{name_list[2][0]}"
res = f"{initials}"
res = res.replace(".", "")
print(res.replace(".", ""))
print(len(name) - name.count(" ") + 2)
print(
    "ФИО:",
    name,
    "\nИнициалы:",
    res.upper(),
    "\nДлина(символов):",
    len(name) - name.count(" ") + 2,
)
