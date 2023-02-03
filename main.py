def main():
    ##################################################
    # Comlete your code here
    ##################################################
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    total = val1+val2+val3
    avg = total/3
    print('Values: {0} {1} {2}'.format(val1, val2, val3))
    print('Total: {0:10d}'.format(total))
    print('Average: {:.2f}'.format(avg))
    pass


if __name__ == '__main__':
    main()
