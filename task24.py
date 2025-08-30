matn=input('Email kiriting: ')

if not matn.startswith('@') and matn.endswith('.com'):
    print(True)

else:
    print(False)
