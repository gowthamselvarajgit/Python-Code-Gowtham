def echo_maker(text):
    return text + " " + text

def title_caser(text):
    return text.title()
    
input_text = input("Enter the Value: ")
output = title_caser(echo_maker(input_text))
print(output)