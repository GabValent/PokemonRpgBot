import PyPDF2
import re

def buscarTextoPaginas(pdf_path, texto_procurado):
    with open(pdf_path, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        if texto_procurado=='Investida':
              page = 224
        elif texto_procurado=='Explosão 7':
              page = 218
        else:
            page = acharPagina(leitor_pdf,texto_procurado)
        texto_pagina = ""
        for i in range(page,page+2):
            pagina = leitor_pdf.pages[i]
            texto_pagina += pagina.extract_text()
            texto_pagina += 'EOF'

        return texto_pagina


def acharPagina(leitor_pdf,texto_procurado):
    for num_pagina in range(198, 249):
                pagina = leitor_pdf.pages[num_pagina]
                texto_auxiliar = pagina.extract_text()
                if texto_procurado in texto_auxiliar:
                      return num_pagina




