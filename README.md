# OCR Dataset Preprocessing

Este repositório contém um script para pré-processamento de um dataset de OCR (Reconhecimento Óptico de Caracteres), convertendo imagens organizadas em pastas para o formato `.csv`, utilizando bibliotecas como `NumPy`, `Pandas` e `OpenCV`.

---

## 📦 Fonte dos dados

O conjunto de dados original pode ser obtido no Kaggle, neste link:

🔗 [OCR Dataset - Kaggle](https://www.kaggle.com/datasets/harieh/ocr-dataset)

Ele é composto por:

- **62 diretórios**, cada um representando uma classe (números, letras maiúsculas e minúsculas);
- Cada diretório contém aproximadamente **3.473 imagens**;
- Total aproximado de **215.326 amostras** no formato de imagem `40x60` pixels em escala de cinza.

---

## 🛠️ Motivação

Esse formato em pastas não é ideal para o treinamento direto de modelos de *Machine Learning* supervisionados. Por isso, este projeto aplica técnicas de:

- Leitura e pré-processamento de imagens;
- Conversão de imagens para vetores numéricos;
- Criação de tabelas `.csv` com `Pandas` contendo os dados e os rótulos.

O objetivo é facilitar a ingestão dos dados em pipelines de *Machine Learning* e *Deep Learning*.

---

## 📁 Estrutura do Repositório

``` bash
OCR_dataset_preprocessing/
├── src/
│ └── main.py
├── dataset_csv/
│ ├── OCR_X.zip
│ └── OCR_y.zip
```

- `main.py`: Script responsável por converter as imagens em um CSV.
- `OCR_X.zip`: Arquivo compactado contendo os dados (vetores das imagens).
- `OCR_y.zip`: Arquivo compactado contendo os rótulos das imagens.

> ⚠️ **Atenção**: O arquivo `OCR_X.csv` possui aproximadamente **1.1 GB**. Certifique-se de ter espaço em disco antes de descompactar.

---

## ⚠️ Sobre a perda de amostras

Durante o processo de conversão, cerca de **5.100 imagens não foram carregadas corretamente**, resultando em um total final de **210.226 amostras**.

Possíveis causas:
- Arquivos ausentes ou com nomes inconsistentes;
- Imagens corrompidas;
- Diferença no padrão de nomenclatura entre as pastas.

Estou ciente dessa limitação e pretendo atualizar o repositório futuramente com uma versão completa. **Considere esta versão como provisória**.

---

## 🔁 Reproduzindo o processo

Para repetir a conversão do dataset:

1. Baixe o dataset original do Kaggle.
2. Coloque a pasta `dataset/` na **mesma raiz do script** `main.py`.
3. Execute o script para gerar os arquivos CSV.

---

## 📌 Considerações finais

A justificativa de ser uma versão provisória **não compromete a utilidade do projeto** — ao contrário, documentar isso demonstra maturidade e responsabilidade no compartilhamento de dados.

Caso queira sugestões para melhorar o script e evitar perdas na próxima versão, fico à disposição.

---

