# Proyecto Grupo 1

## Pasos para utilizar GitHub:

```bash
cd workspace/src/
git clone https://github.com/brunaldihno/proyecto_grupo_1_2025
cd ..
colcon build --symlink-install
source install/local_setup.bash
```

## Pasos para actualizar el GitHub:

```bash
cd workspace/src/proyecto_grupo_1_2025
git pull origin main
cd ../..
colcon build --symlink-install
source install/local_setup.bash
```

## Pasos para agregar un archivo:

1. Agregar `archivo.py` en la carpeta `nodes`.  
   Asegurarse de que la línea 1 sea explícitamente:  
   ```python
   #!/usr/bin/env python3
   #
   ```
2. Modificar `CMakeLists.txt` para incluir su archivo en la línea 19.

## Pasos para agregar un launch:

Agregar `launch.xml` en la carpeta `launch`.

## Cómo correr un nodo:

```bash
$ ros2 run proyecto_grupo_1_2025 archivo.py
```

## Cómo lanzar un archivo launch:

```bash
$ ros2 launch proyecto_grupo_1_2025 launch.xml
```
