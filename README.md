# Univesp-PI-IV-2025
IV Projeto Integrador dos Alunos Univesp 
Na maquina Ubuntu , insira esses comando no terminal :
sudo apt update
sudo apt install git python3-pip -y
git clone https://github.com/SEU_USUARIO/sp-api.git
cd Univesp-PI-IV-2025
⚙️ ETAPA 1 — Instalar dependências
pip install -r requirements.txt
🚀 ETAPA 2 — Rodar a API na VPS
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000

Agora ela vai estar acessível em:

http://SEU_IP_PUBLICO:8000


(exemplo: http://20.45.11.180:8000/docs)
