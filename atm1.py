#Bakiyeler
Mustafa=1000
Hasan=2000
Filiz=500
Yasin=700

#Şifreler
#msifre=2834
#hsifre=4563
#fsifre=9275
#ysifre=3260

hesap = input('Lütfen isminizi giriniz: ')  #Kullanıcıya ismini sorar.

if hesap == 'Mustafa':                                                  #Mustafa
    msifre = input('Şifrenizi giriniz: ')
    if int(msifre) == 2834:     
        para = input("""Hoşgeldiniz.

Lütfen yapmak istediğiniz işlemi seçiniz.
Para gönderme = 1
Para çekme = 2
Para yatırma = 3 
Bakiye sorgulama = 4 """)

        if int(para) == 1:
            gonder = input('Lütfen para göndermek istediğiniz kişiyi seçiniz.')
            para1 = input('Lütfen göndermek istediğiniz miktarı giriniz.')
            print(str(gonder) , 'adlı kişiye ', int(para1) , 'tl gönderildi. Yeni bakiyeniz = ', int(Mustafa) - int(para1))

        elif int(para) == 2:
            para2 = input('Lütfen çekmek istediğiniz miktarı giriniz. ')
            print('Hesabınızdan ', int(para2) ,'tl çekildi. Yeni bakiyeniz = ', int(Mustafa) - int(para2))

        elif int(para) == 3:
           yatir = input('Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz.')
           print( int(yatir) , ' tl hesabınıza yatırıldı. Yeni bakiyeniz = ', int(Mustafa + int(yatir)))

        elif int(para) == 4:
            print('Bakiyeniz ', Mustafa , ' tl. ')

        else:
            print('Geçersiz işlem seçildi. ')
    else:
        print('Lütfen tekrar deneyiniz. ')

elif hesap == 'Filiz':                                                      #Filiz
    fsifre=input('Şifrenizi giriniz. ')
    if int(fsifre) == 9275:
        para=input("""Hoşgeldiniz.
                   
Lütfen yapmak istediğiniz işlemi seçiniz.
Para gönderme = 1
Para çekme = 2
Para yatırma = 3
Bakiye sorgulama = 4 """)
        if int(para) == 1:
            gonder = input('Lütfen para göndermek istediğiniz kişiyi seçiniz.')
            para1 = input('Lütfen göndermek istediğiniz miktarı giriniz.')
            print(str(gonder) , 'adlı kişiye ', int(para1) , 'tl gönderildi. Yeni bakiyeniz = ', int(Filiz) - int(para1))

        elif int(para) == 2:
            para2 = input('Lütfen çekmek istediğiniz miktarı giriniz. ')
            print('Hesabınızdan ', int(para2) ,'tl çekildi. Yeni bakiyeniz = ', int(Filiz) - int(para2))

        elif int(para) == 3:
           yatir = input('Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz.')
           print( int(yatir) , ' tl hesabınıza yatırıldı. Yeni bakiyeniz = ', int(Filiz + int(yatir)))

        elif int(para) == 4:
            print('Bakiyeniz ', Filiz , ' tl. ')
        else:
            print('Geçersiz işlem seçildi. ')
    else:
        print('Lütfen tekrar deneyiniz. ')

elif hesap == 'Hasan':                                                          #Hasan
    hsifre = input('Şifrenizi giriniz.')
    if int(hsifre) == 4563:
        hpara = input("""Hoşgeldiniz.
        
Lütfen yapmak istediğiniz işlemi seçiniz. 
Para gönderme = 1
Para çekme = 2
Para yatırma = 3
Bakiye sorgulama = 4: """)

        if int(hpara) == 1:
            gonder = input('Lütfen para göndermek istediğiniz kişiyi seçiniz.')
            para1 = input('Lütfen göndermek istediğiniz miktarı giriniz.')
            print(str(gonder), 'adlı kişiye', int(para1), 'tl gönderildi. Yeni bakiyeniz = ', Hasan - int(para1))

        elif int(hpara) == 2:
            para2 = input('Lütfen çekmek istediğiniz miktarı giriniz. ')
            print('Hesabınızdan', int(para2), 'tl çekildi. Yeni bakiyeniz = ', Hasan - int(para2))

        elif int(hpara) == 3:
            yatir = input('Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz.')
            print(int(yatir), ' tl hesabınıza yatırıldı. Yeni bakiyeniz = ', Hasan + int(yatir))

        elif int(hpara) == 4:
            print('Bakiyeniz ', Hasan, ' tl. ')

        else:
            print('Geçersiz işlem seçildi. ')
    else:
        print('Lütfen tekrar deneyiniz. ')

elif hesap == 'Yasin':                                      #Yasin
    ysifre = input('Şifrenizi giriniz.')
    if int(ysifre) == 3260:
        para = input("""Hoşgeldiniz.
        
Lütfen yapmak istediğiniz işlemi seçiniz. 
Para gönderme = 1
Para çekme = 2
Para yatırma = 3
Bakiye sorgulama = 4: """)

        if int(para) == 1:
            gonder = input('Lütfen para göndermek istediğiniz kişiyi seçiniz.')
            para1 = input('Lütfen göndermek istediğiniz miktarı giriniz.')
            print(str(gonder), 'adlı kişiye', int(para1), 'tl gönderildi. Yeni bakiyeniz = ', Yasin - int(para1))

        elif int(para) == 2:
            para2 = input('Lütfen çekmek istediğiniz miktarı giriniz. ')
            print('Hesabınızdan', int(para2), 'tl çekildi. Yeni bakiyeniz = ', Yasin - int(para2))

        elif int(para) == 3:
            yatir = input('Lütfen hesabınıza yatırmak istediğiniz tutarı giriniz.')
            print(int(yatir), ' tl hesabınıza yatırıldı. Yeni bakiyeniz = ', Yasin + int(yatir))

        elif int(para) == 4:
            print('Bakiyeniz ', Yasin, ' tl. ')

        else:
            print('Geçersiz işlem seçildi. ')
    else:
        print('Lütfen tekrar deneyiniz. ')
else:
    print('Kullanıcı adı hatalı. ')