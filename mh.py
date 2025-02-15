def MaHoa(plaintext, key):
    ciphertext=""
    for c in plaintext:
        if c!=' ':
            so = ord(c) - 65
            so = (so + key) % 26
            ciphertext = ciphertext + chr(so + 65)
        else:
            ciphertext = ciphertext + c
    return ciphertext

# def GiaiMa(ciphertext, key):
#     plaintext= ""
#     for c in cirphertext:
#         if c != ' ':
#             so = ord(c) - 65
#             so = (so - key + 26) % 26
#         else:
#             ciphertext = ciphertext + c
#     return ciphertext
            
    p = "Tran Thi Dieu Linh"
    p=p.upper
    key = 10
    c = MaHoa(p, key)
    print("Sau khi ma hoa doan: ",c)
    # s = GiaiMa(c, key)
    # print("Sau khi giai ma: ",s)
    