# -*- coding: utf-8 -*-
"""random_consuelo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cDwPy5m2UUcAVBz6HDAle6nE1l6Ywho4
"""

def consuel(*args):
  import random 
  var=args[0]
  opts=args[0]
  par1 = random.choice(["no te preocupes, ", "Me da gusto que lo intentes,", " "])
  par2 = random.choice(["sigue adelante", "lucha" , "termina ", "Continua" , "animo" , "no te rindas" , "fuerza", "adelante", "ten fe"])
  par3 = random.choice(["posiblemente es una situación dificil","posiblemente solo fue un día malo", "posiblemente sea algo dificil"])
  par4 = random.choice(["La proxima saldrás ganando", "tenemos el partido ganado", "Tal vez un poco de agua en la frente y recostarte te haga sentir mejor", "Cuando empiezes a pensar que las cosas van mal siempre es bueno concentra en otra cosa", "muchos renacen cuando las cosas van mal", "puedes hacer los cambios que tu decidas", "avanza al paso que puedas"])
  par5 = random.choice(["pero", "Sin embargo"])
  par6 = random.choice(["sin ello nunca ", "seguro"])
  par7 = random.choice(["siempre podrás encontrar un lugar seguro ", "yo confio en tí", "es parte del proceso", "es parte del camino", "lo mejor es seguir intentando"])
  par8 = random.choice(["una mejor persona", "una persona muy especial", "más fuerte", "mas grande"])
  par9 = random.choice(["eres una gran persona" ])
  par10 = random.choice(["se que tienes la fuerza para ser mejor", "no te rindas"])
  par11 = random.choice(["Te prometo que te estaré apoyando.", " yo te apoyo.", "no estás solo."])
                    
  consu = random.choice([(par1 , par2 , par3 , par5 ,"seras", par8, "despues de esto") , (par1 , par2 , par4 , par7 , par9) , (par1 , par9 , par10) , (par1 , par2 , par7 ,  par9 , par11), (par1 , par2) , (par1 , par10) , (par1 , par11) , (par1 , par2 , par4) , (par1 , par4 , par7) , (par1 , par2 , par10) , ( par1 , par2 , par11) , (par2 , par1 , par4) , (par4 , par1 , par7), (par2 , par1 , par10), (par2 , par11 , par1) , ( par4 , par1 , par2) , (par7 , par1, par4) ,(par10, par1, par2), (par11, par1, par2), (par1) , (par2) , (par4) , (par7) , (par10) , (par11)])  
  return 'set_slot {0} "{1}"'.format(var,consu)