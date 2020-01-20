def items(x,L):
  print("プレゼントしたいアイテムは？ リップ…0, チーク…1, アイシャドウ…2, ファンデ…3")
  x=int(input())
  return L.append(x)
def questions(a,L):
  print("あなたの友達のイメージは？")
  print(a)
  x=int(input())
  return L.append(x)
#ブランドの定義
#L.LIP0 C.CHEEK1 E.Eye2 F.fandertion3
Jill_L = [0,0,0,0]
Jill_C = [0,0,0,1]
Jill_E = [0,0,0,2]
Jill_F = [0,0,0,3]
Paul_L = [0,0,1,0]
Paul_C = [0,0,1,1]
Paul_E = [0,0,1,2]
Paul_F = [0,0,1,3]
#Mac = [0,2,0] OR [1,2,0]
#Anasui = [0,2,1] OR [1,2,1]
Dior_L = [1,1,0,0]
Dior_C = [1,1,0,1]
Dior_E = [1,1,0,2]
Dior_F = [1,1,0,3]
Chanel_L = [1,1,1,0]
Chanel_C = [1,1,1,1]
Chanel_E = [1,1,1,2]
Chanel_F = [1,1,1,3]
Nars_L = [1,0,0,0]
Nars_C = [1,0,0,1]
Nars_E = [1,0,0,2]
Nars_F = [1,0,0,3]
Addi_L = [1,0,1,0]
Addi_C = [1,0,1,1]
Addi_E = [1,0,1,2]
Addi_F = [1,0,1,3]
"""
Jill=[0,0,0]
Paul = [0,0,1]
Mac = [0,2,0] OR [1,2,0]
Anasui = [0,2,1] OR [1,2,1]
Dior = [1,1,0]
Chanel = [1,1,1]
Nars = [1,0,0]
Adi = [1,0,1]
"""
while True:
  L=[]
  x=0
  a1="かわいい…0　クール…1"
  questions(a1,L)
  #print(L)
  if L==[0]: #or[1,2]:
    a2 = "甘め…0　フェミニン…1　ギャル…2"
    questions(a2,L)
    if L==[0,0]:
      a4 = "お嬢様系…0　綺麗系…1"
      questions(a4,L)
      items(x,L)
      if L==[0,0,0,0]:
        print("あなたのお友達へのプレゼントは【JILLSTUARTのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Jil Lip
          url = "https://www.jillstuart-floranotisjillstuart.com/site/jillstuart/g/gSJLA060/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,0,1]:
        print("あなたのお友達へのプレゼントは【JILLSTUARTのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Jil Cheek
          url = "https://www.jillstuart-floranotisjillstuart.com/site/jillstuart/g/gSTAI007/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,0,2]:
        print("あなたのお友達へのプレゼントは【JILLSTUARTのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Jil eye
          url = "https://www.jillstuart-floranotisjillstuart.com/site/jillstuart/g/gSJEM005/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,0,3]:
        print("あなたのお友達へのプレゼントは【JILLSTUARTのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Jil base
          url = "https://www.jillstuart-floranotisjillstuart.com/site/jillstuart/g/gSJZC103/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,1,0]:
        print("あなたのお友達へのプレゼントは【PAUL & JOEのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Paul Lip
          url = "https://www.paul-joe-beaute.com/jp/products/APADTE/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,1,1]:
        print("あなたのお友達へのプレゼントは【PAUL & JOEのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Paul Cheek
          url = "https://www.paul-joe-beaute.com/jp/products/APABJX/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,1,2]:
        print("あなたのお友達へのプレゼントは【PAUL & JOEのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Paul Eye
          url = "https://www.paul-joe-beaute.com/jp/products/APACEU/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,0,1,3]:
        print("あなたのお友達へのプレゼントは【PAUL & JOEのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Paul base
          url = "https://www.paul-joe-beaute.com/jp/products/APAAVL/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
    if L==[0,1]:
      a5 = "シンプル…0　オーガニック…1"
      questions(a5,L)
      items(x,L)
      if L==[0,1,0,0]:
        print("あなたのお友達へのプレゼントは【RMKのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #リップ
          url = "https://onlineshop.rmkrmk.com/shopdetail/000000000411/lips/page1/recommend/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,0,1]:
        print("あなたのお友達へのプレゼントは【RMKのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #チーク
          url = "https://onlineshop.rmkrmk.com/shopdetail/000000000420/cheeks/page1/recommend/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,0,2]:
        print("あなたのお友達へのプレゼントは【RMKのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #アイシャドウ
          "https://onlineshop.rmkrmk.com/shopdetail/000000000988/eyes/page1/recommend/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,0,3]:
        print("あなたのお友達へのプレゼントは【RMKのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ファンデ
          "https://onlineshop.rmkrmk.com/shopdetail/000000001007/foundation/page1/recommend/"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,1,0]:
        print("あなたのお友達へのプレゼントは【THREEのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Three Lip
          url = "https://www.threecosmetics.com/onlineshop/products/detail/poi-0401003"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,1,1]:
        print("あなたのお友達へのプレゼントは【THREEのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Three Cheek
          url = "https://www.threecosmetics.com/onlineshop/products/detail/poi-0406002"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,1,2]:
        print("あなたのお友達へのプレゼントは【THREEのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Three Eye
          url = "https://www.threecosmetics.com/onlineshop/products/detail/poi-0402009"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,1,1,3]:
        print("あなたのお友達へのプレゼントは【THREEのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #Three base
          url = "https://www.threecosmetics.com/onlineshop/products/detail/bas-0302002"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
    if L==[0,2]:
      a8 = "モノトーン好き！…0　モノトーンはいいや笑…1"
      questions(a8,L)
      items(x,L)
      if L==[0,2,0,0]:
        print("あなたのお友達へのプレゼントは【MACのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #リップ
          url = "https://m.maccosmetics.jp/product/13854/310/makeup/matte-lipstick/lipstick"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,0,1]:
        print("あなたのお友達へのプレゼントは【MACのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #チーク
          url = "https://www.maccosmetics.jp/product/13842/31094/makeup/mineralize-blush"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,0,2]:
        print("あなたのお友達へのプレゼントは【MACのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #アイシャドウ
          url = "https://www.maccosmetics.jp/product/13840/363/makeup/eye-shadow/small-eye-shadow"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,0,3]:
        print("あなたのお友達へのプレゼントは【MACのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ファンデ
          url = "https://www.maccosmetics.jp/product/13847/41471/makeup/studio-fix-fluid-spf15pa-foundation-skin-balancing-complex"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,1,0]:
        print("あなたのお友達へのプレゼントは【ANNA SUIのリップ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ANNA SUI Lip
          url = "https://jp.annasui.com/products/asafts"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,1,1]:
        print("あなたのお友達へのプレゼントは【ANNA SUIのチーク】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ANNA SUI Cheek
          url = "https://jp.annasui.com/products/asabjd"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,1,2]:
        print("あなたのお友達へのプレゼントは【ANNA SUIのアイシャドウ】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ANNA SUI Eye
          url = "https://jp.annasui.com/products/asagea"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
      if L==[0,2,1,3]:
        print("あなたのお友達へのプレゼントは【ANNA SUIのファンデーション】！")
        print("HPに行く…0  最初に戻る…1")
        m=int(input())
        if m==0:
          import webbrowser
          #ANNA SUI base
          url = "https://jp.annasui.com/products/asabfe"
          webbrowser.open(url)
          break
        if m==1:
          print("最初から！")
  if L == [1]:
      a3 = "モード…0　エレガント…1　ギャル…2"
      questions(a3,L)
      if L==[1,0]:
          a7 = "予算は奮発しちゃう！…0　予算は安めがいい！…1"
          questions(a7,L)
          items(x,L)
          if L==[1,0,0,0]:
              print("あなたのお友達へのプレゼントは【NARSのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #NARS Lip
                  url = "https://www.narscosmetics.jp/powermatte-lip-pigment/864901.html?dwvar_864901_color=2760&cgid=lips"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,0,1]:
              print("あなたのお友達へのプレゼントは【NARSのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #NARS cheek
              url = "https://www.narscosmetics.jp/blush/866201.html?dwvar_866201_color=4001N&cgid=blush"
              webbrowser.open(url)
              break
              if m==1:
                  print("最初から！")
          if L==[1,0,0,2]:
              print("あなたのお友達へのプレゼントは【NARSのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #NARS Eye
                  url = "https://www.narscosmetics.jp/quad-eyeshadow-3972/4535683962803.html?cgid=eyeshadow"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,0,3]:
              print("あなたのお友達へのプレゼントは【NARSのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #NARS base
                  url ="https://www.narscosmetics.jp/natural-radiant-longwear-foundation/869801.html?dwvar_869801_color=6599&cgid=best-sellers"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,1,0]:
              print("あなたのお友達へのプレゼントは【ADDICTIONのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #ad  Lip
                  url = "https://onlineshop.addiction-beauty.com/ItemDetail?cmId=1330"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,1,1]:
              print("あなたのお友達へのプレゼントは【ADDICTIONのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #ad cheek
                  url = "https://onlineshop.addiction-beauty.com/ItemDetail?cmId=1041"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,1,2]:
              print("あなたのお友達へのプレゼントは【ADDICTIONのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #ad Eye
                  url = "https://onlineshop.addiction-beauty.com/ItemDetail?cmId=614"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,0,1,3]:
              print("あなたのお友達へのプレゼントは【ADDICTIONのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #ad base
                  url = "https://onlineshop.addiction-beauty.com/ItemDetail?cmId=1259"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
      if L==[1,1]:
          a6 = "華やか…0　洗練…1"
          questions(a6,L)
          items(x,L)
          if L==[1,1,0,0]:
              print("あなたのお友達へのプレゼントは【DIORのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #dior Lip
                  url = "https://www.dior.com/ja_jp/"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,0,1]:
              print("あなたのお友達へのプレゼントは【DIORのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #dior Cheek
                  url = "https://www.dior.com/ja_jp/products/beauty-Y0000004"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,0,2]:
              print("あなたのお友達へのプレゼントは【DIORのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
              #dior eye
                  url = "https://www.dior.com/ja_jp/products/beauty-Y0012000"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,0,3]:
              print("YESあなたのお友達へのプレゼントは【DIORのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #dior base
                  url = "https://www.dior.com/ja_jp/products/beauty-Y0071000"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,1,0]:
              print("あなたのお友達へのプレゼントは【CHANELのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #chanel Lip
                  url = "https://www.chanel.com/ja_JP/fragrance-beauty/makeup/p/lips/lipsticks/rouge-coco-flash-colour-shine-intensity-in-a-flash-p174052.html#skuid-0174080"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,1,1]:
              print("あなたのお友達へのプレゼントは【CHANELのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #chanel cheek
                  url = "https://www.chanel.com/ja_JP/fragrance-beauty/makeup/p/complexion/blush/joues-contraste-powder-blush-p168000.html#skuid-0168640"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,1,2]:
              print("あなたのお友達へのプレゼントは【CHANELのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #chanel Eye
                  url = "https://www.chanel.com/ja_JP/fragrance-beauty/makeup/p/eyes/eyeshadows/les-4-ombres-multi-effect-quadra-eyeshadow-p164202.html#skuid-0164294"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,1,1,3]:
              print("あなたのお友達へのプレゼントは【CHANELのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #chanel base
                  url = "https://www.chanel.com/ja_JP/fragrance-beauty/makeup/p/complexion/foundations/les-beiges-healthy-glow-gel-touch-foundation-spf-25--pa--p184610.html#skuid-0184610"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
      if L==[1,2]:
          a8 = "モノトーン好き！…0　モノトーンはいいや笑…1"
          questions(a8,L)
          items(x,L)
          if L==[1,2,0,0]:
              print("あなたのお友達へのプレゼントは【MACのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #リップ
                  url = "https://m.maccosmetics.jp/product/13854/310/makeup/matte-lipstick/lipstick"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,0,1]:
              print("あなたのお友達へのプレゼントは【MACのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #チーク
                  url = "https://www.maccosmetics.jp/product/13842/31094/makeup/mineralize-blush"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,0,2]:
              print("あなたのお友達へのプレゼントは【MACのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #アイシャドウ
                  url = "https://www.maccosmetics.jp/product/13840/363/makeup/eye-shadow/small-eye-shadow"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,0,3]:
              print("あなたのお友達へのプレゼントは【MACのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #ファンデ
                  url = "https://www.maccosmetics.jp/product/13847/41471/makeup/studio-fix-fluid-spf15pa-foundation-skin-balancing-complex"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,1,0]:
              print("あなたのお友達へのプレゼントは【ANNA SUIのリップ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #ANNA SUI Lip
                  url = "https://jp.annasui.com/products/asafts"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,1,1]:
              print("あなたのお友達へのプレゼントは【ANNA SUIのチーク】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #ANNA SUI Cheek
                  url = "https://jp.annasui.com/products/asabjd"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,1,2]:
              print("あなたのお友達へのプレゼントは【ANNA SUIのアイシャドウ】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #ANNA SUI Eye
                  url = "https://jp.annasui.com/products/asagea"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
          if L==[1,2,1,3]:
              print("あなたのお友達へのプレゼントは【ANNA SUIのファンデーション】！")
              print("HPに行く…0  最初に戻る…1")
              m=int(input())
              if m==0:
                  import webbrowser
                  #ANNA SUI base
                  url = "https://jp.annasui.com/products/asabfe"
                  webbrowser.open(url)
                  break
              if m==1:
                  print("最初から！")
else:
  print("指定された数字のみ入力してください。")