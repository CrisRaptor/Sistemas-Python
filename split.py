def mysplit(strng):
    result = []
    word = ""
    for i in strng:
        if i == " " :
            if word != "":
                result.append(word)
                word = ""
        else:
            word += i
    return (result)

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))