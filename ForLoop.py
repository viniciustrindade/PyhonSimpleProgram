#!/usr/bin/env python
# -*- coding: utf-8 -*-
print " ==========================================================\n"
print " ======================= Exercises ========================\n"
print " ==========================================================\n"

print "\n LabII: Usando \"For\"\n ==========================================================\n"
soma = 0
for i in range(0,5):
	print "oi"
for i in range(1,7):
	for j in range(1,4):
		soma += 1
		if (soma == 18):
			print str(soma)
			#print str(soma) + "(" + str(i) + "*" +  str(j) + ")."
			break
print "\n LabIII: Usando Arrays\n ==========================================================\n"
vetorInteiro = [None] * 5
index = 0

while (index < 5):
	vetorInteiro[index] = 10 + index
	index += 1

for item in vetorInteiro:
	print item	
vetorString = ["Zé","João","Tonho"]

for item in vetorString:
	print item	

vetorString[0] = "Maria"

for item in vetorString:
	print item	

print "\n LabIV: Usando If\n ==========================================================\n"
#quente=40; frio=10; atual=None
#atual = input("Qual a temperatura atual?")
#print "A temperatura atual é de %s graus celsius" %atual
#if (atual == frio):
#	print "FRIO"
#elif (atual == quente):
#	print "Quente"
#elif (atual > frio and atual < quente):
#	print "Normal"
#else:
#	print "Temperatura Extrema"

print "\n LabIV: Definindo e Usano Métodos em Python \n ==========================================================\n"		
class MetodoClass:
	def welcome(self):
		print "Seja Bem Vindo !!!"
	def __addTwo(self,i):
		return i+2
	def main(self):
		self.welcome()
		variavel = 3
		print "addTwo(%s) é %s " %(str(variavel),self.__addTwo(variavel))
		variavel = 19
		print "addTwo(%s) é %s " %(str(variavel),self.__addTwo(variavel))
MetodoClass().main()