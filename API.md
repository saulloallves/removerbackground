# API Remover Background - Documentação

**Base URL:** `https://remove.girabot.com.br`

API para remoção de fundo de imagens, baseada no [rembg](https://github.com/danielgatis/rembg) v2.0.72.

---

## Endpoints

### 1. Remover fundo via upload de arquivo

```
POST /api/remove
```

Envia uma imagem no corpo da requisição e retorna a imagem sem fundo.

**Content-Type:** `multipart/form-data`

#### Parâmetros (form-data)

| Campo   | Tipo    | Obrigatório | Padrão  | Descrição |
|---------|---------|-------------|---------|-----------|
| `file`  | binary  | Sim         | —       | Arquivo de imagem (PNG, JPG, WEBP, etc.) |
| `model` | string  | Não         | `u2net` | Modelo de IA para processamento (ver [modelos disponíveis](#modelos-disponíveis)) |
| `a`     | boolean | Não         | `false` | Ativar Alpha Matting (melhora bordas) |
| `af`    | integer | Não         | `240`   | Alpha Matting - Foreground Threshold (0-255) |
| `ab`    | integer | Não         | `10`    | Alpha Matting - Background Threshold (0-255) |
| `ae`    | integer | Não         | `10`    | Alpha Matting - Erode Structure Size (≥0) |
| `om`    | boolean | Não         | `false` | Retornar apenas a máscara (preto e branco) |
| `ppm`   | boolean | Não         | `false` | Pós-processar a máscara |

#### Parâmetros (query string)

| Campo   | Tipo   | Obrigatório | Descrição |
|---------|--------|-------------|-----------|
| `bgc`   | string | Não         | Cor de fundo (ex: `#FF0000` para vermelho) |
| `extras`| string | Não         | Parâmetros extras em formato JSON |

#### Exemplo com cURL

```bash
curl -X POST https://remove.girabot.com.br/api/remove \
  -F "file=@minha_foto.jpg" \
  -o resultado.png
```

#### Exemplo com modelo específico

```bash
curl -X POST https://remove.girabot.com.br/api/remove \
  -F "file=@minha_foto.jpg" \
  -F "model=birefnet-general" \
  -o resultado.png
```

#### Exemplo com Alpha Matting

```bash
curl -X POST https://remove.girabot.com.br/api/remove \
  -F "file=@minha_foto.jpg" \
  -F "a=true" \
  -F "af=240" \
  -F "ab=10" \
  -F "ae=10" \
  -o resultado.png
```

#### Exemplo com cor de fundo

```bash
curl -X POST "https://remove.girabot.com.br/api/remove?bgc=%23FF0000" \
  -F "file=@minha_foto.jpg" \
  -o resultado.png
```

#### Exemplo com apenas a máscara

```bash
curl -X POST https://remove.girabot.com.br/api/remove \
  -F "file=@minha_foto.jpg" \
  -F "om=true" \
  -o mascara.png
```

---

### 2. Remover fundo via URL da imagem

```
GET /api/remove
```

Processa uma imagem a partir de uma URL pública.

#### Parâmetros (query string)

| Campo   | Tipo    | Obrigatório | Padrão  | Descrição |
|---------|---------|-------------|---------|-----------|
| `url`   | string  | Sim         | —       | URL pública da imagem |
| `model` | string  | Não         | `u2net` | Modelo de IA (ver [modelos disponíveis](#modelos-disponíveis)) |
| `a`     | boolean | Não         | `false` | Ativar Alpha Matting |
| `af`    | integer | Não         | `240`   | Alpha Matting - Foreground Threshold (0-255) |
| `ab`    | integer | Não         | `10`    | Alpha Matting - Background Threshold (0-255) |
| `ae`    | integer | Não         | `10`    | Alpha Matting - Erode Structure Size (≥0) |
| `om`    | boolean | Não         | `false` | Retornar apenas a máscara |
| `ppm`   | boolean | Não         | `false` | Pós-processar a máscara |
| `bgc`   | string  | Não         | —       | Cor de fundo |
| `extras`| string  | Não         | —       | Parâmetros extras em JSON |

#### Exemplo com cURL

```bash
curl "https://remove.girabot.com.br/api/remove?url=https://exemplo.com/foto.jpg" \
  -o resultado.png
```

#### Exemplo com modelo específico

```bash
curl "https://remove.girabot.com.br/api/remove?url=https://exemplo.com/foto.jpg&model=birefnet-general" \
  -o resultado.png
```

---

## Modelos Disponíveis

| Modelo | Descrição |
|--------|-----------|
| `u2net` | Modelo padrão, bom equilíbrio entre qualidade e velocidade |
| `u2netp` | Versão leve do u2net, mais rápido |
| `u2net_human_seg` | Otimizado para segmentação de pessoas |
| `u2net_cloth_seg` | Segmentação de roupas |
| `u2net_custom` | Modelo u2net customizado |
| `silueta` | Modelo alternativo |
| `isnet-general-use` | ISNet para uso geral |
| `isnet-anime` | Otimizado para imagens de anime |
| `dis_custom` | Modelo DIS customizado |
| `sam` | Segment Anything Model |
| `birefnet-general` | BiRefNet - uso geral (alta qualidade) |
| `birefnet-general-lite` | BiRefNet lite - mais rápido |
| `birefnet-portrait` | BiRefNet otimizado para retratos |
| `birefnet-dis` | BiRefNet para segmentação dicotômica |
| `birefnet-hrsod` | BiRefNet para detecção de objetos salientes |
| `birefnet-cod` | BiRefNet para detecção de objetos camuflados |
| `birefnet-massive` | BiRefNet modelo massivo (máxima qualidade) |
| `bria-rmbg` | Modelo BRIA RMBG |
| `ben_custom` | Modelo BEN customizado |

---

## Exemplos de Integração

### JavaScript (Fetch API)

```javascript
async function removerFundo(arquivo) {
  const formData = new FormData();
  formData.append('file', arquivo);
  formData.append('model', 'u2net');

  const response = await fetch('https://remove.girabot.com.br/api/remove', {
    method: 'POST',
    body: formData
  });

  if (!response.ok) throw new Error(`Erro: ${response.status}`);

  const blob = await response.blob();
  return URL.createObjectURL(blob);
}

// Uso com input file
const input = document.querySelector('input[type="file"]');
input.addEventListener('change', async (e) => {
  const url = await removerFundo(e.target.files[0]);
  document.querySelector('img').src = url;
});
```

### Python (requests)

```python
import requests

# Via upload de arquivo
with open('foto.jpg', 'rb') as f:
    response = requests.post(
        'https://remove.girabot.com.br/api/remove',
        files={'file': f},
        data={'model': 'u2net'}
    )

with open('resultado.png', 'wb') as f:
    f.write(response.content)

# Via URL
response = requests.get(
    'https://remove.girabot.com.br/api/remove',
    params={'url': 'https://exemplo.com/foto.jpg'}
)

with open('resultado.png', 'wb') as f:
    f.write(response.content)
```

### Node.js (axios + form-data)

```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

async function removerFundo(caminhoImagem) {
  const form = new FormData();
  form.append('file', fs.createReadStream(caminhoImagem));
  form.append('model', 'u2net');

  const response = await axios.post(
    'https://remove.girabot.com.br/api/remove',
    form,
    {
      headers: form.getHeaders(),
      responseType: 'arraybuffer'
    }
  );

  fs.writeFileSync('resultado.png', response.data);
}

removerFundo('foto.jpg');
```

### PHP (cURL)

```php
<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://remove.girabot.com.br/api/remove');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, [
    'file' => new CURLFile('foto.jpg'),
    'model' => 'u2net'
]);

$resultado = curl_exec($ch);
curl_close($ch);

file_put_contents('resultado.png', $resultado);
```

---

## Respostas

| Código | Descrição |
|--------|-----------|
| 200    | Sucesso - retorna a imagem processada (PNG) |
| 422    | Erro de validação - parâmetros inválidos |
| 404    | Endpoint não encontrado |

### Resposta de Sucesso (200)

Retorna o binário da imagem PNG sem fundo diretamente no corpo da resposta.

**Content-Type:** `image/png`

### Resposta de Erro (422)

```json
{
  "detail": [
    {
      "loc": ["body", "file"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## Limites

- **Tamanho máximo do arquivo:** 50 MB
- **Timeout da requisição:** 300 segundos (5 minutos)
- **Formatos aceitos:** PNG, JPG, JPEG, WEBP, BMP, TIFF

---

## Interface Web

Acesse `https://remove.girabot.com.br` para utilizar a interface visual com drag-and-drop.
