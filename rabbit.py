class Rabbit:
    age = 0    
    def __init__(self, name):
        self.name = name
        self.__age = 0
        print("Создание объекта")

    @property
    def age(self):
        return self.__age + 1

    @age.setter
    def age(self, age):
        if isinstance(age,(int, float)) and age in range(0, 10):
            self.__age = age
        else:
            print("Не правильно указан возраст")

    def increase_age(self):
        self.__age = self.__age + 1

    def __str__(self):
        return f"name:{self.name}, age: {self.__age}" + """
        
                              .=""--._
                 __..._    ,="_`/.--""
            ..-""__...._"""       `^"\
          .'  ,/_,.__.- _,       _  .`.
        .'       _.' .-';       /_\ \o|_
      .'       -" .-'  /        `o' /   \,-
      `"""""----""    (        `.--'`---'='
                       `..     .'.`-..-/`\
                          `";`7 'j`"--'
                          _.| |  |
                       .-'    ;  `.
                    .-'  .-   :`   ;
                 .-'_.._7___ _7   ;|.---.
                (           `"\  /--..r=`)
                 \__..--"7'`. ,`7     `}\'
       __.    .-"       /    J/}/
   .-""   \.-"        .'     `;
  :      .'         .'       ;
  ;     /          :         |       .-._
  `.   :           |         ;-.    /`. `/
    `--|           ;        /   \  ;`. ` :
      _;           ;      .'     : :  .-':
    .' \          ;  _.--'       :/ .'  /
    |  ,__     .-'"""""--.       7 /   /
    :    \`""""           `.    ' /   /
     :    J__..._           `.   ;  .'
      \    -. `-.\            `,J.-'
       `._   `._.'                   
          `""""
          """
     

if __name__ == "__main__":
    rabbit1 = Rabbit("Nemo")
    #rabbit1.age = 10
    rabbit1.increase_age()
    print(rabbit1.name, rabbit1.age) 

    rabbit2 = Rabbit("Dori") 
    #rabbit2.age = 2
    rabbit2.increase_age()
    print(rabbit2.name, rabbit2.age)

    rabbit.age = 13
    rabbit.age = "Test"

    print(rabbit2)