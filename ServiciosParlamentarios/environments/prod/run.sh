#!/bin/bash
# ex30a.sh: "Colorized" version of ex30.sh.
DATE_FILE=$(date)
readonly SP_PATH=/var/log/ServiciosParlamentarios
red='\E[1;31m'
green='\E[1;32m'
wipe="\033[1m\033[0m"

if [ -d "$SP_PATH" ]; then
        python manage.py runsslserver --certificate /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.crt --key /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.key --addrport api.hcdn.gob.ar:8000
        #nohup python /opt/servicios_parlamentarios/current_release/ServiciosParlamentarios/manage.py runsslserver --certificate /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.crt --key /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.key --addrport api.hcdn.gob.ar:9000 --noreload >> $SP_PATH/nohup.log 2>&1&
else
        echo -e "$red"
        echo "***Ambiente no configurado***"
        echo "Ejecutar setenv.sh con permisos de root para configurar ambiente, luego ejecutar run.sh (sin permisos de root)."
fi

echo -e "$wipe"