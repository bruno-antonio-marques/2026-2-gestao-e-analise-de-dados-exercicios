@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo ============================================================
echo Criacao da estrutura de diretorios, READMEs e exercicios
echo ============================================================
echo.

for %%A in (
    "00-2026-08-04-apresentacao_do_plano_de_ensino"
    "01-2026-08-11-dados_como_ativo_estrategico_e_introducao_ao_machine_learning"
    "02-2026-08-18-governanca_de_dados_e_ciclo_de_vida_de_machine_learning"
    "03-2026-08-25-coleta_de_dados_e_regressao_linear"
    "04-2026-09-01-organizacao_e_preparacao_dos_dados_regressao_logistica_e_knn"
    "05-2026-09-08-analise_de_dados_dilema_vies-variancia_e_metricas_de_avaliacao"
    "06-2026-09-15-relatorios_kpis_avaliacao_de_modelos_e_arvores_de_decisao"
    "07-2026-09-29-business_intelligence_random_forest_e_ensemble_learning"
    "08-2026-10-06-big_data_e_support_vector_machines"
    "09-2026-10-13-data-driven_decision_making_e_reducao_de_dimensionalidade"
    "10-2026-10-20-modelos_de_gestao_de_riscos_e_tecnicas_de_agrupamento"
    "11-2026-10-27-inteligencia_artificial_analise_preditiva_e_selecao_de_caracteristicas"
    "12-2026-11-03-monitoramento_continuo_melhoria_de_processos_e_ciclo_de_vida_de_modelos_de_machine_learning"
) do (

    echo Criando estrutura da aula: %%~A

    rem README da aula
    call :criar_readme "%%~A"

    rem =========================================================
    rem TURMA TI4P40
    rem =========================================================

    call :criar_aluno "%%~A" "TI4P40" "BRUNO_ANTONIO_MARQUES-F362BF0"
    call :criar_aluno "%%~A" "TI4P40" "CAIO_CESAR_BALBINO_DA_SILVA-R536FA6"
    call :criar_aluno "%%~A" "TI4P40" "ITALO_KEVIN_RODRIGUES_DA_SILVA-R8133G7"
    call :criar_aluno "%%~A" "TI4P40" "RAMON_BORGES_DE_HOLANDA-R854124"
    call :criar_aluno "%%~A" "TI4P40" "ZACK_SALES_LEMOS_SILVA-G86GJA2"

    rem =========================================================
    rem TURMA TI3P40
    rem =========================================================

    call :criar_aluno "%%~A" "TI3P40" "BRYAN_LUCENA_BARBOSA_DA_SILVA-N0296A6"
    call :criar_aluno "%%~A" "TI3P40" "MAYSA_KELLY_DOS_SANTOS_FREITAS-F3648I0"

    echo.
)

echo ============================================================
echo Estrutura criada com sucesso.
echo ============================================================

pause
exit /b


rem =============================================================
rem CRIA ESTRUTURA DO ALUNO
rem =============================================================

:criar_aluno

set "AULA=%~1"
set "TURMA=%~2"
set "ALUNO=%~3"

set "PASTA_TURMA=%AULA%\%TURMA%"
set "PASTA_ALUNO=%PASTA_TURMA%\%ALUNO%"

rem README da turma
call :criar_readme "%PASTA_TURMA%"

rem README do aluno
call :criar_readme "%PASTA_ALUNO%"

rem Cria os 10 exercicios
for /L %%N in (1,1,10) do (

    set "NUM=0%%N"
    set "NUM=!NUM:~-2!"

    set "PASTA_EXERCICIO=%PASTA_ALUNO%\exercicio_!NUM!"

    rem README do exercicio
    call :criar_readme "!PASTA_EXERCICIO!"

    rem Arquivo Python do exercicio
    if not exist "!PASTA_EXERCICIO!\exercicio!NUM!.py" (
        type nul > "!PASTA_EXERCICIO!\exercicio!NUM!.py"
    )
)

exit /b


rem =============================================================
rem CRIA DIRETORIO E README.md
rem =============================================================

:criar_readme

set "DIRETORIO=%~1"

if not exist "%DIRETORIO%" (
    mkdir "%DIRETORIO%"
)

if not exist "%DIRETORIO%\README.md" (
    type nul > "%DIRETORIO%\README.md"
)

exit /b