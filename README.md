# Projeto GerênciaRedeRF
Um projeto feito com intuito de servir como ferramenta interna de controle das estações retransmissoras da TV Cultura.
Feito com Django 5.1.4 e Python 3.10.12.

### Funcionalidades da versão 1.0
- Via Django Admin
  - Controle de Inventário
  - Controle de dados regulatórios (Anatel)
  - Controle de informações gerais das estações
    
- Via frontend
  - Visualização básica das informações das estações.
 
### Melhorias futuras
- Melhoria do frontend (Adição de gráficos etc)

### Tutorial de instalação
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git e depois:

```
git clone https://github.com/devtvc/gerenciarederf.git
cd gerenciarederf
pip install -r requirements.txt
python3 manage.py runserver
```