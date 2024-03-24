# 4 Zadaća

Ovaj folder (`z4_pubsub`) nalazi se u `ros2_ws/src` folderu

## Build

Iz `ros2_ws` foldera pokrenuti

`rosdep install -i --from-path src --rosdistro humble -y`

`colcon build`

`source install/setup.bash`

## Run

U 4 različita terminala pokrenuti

`ros2 run z4_pubsub brojcanik`

`ros2 run z4_pubsub kvadriranje_broja`

`ros2 topic echo /broj`

`ros2 topic echo /kvadrat_broja`


## Napomena
Ovo sam pisao za sebe da kad zaboravim mogu negdje pogledat kak sam to rjesio 😂
