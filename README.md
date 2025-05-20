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

