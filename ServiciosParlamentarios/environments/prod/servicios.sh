#!/bin/bash
SP_PATH=/var/log/ServiciosParlamentarios
LOG_FILE=ServiciosParlamentarios_nohup_`date +%d_%m_%Y`.log

pgrep -f 'api.hcdn.gob.ar:9000' > /dev/null

if [ $? -ne 0 ]; then
        echo $(date) " Servicios caidos, levantando..." >> $SP_PATH/$LOG_FILE
        nohup python /opt/servicios_parlamentarios/current_release/ServiciosParlamentarios/manage.py \
        runsslserver --certificate /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.crt \
        --key /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.key \
        --addrport api.hcdn.gob.ar:9000 --noreload >> $SP_PATH/$LOG_FILE 2>&1&
fi
 
