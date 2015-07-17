#!/bin/bash
LOG=/var/log/ServiciosParlamentarios
LOG_FILE=ServiciosParlamentarios_nohup_`date +%d_%m_%Y`.log

pgrep -f 'srv-sparl-5.hcdn.gob.ar:8000' > /dev/null

if [ $? -ne 0 ]; then
	echo $(date) " Servicios Parlamentarios caidos, levantando..." >> $SP_PATH/$LOG_FILE
        nohup python /opt/spd-back-end/ServiciosParlamentarios/manage.py \
        runserver srv-sparl-5.hcdn.gob.ar:8000 --noreload >> $SP_PATH/$LOG_FILE 2>&1&
fi
