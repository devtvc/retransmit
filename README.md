# retransmit
Um projeto feito com intuito de servir como ferramenta interna de controle das estações retransmissoras da TV Cultura.
Feito com Django 5.1.4 e Python 3.10.12.

### Funcionalidades da versão 1.0
- Via Django Admin
  - Controle de Inventário;
  - Controle de dados regulatórios (Anatel);
  - Controle de informações gerais das estações;
  - Controle de pagamentos de contas das estações;
  - Controle da instalação do sistema de telemetria;
  - Controle de manutenções.
    
- Via frontend
  - Visualização básica das informações das estações;
  - Visualização da disponibilidade das estações.
 
### Melhorias futuras
- Frontend (Mais informações sobre as estações)

### Tutorial de instalação
Abaixo uma lista de comandos para clonar e rodar este projeto na sua 
máquina local:

- Instalar git e depois:

```
git clone https://github.com/devtvc/gerenciarederf.git
cd gerenciarederf/src
pip install -r requirements.txt
python3 manage.py runserver
```