from sympy import mod_inverse

def rsa_ma_hoa(thong_diep, p, q, e):
    n = p * q
    
    print(f"Khoa cong khai: (e={e}, n={n})")

    ma_hoa_thong_diep = [pow(ord(ky_tu), e, n) for ky_tu in thong_diep]
    print("Thong diep da ma hoa:", ma_hoa_thong_diep)

p = 17
q = 23
e = 5
thong_diep = "Tran Thi Dieu Linh"

rsa_ma_hoa(thong_diep, p, q, e)
