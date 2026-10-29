SELECT

       e.entity_group                    AS grupo,
       e.department_name                 AS departamento,
       e.entity_name                     AS nome,
       e.record_number                   AS registro,
       e.transaction_id                  AS transacao,
       e.start_date                      AS data_inicio,
       e.external_reference              AS referencia_externa,
       e.responsible_person              AS responsavel,
       e.location_name                   AS localizacao

FROM vw_active_entities e

LEFT JOIN entity_details d
       ON d.entity_id = e.entity_id

WHERE e.organization_id = 1
  AND e.end_date IS NULL

ORDER BY
       e.entity_group,
       e.department_name,
       e.entity_name;