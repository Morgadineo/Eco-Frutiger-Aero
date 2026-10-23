import random
from googletrans import Translator
import scipy.io.wavfile as wav
import sounddevice as sd
import speech_recognition as sr


def gravar(idioma):
    duration = 3  # segundos de gravação
    sample_rate = 44100
    print("\nFale agora...")

    # CORREÇÃO 1: Sintaxe da multiplicação de amostras
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sd.wait()  # Aguarda o término da gravação

    wav.write("output.wav", sample_rate, recording)
    print("Gravação concluída, processando áudio...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio, language=idioma)
    return text


def traduzir(texto, idioma="en"):
    # CORREÇÃO 2: Uso da variável 'texto' recebida como parâmetro
    # CORREÇÃO 3: Uso do parâmetro 'dest=idioma' em vez de fixar em "en"
    tradutor = Translator()
    traducao = tradutor.translate(texto, dest=idioma).text
    return traducao


words_by_level = {
    "facil": ["gato", "cachorro", "maçã", "leite", "sol"],
    "medio": ["casa", "escola", "amigo", "janela", "amarelo"],
    "dificil": [ "tecnologia", "universidade", "informação", "pronúncia", "imaginação",],
}

print("====================================================")
print("                 SPEAK RIGHT!                       ")
print(" UM JOGO PARA APRENDER E APERFEIÇOAR IDIOMAS        ")
print("====================================================")

pontos = 0

while True:
    dificuldade = input(
        "\nDigite qual dificuldade quer escolher:\n(2 pontos) Facil\n(3 pontos) Medio\n(5 pontos) Dificil\nDigite (ou 'parar' para sair): "
    )

    dificuldade_clean = dificuldade.lower().strip()

    if dificuldade_clean == "facil":
        palavra = random.choice(words_by_level["facil"])
        
    elif dificuldade_clean == "medio":
        palavra = random.choice(words_by_level["medio"])

    elif dificuldade_clean == "dificil":
        palavra = random.choice(words_by_level["dificil"])

    elif dificuldade_clean == "parar":
        print("Encerrando o jogo...")
        break
    else:
        print("Opção inválida! Digite novamente sem acentos.")
        print("--------------------------------------")
        continue

    # === FALA === #
    print(f"\nSua palavra é: **{palavra.upper()}**")

    try:
        text = gravar("pt-BR")
        print(f"Você disse (em Português): {text}")
        print(f"A palavra é: {traduzir(palavra)}")
        if text == traduzir(palavra):
            print(f"Você acertou! A palavra era: {traduzir(palavra)}")
            
            if dificuldade_clean == "facil":
                pontos += 2
            elif dificuldade_clean == "medio":
                pontos += 3
            if dificuldade_clean == "dificil":
                pontos += 5


        if "parar" in text.lower().split():
            print("Você disse 'parar'! Encerrando o programa!")
            break

        # === TRADUZINDO === #
        traducao = traduzir(text, "en")
        print(f"Tradução para o Inglês: {traducao}")

    except sr.UnknownValueError:
        print("A fala não pôde ser reconhecida. Tente falar mais perto do microfone.")
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de voz: {e}")

#=== PONTUAÇÂO ===#
print("Sua pontuação foi:", pontos)
