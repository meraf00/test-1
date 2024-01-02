test_cases = int(input())

for _ in range(test_cases):
    chest, key, stamina = map(int, input().split())

    if key <= chest:
        print(chest)

    else:
        if stamina >= key - chest:
            print(key)
        
        else:
            print(key + key - chest - stamina)