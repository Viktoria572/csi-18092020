import random
opiration = ["камень", "ножницы", "бумага"]

print('Поиграем в камень, ножницы, бумага ?')
while True:
    choice = input('Выбери знак 0-камень, 1 - ножницы, 2-бумага \n')

    computer_opiration = random.randrange(0, 3)
    try:
        choice = int(choice)
        if choice > 2:
            break
        if choice == 0:
            if computer_opiration == 0:

                print('Ничья')

            if computer_opiration == 1:

               print('Вы проиграли')

            if computer_opiration == 2:

                print('Поздравляю, вы выиграли!')
        if choice == 1:
            if computer_opiration == 1:
                print ('Ничья')
            if computer_opiration == 2:
                print('Вы выиграли')
        if choice== 2:
            if computer_opiration == 1:
                print('Вы выиграли')
            if computer_opiration == 2:
                print ('Ничья')
            if computer_opiration == 0:
                print('Вы выиграли')





            








    except:
        print("не правильно число")
