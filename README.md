# 🔐 Block Cipher File Encryption (AES-like)

Projeto desenvolvido para demonstrar a implementação de um **algoritmo de cifragem e decifragem baseado em cifras de bloco**, inspirado no funcionamento do **AES (Advanced Encryption Standard)**. O sistema é capaz de processar **arquivos binários**, como imagens (.jpg, .png) e documentos (.pdf), realizando sua criptografia e posterior recuperação.

O algoritmo foi desenvolvido **sem o uso de bibliotecas de criptografia prontas**, implementando manualmente as principais operações de uma cifra de bloco, bem como o método de **padding PKCS#7** para tratamento de arquivos cujo tamanho não é múltiplo do tamanho do bloco.

---

# 📚 Fundamentação Teórica

## Cifras de Bloco

Cifras de bloco são algoritmos criptográficos que trabalham dividindo os dados em **blocos de tamanho fixo** e aplicando transformações matemáticas utilizando uma **chave secreta**.

Alguns exemplos conhecidos de cifras de bloco são:

- AES (Advanced Encryption Standard)
- DES (Data Encryption Standard)
- 3DES (Triple DES)

Esses algoritmos transformam blocos de dados em texto cifrado (ciphertext), tornando-os ilegíveis sem a chave correta. O processo inverso permite recuperar exatamente os dados originais.

---

## Estrutura Inspirada no AES

O algoritmo implementado neste projeto utiliza uma estrutura inspirada no AES, composta por múltiplas rodadas de transformação.

Cada rodada realiza as seguintes operações:

### SubBytes
Substituição de cada byte do bloco por outro valor utilizando uma **S-Box (Substitution Box)**.

### ShiftRows
Reorganização dos bytes dentro do bloco para promover difusão dos dados.

### XOR com Chave
Cada bloco é combinado com a chave utilizando a operação lógica **XOR**, garantindo dependência da chave no processo de criptografia.

Essas operações são repetidas em múltiplas rodadas para aumentar a complexidade e segurança do processo.

---

## Padding PKCS#7

Arquivos geralmente não possuem tamanho múltiplo do bloco (16 bytes).  
Para resolver isso, foi implementado manualmente o **PKCS#7 Padding**.

Esse método adiciona bytes extras ao final do arquivo para completar o tamanho do bloco.

Durante a decifragem, esses bytes adicionais são removidos para restaurar o arquivo original.

---

# 🧠 Funcionamento do Sistema

O sistema possui dois processos principais.

## 1️⃣ Cifragem

1. O usuário informa uma **chave secreta**
2. O arquivo é lido em **modo binário**
3. O sistema aplica **padding PKCS#7**
4. Os dados são divididos em **blocos de 16 bytes**
5. Cada bloco passa pelas **rodadas de cifragem**
6. O arquivo criptografado é salvo

---

## 2️⃣ Decifragem

1. O arquivo criptografado é lido
2. Cada bloco passa pelo **processo inverso**
3. O **padding é removido**
4. O arquivo original é reconstruído

Após esse processo, o arquivo recuperado deve ser **idêntico ao original e totalmente funcional**.

---

# 📂 Estrutura do Projeto


Descrição dos arquivos:

- **encrypt_decrypt.py** → implementação do algoritmo de cifragem e decifragem
- **exemplo.jpg** → arquivo original utilizado para teste
- **exemplo_encrypted.bin** → arquivo criptografado
- **exemplo_recuperado.jpg** → arquivo restaurado após decifragem
- **README.md** → documentação do projeto

---

# ⚙️ Requisitos

Para executar o projeto é necessário:

- Python 3.x

Verifique a instalação com:

```bash
python --version

## ▶️ Como Executar

Execute o programa no terminal:

```bash
python encrypt_decrypt.py
```

ou

```bash
python3 encrypt_decrypt.py
```

O sistema exibirá o seguinte menu:

```
1 - Encrypt File
2 - Decrypt File
```

---

## 🔐 Exemplo de Criptografia

Entrada no terminal:

```
Choice: 1
Key: minhasenha
Input file: imagem.jpg
Output file: imagem_encrypted.bin
```

O arquivo será criptografado.

---

## 🔓 Exemplo de Descriptografia

Entrada no terminal:

```
Choice: 2
Key: minhasenha
Input file: imagem_encrypted.bin
Output file: imagem_recuperada.jpg
```

Após a execução, o arquivo recuperado abrirá normalmente.

---


## 👨‍💻 Autor

**Bruno Eugênio**

Estudante de Análise e Desenvolvimento de Sistemas.

Projeto desenvolvido para fins acadêmicos.

---

## 📜 Licença

Este projeto foi desenvolvido exclusivamente para fins **educacionais e acadêmicos**.
