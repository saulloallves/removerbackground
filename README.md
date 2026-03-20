<div align="center">

# 🎨 Remove Background API

### Remova o fundo de qualquer imagem em segundos com IA

[![Live Demo](https://img.shields.io/badge/Demo-remove.girabot.com.br-blueviolet?style=for-the-badge&logo=google-chrome&logoColor=white)](https://remove.girabot.com.br)
[![API Status](https://img.shields.io/badge/API-Online-success?style=for-the-badge&logo=statuspage&logoColor=white)](https://remove.girabot.com.br/api/remove)
[![Docker](https://img.shields.io/badge/Docker-Powered-2496ED?style=for-the-badge&logo=docker&logoColor=white)](#infraestrutura)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br/>

> **API REST gratuita** para remoção de fundo de imagens usando inteligência artificial.
> 19 modelos disponíveis — de remoção rápida a qualidade máxima.

<br/>

</div>

---

## ✨ Features

| Feature | Descrição |
|---------|-----------|
| 🖼️ **Upload de Imagem** | Envie qualquer imagem via POST (PNG, JPG, WEBP, BMP, TIFF) |
| 🔗 **Via URL** | Passe a URL de uma imagem pública via GET |
| 🤖 **19 Modelos de IA** | De `u2net` (rápido) a `birefnet-massive` (máxima qualidade) |
| 🎭 **Alpha Matting** | Melhora bordas com cabelos, pelos e detalhes finos |
| 🎨 **Cor de Fundo** | Substitua o fundo por qualquer cor |
| 🖤 **Apenas Máscara** | Retorne somente a máscara preto/branco |
| 📱 **Interface Web** | Drag-and-drop com preview em tempo real |
| ⚡ **Sem Limites de Requisição** | Sem rate limiting, sem API key necessária |

---

## 🚀 Quick Start

### Remover fundo com cURL

```bash
# Via upload de arquivo
curl -X POST https://remove.girabot.com.br/api/remove \
  -F "file=@foto.jpg" \
  -o sem_fundo.png

# Via URL
curl "https://remove.girabot.com.br/api/remove?url=https://exemplo.com/foto.jpg" \
  -o sem_fundo.png
```

### Python

```python
import requests

with open('foto.jpg', 'rb') as f:
    r = requests.post('https://remove.girabot.com.br/api/remove', files={'file': f})

with open('sem_fundo.png', 'wb') as f:
    f.write(r.content)
```

### JavaScript

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('https://remove.girabot.com.br/api/remove', {
  method: 'POST',
  body: formData
});

const blob = await response.blob();
const url = URL.createObjectURL(blob);
```

### Node.js

```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const form = new FormData();
form.append('file', fs.createReadStream('foto.jpg'));

const { data } = await axios.post('https://remove.girabot.com.br/api/remove', form, {
  headers: form.getHeaders(),
  responseType: 'arraybuffer'
});

fs.writeFileSync('sem_fundo.png', data);
```

### PHP

```php
$ch = curl_init('https://remove.girabot.com.br/api/remove');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, ['file' => new CURLFile('foto.jpg')]);
file_put_contents('sem_fundo.png', curl_exec($ch));
```

---

## 📡 API Reference

### `POST /api/remove` — Upload de arquivo

**Content-Type:** `multipart/form-data`

| Parâmetro | Tipo | Obrigatório | Default | Descrição |
|-----------|------|:-----------:|---------|-----------|
| `file` | binary | ✅ | — | Imagem para processar |
| `model` | string | — | `u2net` | Modelo de IA |
| `a` | boolean | — | `false` | Ativar Alpha Matting |
| `af` | integer | — | `240` | Foreground Threshold (0-255) |
| `ab` | integer | — | `10` | Background Threshold (0-255) |
| `ae` | integer | — | `10` | Erode Structure Size |
| `om` | boolean | — | `false` | Retornar apenas máscara |
| `ppm` | boolean | — | `false` | Pós-processar máscara |

**Query string:** `bgc` (cor de fundo, ex: `#FF0000`), `extras` (JSON)

### `GET /api/remove` — Via URL

| Parâmetro | Tipo | Obrigatório | Default | Descrição |
|-----------|------|:-----------:|---------|-----------|
| `url` | string | ✅ | — | URL pública da imagem |
| `model` | string | — | `u2net` | Modelo de IA |
| *(demais)* | — | — | — | Mesmos do POST acima |

### Resposta

| Código | Descrição |
|--------|-----------|
| `200` | ✅ Imagem PNG sem fundo (`image/png`) |
| `422` | ❌ Parâmetros inválidos |

---

## 🤖 Modelos Disponíveis

<details>
<summary><b>Ver todos os 19 modelos</b></summary>

| Modelo | Tipo | Descrição |
|--------|------|-----------|
| `u2net` | 🟢 Padrão | Bom equilíbrio qualidade/velocidade |
| `u2netp` | ⚡ Rápido | Versão leve, mais veloz |
| `u2net_human_seg` | 👤 Pessoas | Otimizado para segmentação humana |
| `u2net_cloth_seg` | 👕 Roupas | Segmentação de vestuário |
| `u2net_custom` | 🔧 Custom | Modelo customizado |
| `silueta` | 🟢 Geral | Modelo alternativo |
| `isnet-general-use` | 🟢 Geral | ISNet para uso geral |
| `isnet-anime` | 🎌 Anime | Otimizado para anime/ilustrações |
| `dis_custom` | 🔧 Custom | DIS customizado |
| `sam` | 🧠 Avançado | Segment Anything Model (Meta AI) |
| `birefnet-general` | ⭐ Alta Qualidade | BiRefNet uso geral |
| `birefnet-general-lite` | ⚡ Rápido | BiRefNet versão leve |
| `birefnet-portrait` | 👤 Retratos | Otimizado para fotos de rosto |
| `birefnet-dis` | 🔬 Precisão | Segmentação dicotômica |
| `birefnet-hrsod` | 🎯 Objetos | Detecção de objetos salientes |
| `birefnet-cod` | 🦎 Camuflagem | Objetos camuflados |
| `birefnet-massive` | 🏆 Máxima | Maior qualidade possível |
| `bria-rmbg` | ⭐ Alta Qualidade | Modelo BRIA |
| `ben_custom` | 🔧 Custom | Modelo BEN customizado |

</details>

**Recomendações:**
- 📸 **Fotos gerais:** `u2net` ou `birefnet-general`
- 👤 **Retratos/pessoas:** `birefnet-portrait` ou `u2net_human_seg`
- ⚡ **Velocidade:** `u2netp` ou `birefnet-general-lite`
- 🏆 **Máxima qualidade:** `birefnet-massive`
- 🎌 **Anime/ilustrações:** `isnet-anime`

---

## 🏗️ Infraestrutura

```
┌─────────────────────────────────────────────────┐
│                    NGINX                         │
│          remove.girabot.com.br (443)             │
│                                                  │
│   /          → Static HTML (frontend)            │
│   /api/*     → Proxy → localhost:5000            │
└──────────────────────┬──────────────────────────┘
                       │
              ┌────────▼────────┐
              │  Docker: rembg  │
              │  Port 5000→7000 │
              │  danielgatis/   │
              │  rembg:latest   │
              └─────────────────┘
```

| Componente | Tecnologia |
|------------|-----------|
| **Engine** | [rembg](https://github.com/danielgatis/rembg) v2.0.72 |
| **Container** | Docker (`danielgatis/rembg:latest`) |
| **Proxy** | Nginx 1.18 + SSL (Certbot) |
| **Frontend** | HTML/CSS/JS vanilla (drag-and-drop) |

---

## 🛠️ Deploy Local

```bash
# 1. Subir o container rembg
docker run -d --name rembg -p 5000:7000 --restart unless-stopped danielgatis/rembg s api

# 2. Testar
curl -X POST http://localhost:5000/api/remove -F "file=@foto.jpg" -o resultado.png
```

---

## 📋 Limites

| Limite | Valor |
|--------|-------|
| Tamanho máximo | **50 MB** |
| Timeout | **300 segundos** (5 min) |
| Formatos | PNG, JPG, JPEG, WEBP, BMP, TIFF |
| Rate limit | Sem limite |
| Autenticação | Não requer |

---

## 📄 Documentação Completa

Consulte o arquivo [API.md](API.md) para documentação detalhada com todos os exemplos de integração.

---

<div align="center">

**[🌐 Demo ao Vivo](https://remove.girabot.com.br)** · **[📄 Documentação](API.md)**

<sub>Powered by <a href="https://github.com/danielgatis/rembg">rembg</a> · Mantido por <a href="https://github.com/saulloallves">@saulloallves</a></sub>

</div>
