# HydraStrike 🌊

HydraStrike é uma ferramenta de ataque DDoS multi-vetor e multi-thread para Termux, projetada para testes de estresse e pesquisa de segurança. Ela utiliza uma rede de proxies gratuitos ("bots") para distribuir o ataque e maximizar o impacto.

 <!-- Tire um print da sua ferramenta rodando e coloque o link aqui -->

## ✨ Funcionalidades

- **Interface Amigável**: Menu interativo e colorido para fácil utilização.
- **Scraper de Proxies**: Baixa e atualiza automaticamente milhares de proxies HTTP gratuitos de fontes confiáveis.
- **Multi-Threading**: Lança centenas ou milhares de threads para um ataque massivo e simultâneo.
- **Cache-Busting**: Adiciona parâmetros aleatórios às URLs para tentar contornar sistemas de cache e proteções como a da Cloudflare.
- **User-Agents Aleatórios**: Simula tráfego de diferentes navegadores para dificultar a filtragem.
- **Relatório de Ataque**: Mostra estatísticas detalhadas no final de cada operação.

## 🚀 Instalação (Termux)

A instalação é simples. Apenas clone o repositório e execute o script de instalação.

```bash
# 1. Atualize o Termux e instale o Git
pkg update -y && pkg upgrade -y
pkg install git -y

# 2. Clone o repositório do HydraStrike
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

# 3. Entre no diretório da ferramenta
cd SEU-REPOSITORIO

# 4. Execute o script de instalação
bash install.sh
```

## ⚙️ Como Usar

Após a instalação, inicie a ferramenta com o seguinte comando:

```bash
python hydra.py
```

Você será apresentado a um menu principal:

- **`[1] Iniciar Ataque`**: Configura e lança um novo ataque. Você precisará fornecer a URL do alvo, o número de threads e a duração.
- **`[2] Atualizar Lista de Bots`**: Baixa uma nova lista de proxies. A ferramenta faz isso automaticamente no primeiro ataque, mas você pode forçar uma atualização aqui.
- **`[3] Sobre`**: Exibe informações sobre a ferramenta.
- **`[4] Sair`**: Encerra o programa.
