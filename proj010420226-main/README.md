# 🐳 Projeto Docker – Frontend + API (Flask)

## 🎯 Objetivo

Este projeto demonstra como criar e executar uma aplicação composta por:

- 🌐 Frontend (HTML + Nginx)
- ⚙️ Backend (API Flask)
- 🐳 Containers com Docker
- 🔗 Orquestração com Docker Compose

---

## 🧠 Conceitos abordados

- Dockerfile
- Containers
- Docker Compose
- Comunicação entre serviços
- CORS (Cross-Origin Resource Sharing)

---

## 📁 Estrutura do Projeto

```
projeto/
│
├── backend/
│   ├── app.py
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
└── docker-compose.yml
```

---

## ⚙️ Tecnologias utilizadas

- Python + Flask
- Flask-CORS
- Nginx
- Docker
- Docker Compose

---

## 🔧 Backend (API)

### 📄 `app.py`

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api*": {"origins": "http://localhost:8080"}})

@app.route('/api', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from backend!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 📄 `Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask flask-cors

CMD ["python", "app.py"]
```

---

## 🌐 Frontend

### 📄 `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Docker App</title>
</head>
<body>

<h1>Frontend Docker 🚀</h1>

<button onclick="chamarAPI()">Chamar API</button>

<p id="resultado"></p>

<script>
function chamarAPI() {
    fetch('http://localhost:8000/api')
        .then(res => res.json())
        .then(data => {
            document.getElementById("resultado").innerText = data.message;
        });
}
</script>

</body>
</html>
```

---

### 📄 `Dockerfile`

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

---

## 🐳 Docker Compose

### 📄 `docker-compose.yml`

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:5000"

  frontend:
    build: ./frontend
    ports:
      - "8080:80"
```

---

## ▶️ Como executar o projeto

```bash
docker compose up --build
```

---

## 🌍 Acessos

- Frontend: http://localhost:8080
- API: http://localhost:8000/api

---

## 🧪 Teste esperado

1. Acesse o frontend  
2. Clique no botão "Chamar API"  
3. A mensagem exibida deve ser:

```
Hello from backend!
```

---

## 🚨 Problemas comuns

### ❌ Erro de CORS
Já tratado com flask-cors no backend.

### ❌ Porta 5000 não funciona no Mac
Solução aplicada:
```
8000:5000
```

### ❌ Erro no docker-compose
- Use 2 espaços (não TAB)
- Verifique identação YAML
