def main():
    i=0
    with open("/root/workspace/github.com/FrankJKolski/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    textfile= file_contents.split()
    for string in textfile:
        i=i+1
    print(i)

    filelower= file_contents.lower()
    charcount= {}
    for char in filelower:
        if char.isalpha():
            if char in charcount:
                charcount[char]+=1
            else: 
                charcount[char]=1
    print(charcount)
main()