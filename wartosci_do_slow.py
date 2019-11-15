def number_to_letter(number):
    '''changes number inserted into letter, insert as a floating point number with 2 spaces after coma'''

    jednosci = {'0':'', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem',
                '9': 'dziewięć'}
    nastki = {'0': 'dziesięć', '1': 'jedenaście', '2': 'dwanaście', '3': 'trzynaście', '4': 'czternaście', '5': 'piętnaście',
              '6': 'szesnaście', '7': 'siedemnaście', '8': 'osiemnaście', '9': 'dziewiętnaście'}
    dziesiatki = {'2': 'dwadzieścia', '3': 'trzydzieści', '4': 'czterdzieści', '5': 'pięćdziesiąt', '6': 'sześćdziesiąt',
                  '7': 'siedemdziesiąt', '8': 'osiemdziesiąt', '9': 'dziewięćdziesiąt'}
    setki = {'1': 'sto', '2': 'dwieście', '3': 'trzysta', '4': 'czterysta', '5': 'pięćset', '6': 'sześćset', '7': 'siedemset',
             '8': 'osiemset', '9': 'dziewięćset'}
    tysiace = {'1': 'tysiąć', '2': 'dwa tysiące', '3': 'trzy tysiące', '4': 'cztery tysiące', '5': 'pięć tysięcy',
               '6': 'sześć tysięcy', '7': 'siedem tysięcy', '8': 'osiem tysięcy', '9': 'dziewięć tysięcy'}
    milion = {'1': 'jeden milion', '2': 'dwa miliony', '3': 'trzy miliony', '4': 'cztery miliony', '5': 'pięć milionów',
              '6': 'sześć milionów', '7': 'siedem milionów', '8': 'osiem milionów', '9': 'dziewięć milionów'}


    num_in_words=[]
    liczba=str(number)

    # grosze
    if len(liczba)>=3:
        if liczba[-3]=='.':
            num_in_words.insert(0, 'groszy')
            if liczba[-2]=='0':
                num_in_words.insert(0, jednosci[liczba[-1]])
            elif liczba[-2]=='1':
                num_in_words.insert(0, nastki[liczba[-1]])
            elif liczba[-2]=='0' and liczba[-1]=='0':
                num_in_words.insert(0, 'zero')
            else:
                num_in_words.insert(0, jednosci[liczba[-1]])
                num_in_words.insert(0, dziesiatki[liczba[-2]])
        else:
            liczba+='.00'
            num_in_words.insert(0, 'zero groszy')
    else:
        liczba += '.00'
        num_in_words.insert(0, 'zero groszy')


    num_in_words.insert(0, 'złotych')

    # jedności i dziesiątki
    if len(liczba)>=5:
        if liczba[-5]=='1':
            num_in_words.insert(0, nastki[liczba[-4]])
        else:
            num_in_words.insert(0, jednosci[liczba[-4]])
            num_in_words.insert(0, dziesiatki[liczba[-5]])
    else:
        num_in_words.insert(0, jednosci[liczba[-4]])

    # setki
    if len(liczba)>=6:
        num_in_words.insert(0, setki[liczba[-6]])

    # tysiące
    if len(liczba)>=8:
        if liczba[-8]=='1':
            num_in_words.insert(0, nastki[liczba[-7]]+' tysięcy')
        else:
            num_in_words.insert(0, jednosci[liczba[-7]]+' tysięcy')
            num_in_words.insert(0, dziesiatki[liczba[-8]])
    elif len(liczba)>=7:
        num_in_words.insert(0, tysiace[liczba[-7]])

    if len(liczba)>=9:
        num_in_words.insert(0, setki[liczba[-9]])

    # miliony
    if len(liczba)>=11:
        if liczba[-11] == '1':
            num_in_words.insert(0, nastki[liczba[-10]] + ' milionów')
        else:
            num_in_words.insert(0, jednosci[liczba[-10]] + ' milionów')
            num_in_words.insert(0, dziesiatki[liczba[-11]])
    else:
        if len(liczba)>=10:
            num_in_words.insert(0, milion[liczba[-10]])

    if len(liczba)>=12:
        num_in_words.insert(0, setki[liczba[-12]])


    return print(num_in_words)

number_to_letter(111111111111111.11)










