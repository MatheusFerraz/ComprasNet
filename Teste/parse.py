#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree

nome_arquivo = 'pregoes.xml'
arvore = etree.parse(nome_arquivo)

array_objetos_pregoes = []

print("Iniciando tratamento do xml de pregões da Câmara Legislativa... \n")

for elemento in arvore.findall('.//resource/tx_objeto'):
	array_objetos_pregoes.append(elemento.text)

print("Tratamento finalizado. Iniciando escrita dos objetos dos pregões em arquivo... \n")

file = open("Objetos.txt", "w")

for item in array_objetos_pregoes:
	file.write(item.encode("UTF-8"))
	file.write("\n\n")

file.close()