# 🖼️ Gera Ícone a partir de Imagem com Remoção de Fundo

Este script em Python converte uma imagem comum (como `.png` ou `.jpg`) em um arquivo `.ico`, removendo automaticamente o fundo.

---

## 🚀 Requisitos

- Python 3.8+
- Git Bash (Windows) ou terminal Linux/macOS
- Pip

---

## 🛠️ Como usar

### Etapa 1: Clonar o repositório

```bash
git clone https://github.com/xgabrielrf/gera-ico.git
cd nome-do-repositorio
```

### Etapa 2: Criar e ativar ambiente virtual (venv)

**No Windows (usando Git Bash):**

```bash
python -m venv venv
source venv/Scripts/activate
```

**No Linux/macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### Etapa 3: Instalar as dependências

```bash
pip install -r requirements.txt
```

### Etapa 4: Executar o script

```bash
python gera-ico.py nome-da-imagem.png
```

O script vai gerar um arquivo `.ico` com o mesmo nome base da imagem original.

---

## 💡 Exemplo prático

```bash
python gera-ico.py minha-logo.png
```

Isso gera um arquivo `minha-logo.ico` no mesmo diretório.

---

## 📁 Estrutura do projeto

```
📁 nome-do-repositorio/
├── gera-ico.py
├── requirements.txt
└── README.md
```

---

## ℹ️ Observações

- O fundo da imagem é removido automaticamente usando o pacote `rembg` (baseado em IA).
- O tamanho do ícone final é de 256x256 pixels.
- O script gera o `.ico` no mesmo diretório da imagem original.

---

## 🤝 Contribuições

Pull requests são bem-vindos! Forka o repositório, faz tua melhoria e manda um PR. 😄

---

## 📄 Licença

Este projeto está sob a licença MIT.
