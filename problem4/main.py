def muncul_sekali(angka):
    muncul_sekali = []
    for digit in angka:
        if angka.count(digit) == 1: 
            muncul_sekali.append(int(digit))  
    return muncul_sekali

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]