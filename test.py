def change_list(L):
    L[0] = 3
    return L

def main():
    L = [1, 2, 3, 4]
    L2 = change_list(L)
    print(L)
    print(L2)

if __name__ == '__main__':
    main()
