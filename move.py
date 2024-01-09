import PyPDF2
from searchMove import buscarTextoPaginas
import re


# Exemplo de uso
def catchMove(texto_procurado):
  caminho_do_pdf = "pokemon-livro-do-jogador-biblioteca-elfica.pdf"
  if texto_procurado == "Explosão":
      texto_procurado = "Explosão 7" 
  pagina = buscarTextoPaginas(caminho_do_pdf,texto_procurado)
  
  
  pagina = re.sub(r'^\s*$', '\nEND\n', pagina, flags=re.MULTILINE)
  
  
  index =pagina.index(texto_procurado)
  
  
  end = False
  
  move = ''
  
  while( not end):
      if (pagina[index] == 'E' and pagina[index+1] == 'N' and pagina[index+2] == 'D' ):
          end = True
      else:
          move+=(pagina[index])
  
      index+=1
  
  move = re.sub('EOF', '', move)
  
  for i in range(198,249):
      if str(i) in move:
          move = re.sub(str(i), '', move)
          break
  
  return move