#!/bin/bash
echo "========================================"
echo "   Iniciando Instalador do Ataque-Feroz   "
echo "========================================"
echo ""
echo "[*] Preparando seu Termux..."
pkg update -y && pkg upgrade -y
echo "[*] Instalando programas necessarios (Python, Git)..."
pkg install -y python git curl
echo "[*] Instalando as 'ferramentas magicas' do Python..."
pip install requests fake-useragent
echo "[*] Dando permissao de execucao..."
chmod +x hydra.py
echo ""
echo "========================================"
echo "    TUDO PRONTO! INSTALADO COM SUCESSO!   "
echo ""
echo "    Para iniciar, digite: python hydra.py"
echo "========================================"
