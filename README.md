Atividade MAPA da matéria de INTERFACE GRÁFICA COM O USUÁRIO EM PYTHON ESP.
<H2>O que foi pedido:</H2>
O Sr. Roberto é dono da Py Assessoria e solicitou uma aplicação para cadastrar/consultar os imóveis com os quais ele trabalha. Sendo assim, é necessário que você desenvolva:
- A interface gráfica da aplicação;
- A tabela do banco que irá receber os dados;
- A programação para armazenar os dados;
- O sistema deverá permitir a seleção do Tipo de negociação para o imóvel: Venda, Locação, Venda/Locação;
- Deve haver um local para seleção do status: Disponível, Locado, Vendido, À liberar;
- O campo identificação deve ser preenchido automaticamente pelo sistema;
- O endereço pode estar armazenado em um único campo ou separado em campos para armazenamento do número, complemento, CEP, Bairro e Estado;
- O sistema deve permitir o cadastro de uma descrição curta para o imóvel. Essa descrição será usada nos anúncios;
- Deve haver um campo para seleção do tipo do imovel: Apartamento, Casa, Terreno;
- O sistema deve possuir um campo de texto no qual armazenará as Características do Imóvel. Aqui devem constar os detalhes;
- Deve haver armazenamento do Preço, porém você poderá optar por permitir que o usuário o armazene nas características do imóvel ou criar um campo exclusivo;
- O mesmo caso acima serve para Condições. Você pode criar um campo de texto para preenchimento ou deixar que o usuário registre no campo das características do imóvel;
- Deve existir um campo para registro das Observações.

<H2>O que foi feito:</H2>
- Acesso através de login e senha, com mensagens para usuário inexistente, senha inválida, etc. Buscando as credenciais de acesso no bd para validação;
- Criação de dois usuários de forma automática, para que seja possível testar a aplicação (em uma sutuação normal este código seria removido da aplicação);
- Sistema de gerenciamento de cadastros com dois níveis de acesso: administrador e usuário comum;
  - Adminstradores: Conseguem atualizar cadastro de outros usuários (nome, senha, tipo de acesso), incluindo outros administadores. Assim como adicionar ou remover usuários (comuns ou adm) da aplicação;
  - Usuários comuns: Só conseguem alterar o próprio acesso;
- Tela de cadastro de imóveis
  - Uso de checkboxes para facilitar a definição de algumas características como: possui churrasqueiras, aceita pet, garagem coberta, quadra poliesprotiva, portaria 24h, etc;
  - Buscador de CEP usando a biblioteca brazilcep, mas ela contantemente dá o erro de BlockedByFlood, que, até onde entendi, é um erro devido a uma quantidade grande de consultas em um curto espaço de tempo;
  - Uso de comboboxes e máscaras de entrada para facilitar e padronizar a inserção de dados;
  - Validação de dados de acordo com o tipo do imóvel, antes de inserir no banco de dados. Por exemplo: Imóvel do tipo apartamento com 0 quartos, negociado para locação mas com valor de aluguel =0. Ele vai mostrar um pop-up avisando que não pode ter um apartamento com 0 quartos, e uma negociação de locação sem valor de aluguel, e só vai deixar inserir quando arrumar estes campos;
