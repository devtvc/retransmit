# GerênciaRedeRF
Um projeto que visa otimizar o controle (gerencial e técnico) das estações retransmissoras da TV Cultura no estado de São Paulo
Desenvolvido usando Django 5.1.4 e Python 3.10.12.

### Uso interno da engenharia e equipe técnica da Fundação Padre Anchieta.
Criado pela equipe de desenvolvimento da Fundação Padre Anchieta, com o intuito de ser usada como ferramenta interna de controle das estações.

### Funcionalidades da versão 1.0
- Cadastro e visualização dos dados regulatórios das estações
- Cadastro e visualização dos dados gerais das estações (Canal virtual, potência de operação e resposabilidade no pagamento de contas)
- Cadastro e visualização do inventário das estações (Transmissor, Receptor, Ar condicionado etc)
- Cadastro e visualização de relatórios de manutenção das estações
- Frontend simples com informações básicas das estações

### Melhorias futuras
- Melhorias no Frontend (Inclusão de gráficos, disponibilidade, manutenções etc)

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
