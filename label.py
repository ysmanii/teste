indice_pergunta = 0
pontuacao = 0

def verificar_resposta(resposta):
    global indice_pergunta, pontuacao
    if resposta == perguntas[indice_pergunta]["resposta"]:
        pontuacao += 1
    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        mostrar_pergunta()
    else:
        finalizar_quiz()

# Função para mostrar a pergunta
def mostrar_pergunta():
    global indice_pergunta
    pergunta_atual = perguntas[indice_pergunta]

    # Limpar a janela
    for widget in root.winfo_children():
        widget.destroy()

    # Exibir pergunta
    lbl_pergunta = tk.Label(root, text=pergunta_atual["pergunta"], font=("Arial", 16))
    lbl_pergunta.pack(pady=20)

    # Exibir opções
    for opcao in pergunta_atual["opções"]:
        btn_opcao = tk.Button(root, text=opcao, font=("Arial", 14),
                              command=lambda opcao=opcao: verificar_resposta(opcao))
        btn_opcao.pack(fill="x", padx=20, pady=5)

# Função para finalizar o quiz e exibir a pontuação
def finalizar_quiz():
    for widget in root.winfo_children():
        widget.destroy()

    # Mensagem final e opções de reiniciar ou sair
    lbl_resultado = tk.Label(root, text=f"Sua pontuação: {pontuacao} de {len(perguntas)}", font=("Arial", 16))
    lbl_resultado.pack(pady=20)

    btn_reiniciar = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=reiniciar_quiz)
    btn_reiniciar.pack(pady=10)

    btn_sair = tk.Button(root, text="Sair", font=("Arial", 14), command=sair_quiz)
    btn_sair.pack(pady=10)

# Função para reiniciar o quiz
def reiniciar_quiz():
    global indice_pergunta, pontuacao
    indice_pergunta = 0
    pontuacao = 0
    mostrar_pergunta()


# Iniciar o quiz com a primeira pergunta
mostrar_pergunta()

root.mainloop()