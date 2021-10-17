small_chars = [chr(item) for item in range(ord('a'), ord('z')+1)]
upper_chars = [item.upper() for item in small_chars]

def encode_chr(chr_item, is_upper_case):
    '''
    Cipher each chr_item.
    '''
    # setting orig and end order.
    if is_upper_case:
        orig_ord = ord('A')
        end_ord  = ord('Z')
    else:
        orig_ord = ord('a')
        end_ord  = ord('z')
    # calculating shift    
    temp_ord = ord(chr_item)+shift
    # calculating offset order with modulo.
    # char is after end_ord, calculating offset
    num_of_chars = 26
    offset_ord = (temp_ord - end_ord - 1)%num_of_chars
    return chr(orig_ord + offset_ord)

# enable while loop to repeat until status not 'y'
status = 'y'
while status == 'y':
    # enter word to cipher.
    word = raw_input("Word: ")
    # enter char shift
    shift = input("Shift: ")
    # create cipher list variable
    cipher = list()
    # loop trough each char in word
    for chr_item in word:
        # encode just letters.
        # replace non-alfa with underscore: "_"
        if chr_item in upper_chars or chr_item in small_chars:
            # set is_uppser_case to True for upper case chars.
            is_upper_case = (chr_item in upper_chars) and True
            # cipher char.
            temp_chr = encode_chr(chr_item, is_upper_case)
            # append ciphered char to list
            cipher.append(temp_chr)
        elif chr_item is ' ':
            cipher.append(chr_item)
        else:
            cipher.append('_')
    # print word
    print(word)
    # print ciphered word
    print(cipher)
    # repeat again for another word?
    status = raw_input("Repeat? [y|n]: ")