inputdir = input("Введите расположение своего проекта. \n Пример /storage/emulated/0/myproject/project.txt: ")
project = open(inputdir, 'r', encoding = 'utf_8')
replace = project.read().replace("а","a").replace("р", "p").replace("о","o").replace("х","x").replace("у","y").replace(" ","⠀")

outputdir = input("Введите подходящее расположение отредактированого проекта. \n /storage/emulated/0/myproject/redactedproject.txt: ")
project2 = open(outputdir, 'w', encoding = 'utf_8')
project2.write(str(replace) + '\n')