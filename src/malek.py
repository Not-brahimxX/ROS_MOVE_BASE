import RPi.GPIO as GPIO
import os
import rospy
import signal
import sys

# Définir le pin GPIO
pin = 12

# Configurer le mode du GPIO
GPIO.setmode(GPIO.BOARD)

# Configurer le GPIO en entrée
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Fonction de gestionnaire de signal pour intercepter le signal SIGINT
def handler(sig, frame):
    print("ctrl+c detecter")
    # Arrêter tous les nodes ROS
    rospy.signal_shutdown("ctrl+c detecter")
    # Arrêter le roscore
    os.system('killall roscore')
    # Quitter le programme
    sys.exit(0)

# Associer la fonction de gestionnaire de signal au signal SIGINT
signal.signal(signal.SIGINT, handler)

# Démarrer le roscore
os.system('roscore &')

# Attendre que l'état du GPIO soit bas
while GPIO.input(pin) == GPIO.HIGH:
    pass

# Chemin vers notre fichier launch
robot2_path = "roslaunch launcher robot2.launch"

# Lancer le fichier launch
os.system(robot2_path)

# Attendre que le fichier launch se termine
rospy.spin()

