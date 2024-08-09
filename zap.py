import pywhatkit as kit
from datetime import datetime

def enviar_mensagem_whatsapp(numero, mensagem):
    # Envia a mensagem para o número fornecido com o formato correto (código do país + número)
    kit.sendwhatmsg_instantly(f"+{numero}", mensagem)

# Exemplo de uso:
if __name__ == "__main__":
    numero = "5511999999999"  # Substitua pelo número de WhatsApp com código do país
    mensagem = "Olá, aqui estão os detalhes da sua ficha..."
    enviar_mensagem_whatsapp(numero, mensagem)
