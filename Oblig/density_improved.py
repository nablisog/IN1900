
file = "densities.txt"
def density(file):
     with open(file,"r") as infile:
          densities={}
          for line in infile:
               words = line.split()
               word = float(words[-1])
               substance = " ".join(words[:-1])
               densities[substance]  = word
     return densities


file = "densities.txt"             
def density_values(file):
     with open(file,"r") as infile:
          densities={}
          for line in infile:
               words = line.split()
               word = float(words[-1])
               substance = line[:12]
               substance = substance.strip()
               densities[substance] = word
     return densities

print(density(file) == density_values(file))


def density_test():
     file = "densities.txt"
     caller_1 = density(file)
     caller_2 = density_values(file)
     if caller_1 == caller_2:
          success = True
     else:
          False
     msg = "Message shown if test fails"
     assert success, msg
     
density_test()    


             
                            
               
