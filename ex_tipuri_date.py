# #int, str, float, bool
#
# v_1 = 7
# print(type(v_1))
#
# v_2 = 10.5
# print(type(v_2))
#
# v_3 = """ Ion
# Maria
# """
# print(v_3)
# print(type(v_3))

# v_4 = False
# print(type(v_4))
#Pentru a comenta cod ce nu vrem sa se execute, selectam liniile si apasam Ctrl+/

v_5 = 6 > 8
#v_5 a stocat evaluarea bool a acestei expresii, si anume False
print(v_5)
print(type(v_5))

num_1 = 15
num_2 = 5 + 10
v_6 = num_1 == num_2
#(sau) v_6 = 15 == num_2
#== inseamna verificarea/evaluarea egalitatii a doua variabile sau valori
print(v_6)
print(type(v_6))

#1_num -numele variabilei nu poate incepe cu numar

#conventii (estetic) de denumiri a variabilelor
#ceva_variabila - conventia snake_case
#CevaVariabila - conventia CamelCase
#vom folosi mai tarziu pentru functii si clase.

var_x = 1
var_x = "unu"
print(var_x)
#valoarea variabilei s-a schimbat, DAR s-a schimbat si tipul ei
#adica din type int in type str
#in alte limbaje de programare, tipul variabilei este mult mai stabil
#dynamically typed - este mult mai flexibil cu tipul variabilelor

#In alte limbaje de programare trebuie sa definim clar tipul variabilelor
#de exemplu Rust: let variable String = String::from("Hello") , echivalent cu variable = "Hello" in python


#type hints, verificam tipul de date in python, pentru o mai buna securitate a codului

num_1 = 5
num_2 :int = 5 #type hint ca num_2 este int
num_3 :str = 5 #type hint nu este restrictie
print(num_1, num_2, num_3) #toate vor fi printate

print(type(num_3)) #va printa int, nu str

#Trebuie sa evitam denumirea variabilelor cu cuvinte cheie
andx = 7
print(andx)




