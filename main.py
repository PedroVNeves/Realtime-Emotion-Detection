import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 1. Carregar o modelo de emoção treinado
try:
    model = load_model('modelo_emocao_ckextended.h5')
    print("Modelo 'modelo_emocao_ckextended.h5' carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    print("Certifique-se de que o arquivo 'modelo_emocao_ckextended.h5' existe no diretório correto.")
    exit() # Encerra o script se o modelo não puder ser carregado

# Mapeamento das emoções (deve ser o mesmo usado no treinamento)
emotion_labels = {0: 'Raiva', 1: 'Desgosto', 2: 'Medo', 3: 'Felicidade', 4: 'Tristeza', 5: 'Surpresa', 6: 'Neutro'}

# 2. Carregar o classificador de detecção facial Haar Cascade
# OpenCV já vem com esses arquivos pré-treinados
# Certifique-se de que 'haarcascade_frontalface_default.xml' está no diretório de dados do OpenCV ou no seu diretório de trabalho
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Erro: Não foi possível carregar o classificador Haar Cascade para detecção facial.")
    print("Verifique o caminho: '", cv2.data.haarcascades + 'haarcascade_frontalface_default.xml', "'")
    exit()

# 3. Iniciar a captura de vídeo da câmera
cap = cv2.VideoCapture(0) # 0 para a câmera padrão do seu computador

if not cap.isOpened():
    print("Erro: Não foi possível acessar a câmera. Verifique se ela está conectada e não está em uso.")
    exit()

print("Captura de vídeo iniciada. Pressione 'q' para sair.")

while True:
    # Ler o frame da câmera
    ret, frame = cap.read()
    if not ret:
        print("Erro ao ler o frame da câmera. Saindo...")
        break

    # Converter o frame para escala de cinza (modelos de emoção geralmente esperam grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame em escala de cinza
    faces = face_cascade.detectMultiScale(gray_frame,
                                          scaleFactor=1.1, # Escala de redução da imagem a cada iteração
                                          minNeighbors=5,  # Quantos vizinhos cada retângulo candidato deve ter
                                          minSize=(30, 30) # Tamanho mínimo do objeto a ser detectado
                                         )

    # Para cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto detectado
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Azul, espessura 2

        # Recortar a região de interesse (ROI) do rosto
        roi_gray = gray_frame[y:y+h, x:x+w]

        # Redimensionar a ROI para 48x48 pixels (tamanho de entrada do modelo)
        try:
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        except cv2.error as e:
            # Isso pode acontecer se w ou h forem 0 ou muito pequenos, resultando em ROI vazia
            print(f"Erro ao redimensionar ROI. Ignorando rosto. Detalhes: {e}")
            continue

        # Normalizar os pixels (de 0-255 para 0-1) e adicionar a dimensão do canal
        # O modelo espera um array NumPy de forma (1, 48, 48, 1) para uma única imagem
        roi_normalized = roi_gray.astype('float32') / 255.0
        roi_input = np.expand_dims(roi_normalized, axis=0) # Adiciona a dimensão do batch
        roi_input = np.expand_dims(roi_input, axis=-1)   # Adiciona a dimensão do canal (se não foi adicionada no reshape)

        # Fazer a predição da emoção
        prediction = model.predict(roi_input, verbose=0)[0]
        # Obter a emoção com maior probabilidade
        emotion_index = np.argmax(prediction)
        predicted_emotion = emotion_labels[emotion_index]
        confidence = prediction[emotion_index] * 100

        # Exibir a emoção e a confiança no frame
        text = f"{predicted_emotion}: {confidence:.2f}%"
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Exibir o frame processado
    cv2.imshow('Realtime Emotion Detection - Sentimento Visivel', frame)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e fechar todas as janelas do OpenCV
cap.release()
cv2.destroyAllWindows()
print("\nDetecção de emoções em tempo real encerrada.")