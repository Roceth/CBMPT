# -*- coding: utf-8 -*-
"""random_halagos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QvAfLA5nurt-ZQnhQmEE--shtESXJTtT
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def halag(*args):
  import random 
  var=args[0]
  opts=args[0]

  adje = random.choice(["bien", "atractivo", "curioso", "bueno", "original", "simpático", "agradable", "bonito", "adecuado", "amable", "amistoso", "bonito", "estupendo", "excepcional", "fantástico", "genial", "optimista", "hábil", "positivo", "hermoso", "carísmático", "coherente", "ingenioso", "razonable", "Inteligente", "interesante", "marivilloso"])
  
  adje1 = random.choice(["atractivo", "curioso", "bueno", "original", "simpático", "agradable", "bonito", "adecuado", "amable", "amistoso", "bonito", "estupendo", "excepcional", "fantástico", "genial", "optimista", "hábil", "positivo", "hermoso", "carísmático", "coherente", "ingenioso", "razonable", "Inteligente", "interesante", "marivilloso"])

  verb = random.choice(["suena", "se escucha", "parece"])

  verb1 = random.choice(["es", "suena como algo", "suena", "parece", "se escucha"])

  sust = random.choice(["eso", "lo que dices", "lo que escribes", " "])

  ary = random.choice([("Que", adje , verb , sust) , (sust , verb , adje1) , (verb1 , adje1 , "de tu parte")])

  return 'set_slot {0} "{1}"'.format(var,ary)