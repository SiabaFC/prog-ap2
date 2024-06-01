[X] transportar o mapa para a interface gráfica
[X] movimento do aventureiro
[X] visualizar na tela os atributos do aventureiro
[X] resumir o combate na tela

[X] skins (caractere e cor)
- Adicionar novas cores
- Criar lista de cores possíveis
- Criar lista de caracteres possíveis
- Criar métodos para mudar de cor e caractere
- Criar atalhos no teclado
- Refatorar método de renderização

[X] criar um boss no local do tesouro
- Criar uma classe que herda Monstro
- Definir novos atributos
- Quando a posição do aventureiro for igual à do tesouro, iniciar um combate com o boss

[X] criar monstros diferentes
- Criar subclasses de Monstro
- Criar a lista de monstros
- Na função `movimentar`, quando for definido que um monstro vai aparecer, escolher aleatoriamente entre os monstros

[X] montar sistema de níveis de dificuldades
- Criar uma variável `dificuldade` no módulo `mecanicas`
- Alterar as classes de monstros para receber o nível de dificuldade
- Alterar a definição dos atributos dos monstros conforme a dificuldade
- Alterar as chamadas dos monstros nos combates
- Associar a mudança de dificuldade a duas teclas do teclado

[X] sistema de níveis
- Criar um atributo xp para os monstros
- Criar atributos xp e nível para o aventureiro
- Criar métodos para o aventureiro ganhar xp e subir de nível
- Criar uma forma de progressão dos atributos do aventureiro (vida, força e defesa)
- Alterar a função de combate, para que o aventureiro ganhe xp quando derrotar o monstro
- Alterar a interface para mostrar o nível do aventureiro

[X] criar um inputbox para pedir o nome
- Criar uma nova classe InputBox, semelhante à Tela, para ter a interface para ler textos
- Refatorar o módulo mecanicas para melhorar a organização do código
- Criar um módulo inputbox com uma função que retorna o texto inserido pelo usuário
- Ajustar a função jogo para ler o nome e atribuir ao aventureiro antes do jogo começar

[X] criar sistema de classes
- Criar subclasses para cada classe de aventureiro
- Definir mudanças de atributos para cada nova classe
- Criar nova classe ButtonBox na GUI
- Criar uma nova função em mecanicas para selecionar a classe
- Instanciar a classe desejada ao invés de Aventureiro

[X] criar obstáculos no mapa
- Criar classes de obstáculos
- Modificar método `andar` do `Aventureiro` para separar a mudança de posição do cálculo da posição futura
- Incluir função para verificar se há alguma barreira na coordenada passada
- Modificar renderização na tela

[X] criar um relógio na tela
- Criar um módulo `relogio` no pacote `mecanicas`, com uma variável global `tempo`
    - Criar uma função `tempo_decorrido`, que retorna o tempo em `MM:SS`
- No módulo `main`, iniciar o relógio
- No módulo `tela`, renderizar o tempo decorrido no canto superior direito

[X] possibilitar salvar o jogo
- Criar módulo `save` no pacote `mecanicas`
- Criar métodos em `Aventureiro`, `Tesouro` e `Obstaculo` que retornam os dados do objeto
- Criar métodos em `Aventureiro`, `Tesouro` e `Obstaculo` que sobrescrevem os dados do objeto
- Criar ou modificar funções do relógio
- No módulo `save`, obter os dados dos elementos do jogo e salvar em um arquivo .json
- No módulo `save`, ler um arquivo .json e retornar instâncias dos objetos
- No loop, criar botões de acesso para salvar e carregar um jogo

[X] criar uma música de fundo e efeitos de som
- Baixar arquivos de som para o jogo
- Criar um módulo `som`
- Modificar a `main` para inicializar o mixer da pygame e começar a música
- Modificar o método `subir_nivel` do `Aventureiro` para tocar um som



[ ] criar sistema de itens
[ ] criar sistema de equipamentos
[ ] outros atributos
[ ] sistema de batalhas por turnos
[ ] habilidades diferentes
[ ] ataques especiais para monstros
[ ] sistema de drop
[ ] mecânica de elementos
[ ] expandir o mapa
[ ] sistema de andares
[ ] sistema de loja no jogo (drop de dinheiro e compra de itens)
[ ] criar um monstro especial que persegue o aventureiro
