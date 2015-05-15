@echo off
echo REVERT_DB 1.0 (Alexei Martchenko, 15/04/15)
echo Revertendo Banco "%~n1%~x1"...
"%ProgramFiles%\Winrar\winrar.exe" e -inul -y %1 %TEMP%
set unzipped=%TEMP%\%~n1
set dbname=%~n1
set dbname=%dbname:~3,11%
echo Unzipped %dbname% backup to %unzipped%
echo Dropando DB antigo...
"%ProgramFiles%\PostgreSQL\9.2\bin\dropdb" -U postgres %dbname%
echo Recriando...
"%ProgramFiles%\PostgreSQL\9.2\bin\psql" -U postgres -c "CREATE DATABASE %dbname% WITH OWNER = %dbname%user ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'Portuguese_Brazil.1252' LC_CTYPE = 'Portuguese_Brazil.1252' CONNECTION LIMIT = -1;"
echo Restaurando...
"%ProgramFiles%\PostgreSQL\9.2\bin\psql" -U %dbname%user -d %dbname% -f "%unzipped%"
echo Limpando Temps...
del "%unzipped%"
echo DONE.


