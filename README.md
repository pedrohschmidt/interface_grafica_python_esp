Esta aplicação refere-se a atividade MAPA da matéria de INTERFACE GRÁFICA COM O USUÁRIO EM PYTHON ESP.
Desenvolvida pelo aluno: <b>Pedro Henrique Schmidt do Nasicmento</b>
<H2>O que foi pedido:</H2>
O Sr. Roberto é dono da Py Assessoria e solicitou uma aplicação para cadastrar/consultar os imóveis com os quais ele trabalha. Sendo assim, é necessário que você desenvolva:
<ol>
<li>A interface gráfica da aplicação;</li>
<li>A tabela do banco que irá receber os dados;</li>
<li>A programação para armazenar os dados;</li>
</ol>
<h3>Requisitos:</h3>
<ol>
<li>O sistema deverá permitir a seleção do Tipo de negociação para o imóvel: Venda, Locação, Venda/Locação</li>
<li>Deve haver um local para seleção do status: Disponível, Locado, Vendido, À liberar</li>
<li>O campo identificação deve ser preenchido automaticamente pelo sistema.</li>
<li>O endereço pode estar armazenado em um único campo ou separado em campos para armazenamento do número, complemento, CEP, Bairro e Estado</li>
<li>O sistema deve permitir o cadastro de uma descrição curta para o imóvel. Essa descrição será usada nos anúncios</li>
<li>Deve haver um campo para seleção do tipo do imovel: Apartamento, Casa, Terreno</li>
<li>O sistema deve possuir um campo de texto no qual armazenará as Características do Imóvel. Aqui devem constar os detalhes.</li>
<li>Deve haver armazenamento do Preço, porém você poderá optar por permitir que o usuário o armazene nas características do imóvel ou criar um campo exclusivo.</li>
<li>Mesmo caso acima serve para Condições. Você pode criar um campo de texto para preenchimento ou deixar que o usuário registre no campo das características do imóvel.</li>
<li>Deve existir um campo para registro das Observações.</li>
</ol>
<h2>O que foi feito:</h2>
<h3>Gestão de acesso:</h3>
<ol>
<li>Acesso através de login e senha, com mensagens para usuário inexistente, senha inválida, etc. Buscando as credenciais de acesso no bd para validação.</li>
<li>Criação de dois usuários de forma automática, para que seja possível testar a aplicação (em uma sutuação normal este código seria removido da aplicação)</li>
<li>Sistema de gerenciamento de cadastros com dois níveis de acesso: administrador e usuário comum</li>
<ol type="a">
<li>Adminstradores: Conseguem atualizar cadastro de outros usuários (nome, senha, tipo de acesso), incluindo outros administadores. Assim como adicionar ou remover usuários (comuns ou adm) da aplicação.</li>
<li> Usuários comuns: Só conseguem alterar o próprio acesso.</li>
</ol>
</ol>
<h3>Gestão de imóveis:</h3>
<h4>Cadastro de imóveis</h4>
<ol>
<li> Uso de checkboxes para facilitar a definição de algumas características como: possui churrasqueiras, aceita pet, garagem coberta, quadra poliesprotiva, portaria 24h, etc...</li>
<li>Buscador de CEP usando a biblioteca brazilcep, mas ela contantemente dá o erro de BlockedByFlood, que, até onde entendi, é um erro devido a uma quantidade grande de consultas em um curto espaço de tempo</li>
<li>Uso de comboboxes e máscaras de entrada para facilitar e padronizar a inserção de dados</li>
<li>Validação de dados de acordo com o tipo do imóvel, antes de inserir no banco de dados. Por exemplo: Imóvel do tipo apartamento com 0 quartos, negociado para locação mas com valor de aluguel =0. Ele vai mostrar um pop-up avisando que não pode ter um apartamento com 0 quartos, e uma negociação de locação sem valor de aluguel, e só vai deixar inserir quando arrumar estes campos.</li>
</ol>
<h4>Busca de imóveis</h4>
<ol>
<li>Filtro dinâmico de imóveis, atualizado automaticamente a medida que se alteram os filtros;</li>
<li></li>
</ol>
<h3>Pendente de desenvolvimento:</h3>
<ol>
<li>Trazer todos os detalhes do imóvel conforme for selecionado na tabela (duplo-clique)</li>
<li>Lista de contatos vinculada ao imóvel</li>
<li>Adicionar imagens ao cadastro de imóveis</li>
</ol>