import random


print"""
        ====================
        ======POKEGOCHI=====
        ====================
       ;-.               ,
        \ '.           .'/
         \  \ .---. .-' /
          '. '     `\_.'
            |(),()  |     ,
            (  __   /   .' \.
           .''.___.'--,/\_,|
          {  /     \   }   |
           '.\     /_.'    /
            |'-.-',  `; _.'
            |  |  |   |`
            `''`''`'''` """
nama = raw_input('Masukan Nama Poke : ')
poke = {"nama": nama, 'power': 50}

def goEat():
    poke['power'] += random.randint(1,150)
    print"""
        ;-.               ,
        \ '.           .'/
         \  \ .---. .-' /
          '. '     `\_.'
            |(),()  |     , nyam... nyamm...
            (  __   /   .' \. nyamm....
           .''.___.'--,/\_,|
          {  /     \   }   |
           '.\     /_.'    /
            |'-.-',  `; _.'
            |  |  |   |`
            `""`""`'''` """
    print '------------------------------------------------------------------------------'
    pilihan()

def goFight():
    powermonster = random.randint(1,200)
    pwr = int(powermonster)
    kekuatan = int(poke['power'])
    print"""
                 .~~-.      _.             ;-.               ,
       .''..    (_~)  ) _.-'. ;            \ '.           .'/
       '.'..'..-(_~ _-'*. .'.'              \  \ .---. .-' /
         ''.'.. _ ~~  _  ';'                 '. '     `\_.'
          .''. (_)   (_)  '.                   |(),()  |     ,
          ;      "..."     '.                  (  __   /   .' \.
      .''.'.   .''`-'''.    '.''.    vs       .''.___.'--,/\_,|
      '.  '   ;         ;    ;  ;            {  /     \   }   |
        '.   ;           ;   ' ;              '.\     /_.'    /
         '.  ;           ;    ;                |'-.-',  `; _.'
          '.  ;         ;   .'                 |  |  |   |`
          .'...:..___..:..':.                  `''`''`'''` '''
       .''     ..'    '...   ~)   
      (.....'''           ''''
        -----------------------------------------------------------------
        power monster """,powermonster,"        power",nama," ",kekuatan
    if pwr > kekuatan:
        print '######',nama,' kalah dalam pertandingan ini, tingkatkan lagi power ',nama
    else:
        print '######','horee ',nama,' berhasil mengalahkan monster'
    print '------------------------------------------------------------------------------'
    pilihan()

def goStatus():
    print '######',poke
    print '------------------------------------------------------------------------------'
    pilihan()

def pilihan():
    print '''
           =====================B
           ======PokeGochi======y
           =====================
           1. Makan             Z
           2. Bertarung         N
           3. Lihat Status      L
           4. Keluar
           ====================='''
    pilih = input('     Masukan Pilihan [1-4] :')
    if pilih==1:
        goEat()
    elif pilih==2:
        goFight()
    elif pilih==3:
        goStatus()
    elif pilih==4:
        quit()
    else:
        print "Tidak Ada pilihan"

pilihan()
