# Automated Reporting and Observability Platform

## Objetivo

Automatizar a geração e distribuição de relatórios operacionais a partir de consultas em banco de dados Oracle, incluindo mecanismos de rastreabilidade, monitoramento e observabilidade.

## Principais Recursos

✅ Consulta automatizada de dados Oracle

✅ Geração dinâmica de relatórios HTML

✅ Envio automatizado de e-mails via SMTP

✅ Logs de execução

✅ Controle de concorrência (Lock File)

✅ Histórico de execuções

✅ Base para detecção de anomalias

✅ Integração com Windows Task Scheduler

---

## Arquitetura

```text
Oracle Database
        |
        ▼
   Python ETL
        |
        ▼
 Relatório HTML
        |
        ▼
 SMTP / E-mail
        |
        ▼
 Logs
        |
        ▼
 Histórico de Execuções
        |
        ▼
 Detector de Anomalias
```

---

## Estrutura do Projeto

```text
src/
├── anomaly_detector/
├── templates/
├── sql/
├── logger.py
├── lock_manager.py
├── main.py

output/
logs/
```

---

## Tecnologias

- Python
- Oracle Database
- Pandas
- OpenPyXL
- SMTP
- HTML
- python-dotenv

---

## Segurança

Credenciais são carregadas através de variáveis de ambiente.

Exemplo:

```env
ORACLE_USER=
ORACLE_PASSWORD=

ORACLE_HOST=
ORACLE_PORT=
ORACLE_SERVICE=

EMAIL_USER=
EMAIL_PASSWORD=
```

---

## Observabilidade

O projeto registra métricas operacionais em formato JSON:

```json
{
  "data_execucao": "2026-10-28 16:56:23",
  "grupos_processados": 17,
  "duracao_segundos": 57,
  "status": "SUCESSO"
}
```

As métricas são utilizadas para construção da camada de detecção de anomalias.

---

## Funcionalidades de Confiabilidade

### Lock de Execução

Impede múltiplas execuções simultâneas:

```text
Execução A
✅ Executa

Execução B
🚫 Bloqueada
```

### Logs

Rastreabilidade completa das execuções.

### Histórico de Execuções

Persistência de métricas para monitoramento e análise.

---

## Próximas Evoluções

- Detector de Anomalias
- Identificação de execuções duplicadas
- Detecção de lentidão
- Análise estatística das execuções
- Machine Learning para detecção de comportamentos atípicos

## Visão Geral

docs/image.png