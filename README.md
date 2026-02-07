# Analisa-o-Documento-e-o-texto-e-retorna-resumo-e-principais-pontos-com-LangChain-e-Groq
Propósito do projeto
- Este projeto tem como objetivo demonstrar como integrar Inteligência Artificial a fluxos reais de backend, permitindo que a IA leia arquivos de texto automaticamente e gere análises estruturadas a partir do conteúdo.
- O sistema transforma arquivos .txt em insumos para modelos de linguagem, simulando cenários comuns em aplicações corporativas, como análise de documentos, relatórios e textos extensos.


Como a IA responde
A IA recebe o conteúdo do arquivo como texto bruto, processado previamente pelo Python, e retorna:
- Um resumo do conteúdo
- Uma lista com os principais pontos abordados
A resposta é gerada com base em um PromptTemplate, garantindo consistência e reutilização do formato da análise.


Tecnologias e conceitos utilizados
- Python
- LangChain
- Groq (LLaMA 3.1)
- PromptTemplate
- Leitura de arquivos (File I/O)
- Caminhos absolutos
- Prompt Engineering
- Integração com LLM
- Variáveis de ambiente (.env)

Estrutura do projeto
projeto/
├── analisador_documento_ia.py
├── dados.txt
├── .env
└── README.md


Destaque técnico:
- O uso de caminhos absolutos garante que o script funcione corretamente em qualquer ambiente (IDE, terminal ou servidor).

Como executar o projeto
  1.) Clone o repositório:

        git clone https://github.com/seu-usuario/analisador-documentos-langchain

  2.) Instale as dependências:

        pip install langchain langchain-groq python-dotenv

  3.) Configure o arquivo .env:

        GROQ_API_KEY=sua_chave_aqui

  4.) Execute o script:

        python analisador_documento_ia.py

Alterando o texto analisado
- Para analisar outro conteúdo, basta editar o arquivo dados.txt.
- O sistema continuará funcionando da mesma forma, independentemente do tamanho ou do tema do texto, mantendo o mesmo padrão de resposta.

Por que este projeto é relevante?
- Porque ele demonstra uso prático de IA aplicada a dados reais, indo além de prompts fixos.
- Aqui você mostra que sabe:
  * Ler arquivos corretamente
  * Preparar dados para um LLM
  * Arquitetar prompts reutilizáveis
  * Integrar IA a fluxos de backend
  * Criar soluções aplicáveis a cenários reais
- Esse padrão é base para:
  * Análise de contratos
  * Leitura de currículos
  * Resumo de relatórios
  * Processamento de documentos corporativos

Resumo profissional
- Projeto em Python utilizando LangChain e Groq para análise automática de documentos de texto.
- O sistema lê arquivos .txt, envia o conteúdo para um modelo de linguagem e retorna resumos e pontos-chave, aplicando boas práticas de Prompt Engineering e integração com LLMs em aplicações backend.
