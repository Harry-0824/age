driving = input('請問你有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('好好回答可以嗎?')
	raise SystemExit
age = input('請問你的年齡? ')
age = int(age)
if driving == '有' or driving == 'yes':
    if age >= 18:
        print('你通過測驗了~!!')
    else:
        print('未成年你怎麼會開過車?!')
elif driving == '沒有' or driving == 'no':
	if age >= 18:
		print('成年了就快去考啊!')
	else:
		print('再過幾年就可以考了~')
else:
    print('你在公三小?')

