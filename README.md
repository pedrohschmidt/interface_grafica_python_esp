Atividade MAPA da matéria de INTERFACE GRÁFICA COM O USUÁRIO EM PYTHON ESP.

O objetivo da atividade é desenvolver uma aplicação que respeite os seguintes requisitos:

- O sistema deverá permitir a seleção do Tipo de negociação para o imóvel: Venda, Locação, Venda/Locação
- Deve haver um local para seleção do status: Disponível, Locado, Vendido, À liberar
- O campo identificação deve ser preenchido automaticamente pelo sistema.
- O endereço pode estar armazenado em um único campo ou separado em campos para armazenamento do número, complemento, CEP, Bairro e Estado
- O sistema deve permitir o cadastro de uma descrição curta para o imóvel. Essa descrição será usada nos anúncios
- Deve haver um campo para seleção do tipo do imovel: Apartamento, Casa, Terreno
- O sistema deve possuir um campo de texto no qual armazenará as Características do Imóvel. Aqui devem constar os detalhes.
- Deve haver armazenamento do Preço, porém você poderá optar por permitir que o usuário o armazene nas características do imóvel ou criar um campo exclusivo.
- O mesmo caso acima serve para Condições. Você pode criar um campo de texto para preenchimento ou deixar que o usuário registre no campo das características do imóvel.
- Deve existir um campo para registro das Observações.

O que eu fiz:
- Acesso através de login e senha, com mensagens para usuário inexistente, senha inválida, etc. Buscando as credenciais de acesso no bd para validação.
- Sistema de gerenciamento de cadastros com dois níveis de acesso: administrador e usuário comum
  - Adminstradores: Conseguem atualizar cadastro de outros usuários (nome, senha, tipo de acesso), incluindo outros administadores. Assim como adicionar ou remover usuários (comuns ou adm) da aplicação.
  - Usuários comuns: Só conseguem alterar o próprio acesso.
