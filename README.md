# Social Media (Examen Backend)

Este proyecto de backend lo realicé para la empresa AbhrilSoft. En el cual, predominan las tecnologías Django y Tailwind.
A continuación dejaré la forma correcta de poder ejecutar este proyecto y algunas características notables en el desarrollo.

## Clonar el repositorio a local

Tenemos que seleccionar una ubicación en nuestro ordenador, donde nos sea más cómodo trabajar con este proyecto, posteriormente, se debe ejecutar el siguiente comando:

    git clone https://github.com/JulioAbhril/Social-Media.git

Ahora, tendremos un proyecto como este:

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/8bbf9435-974e-4968-a17a-79453b23a572)

Por el momento se creo un archivo Dockerfile y un archivo docker-compose.yml, sólo que aún existe un bug con respecto al SECRET_KEY

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/233617c1-8921-4c5d-b235-cf65f36b98cf)

Por ese motivo, es necesario ejecutarlo en local, y para poder hacerlo, es recomendable crear un entorno virtual. Ejecuta el siguiente comando:

    python3 -m venv env


Después, activa el entorno virtual desde la terminal con el siguiente comando:

    source env/bin/activate

Ahora que contamos con un entorno aislado, podremos instalar las dependencias necesarias para que el código funcione. Para esto, podemos observar en el directorio, que contamos con un archivo requirements.txt, por lo tanto, ejecuta los siguientes comandos: 

    pip3 install -r requirements.txt

    brew services start postgresql

	brew install libpq
	
### Nota importante

En algunos sistemas operativos no se tiene instalado **pg_config**, en ese caso es necesario lo instales, ya que si no lo haces, te puede aparecer el siguiente error:

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/b824482d-2932-49a8-9ffe-fdec4db9e494)

Para instalarlo, has lo siguiente:
Debian/ ubuntu

    sudo apt-get update sudo apt-get install libpq-dev
   
 
Fedora

    sudo dnf install postgresql-devel

MacOs:
     brew install postgresql



También puedes intentar instalar postgresql antes de los requerimientos.
    sudo apt install postgresql

El motivo es porque psycopg2 es un controlador de PostgreSQL.


	
"si deseas saber más sobre pg":
https://www.postgresql.org/docs/current/app-pgconfig.html

## Instalar PostgresSQL
Dando por hecho que se tiene instalado homebrew, ejecuta el siguiente comando: 

    brew install postgresql



Muy bien... En este momento ya tenemos lo necesario para ejecutar el programa, por motivos de agilizar el proceso de ejecución, se dejó el archivo .env.


#### Crea una base de datos 

El siguiente comando sirve para poder ingresar a la base de datos default de postgres:

    sudo -u postgres psql postgres

En ella podrás crear una nueva base de datos con el siguiente comando:

    create database <nombre_de_la_bd>;

O si tienes un manejador de bd, también lo puedes hacer desde ahí.


## Regresando a Django

Es necesario realizar las migraciones, por lo tanto...
Ejecuta lo siguiente en la terminal estando en el mismo nivel que el archivo manage.py:

    python manage.py makemigrations accounts social_media
    python manage.py migrate

## Ejecuta el servidor

Para poder acceder al servidor de Django, ejecuta el siguiente código:

    python manage.py runserver

Ahora, tendremos un proyecto como este, sólo ingresa la siguiente dirección en tu navegador: 127.0.0.1:8000

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/63579c1b-5472-48f0-8f46-647bef101a6a)


Como lo mencioné al inicio, este proyecto también usa Tailwind, por lo cual, será necesario ejecutar el siguiente comando, para lograr que se activen las clases en el CSS
  

    python manage.py tailwind start
    
El login valida si el usuario y contraseña son correctos
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/d5325141-23f0-4fc1-8713-765cc89fb32c)


Permite recuperar la contraseña
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/bda803d7-b32a-4beb-a6db-22f264bf7fec)

Se logró cierta configuración en settings, además de una función hecha en el views.py de core 

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/cd978c67-169a-4344-b94d-e876aa422f1b)

El reseteo de la contraseña llega por correo, al igual que la confirmación al registrarse por primera vez.
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/ddb79d2b-5cf7-4a86-a7c5-3a635d4c7d61)

Al ingresar:
1: Es el lugar donde podemos postear una imagen con texto o simplemente texto.
2: La opción para editar y para borrar
3: El botón para poder ingresar al perfil del usuario
4: El botón para des-loguear al usuario.

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/7bd6c688-0e91-4733-9ab2-a9643768086c)

Se habilitaron los likes
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/22169b25-c2a4-406f-a4b6-98610d16d306)

En automático al crear un usuario, se carga una foto de perfil y banner por default
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/c35d3efd-3d86-4d62-a67e-9f317f852697)

Se pueden actulizar los datos del usuario
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/5aaf14d4-d419-455a-a055-2fa4c91ac1e2)


Cada aplicación con modelos cuenta con un archivo de test
![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/5d376ea7-4f74-4557-aabd-eacb21e124fd)


En el endpoint :http://127.0.0.1:8000/api/auth/login/ podemos generar nuestro token

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/89b06576-41d5-4d3a-8fd2-e062f87a0b9c)

Puedes utilizar este cliente, sólo ingresa tu usuario y contraseña en formato json:

    {  "username":  "johndoe",  "password":  "mypassword"  }

Estas son las rutas de las apis-rest:

    127.0.0.1:800/api/rest/profile
    127.0.0.1:800/api/rest/post
    127.0.0.1:800/api/rest/image

![image](https://github.com/JulioAbhril/Social-Media/assets/133718524/593a093a-73b6-4c4d-85dc-81ff3048eb26)


# Gracias por llegar hasta aquí ¡Saludos!
