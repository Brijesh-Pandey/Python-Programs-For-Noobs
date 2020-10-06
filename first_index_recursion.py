string=input()
char_to_check=input()
def first_index(string,char,si):
    z=0
    if len(string)==0 or si==len(string):
        return -1
    if string[si]==char:
        z=1
    if z:
        return si
    else:
        return 0+first_index(string,char,si+1)
print(first_index(string,char_to_check,0))