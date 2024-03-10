#programa que me recuerda como funciona la programacion orientada a objetos
class Pokemon: #se define la clase
  def __init__(self,entry,name,types,description,id_caugth): #se define el metodo constructor
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.id_caugth=id_caugth
  

  def speak(self): #se define un metodo para que el pokemon hable
    print(self.name) 

  def display_details(self): #se define un metodo para que el pokemon muestre sus detalles
    print(f"Entry Number: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Type: {self.types}")
    print(f"Description: {self.description}")
    print(f"{self.name} has already been caugth!")  


# Pokemon 1
pikachu = Pokemon(25, 'Pikachu', 'Electric', 'A popular and beloved electric rodent Pokemon.', '001')
pikachu.name = 'Pikachuuuuu'  # Cambiar el nombre de Pikachu esto sirve para cambiar un atributo de la clase

# Pokemon 2
charmander = Pokemon(4, 'Charmander', 'Fire', 'A fire Pokemon that is rare to catch in the wild.', '002')

# Pokemon 3
squirtle = Pokemon(7, 'Squirtle', 'Water', 'A water Pokemon known for its defensive moves and speed.', '003')

#Usando metodos creados
pikachu.speak()
charmander.speak()
squirtle.speak()

pikachu.display_details()
squirtle.display_details()
charmander.display_details()
