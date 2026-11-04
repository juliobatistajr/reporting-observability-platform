# Automated Reporting & Observability Platform

Projeto de portfólio em Python que demonstra automação de relatórios operacionais, registro de execuções e detecção de anomalias por regras.

> **Escopo:** demonstração técnica, não uma solução pronta para produção. Os exemplos SQL são sintéticos; executar o fluxo completo requer infraestrutura e configurações externas.

## Funcionalidades implementadas

- Consultas SQL em banco Oracle e processamento de dados com Python/Pandas.
- Geração de relatórios HTML e envio por SMTP.
- Logs e histórico de execuções em JSON (data, quantidade de grupos, duração e status).
- Lock file para reduzir o risco de execuções simultâneas.
- Tratamento de falhas por grupo e status `SUCESSO`, `SUCESSO_PARCIAL` ou `FALHA`.
- Detector baseado em regras: quantidade de grupos abaixo do esperado, execução demorada ou status de falha.

**Importante:** o detector é baseado em regras fixas; não utiliza machine learning. O agendamento pode ser configurado externamente com o Windows Task Scheduler.

## Visão da arquitetura

```text
Oracle / consultas SQL
          |
          v
Python + Pandas (processamento por grupo)
          |
          +----> HTML ----> SMTP / e-mail
          |
          +----> Logs + histórico JSON
                         |
                         v
                  Detector por regras
```

## Tecnologias

Python, Oracle Database, SQL, Pandas, OpenPyXL, HTML, SMTP, python-dotenv e Windows Task Scheduler (agendamento externo).

## Organização

- `src/main.py`: orquestração da rotina.
- `src/queries.py` e `sql/`: consultas e carregamento dos dados.
- `src/processador.py`: separação dos dados por grupo.
- `src/email_builder.py` e `src/email_sender.py`: composição e envio.
- `src/logger.py` e `src/lock_manager.py`: rastreabilidade e lock.
- `src/anomaly_detector/`: persistência do histórico e detector por regras.

## Preparação do ambiente

Requer Python, acesso autorizado a uma instância Oracle compatível, configuração de e-mail SMTP e uma planilha local de parâmetros/destinatários.

```bash
git clone https://github.com/juliobatistajr/reporting-observability-platform.git
cd reporting-observability-platform
python -m venv .venv
pip install -r requirements.txt
```

Configure as variáveis de ambiente em um arquivo `.env` local com base em `.env.example`. **Nunca versione credenciais.**

O fluxo principal depende de um arquivo local `config/CONVENIOS_EMAIL.xlsx`, que não é publicado, e de uma conexão Oracle configurada para o ambiente. Os SQLs do repositório são exemplos sintéticos e podem exigir adaptação ao banco utilizado. Portanto, a execução ponta a ponta **não é reproduzível apenas com o clone**.

## Executando o detector isoladamente

O detector pode ser executado a partir da raiz do repositório, utilizando o histórico JSON presente em `src/anomaly_detector/`:

```bash
python -m src.anomaly_detector.detector
```

Regras demonstrativas: menos de 17 grupos, duração acima de 120 segundos ou status `SUCESSO_PARCIAL`/`FALHA`. Esses limites são exemplos e precisam ser adaptados a cada operação.

## Histórico e confiabilidade

Cada execução registra, em JSON, data/hora, grupos processados, duração e status. Se nenhum grupo for processado, o status é `FALHA`. O controle de concorrência é baseado em arquivo local, adequado para demonstrar o conceito, mas não substitui mecanismos robustos de orquestração.

## Segurança e limitações

- Não incluir dados reais, credenciais, destinatários ou artefatos internos.
- Exemplos de consultas e valores são sintéticos.
- O projeto não fornece infraestrutura Oracle/SMTP, dados de teste completos ou ambiente de demonstração autônomo.
- O detector é demonstrativo, baseado na última execução e em limites fixos.
- Para uso em produção seriam necessários testes de integração, gestão de segredos, validações de infraestrutura e controles operacionais adicionais.

## Possíveis evoluções (não implementadas)

Análise estatística do histórico, limites configuráveis, alertas automatizados e detecção de anomalias com modelos de machine learning.
