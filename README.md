# Proyecto Grupo 1

## Pasos para utilizar GitHub:

```bash
cd workspace/src/
git clone https://github.com/brunaldihno/proyecto_grupo_1_2025
cd ..
colcon build --symlink-install
source install/local_setup.bash
```
## Codigos RUN para las actividades:

```bash
ACT2
ros2 run slam_toolbox sync_slam_toolbox_node --ros-args \
  -p odom_frame:=odom \
  -p base_frame:=base_link \
  -p map_frame:=map \
  -p scan_topic:=/scan \
  -p map_update_interval:=1.0 \
  -p max_laser_range:=5.0 \
  -p minimum_travel_distance:=0.1 \
  -p use_scan_matching:=true \
  -p minimum_travel_heading:=1.57 \
  -p do_loop_closing:=true

ros2 run teleop_twist_keyboard teleop_twist_keyboard

ros2 run nav2_map_server map_saver_cli -f my_first_slam_map

ACT3

ros2 run nav2_util lifecycle_bringup amcl

ACT4

ros2 run nav2_util lifecycle_bringup amcl
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
