#Python para Machine Learnig aula 7
#Função Lambda e funçoes anônimas

#função normal

def somaquadrados(a,b):
    somaQ = a**2 + b**2
    return somaQ
somaquadrados(2,4)

#função Lambda

somaquadrados2 = lambda a,b: a**2 + b**2
somaquadrados2(2,4)

def hex_para_bin(num):
    num = int(num, 16)  
    dec_para_bin(num)

hex_para_bin = lambda num: int(num,16),lambda num: dec_para_bin(num)


def hex_para_dec(num):
    num = int(num, 16)
    print(num,"dec")

hex_para_dec = lambda num: int(num, 16), lambda num:print(num,"dec")
