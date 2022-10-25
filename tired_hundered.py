First_number=int(input())
Second_number=int(input())
First_number_string,Second_number_string=str(First_number),str(Second_number)
size_First,size_Second=len(First_number_string),len(Second_number_string)
reverse_First_number,reverse_Second_number=First_number_string[size_First::-1],Second_number_string[size_Second::-1]

if reverse_First_number==reverse_Second_number:print(First_number," = ",Second_number)
elif min(reverse_First_number,reverse_Second_number)==reverse_Second_number:
    print(Second_number," < ",First_number)
else:print(First_number," < ",Second_number)
