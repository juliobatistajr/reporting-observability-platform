SELECT
       pi.ds_convenio                                                   AS convenio,
       pi.ds_setor_atendimento                                          AS setor,
       pi.nm_paciente                                                   AS paciente,
       pi.nr_prontuario                                                 AS prontuario,
       pi.nr_atendimento                                                AS atendimento,
       pi.dt_entrada                                                    AS data_atendimento,
       pi.dt_alta                                                       AS data_alta,
       pi.cd_usuario_convenio                                           AS matricula,

       substr(
            pi.nm_medico
            || ' / '
            || obter_especialidade_medico(
                    pi.cd_medico_resp,
                    'D'
               ),
            1,
            200
       )                                                                AS medico_especialidade,

       ma.ds_motivo_alta                                                AS tipo_alta,

       pi.ds_unidade                                                    AS leito

FROM paciente_internado_v pi

LEFT JOIN pessoa_fisica pf
       ON pf.cd_pessoa_fisica = pi.cd_pessoa_fisica

LEFT JOIN motivo_alta ma
       ON ma.cd_motivo_alta = pi.cd_motivo_alta

WHERE pi.cd_estabelecimento = 5
       AND pi.dt_alta >= TRUNC(SYSDATE)
       AND pi.dt_alta <= SYSDATE

ORDER BY
       pi.ds_convenio,
       pi.ds_setor_atendimento,
       pi.nm_paciente