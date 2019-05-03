from math import pi
class Planet:
     def __init__ (self,name,radius,mass,population):
          self.name=name
          self.radius=radius
          self.mass=mass
          self.population=population

     def density(self):
          volume=(4/3)*pi*self.radius**3
          return volume/self.mass
          
     def print_info(self):
           print(self.name,self.radius,self.mass)
           print(density())

name="Earth"

Planet1=Planet(name,0,0,7497486172)

print(Planet1.name, " has a population of ", Planet1.population)
