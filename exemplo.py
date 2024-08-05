#!/usr/bin/python3

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('drone_navigation')

# Serviço de controle de navegação
navigate = rospy.ServiceProxy('navigate', srv.Navigate)

# Serviço de obtenção de telemetria
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

# Serviço de pouso
land = rospy.ServiceProxy('land', Trigger)

def takeoff():
    # Decolar para uma altitude de 1 metro
    navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
    rospy.sleep(5)

def move(x, y, z, speed):
    # Mover o drone para a posição especificada
    navigate(x=x, y=y, z=z, speed=speed, frame_id='body')
    rospy.sleep(5)

def landing():
    # Pousar o drone
    land()
    rospy.sleep(5)

if __name__ == '__main__':
    try:
        takeoff()
        move(1, 0, 0, 0.5)  # Mover 1 metro para frente
        move(0, 1, 0, 0.5)  # Mover 1 metro para a direita
        move(0, 0, 1, 0.5)  # Subir 1 metro
        landing()
    except rospy.ROSInterruptException:
        pass