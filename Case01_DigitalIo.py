import RPi.GPIO as GPIO #Llamar la libreria que permite utilizar los pines GPIO, y renombrarla de una manera mas simple
import time #Llamar a la libreria que permite trabajar con funciones de manejo de tiempo

PIN_BOTON = 3
PIN_LED = 7

estadoBoton = 0 #Inicializar una variable para alternar el estado del boton

GPIO.setmode(GPIO.BOARD) #Configurar los pines de la raspberry segun la numeracion fisica
GPIO.setup(PIN_LED, GPIO.OUT) #Configurar el pin fisico 7 como salida
GPIO.setup(PIN_BOTON, GPIO.IN) #Configurar pin fisico 3 como entrada


while True: #ciclo infinito (void loop)
	estadoBoton = GPIO.input(PIN_BOTON) #Leer entrada digital
	GPIO.output(7, estadoBoton) # enviar el estado de el boton al pin 7 (digitalWrite)
	
	if estadoBoton == 1: #Si el boton esta presionado entonces:
		print("ENCENDIDO") #imprimir mensaje de encendido
		time.sleep(1) # realizar una pausa de 1 seg
	else: #si no esta encendido, entonces:
		print("APAGADO") # esta apagado
		time.sleep(1) 
