# Contador de Histórias

## Discentes:
- Amanda Rigaud
- Juliane Coimbra

## Docente:
- Ariel Menezes de Almeida Júnior

<p>Este projeto é uma aplicação web desenvolvida em Flask que permite aos usuários ouvir histórias infantis geradas automaticamente. Utilizamos a API da OpenAI para criar histórias personalizadas, gerar imagens relacionadas e sintetizar áudio para a narração das histórias.</p>

## Tecnologias Utilizadas
- Flask
- JavaScript
- OpenAI API

## Funcionalidades
- Geração de histórias: Os usuários podem solicitar histórias personalizadas inserindo um texto na área de texto.
- Geração de imagem : Uma imagem é gerada com base na história criada.
- Geração de áudio : A história gerada é convertida em áudio para que as crianças possam ouvi-la.

## Passo a Passo para utilização

1. Clone o repositório:

```bash
     git clone https://github.com/AmandaRigaud/TAIC_AV3.git
```

2. Entre na pasta:

```bash
     cd TAIC_AV3
```

3. Crie a venv:

```bash
     python3 -m venv venv
     source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

 4. Instale as dependências:

 ```bash
    pip install -r requirements.txt
```

 5. Execute a aplicação:

 ```bash
     python src/app.py
```