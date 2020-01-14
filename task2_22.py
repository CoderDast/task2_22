
def tem_(Type_tem,number_tem):
    if Type_tem == 'F':
        number_tem = (number_tem - 32) * 5/9
        return number_tem
    elif Type_tem == 'C':
        number_tem = number_tem * 5/9 + 32
        return number_tem
    else:
        print('Not Correct')
        choose_tem = input('Kind of temperature \'F or C = ')
number_tem = int(input('Size of temperature = '))
choose_tem = input('Kind of temperature \'F or C = ')
print(tem_(choose_tem,number_tem))