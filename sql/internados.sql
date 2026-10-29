SELECT
       pi.ds_convenio                                                   AS convenio,
       pi.ds_setor_atendimento                                          AS setor,
       pi.nm_paciente                                                   AS paciente,
       pi.nr_prontuario                                                 AS prontuario,
       pi.nr_atendimento                                                AS atendimento,
       pi.dt_entrada                                                    AS data_atendimento,
       pi.cd_usuario_convenio                                           AS matricula,
       pi.nm_medico                                                     AS medico,
       pi.ds_unidade                                                    AS leito

FROM paciente_internado_v pi

LEFT JOIN pessoa_fisica pf
       ON pf.cd_pessoa_fisica = pi.cd_pessoa_fisica

WHERE pi.cd_estabelecimento = 5
  AND pi.dt_alta IS NULL

ORDER BY
       pi.ds_convenio,
       pi.ds_setor_atendimento,
       pi.nm_paciente