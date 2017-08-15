import urllib2
url = "http://compras.dados.gov.br/pregoes/v1/pregoes.xml?co_uasg=974004"
s = urllib2.urlopen(url)
contents = s.read()
file = open("pregoes.xml","w")
file.write(contents)
file.close()