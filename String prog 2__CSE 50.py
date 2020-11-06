def reverse(str):
    words=str.split(' ')
    r=' '.join(reversed(words))
    return r



str=input("Enter a sentence : ")
r=reverse(str)

print(r)