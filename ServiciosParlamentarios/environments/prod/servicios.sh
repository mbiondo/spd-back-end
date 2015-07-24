#!/bin/bash
SP_PATH=/var/log/ServiciosParlamentarios
LOG_FILE=ServiciosParlamentarios_nohup_`date +%d_%m_%Y`.log
HOST=api.hcdn.gob.ar
PORT=9000

pgrep -f $HOST':'$PORT > /dev/null

if [ $? -ne 0 ]; then
        echo $(date) " Servicios caidos, levantando..." >> $SP_PATH/$LOG_FILE
        nohup python /opt/servicios_parlamentarios/current_release/ServiciosParlamentarios/manage.py \
        runsslserver --certificate /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.crt \
        --key /usr/share/ca-certificates/hcdn/api.hcdn.gob.ar.key \
        --addrport $HOST:$PORT --noreload >> $SP_PATH/$LOG_FILE 2>&1&
fi
 
