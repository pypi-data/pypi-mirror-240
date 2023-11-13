# -*- coding: utf-8 -*-
El objetivo de este proyecto es desarrollar una librería para Python que aporte a sus usuarios, facilitando la conversión de distintos tipos de medidas. Estará enfocada sobre todo a datasets con objetivo de poder transformar variables entre unidades de medición.

Funcionalidades:
    - Herencias:
        - Simples: Heredar funciones de una única clase.
        - Múltiples: Heredar funciones de varias clases.
    - Excepciones:
        - Los valores introducidos tienen que ser numéricos.
        - Las unidades introducidas tienen que existir y estar comprendidas en la librería.

Instalación
    -pip install Conversor

Dependencias
    - pip install requests

USO
    - from Conversor import Conversor

    Ejemplo de conversión de longitud
        - conversor = Conversor(value_or_values=df["distancia"], measure_from="M", measure_to="KM")
        - conversor.value_or_values()
        - print(conversor)

    Ejemplo DF
        - conversor = Conversor(value_or_values=df["distancia"], measure_from="M", measure_to="KM")
        - conversor.value_or_values()
        - df["distancia"] = conversor
        - print(df["distancia"])

Autores: Iker Núñez González y Gorka Elorriaga Menendez.