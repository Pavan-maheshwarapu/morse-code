# code for text to morse code conversion and vice versa
codes = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '---',
         '.__.', '__._', '._.', '...', '-', '.._', '..._', '.__', '_.._', '_.__', '__..']

def ttm(text):
    # ttm indicates text to morse code conversion function
    # can give any case of letters, [.lower()] will convert it to lower case of letters
    text = text.lower()
    morse_str = ''

    for x in text:
        morse_str += codes[ord(x) - 97] + ' '
        #ord is function to get ASCII code of a string
    print('morse code for entered text is ', morse_str)

def mtt(mcode):
    mcode = mcode.strip().split(' ')
    # splits the morse code of each letter with space given between each morse code of a string
    text = ''

    for code in mcode:
        if code in codes:
            index = codes.index(code)
            text += chr(index + 97)
            #chr function gives string with the ASCII code given

    print('Decoded text:', text)

# can call any function according to the requirement
# for example
ttm('PavAN')
#output is ('.__.', '._', '..._', '._', '_.')

mtt("._ _... _._")
#output is ('abk')
