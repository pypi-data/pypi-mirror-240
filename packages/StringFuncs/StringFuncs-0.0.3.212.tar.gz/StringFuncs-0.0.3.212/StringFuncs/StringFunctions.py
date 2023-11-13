
class string_funcs:
    def Len_Last_Word(s, separator):
        """Replaces separator with spaces and gets rid of unnecessary whitespace
           Returns the length of the last word in a string as a int
           Ex. print(StringFunctions.string_funcs.Len_Of_Last_Word("....This.Is.A.Example....","."))

           Output:
           7 
        """
        string = " ".join((s.replace(separator, " ")).split())
        lastspace=-1
        for indexvalue in range(len((string))):
            if string[indexvalue] == " ":
                lastspace =indexvalue
        return len(string) - (lastspace+1)
    def Len_First_Word(s, separator):
        """Replaces separator with spaces and gets rid of unnecessary whitespace 
           Returns the length of the First Word in a string as a int 
           Ex. print(StringFunctions.string_funcs.Len_Of_Last_Word("This is a Example"," "))

           Output:
           4
        """

        string = " ".join((s.replace(separator, " ")).split())
        iterations=0
        while string[iterations]!=" ":
             iterations+=1
        return iterations
    def Get_First_Word(s, separator):
        """Replaces separator with spaces and gets rid of unnecessary whitespace 
           Returns the first  word in a sequence 
           Ex. print(StringFunctions.string_funcs.Get_First_Word("This is a Example"," "))

           Output:
           This
        """
        string = " ".join((s.replace(separator, " ")).split())
        output = ""
        iterations=0
        while string[iterations]!=" ":
             output+=string[iterations]
             iterations+=1
        return output
if __name__ == "__main__":
    s= "              Hey___________huys                                     "
    sep= "_"
    print(len(" ".join((s.replace(sep, " ")).split())))
    print(string_funcs.Len_Last_Word("hey this is samt", "="))
