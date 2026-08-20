def verify_card_number(card_number):
    stringa = str(card_number).replace(" ","").replace("-","")
    inverted = stringa[::-1]
    somma_totale = 0
    for i, cifra in enumerate(inverted):
        cifra = int(cifra)
        if i % 2!= 0:
            cifra *= 2
            if cifra > 9:
                cifra -= 9
        somma_totale += cifra
    if somma_totale % 10 == 0:
        return 'VALID!'   
    else:
        return 'INVALID!'

# Test       
print(verify_card_number("453914889"))
verify_card_number("4111-1111-1111-1111")
verify_card_number("1234 5678 9012 3456")