#!/bin/bash
# ex30a.sh: "Colorized" version of ex30.sh.

red='\E[1;31m'
green='\E[1;32m'
wipe="\033[1m\033[0m"

usage="
$(basename "$0") [-h] <ambiente> <version_actual> <version_nueva> <host> <port> -- script para hacer deploy de los Servicios Parlamentarios.

where:
    -h                  muestra esta ayuda
    <ambiente>          {local, desa, prod}
    <version_actual>    versión que esta ejecutandose actualmente en el ambiente
    <version_nueva>     versión nueva que se ejecutará en el ambiente
    <host>              ejemplo: api.hcdn.gob.ar
    <port>              ejemplo: 9000"

while getopts ':hs:' option; do
    case "$option" in
      h) echo -e "$red"
         echo "$usage"
         echo -e "$wipe"
         exit 0
         ;;
    esac
done
shift $((OPTIND - 1))
    
if [ ! $# -eq 5 ]; then
    echo -e "$red"
    echo "$usage"
    echo -e "$wipe"
    exit 0
fi

echo -e "$green"
echo "Comenzando a hacer el deploy en $1."
echo -e "$wipe"

ENVIRONMENT_PATH=/opt/servicios_parlamentarios
RELEASES_PATH=releases

ENVIRONMENT=$1
RELEASE_ACTUAL=release_$2
RELEASE_NUEVA=release_$3
HOST=$4
PORT=$5

#Crear ambiente si no existe
if [ ! -d "$ENVIRONMENT_PATH" ]; then
    sudo mkdir $ENVIRONMENT_PATH
    sudo mkdir $ENVIRONMENT_PATH/$RELEASES_PATH
fi

#Acceder al directorio de ambientes
cd $ENVIRONMENT_PATH

#Stop crontab
sudo service cron stop

#Detener la aplicacion
sudo pkill -f $HOST:$PORT

#Mover version anterior a /releases
if [ -d "$RELEASE_ACTUAL" ]; then
    sudo mv $RELEASE_ACTUAL $ENVIRONMENT_PATH/$RELEASES_PATH/$RELEASE_ACTUAL
fi

#Crear nueva carpeta de la release actual (parametro)
sudo mkdir $RELEASE_NUEVA

#Acceder al directorio del nuevo release
cd $ENVIRONMENT_PATH/$RELEASE_NUEVA

#git clone del proyecto
sudo git clone https://github.com/DSDP/spd-back-end.git

#remove .git
sudo rm -rf spd-back-end/.git

#Move files by environment (desa, prod, local)
sudo cp spd-back-end/ServiciosParlamentarios/environments/$ENVIRONMENT/run.sh spd-back-end/ServiciosParlamentarios/environments/$ENVIRONMENT/setenv.sh spd-back-end/ServiciosParlamentarios/.
sudo cp spd-back-end/ServiciosParlamentarios/environments/$ENVIRONMENT/*.py spd-back-end/ServiciosParlamentarios/ServiciosParlamentarios/.
sudo cp spd-back-end/ServiciosParlamentarios/environments/$ENVIRONMENT/servicios.sh $ENVIRONMENT_PATH/.

#remove environment folder
sudo rm -rf spd-back-end/ServiciosParlamentarios/environments

#Setear environment
sudo spd-back-end/ServiciosParlamentarios/environments/$ENVIRONMENT/setenv.sh

#Editar servicios.sh con VERSION nueva
sudo sed -i '9s/.*/    nohup python \/opt\/servicios_parlamentarios\/'$RELEASE_NUEVA'\/spd-back-end\/ServiciosParlamentarios\/manage.py \\/' $ENVIRONMENT_PATH/servicios.sh

#Dar permisos de ejecución luego de modificar
sudo chmod +x $ENVIRONMENT_PATH/servicios.sh

#Restart crontab
sudo service cron restart

echo -e "$green"
echo "El script ha terminado de realizar el deploy en $1."
echo -e "$wipe"
