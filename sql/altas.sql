SELECT

       e.entity_group                    AS grupo,
       e.department_name                 AS departamento,
       e.entity_name                     AS nome,
       e.record_number                   AS registro,
       e.transaction_id                  AS transacao,
       e.start_date                      AS data_inicio,
       e.end_date                        AS data_fim,
       e.external_reference              AS referencia_externa,

       SUBSTR(
            e.responsible_person
            || ' / '
            || fn_responsible_area(
                    e.responsible_id,
                    'A'
               ),
            1,
            200
       )                                 AS responsavel_area,

       s.status_description              AS status_final,

       e.location_name                   AS localizacao

FROM vw_active_entities e

LEFT JOIN entity_details d
       ON d.entity_id = e.entity_id

LEFT JOIN entity_status s
       ON s.status_id = e.status_id

WHERE e.organization_id = 1
  AND e.end_date >= CURRENT_DATE
  AND e.end_date <= CURRENT_DATE

ORDER BY
       e.entity_group,
       e.department_name,
       e.entity_name;