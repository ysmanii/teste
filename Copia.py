# Exibir opções
    for opcao in pergunta_atual["opções"]:
        btn_opcao = tk.Button(root, text=opcao, font=("Arial", 14),
                              command=lambda opcao=opcao: verificar_resposta(opcao))
        btn_opcao.pack(fill="x", padx=20, pady=5)


 btn_reiniciar = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=reiniciar_quiz)
    btn_reiniciar.pack(pady=10)

    btn_sair = tk.Button(root, text="Sair", font=("Arial", 14), command=sair_quiz)
    btn_sair.pack(pady=10)