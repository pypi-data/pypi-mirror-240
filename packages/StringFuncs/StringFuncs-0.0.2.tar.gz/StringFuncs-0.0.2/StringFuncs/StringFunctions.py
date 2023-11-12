class string_funcs:
    def Length_Of_Last_Word(s, separator):
        string = " ".join((s.replace(separator, " ")).split())
        lastspace=-1
        for indexvalue in range(len((string))):
            if string[indexvalue] == " ":
                lastspace =indexvalue
        return len(string) - (lastspace+1)
    def Length_Of_First_Word(s, separator):
        string = " ".join((s.replace(separator, " ")).split())
        iterations=0
        while string[iterations]!=" ":
             iterations+=1
        return iterations
if __name__ == "__main__":
       print()
