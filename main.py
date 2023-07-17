import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Lista para armazenar os filmes
filmes = []

# Função para adicionar um filme à lista
def adicionar_filme():
    nome = entry_nome.get()
    plataforma = entry_plataforma.get()
    genero = entry_genero.get()
    nota = float(entry_nota.get())
    
    filme = {
        "nome": nome,
        "plataforma": plataforma,
        "genero": genero,
        "nota": nota
    }
    
    filmes.append(filme)
    label_status["text"] = "Filme adicionado com sucesso!"
    
    # Limpar os campos de entrada após adicionar um filme
    entry_nome.delete(0, tk.END)
    entry_plataforma.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Função para exibir a lista de filmes em um documento PDF
def exibir_filmes():
    if filmes:
        # Ordenar a lista de filmes em ordem alfabética pelo nome (desconsiderando o artigo inicial)
        filmes_ordenados = sorted(filmes, key=lambda x: x['nome'][4:] if x['nome'].startswith("The ") else x['nome'])
        
        # Criação do documento PDF
        pdf_filename = "lista_filmes.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        data = [['Nome', 'Gênero', 'Plataforma', 'Nota']]
        
        for filme in filmes_ordenados:
            nome = filme['nome']
            genero = filme['genero']
            plataforma = filme['plataforma']
            nota = filme['nota']
            
            # Adicionar os detalhes do filme à tabela
            data.append([nome, genero, plataforma, nota])
        
        # Definir o estilo da tabela
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ])
        
        table = Table(data)
        table.setStyle(table_style)
        
        # Adicionar a tabela ao documento PDF
        elements = [table]
        doc.build(elements)
        
        label_status["text"] = f"Lista de filmes salva em {pdf_filename}"
    else:
        label_status["text"] = "Nenhum filme encontrado."

# Criação da janela principal
window = tk.Tk()
window.title("Gerenciador de Filmes")
window.geometry("400x400")

# Criação dos widgets
label_nome = tk.Label(window, text="Nome do Filme:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(window)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_plataforma = tk.Label(window, text="Plataforma:")
label_plataforma.grid(row=1, column=0, padx=10, pady=10)
entry_plataforma = tk.Entry(window)
entry_plataforma.grid(row=1, column=1, padx=10, pady=10)

label_genero = tk.Label(window, text="Gênero:")
label_genero.grid(row=2, column=0, padx=10, pady=10)
entry_genero = tk.Entry(window)
entry_genero.grid(row=2, column=1, padx=10, pady=10)

label_nota = tk.Label(window, text="Nota (0 a 5):")
label_nota.grid(row=3, column=0, padx=10, pady=10)
entry_nota = tk.Entry(window)
entry_nota.grid(row=3, column=1, padx=10, pady=10)

button_adicionar = tk.Button(window, text="Adicionar Filme", command=adicionar_filme)
button_adicionar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_exibir = tk.Button(window, text="Exibir Filmes", command=exibir_filmes)
button_exibir.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

label_status = tk.Label(window, text="")
label_status.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
