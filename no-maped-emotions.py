# Encontrar as emoções não mapeadas
unmapped_emotions = df[df['emotion_label'].isnull()]['emotion'].unique()

if len(unmapped_emotions) > 0:
    print(f"Os seguintes códigos de emoção não foram mapeados: {unmapped_emotions}")
    print("\nÉ provável que o dataset CK+ extended possua uma emoção 'Contempt' (Desprezo) que é geralmente mapeada para o número 1 no conjunto de 7 classes, mas às vezes pode vir com um mapeamento diferente ou uma emoção a mais/menos, ou até mesmo desprezo pode ser o 0 no FER.")
    print("No CK+, o mapeamento padrão é geralmente:")
    print("0=Neutro, 1=Raiva, 2=Contempt (Desprezo), 3=Desgosto, 4=Medo, 5=Felicidade, 6=Tristeza, 7=Surpresa.")
    print("\nConsiderando a diferença do dataset FER2013, onde geralmente desprezo é mapeado como 1. O CK+ tem 8 emoções, e o FER2013 tem 7. Precisamos padronizar. A emoção 'Desprezo' (Contempt) é o valor 1 na maioria das implementações do CK+, sendo 'Desgosto' o valor 2.")
    print("\nVamos ajustar o dicionário de mapeamento para as 7 emoções mais comuns, remapeando o 'desprezo' para 'raiva' ou 'desgosto', se o número de emoções for 7, ou adicionando uma nova classe se for 8.")
    print("A forma mais segura é verificar os valores únicos da coluna emotion no dataset completo, para garantir o mapeamento correto.")

    # Vamos verificar todos os valores únicos na coluna 'emotion'
    all_unique_emotions = df['emotion'].unique()
    print(f"\nTodos os códigos de emoção únicos no dataset: {all_unique_emotions}")

    # Para seguir com 7 classes, podemos remapear o desprezo se ele for um valor não mapeado.
    # Se '1' for o valor não mapeado, e no CK+ 'desprezo' é 1, vamos incluí-lo.
    # Para o CK+, o mapeamento padrão é:
    # 0: Neutro
    # 1: Raiva
    # 2: Contempt (Desprezo) - se seu dataset tiver 8, este é o 2
    # 3: Desgosto
    # 4: Medo
    # 5: Felicidade
    # 6: Tristeza
    # 7: Surpresa
    # Mas como estamos usando 7 classes, e o FER2013 tem 0-6, e seu emotion_label tem 0-6,
    # significa que 0-6 já foi mapeado, e o problema é outro número.

    # Vamos tentar o mapeamento mais comum para 7 classes, onde o "desprezo" (contempt)
    # é muitas vezes ignorado ou agrupado com "raiva" ou "desgosto".
    # Pela saída, parece que os valores estão entre 0 e 6 (para 7 classes).
    # O problema são os 18 valores nulos.

    # Assumindo que o CK+ extended que você tem segue o mapeamento de 7 emoções, mas com uma numeração diferente
    # ou que os valores nulos são para uma classe rara que podemos descartar ou remapear.
    # Se os valores não mapeados são por exemplo [7], isso indicaria 8 classes, e precisaríamos ajustar.
    # Pela sua saída inicial, o `emotion` da primeira linha é 6 (Neutro), o que indica que 0-6 é o range.
    # Os valores nulos significam que alguma emoção *dentro* desse range ou fora dele (se for o caso de 8 classes)
    # não está no dicionário.

    # O ideal é confirmar o mapeamento oficial do seu ckextended.csv.
    # No entanto, para continuar, vou assumir que os 18 valores nulos são de uma emoção que não se encaixa nas 7 classes
    # e que, para simplificar, podemos removê-los do dataset.
    # Em um projeto real, você pesquisaria o mapeamento exato para o 'ckextended.csv'.
    print("\nVamos remover as linhas com emoções não mapeadas para simplificar por enquanto.")
    print("Isso pode significar que algumas emoções (ex: desprezo) serão ignoradas se não forem remapeadas.")

    # Remover linhas com emotion_label nulo
    df.dropna(subset=['emotion_label'], inplace=True)
    print(f"\nDataFrame agora com {len(df)} entradas após remover emoções não mapeadas.")

else:
    print("Todos os códigos de emoção foram mapeados com sucesso. Ótimo!")