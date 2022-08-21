#雞兔同龍問題
#假設 🐔頭＋🐰頭=35
#腳的總數是100
#問幾隻雞,兔?

#數學表示
#x+y=35
#2x+4y=100
#求解

#先假設雞有0隻
chicken=0
while True:
    rabbit=35-chicken
    if 2*chicken+4*rabbit==100:
        print("雞有{}隻,兔有{}隻".format(chicken,rabbit))
        break
    chicken+=1
