def maior(*n):
    m = 0
    for i in n:
        if m < i:
            m = i
    print(f'O mair número é {m}')

maior(2, 3, 8, 25)