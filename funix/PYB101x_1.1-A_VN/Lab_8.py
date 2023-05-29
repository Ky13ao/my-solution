from test_proc import multi_testing


def lab8_1():
    # Lab8.1: https://docs.google.com/document/d/1WyD0_gg3KObNtZfFTm7JeR2cxiagOP55/view
    lengthOfAll = set(
        map(float, input().split(' ')))
    return round(sum(lengthOfAll)/len(lengthOfAll), 2)


def lab8_2():
    # Lab8.2: https://docs.google.com/document/d/1OVPZbtfv4D_LPiQUqotYo6U6TeOChBAS/view
    placesStr = input()
    a = set()
    for place in placesStr.split(' '):
        a.add(place)
    return len(a)


def lab8_3():
    # Lab8.3: https://docs.google.com/document/d/1KOmHJBPU7eRfTiC4B3T9HRKm_PJZIFpj/view
    nSet = set(map(int, input().split(' ')))
    removeNums = map(int, input().split('remove')[1:])
    for removeNum in removeNums:
        # num = int(removeNum.strip() if len(removeNum) > 0 else 0)
        if removeNum in nSet:
            nSet.remove(removeNum)
    return sum(nSet)


if __name__ == "__main__":
    '''
    multi_testing(
        lab8_1, [{"input": ["1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80"],
                  "output": "1.71"},
                 {"input": ["1.87 1.92 1.73 1.64 1.79 1.87 1.75 1.75 1.92 1.75"],
                  "output": "1.78"},
                 {"input": ["1.70 1.67 1.65 1.64 1.75 1.67 1.65 1.75 1.78 1.70"],
                  "output": "1.7"}])
    # '''
    '''
    multi_testing(
        lab8_2, [{"input": ["France France Vietnam Germany Germany Italy"],
                  "output": "4"},
                 {"input": ["China USA Ukraina Russia China Holland Laos China Korea"],
                  "output": "7"},
                 {"input": ["Vietnam China Vietnam China Laos Vietnam Campuchia Vietnam Vietnam Thailand"],
                  "output": "5"}])
    # '''
    '''
    multi_testing(
        lab8_3, [{"input": ['10 7 8 9 12 13 15 14',
                            'remove 10 remove 7 remove 16 remove 8 remove 12'],
                  "output": "51"},
                 {"input": ['5 10 15 20 25 30 35 40 40',
                            'remove 3 remove 5 remove 7 remove 10 remove 15 remove 17 remove 25'],
                 "output": "125"},
                 {"input": ['1 7 21 6 1 9 1 7 6 22',
                            'remove 3 remove 2 remove 22 remove 6 remove 1'],
                 "output": "37"}])
    # '''
