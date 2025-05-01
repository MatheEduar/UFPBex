# UFPBex

- Se trata de um projeto para a matéria de Métodos de Projeto de Software

## Padrões de projeto utilizados

### Singleton

- Aplicação no projeto: Utilizado para garantir que a fachada (FacadeSingleton) seja instanciada apenas uma vez durante toda a execução da aplicação.

- Função: Centraliza e controla o acesso às instâncias dos repositórios e serviços, evitando duplicações e mantendo o estado global da aplicação.

### Factory method

- Aplicação no projeto: Implementado na RepositoryFactory, responsável por criar instâncias concretas como CursoRepositoryImpl.

- Função: Desacopla a criação de objetos dos seus usos, permitindo trocar implementações sem mudar quem consome.

### Facade

- Aplicação no projeto: A FacadeSingleton atua como uma fachada para orquestrar interações entre camadas como Controllers, Services e Repositories.

- Função: Fornece uma interface unificada para um conjunto de interfaces em um subsistema, simplificando a complexidade da lógica de negócio.

### Dao

- Aplicação no projeto: Classes como CursoDAOImpl e UserDAOImpl encapsulam a lógica de acesso a arquivos JSON.

- Função: Separa a lógica de persistência de dados (armazenamento/recuperação) da lógica de negócio. Garante flexibilidade e testabilidade.

### Adapter

- Aplicação no projeto: Usado para redirecionar notificações para diferentes meios (como print no terminal ou logging).

- Função: Permite que diferentes formas de saída (terminal, logs, etc.) se integrem a um sistema comum de notificação, adaptando interfaces incompatíveis.

### Observer

- Aplicação no projeto: Observadores (como PrintObserver e LoggerObserver) são notificados quando há atualizações nos cursos.

- Função: Implementa uma comunicação reativa entre os objetos — quando um curso é atualizado, todos os observadores registrados são notificados automaticamente.

### Memento

- Aplicação no projeto: O CursoDAOImpl utiliza CursoMemento para salvar e restaurar o estado da lista de cursos.

- Função: Permite desfazer alterações ou restaurar estados anteriores sem violar o encapsulamento da classe.

### Builder

- Aplicação no projeto: CursoBuilder constrói instâncias de Curso com uma interface fluente.

- Função: Facilita a criação de objetos complexos, melhorando a legibilidade e evitando construtores com muitos parâmetros.

### Command

- Aplicação no projeto: Está sendo usado para encapsular ações como criar, atualizar ou deletar cursos/usuários em objetos de comando.

- Função: Permite encapsular requisições como objetos, facilitando undo/redo, log de comandos e filas de execução.

### Template Method

- Aplicação no projeto: Está sendo usado no relatorio_pdf e no relatorio_html.

- Função: Define o esqueleto de um algoritmo em uma superclasse, permitindo que subclasses personalizem etapas específicas sem alterar a estrutura geral.

---

## Intalações:

### Baixando o venv:

```bash
python -m venv venv
```
### Ativando o venv no windows

```bash
venv\Scripts\activate
```
- Se estiver no VScode não se esqueça de mudar o ambiente de execução

### Baixando as bibliotecas

```bash
pip install -r requirements.txt
```
