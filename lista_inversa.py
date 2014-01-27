def read_list(size):
    '''
    Read a list from keyboard
    '''
    i = 0
    ll = []
    while i < size:
        element = raw_input('Input element: ')
        ll.append(element)
        i += 1
    return ll

def inverse_output(mylist):
    '''
    Prints on screen a list in inverse order
    '''
    i = len(mylist) - 1
    while i >= 0 :
        print "Element %d is %s" %(i,mylist[i])
        i -= 1


def main():
    n = int(raw_input('Size = '))
    ll = read_list(n)
    inverse_output(ll)

main()
