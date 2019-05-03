def read_file(file):
     with open (file, "r") as infile:
          line= infile.read().split()
          v= float(line[1])
          t= map(float, line[3:])
          return v,t


def write_file(file,v,t):
     with open(file, "w") as outfile:
          for i in sorted(t):
               outfile.write(i,v*t-0.5*(9.81*(t**2)))







