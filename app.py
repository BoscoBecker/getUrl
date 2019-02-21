import requests 
import re
import time
import os
clear = lambda: os.system('clear')
clear()
# iniciando programa
print '                                                              '
print '..............................................................'
print '..............................................................'
print '              inicializando modulos requests                  '
print '                                                              '
print '..............................................................'
print '               Powered By @boscoBecker - 2019                 '
print '..............................................................'
print '..............................................................'
print '                                                              '

#coding: utf-8
print 'Importando requests.'
time.sleep(1)

print 'Importando requests..'
time.sleep(1)

print 'Importando requests...'
time.sleep(1)
print '                                                              '
print 'Importando time.'
time.sleep(1)

print 'Importando time..'
time.sleep(1)

print 'Importando time...'
time.sleep(1)
print '                                                              '
print 'Importando re.'
time.sleep(1)

print 'Importando re..'
time.sleep(1)

print 'Importando re...'
time.sleep(1)
print '                                                              '
url = raw_input("Informe uma URL valida: ") 
print 'Inicializando Get da pagina ...'
responde  = requests.get(url)
print 'Realizado get da url: "'+responde.url+'" .... '
print 'Retornando o codigo de status ...'

# retornando Status Codes basicos, 
def statusCode(codigo):
    if  codigo == '100':
     return 'Continue'        
    if codigo == '200':    
      return 'OK'  
    if  codigo == '201':
     return 'Created - Criado'        
    if  codigo == '400':
        return 'Bad Rquest - Requisicao ruim'
    if  codigo == '403':
        return 'Forbidden - Proibido'
    if  codigo == '404':
        return 'Page not found - pagina nao encontrada'        
    if  codigo == '300':
     return 'multiplas escolhas' 

# verificando se a URL e valida
def verificarUrl(url):
    if re.search("http:\\", url, re.IGNORECASE) and re.search("https:\\", url, re.IGNORECASE):  
        return true    
    else:
        return false

print 'Codigo de Status: '+str(statusCode(str(responde.status_code)))
print '                                                              '
content = ''
content = raw_input("Deseja visualizar o conteudo da requisicao ?  *Minusculo (s)/(n) ? ") 
print(content)
if content == 's':
  print 'Conteudo da Pagina '+str(responde.content)
if content == 'n':  
  print 'Download da pagina nao realizado '
print '                                                              '


