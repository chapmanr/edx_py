import string
alphabet = " " + string.ascii_lowercase
print(alphabet)

alpha_dict = {}
count = 0
for ch in alphabet:
    alpha_dict[ch]=count
    count = count + 1

print(alpha_dict["n"])

def current_index(msg_char):
    index = alpha_dict[msg_char]
    return index % 27

def get_shifted_char(msg_char, shift=1):
    curr_index = current_index(msg_char)
    curr_index = curr_index + shift
    curr_index = curr_index % 27
    return alphabet[curr_index]

print(get_shifted_char(" "))
print(get_shifted_char("m"))
print(get_shifted_char("z"))
print("complete")


def encode(message, key):
    new_msg=""
    for ch in message:
        new_msg += get_shifted_char(ch, key)
    return new_msg


g_message = "hi my name is caesar"
#ijanzaobnfajtadbftbs
print(encode(g_message, 1))
encoded_message = encode(g_message, 3)
print(encoded_message)
decoded_message = encode(encoded_message, -3)
print(decoded_message)

