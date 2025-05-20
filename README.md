# OCR_dataset_preprocessing

Nesse repositório compartilho um conjunto de dados para OCR transformado em csv a partir de técnicas de manipulação de arquivos, conversão de imagens em vetores (arrays) e criação e salvamento de datasets pandas.

O conjunto de dados original pode ser obtido dentro do repositório kaggle de datasets públicos. 

Caso possua interesse: https://www.kaggle.com/datasets/harieh/ocr-dataset

o dataset original era composto por 62 diretórios, cada um deles representa uma classe:

cada classe possuia cerca de 3473 totalizando cerca de 215326 amostras para treinamento de imagens 40x60.

No entanto, como sabemos, esse formato de dataset não é conveniente para treinamento de modelos de machine learning, em virtude disso, resolvi aplicar essas técnicas para criar uma tabela csv que agregasse todos esses arquivos em um único.

No repositório você encontrará:

src:
  main.py
dataset_csv:
  OCR_X.zip
  OCR_y.zip

main.py é meu script

OCR_X e OCR_y são os arquivos csv compactados para permitir o commit.

Observação: OCR_X é uma tabela csv com 1.1gb de tamanho, certifique-se de ter espaço suficiente.

Houve uma perda de amostras nesse processo, provavelmente devido a erros de caminho das pastas, futuramente irei atualizar esse repositório com todos os dados. Considere como uma versão temporária, na tabela temos cerca de 210226 amostras de imagens.

lembre-se de colocar a pasta datasets na mesma pasta do script, caso queira repetir o processo.
