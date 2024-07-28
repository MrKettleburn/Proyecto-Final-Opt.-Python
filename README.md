Este es un reproductor de música mp3 con un área para jugar con el teclado reproduciendo notas musicales de tres escalas diferentes con un piano y un chelo disponibles. Usted perdona la interfaz de palito profe LOL pero no hubo mucho más que pudiera hacer con tkinter.

El proyecto incluye varias librerías entre ellas tkinter, matplotlib, numpy, os, pygame, pydub, wave. Estas fueron utilizadas, entre otros propósitos, para la interfaz del proyecto, graficar la onda de sonido de una nota musical, acceder a directorios dentro del proyecto con solo poner su dirección, reproducir sonidos y modificar algunas pistas de audio.

A continuación una explicación de los archivos y clases del proyecto:

Main: file donde se inicia el programa

MainScreen: Es la clase que representa la primera pantalla que se ve del proyecto. En ella se puede acceder a las otras dos áreas: la reproducción de música y el juego con las notas. En esta clase se usa tkinter y PIL para el manejo de fotos en la interfaz.

MusicPlayerApp: Es la clase que representa el reproductor en sí, con los métodos que abren las diferentes pantallas. En esta se utilizó pygame para reproducir un sonido de bienvenida.

NoteKeyBoardScreen: Es la clase que representa la pantalla del juego de las notas musicales. En esta se utilizó pygame para reproducir las notas. Matplotlib, numpy y wave se usaron para lo relacionado con extraer los datos de onda de las notas musicales, convertir a archivos .wav los archivos .mp3 y mostrar el gráfico de la onda en un canvas en la interfaz con tkinter. La clase funciona de conjunto con Sounds que tiene un diccionario con otros diccionarios dentro guardando las direcciones de las pistas de las notas musicales. La clase tiene de atributo un diccionario que se sustituye cada vez que se selecciona un instrumento nuevo.

Octavas: Esta clase no participa activamente durante la ejecución dle programa. Fue usada durante el proceso de desarrollo del proyecto para modificar las pistas de las notas musicales. Las que pude conseguir estaban en la escala central y mediante las funciones de este archivo pude elevar y disminuir una escala de cada nota musical al acelerar o aminorar su velocidad de reproducción lo cual alteró su frecuencia de onda e hizo que suenen más agudas o más graves.

PlayScreen: Es la clase que represneta la pantalla donde se reproduce la música. Está vinculada a la carpeta music del proyecto, donde están las pistas a reproducir pero que el usuario puede ampliar a través del botón + encima de la lista de reproducción.

Sounds: Aquí están los diccionarios de sonidos de las notas musicales divididos por instrumentos.