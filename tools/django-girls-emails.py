#!/usr/bin/env python3

EMAIL_CONFIRMATION = {
    'subject': 'Confirmación: Taller Django Girls en {city}',
    'body': '''Hola!

Te escribimos para comentarte que estás *CONFIRMADA* para participar
en el evento "Taller Django Girls en {city}".

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: {url}

Recordá que necesitás llevar una notebook/laptop para trabajar con
ella durante todo el día ya que no contamos con máquinas en el
auditorio.

Es importante que descargues previamente los recursos necesarios para
poder hacer el taller. Hemos creado un solo archivo para que este
proceso sea mucho más fácil. Descargalo de aquí (116 Mb):

​http://argentinaenpython.com.ar/django-girls/djangogirls-recursos.zip

Como último favor, te pedimos que contestes este email para
confirmarnos que vas a asistir ya que hemos sobrepasado la cantidad de
inscriptos y hemos creado una lista de espera. Entonces, *cualquier
inconveniente* que tengas y no puedas asistir al taller, envianos un
email así otro puede ocupar ese lugar.

Muchas gracias,

--

Manuel Kaufmann -- ​http://argentinaenpython.com.ar/'''
}

EMAIL_WAITING_LIST = {
    'subject': 'Lista de espera: Taller Django Girls en {city}',
    'body': ''' Hola!

Te escribimos para comentarte que estás en *LISTA DE ESPERA* para
participar en el evento "Taller Django Girls en {city}"

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: ​​{url}

Debido a que sobrepasamos el número de inscriptos disponibles para el
lugar, se hizo una selección basada en los formularios de registración
y has quedado en lista de espera.

¿Esto que quiere decir? La lista de espera es para aquellas personas
que quedaron seleccionadas pero que no podemos confirmar debido a la
cantidad de lugares que hay en el aula. En caso de que alguno de los
asistentes confirmados nos informe que no pueda concurrir el día del
taller, nos vamos a poner en contacto con vos para confirmar tu
asistencia.

Sí aún sigues interesada en participar, por favor responde a este
email.

Muchas gracias,

--

Manuel Kaufmann -- ​http://argentinaenpython.com.ar/'''
}

EMAIL_COACH = {
    'subject': 'Guía: Taller Django Girls en {city}',
    'body': '''Hola!

Te escribimos para comentarte que estás *CONFIRMADO* para participar
en el evento "Taller Django Girls en {city}" como *GUÍA /
COACH*. ¡Muchísimas gracias! Este evento no podría ser posible sin tu
ayuda

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: ​{url}

Es importante que nos encontremos todos los que vamos a ser Guías una
media hora antes de comenzar el evento (a las 8 AM será la reunión)
así podemos conocernos y conversar previamente para coordinar cómo
será la jornada completa. Tené en cuenta que la idea de ser guía es
justamente ser eso: un guía, y no "hacer nosotros los ejercicios",
sino ayudarlos a que lo completen ellos solos, motivándolos a
investigar y resolver sus propios problemas a conciencia.

Además, te pedimos que leas la guía que Django Girls ha preparado para
los guías así todos seguimos la misma dinámica para el evento:

​http://coach.djangogirls.org/

Es importante que descargues previamente los recursos necesarios para
que los asistentes realicen el taller y lleves su contenido
descomprimido en un pendrive. Esto nos servirá en caso de tener algún
inconveniente con Internet y/o para acelerar el proceso.

Hemos creado un solo archivo para que este proceso sea mucho más
fácil. Descargalo de aquí (116 Mb):

​http://argentinaenpython.com.ar/django-girls/djangogirls-recursos.zip

Como último favor, te pedimos que contestes este email para
confirmarnos que vas a asistir ya que hemos sobrepasado la cantidad de
inscriptos y hemos creado una lista de espera. Entonces, *cualquier
inconveniente* que tengas y no puedas asistir al taller, envianos un
email.

Muchas gracias,

--

Manuel Kaufmann -- ​http://argentinaenpython.com.ar/'''
}

DATE = 'Sábado 3 de Octubre de 2015'
HOUR = '8:30hs (puntual) a 18:30hs'
PLACE = 'Universidad X, ubicada en calle Y'
CITY = 'Puno'
URL = 'http://argentinaenpython.com.ar/django-girls-puno/'

emails = [EMAIL_CONFIRMATION, EMAIL_WAITING_LIST, EMAIL_COACH]

for email in emails:
    for k, v in email.items():
        print(k.upper())
        print('-' * len(k), end='\n\n')
        print(v.format(
            date=DATE,
            hour=HOUR,
            place=PLACE,
            city=CITY,
            url=URL,
        ), end='\n\n')

    input('Presiona una tecla para ver el siguiente email...')
