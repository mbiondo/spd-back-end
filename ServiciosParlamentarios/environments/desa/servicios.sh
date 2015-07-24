#!/bin/bash
SP_PATH=/var/log/ServiciosParlamentarios
LOG_FILE=ServiciosParlamentarios_nohup_`date +%d_%m_%Y`.log
HOST=srv-sparl-5.hcdn.gob.ar
PORT=8000

pgrep -f $HOST':'$PORT > /dev/null

if [ $? -ne 0 ]; then
	echo $(date) " Servicios Parlamentarios caidos, levantando..." >> $SP_PATH/$LOG_FILE
        nohup python /opt/spd-back-end/ServiciosParlamentarios/manage.py \
        runserver $HOST:$PORT --noreload >> $SP_PATH/$LOG_FILE 2>&1&
fi