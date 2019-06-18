
import random
from random import seed
from random import randint
from random import sample 
from prettytable import PrettyTable

# <<linea [15] = esto pasa valoresa binario en forma de lista y eteros
# print([int(x) for x in list('{0:0b}'.format(result[1]))])>>


bin_a = []
val_fx = []
pareja = [4,5,6,1,2,3]
posi = []
cruce = [0,0,0,0,0,0]
combi = [0,0,0,0,0]
final = [0,0,0,0,0,0]
nx = []
nfx = []
flag = 0
media = 0
p = "La media es: "
puntoc = []

#Fase 1 llenar la tabla y asignar parejas 
val_x = sample(range(1, 31), 6)
for x in range(6):
    bin_a.append(list('{0:05b}'.format(val_x[x])))
    val_fx.append(val_x[x]**2 )
    posi.append(x+1)
    media = media + val_fx[x]
   

# aca veo que la pareja asignada no sea igual a la posicion 
while flag != 1:
   asig =sample(range(1, 7), 6) 
   #print(f'{asig}')
   for z in range(6): 
      if posi[z] == asig[z]:
           flag = 0
           break
      else:
            flag = 1

#emparejamiento
#print(asig)
#z = 0 
#while z != 6:  
#    print(asig)   
 #   if (pareja[z]== 0):
#        pareja[z] = asig[z]
 #       pareja[asig[z]-1]= z+1
#        print(pareja)   
 #   z = z +1    
          
print("\n Tabla 1.- Seleccion")
t = PrettyTable(['(1)', '(2)', '(3)', '(4)', '(5)'])
for y in range(6):
    t.add_row([posi[y], bin_a[y], val_x[y], val_fx[y], pareja[y]])

print(t)
media = media/6
print(f'{p}{media}')

#Fase 2: hacer el Cruce

for x in range(6):
             
        if cruce[x]== 0:
                #print(pareja[x])
                if val_x[x]>val_x[pareja[x]-1]:
                        if cruce[x] == 0:
                                cruce[x] = bin_a[x]
                                cruce[x+1] = bin_a[x]
                                #print(cruce)
                        else:
                                cruce[x+1] = bin_a[x]
                                cruce[x+2] = bin_a[x]
                                #print(cruce)                               
                else:
                        if cruce[x] == 0:
                                cruce[x] = bin_a[pareja[x-1]]
                                cruce[x+1] = bin_a[pareja[x-1]]
                                #print(cruce) 
                        else:
                                cruce[x+1] = bin_a[pareja[x-1]]
                                cruce[x+2] = bin_a[pareja[x-1]]
                                #print(cruce)
                                 
parejac = [3,4,1,2,6,5]
puntoc = [0,0,0,0,0,0]
for z in range(6):
        if puntoc[z] == 0:
                nr = randint(1,4)
                puntoc[z] = nr        
                puntoc[parejac[z]-1]= nr       
        

print("\n Tabla 2.- Cruce")
u = PrettyTable(['(1)', '(2)', '(3)', '(4)'])
for y in range(6):
    u.add_row([posi[y], cruce[y], parejac[y], puntoc[y]])

print(u)

#Fase 3: Poblacion despues del cruce

res_x = []
res_f = []
str1 = ''

for x in range(6):
        
        for y in range(puntoc[x]):
                
                combi[y] = cruce[x][y]
                #print(combi[y])
                
        for z in range(puntoc[x], 5, 1):
                combi[z] = cruce[parejac[x]-1][z]
                #print(combi[z])   
        final[x]= combi.copy()
        #print(combi)        
        #print('---')
        
#print(final) 

media = 0
#connvierto de binario a numero real   
for z in range(6):
        str1 = "0"
        for c in range(5):
                str1 = str1 + final[z][c]
        nx.append(int(str1, 2))
        nfx.append(int(str1, 2)**2)
        media = int(media + nfx[z])      
        

print("\n Tabla 3.- Poblacion tras el Cruce")
g = PrettyTable(['(1)', '(2)', '(3)', '(4)'])
for y in range(6):
    g.add_row([posi[y], final[y], nx[y], nfx[y]])
print(g)
media = media/6
print(f'{p}{media}')


                                   