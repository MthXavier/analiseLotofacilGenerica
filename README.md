# 📊 Análise Estatística da Lotofácil

Este projeto tem como objetivo automatizar a coleta, organização e análise estatística dos resultados da loteria **Lotofácil**, utilizando Python e a biblioteca **pandas**.

---

## ⚙️ Funcionalidades

- 📥 Download automático dos resultados atualizados (.txt) da web  
- 🔄 Conversão do arquivo `.txt` para `.csv`  
- 📊 Análises estatísticas com base nos números sorteados, incluindo:
  - Frequência de cada número
  - Soma total dos números por sorteio
  - Distribuição de pares e ímpares
  - Intervalos entre aparições
  - Números que mais saem juntos

---

## 🧱 Estrutura do Projeto

loteria_generica/
│
├── dados/ # Pasta para arquivos baixados e convertidos
│ └── resultados_lotofacil.txt
│ └── resultados_lotofacil.csv
│
|
├── consumidor.py # Faz o download do arquivo da internet
├── escritor.py # Converte o .txt para .csv formatado
├── minerador.py # Realiza as análises estatísticas
├── main.py # Script principal que executa o fluxo completo
└── README.md

## ▶️ Como Executar

1. **Instale as dependências:**

pip install pandas requests

## 💡 Possibilidades Futuras

- Visualizações gráficas com matplotlib ou seaborn;
- Exportação de relatórios automáticos;
- Interface web com Flask ou Streamlit;
- Análise preditiva com machine learning.