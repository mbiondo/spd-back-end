#!/bin/bash
# ex30a.sh: "Colorized" version of ex30.sh.
DATE_FILE=$(date)
readonly SP_PATH=/var/log/ServiciosParlamentarios
red='\E[1;31m'
green='\E[1;32m'
wipe="\033[1m\033[0m"

if [ -d "$SP_PATH" ]; then
        #nohup python manage.py runserver 10.105.5.55:8000 --noreload &> $SP_PATH/nohup_`date +%Y-%m-%d`.out &
        python manage.py runserver
else
        echo -e "$red"
        echo "***Ambiente no configurado***"
        echo "Ejecutar setenv.sh con permisos de root para configurar ambiente, luego ejecutar run.sh (sin permisos de root)."
fi

echo -e "$wipe"

