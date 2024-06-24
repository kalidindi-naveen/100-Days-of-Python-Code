'''
Espresso -- 50 water,18 coffe, 1.50 $
Latte -- 200 water, 24 coffe, 150 milk, 2.50 $
Cappuccino -- 250 water, 24 coffe, 100 milk, 3.00 $
Resources -- 300 water, 200 milk, 100 coffe
'''
data = {
  "milk":200,
  "water":300,
  "coffe": 100,
}

menu = {
  "espresso" : {
    "ingredients": {
      "water" : 50,
      "coffe" : 18
    },
    "cost" : 1.50
  },
  "latte" : {
    "ingredients": {
      "water" : 200,
      "coffe" : 24,
      "milk" : 150
    },
    "cost" : 2.5
  },
  "cappuccino" : {
    "ingredients": {
      "water" : 250,
      "coffe" : 24,
      "milk" : 100
    },
    "cost" : 3
  }
}