# SheetToDB
 Convierte tus hojas de calculo CSV en una base de datos en pocos minutos.


## Pasos para ejecutar CLI

- Ejecuta con Python el archivo STD_CLI.py, ubicado en "SheetToDB/STD_CLI.py" y sigue los pasos que aparecen en pantalla.

eje : /python STD_CLI.py

- Ingresa las rutas de los archivos .csv a procesar separados por coma.

eje : C:\Users\wkt\Documents\Data\students.csv, C:\Users\wkt\Documents\Data\studentsGrades.csv, C:\Users\wkt\Documents\Data\studentsAssistance.csv

- Ingresa el nombre de la Base de datos a crear.

eje : Estudiantes_Universidad_SanJuan

- Seleccione opcion de tipo de BD a la que se desea exportar. (Solo Sqlite por ahora)

- Verifique el contenido de su Base de datos

## Requerimientos:

- Python 3.6+
- CSV

## Pendiente:

- Compatibilidad con hojas de Excel
- Connector de Mysql
- Opcion de mandar queries ingresados por el usuario al servidor
- Opcion para borrar celdas no necesarias
- Opcion de edicion de celdas y tipos de datos asociados
- Implementacion de interfaz grafica (GUI)
