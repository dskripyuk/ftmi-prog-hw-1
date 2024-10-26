per=input()
per=per.replace('-','_')
alf={'A':'a','Q':'q','W':'w','E':'e','R':'r','T':'t','Y':'y','U':'u','I':'i','O':'o','P':'p','S':'s','D':'d','F':'f','G':'g','H':'h','J':'j','K':'k','L':'l','Z':'z','X':'x','C':'c','V':'v','B':'b','N':'n','M':'m'}
alf_1=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
for i in range(len(per)+1):
    if per[i:i+1] in alf_1:
        if i>0 and per[i-1:i]!=' ':
            per =per[:i] + '_' + alf[per[i:i+1]] + per[i+1:]
        else:
            per = per[:i] + alf[per[i:i + 1]] + per[i + 1:]
while ' ' in per:
    per=per.replace(' ','_')
while '__' in per:
    per=per.replace('__','_')
if per[:1]=='_':
    per=per[1:]
if per[-1:] == '_':
    per = per[:-1]
while  per[:1]=='1' or per[:1]=='2' or per[:1]=='3' or per[:1]=='4' or per[:1]=='5' or per[:1]=='6' or per[:1]=='7' or per[:1]=='8' or per[:1]=='9' or per[:1]=='0':
    per=per[1:]
x=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','_']
a=0
for i in range (len(per)):
    if per[i:i+1] not in x:
        a=1
        print("Введено некорректное имя переменной")
        break
if a==0:
    print(per)

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here (˶ᵔ ᵕ ᵔ˶)
