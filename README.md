# Projeto desenvolvido em Python para fazer requisições HTTP 1.0/1.1 usando bilbioteca Requests

#Requisitos
* Python 2.7
* Biblioteca Requsts
* Biblioteca Time
* Biblioteca os
* Biblioteca re

![Alt Text](https://github.com/{boscobecker}/{getUrl}/raw/{master}/path/to/image.gif)



#funcionamento

1 Basta executar os comandos  "python app.py"

2 informar a URL

3 escolher se deseja visualizar o conteudo HTML ou não 


#Partes do código de verificação de status do request


```python
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

```



#make with Love @boscobecker

