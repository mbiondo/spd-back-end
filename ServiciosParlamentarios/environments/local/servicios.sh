#!/bin/bash
LOG=/var/log/ServiciosParlamentarios
LOG_FILE=ServiciosParlamentarios_nohup_`date +%d_%m_%Y`.log

pgrep -f 'localhost:9000' > /dev/null

if [ $? -ne 0 ]; then
	echo $(date) " Servicios Parlamentarios caidos, levantando..." >> $SP_PATH/$LOG_FILE
        nohup python /opt/spd-back-end/ServiciosParlamentarios/manage.py \
        runserver localhost:9000 --noreload >> $SP_PATH/$LOG_FILE 2>&1&
fi
