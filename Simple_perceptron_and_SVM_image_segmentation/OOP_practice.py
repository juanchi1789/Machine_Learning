# Objet oriented programming

# clases
# instanses
# functions
# inheritance
# Encaptulation
# Properties


# 4 principles of Objet Oriented Programming
# 1) inheritance
# 2) Polymorphism
# 3) Encaptulation
# 4) Abastraction

# <------------------------------------------------------> create a class , create instance , create

# Why do we need clases ??
# --> The clases can represent more complex data
# structures and can contain functions that express the dinamic of the data

# class
class SoftwareEngineer_1:

    alias = "Keyboard Magician" # Class atributes ==> Siempre es la misma por cada instance


    def __init__(self,name,age,level,salary): # Siempre (Lo siguiente es muy importante) # Instance atributes
        # Instance atributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary # todos estos son parametros que pasamos desde afuera
        # y ademas estos parametros se usan dentro de la clase

    #pass # no hace nada


# Instanses
se1 = SoftwareEngineer_1("Max",20,"Junior",5000)
print(se1.name,se1.age,se1.level,se1.salary)
print(se1.alias) # Como podemos ver es la misma para cada instancia
print(SoftwareEngineer_1.alias)

# <------------------------------------------------------> Functions in clasess

class SoftwareEngineer:

    alias = "Keyboard Magician" # Class atributes ==> Siempre es la misma por cada instance

    def __init__(self,name,age,level,salary): # Siempre (Lo siguiente es muy importante) # Instance atributes
        # Instance atributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary # todos estos son parametros que pasamos desde afuera
        # y ademas estos parametros se usan dentro de la clase

    def code(self): # Instance Method! # El self se refiere a la instancia Como podemos ver ahi
                    # cuando le pedimos el numbre
        print(f"{self.name} is writing code ...")

    def code_lenguge(self, language):
        print(f"{self.name} is writing code in {language} ...")

    #def information(self):
     #   information = f"Name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}"
      #  return information

    # Metodos Especiales que ya estan dentro de Python !
    def __str__(self): # Es lo mismo que la funcion anterior pero ahora es algo proio de la clase
        information = f"Name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}"
        return information

    def __eq__(self, other):# Comparar 2 objetos
        return self.name == other.name and self.age == other.age and self.level == other.level and self.salary == other.salary
    # otras funciones
    @staticmethod # aca adentro no puedo usar SELF (Esto se usa cuando hay un metodo que no esta unido a una isntancia en particular)
    def entry_salary(age): # se puede atribuir a una instancia o a todas
        if age < 25:
            return 5000
        if age < 25:
            return 7000




se1 = SoftwareEngineer("Max",20,"Junior",5000)
se2 = SoftwareEngineer("Janny",24,"Senior",15000)
se3 = SoftwareEngineer("Janny",24,"Senior",15000)

se1.code()
se1.code_lenguge("Python")
#print(se1.information())

print(se2 == se3) # esto nos da FALSE porque esta comparando las posiciones en la memoria
                  # Cuando implementemos __eq__ nos da True ==> porque esta comparando todo lo que yo le pedi que compare

print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
