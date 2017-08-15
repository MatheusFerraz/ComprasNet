#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import xml.etree.ElementTree as etree

def baixar_xml_pregoes(uasg):
	print("Baixando pregões da UASG " + str(uasg) + "...")

	url = "http://compras.dados.gov.br/pregoes/v1/pregoes.xml?co_uasg=" + str(uasg)
	pregoes = urllib2.urlopen(url)
	conteudo_arquivo = pregoes.read()

	print("Download dos pregões da UASG " + str(uasg) + " finalizado.")

	nome_arquivo = "pregoes_" + str(uasg) + ".xml";

	print("Iniciando escrita de arquivo xml com pregões da UASG " + str(uasg) + "...")

	file = open(nome_arquivo,"w")
	file.write(conteudo_arquivo)
	file.close()

	print("Escrita de pregões em xml finalizada.\n")

def tratar_xml_pregoes(uasg):
	nome_arquivo = "pregoes_" + str(uasg) + ".xml"
	arvore = etree.parse(nome_arquivo)

	array_objeto_pregao = []
	array_co_portaria = []
	array_dt_portaria = []
	array_co_processo = []
	array_ds_tipo_pregao = []
	array_ds_tipo_pregao_compra = []
	array_co_uasg = []
	array_dt_data_edital = []
	array_dt_inicio_proposta = []
	array_dt_fim_proposta = []

	print("Iniciando tratamento do xml de pregões da UASG " + str(uasg) + "...")

	for co_portaria in arvore.findall('.//resource/co_portaria'):
		array_co_portaria.append(co_portaria.text)

	for dt_portaria in arvore.findall('.//resource/dt_portaria'):
		array_dt_portaria.append(dt_portaria.text)

	for co_processo in arvore.findall('.//resource/co_processo'):
		array_co_processo.append(co_processo.text)

	for ds_tipo_pregao in arvore.findall('.//resource/ds_tipo_pregao'):
		array_ds_tipo_pregao.append(ds_tipo_pregao.text)

	for ds_tipo_pregao_compra in arvore.findall('.//resource/ds_tipo_pregao_compra'):
		array_ds_tipo_pregao_compra.append(ds_tipo_pregao_compra.text)

	for objeto in arvore.findall('.//resource/tx_objeto'):
		array_objeto_pregao.append(objeto.text)

	for co_uasg in arvore.findall('.//resource/co_uasg'):
		array_co_uasg.append(co_uasg.text)

	for dt_data_edital in arvore.findall('.//resource/dt_data_edital'):
		array_dt_data_edital.append(dt_data_edital.text)

	for dt_inicio_proposta in arvore.findall('.//resource/dt_inicio_proposta'):
		array_dt_inicio_proposta.append(dt_inicio_proposta.text)

	for dt_fim_proposta in arvore.findall('.//resource/dt_fim_proposta'):
		array_dt_fim_proposta.append(dt_fim_proposta.text)

	print("Tratamento finalizado. Iniciando escrita das informações dos pregões das UASG " + str(uasg) + " em arquivo csv...")

	tam_array = len(array_objeto_pregao)
	nome_arquivo_pregoes = "pregoes_" + str(uasg) + ".csv"

	file = open(nome_arquivo_pregoes, "w")

	file.write("CO_PORTARIA|DT_PORTARIA|CO_PROCESSO|DS_TIPO_PREGAO|DS_TIPO_PREGAO_COMPRA|TX_OBJETO|CO_UASG|DT_DATA_EDITAL|DT_INICIO_PROPOSTA|DT_FIM_PROPOSTA|")
	file.write("\n")

	for item in range(0, tam_array - 1):
		file.write(array_co_portaria[item].encode("UTF-8") + "|" + array_dt_portaria[item].encode("UTF-8") + 
			"|" + array_co_processo[item].encode("UTF-8") + "|" + array_ds_tipo_pregao[item].encode("UTF-8") + 
			"|" + array_ds_tipo_pregao_compra[item].encode("UTF-8") + "|" + array_objeto_pregao[item].encode("UTF-8") + 
			"|" + array_co_uasg[item].encode("UTF-8") + "|" + array_dt_data_edital[item].encode("UTF-8") + "|" + 
			array_dt_inicio_proposta[item].encode("UTF-8") + "|" + array_dt_fim_proposta[item].encode("UTF-8"))
		file.write("\n")

	file.close()

	print("Escrita finalizada.\n")

#------------------------------------------------------------------------------------------------------

array_uasg_df = [926245, 974004]

tam_array_uasg = len(array_uasg_df)

for i in range(0, tam_array_uasg):
	baixar_xml_pregoes(array_uasg_df[i])

for j in range(0, tam_array_uasg):
	tratar_xml_pregoes(array_uasg_df[j])