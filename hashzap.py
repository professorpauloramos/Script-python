import flet as ft

# Criar uma função principal para rodar o aplicativo
def main(page):
    # Título
    titulo = ft.Text("hashzap")

    # Variável global para armazenar o nome do usuário
    nome_usuario = None

    # Criação do popup para inserir o nome
    campo_nome = ft.TextField(label="Digite seu nome")
    popup = ft.AlertDialog(title=ft.Text("Bem-vindo ao hashzap"),
        content=campo_nome,
        actions=[
            ft.ElevatedButton("Entrar no chat", on_click=lambda e: fechar_popup(e))
        ],
    )

    # Função para abrir o popup
    def abrir_popup(evento):
        page.overlay.append(popup)  # Associa o popup à página
        popup.open = True  # Abre o popup
        page.update()  # Atualiza a página para mostrar o popup

    # Função para fechar o popup e capturar o nome do usuário
    def fechar_popup(evento):
        nonlocal nome_usuario
        nome_usuario = campo_nome.value.strip()  # Captura o valor do campo de texto
        if nome_usuario:  # Verifica se o nome foi digitado
            popup.open = False  # Fecha o popup
            
            # Mensagem de entrada do usuário no chat
            texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
            page.add(texto_mensagem)
            iniciar_chat()  # Inicializa o chat após o nome do usuário ser definido
            page.update()  # Atualiza a página para refletir o fechamento

    # Função para iniciar o chat após o nome ser definido
    def iniciar_chat():
        campo_mensagem = ft.TextField(label="Digite sua mensagem", expand=True)
        chat_area = ft.Column([], expand=True)
        botao_enviar = ft.ElevatedButton(
            "Enviar", 
            on_click=lambda e: enviar_mensagem(campo_mensagem)
        )

        # Função para enviar mensagem
        def enviar_mensagem(campo_mensagem):
            mensagem = campo_mensagem.value
            if mensagem.strip():
                chat_area.controls.append(ft.Text(f"{nome_usuario}: {mensagem}"))  # Adiciona a mensagem no chat
                campo_mensagem.value = ""  # Limpa a caixa de mensagem
                page.update()

        # Criação da linha de envio
        linha_enviar = ft.Row([campo_mensagem, botao_enviar])

        # Adiciona o chat e o campo de envio à página
        page.add(chat_area)
        page.add(linha_enviar)
        page.update()

    # Botão inicial
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Adiciona os elementos à página
    page.add(titulo)
    page.add(botao)

# Inicializa o app Flet
ft.app(target=main)