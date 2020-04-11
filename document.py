class Document:
    def __init__(self, type):
        self.type = type
        self.__size = 7
        print("Создание объекта")

    @property
    def size(self):
        return self.__size  

    @size.setter
    def size(self, size):
        if isinstance(size,(int,float)) and size >= 0 and size <= 10: 
           self.__size = size 
        else:
            print("Не правильно указан размер")      

    def increase_size(self):
        self.__size = self.__size + 1

    def __str__(self):
        return f"type: {self.type}, size: {self.__size}" + """    
      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\      
 //________.|.________\\     
`----------`-'----------'
   """
if __name__ == "__main__":
    document1 = Document("Accounting")
    # document1.size = 10
    document1.increase_size() 
    print(document1.type, document1.size)

    document2 = Document("Tax")
    # document2.size = 13
    document2.increase_size() 
    print(document2.type, document2.size)

    print(document2)