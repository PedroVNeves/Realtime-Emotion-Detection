# Realtime Emotion Detection

## Visão Geral do Projeto

O **Realtime Emotion Detection** é um projeto de aprendizado de máquina que utiliza visão computacional para detectar e classificar emoções faciais em tempo real através da câmera do computador. Desenvolvido em Python, ele emprega uma Rede Neural Convolucional (CNN) treinada em dados de expressões faciais para identificar emoções como Raiva, Desgosto, Medo, Felicidade, Tristeza, Surpresa e Neutro.
O projeto também envolve tratamento e analise de dados para garantir a eficiência do modelo.

## Funcionalidades Principais

* **Detecção Facial em Tempo Real:** Utiliza o OpenCV para identificar rostos no feed de vídeo da câmera.
* **Predição de Emoções:** Um modelo de Deep Learning (CNN) analisa as expressões faciais para prever a emoção predominante.
* **Visualização Interativa:** Exibe a emoção predita e a confiança na tela, sobrepondo-as aos rostos detectados.
* **Baseado em Dataset CK+ Extended:** Modelo treinado e validado em um dataset de expressões faciais reconhecido.

## Tecnologias Utilizadas

* **Python 3.10+** (Recomendado: Python 3.10 ou 3.11 para compatibilidade com TensorFlow)
* **TensorFlow / Keras:** Para construção e treinamento do modelo de Deep Learning.
* **OpenCV (`opencv-python`):** Para acesso à câmera, captura de vídeo e detecção facial.
* **NumPy:** Para manipulação eficiente de dados numéricos (pixels de imagem).
* **Pandas:** Para manipulação e análise do dataset.
* **Scikit-learn:** Para métricas de avaliação do modelo (relatório de classificação, matriz de confusão).
* **Matplotlib e Seaborn:** Para visualização de dados e gráficos.

## Configuração do Ambiente

Siga estes passos para configurar o ambiente e executar o projeto:

### 1. Pré-requisitos

* Certifique-se de ter o **Python 3.10 ou 3.11** instalado no seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/). Durante a instalação, **lembre-se de marcar a opção "Add Python to PATH"**.

### 2. Clonar o Repositório (se estiver no GitHub)

```bash
git clone [https://github.com/SeuUsuario/EmotionNet-Cam.git](https://github.com/SeuUsuario/EmotionNet-Cam.git)
cd EmotionNet-Cam
