from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyttsx3
import speech_recognition as sr

# Configurar o webdriver para o Microsoft Edge
driver_path = './msedgedriver.exe'
service = EdgeService(executable_path=driver_path)
options = webdriver.EdgeOptions()
options.add_argument("user-data-dir=C:/Users/dupla/AppData/Local/Microsoft/Edge/User Data/Selenium")  # Caminho para um perfil do navegador separado

# Configurações para evitar a detecção de automação
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Edge(service=service, options=options)

# Configurar pyttsx3 para síntese de voz
engine = pyttsx3.init()

# Ajustar a taxa de fala (palavras por minuto) para um ritmo mais natural
engine.setProperty('rate', 150)  

# Ajustar o volume da fala (entre 0.0 e 1.0)
engine.setProperty('volume', 1.0)

def speak(text):
    # Dividir o texto em frases para ajustar a entonação
    sentences = text.split('. ')
    for sentence in sentences:
        # Definir diferentes propriedades para cada frase para simular emoção
        if "!" in sentence:
            engine.setProperty('rate', 170)
            engine.setProperty('volume', 1.0)
        elif "?" in sentence:
            engine.setProperty('rate', 160)
            engine.setProperty('volume', 0.9)
        else:
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.8)
        engine.say(sentence)
    engine.runAndWait()

# Configurar reconhecimento de voz
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen():
    with microphone as source:
        print("Estou ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Reconhecendo...")
        query = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Usuário: {query}")
        print("Pensando...")
        return query
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        speak("Desculpe, não entendi.")
        return None
    except sr.RequestError as e:
        print(f"Erro de requisição; {e}")
        speak("Desculpe, houve um erro de requisição.")
        return None

# Função para interagir com o ChatGPT via scraping
def ask_chatgpt(question):
    try:
        # Verifique se a caixa de texto está presente
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea'))
        )
        input_box = browser.find_element(By.CSS_SELECTOR, 'textarea')
        
        # Limpe a caixa de texto antes de enviar a pergunta
        input_box.clear()
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        # Aguarde até que o indicador de digitação apareça
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="result-streaming"]'))
        )


        # Aguarde até que o indicador de digitação desapareça
        WebDriverWait(browser, 60).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="result-streaming"]'))
        )

        # Obtenha a resposta final
        response_elements = browser.find_elements(By.CSS_SELECTOR, 'div.markdown')
        if response_elements:
            response_text = response_elements[-1].text
            print(f"SpeakGPT: {response_text}")
            speak(response_text)
            save_history(question, response_text)
            return response_text
        else:
            return "Não foi possível obter a resposta do ChatGPT."
    except Exception as e:
        print(f"Erro ao encontrar o elemento: {e}")
        return "Não foi possível obter a resposta do ChatGPT."

# Função para salvar o histórico em um arquivo
def save_history(question, answer):
    with open('chatgpt_history.txt', 'a', encoding='utf-8') as file:
        file.write(f"(Usuário): {question}\n")
        file.write(f"(SpeakGPT): {answer}\n")
        file.write("\n")

# Função principal para simular a interação
def main():
    # Abrir a página do ChatGPT uma vez
    browser.get('https://chatgpt.com/?oai-dm=1&temporary-chat=true')
    print("Olá! Pergunte-me qualquer coisa.")
    speak("Olá! Pergunte-me qualquer coisa.")
    
    while True:
        question = listen()
        if question is None:
            continue
        if question.lower() in ["sair", "exit", "quit"]:
            break
        ask_chatgpt(question)

if __name__ == "__main__":
    main()

# Feche o navegador quando terminar
browser.quit()
