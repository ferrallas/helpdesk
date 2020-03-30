================
Helpdesk Project
================

TODO:
- En la vista formulario de tickets:
-- añadir una solapa para Project, en esa solapa:
--- Poder seleccionar un proyecto o una tarea (tiene que añadir 2 campos m2o a project y task).
--- Si busco la tarea sin indicar el proyecto completar el proyecto de esa tarea (onchange en tarea que complete el projecto)
--- si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto (onchange a project que devuelva un domain)
-- poder agrupar, filtrar por proyecto o tarea (modificar vista search)

- En la vista formulario de tareas del proyecto:
-- añadir una solapa para Tickets, en esa solapa:
--- añadir un listado de tickets asociados a esa tarea (o2m asociado al m2o definido en ticket)

- Mejorar UI, para que:
-- las incidencias se registren en las tareas con un botón (con que datos se va a crear, pasar la tarea y proyecto por contexto)
-- se muestre un smart button con el número de incidencias y si se clicka se redirija.
-- Ver como está hecho en el módulo CRM para crear presupuestos desde leads.


Proceso PR:

- Clonar el proyecto de aeodoo, dos opciones:
  - git clone git@github.com:aeodoocurso/helpdesk.git -b webinar_20200325
  - git clone https://github.com/aeodoocurso/helpdesk.git -b webinar_20200325
- Hacer un fork con vuestro usuario desde la web
- desde el directorio del proyecto puedo añadir mi remote
  git remote -v ; puedo ver mis remotes
  git remote add angelmoya https://github.com/angelmoya/helpdesk-1.git ; añado mi remote
- podría hacer directamente clone de mi proyecto, pero no viene mal tener los dos remotes
- tengo que crear una rama con otro nombre
  git checkout -b webinar_20200325_01
- despues de modificar o añadir código tengo que comitear mis cambios.
  git add .
  git commit -am "IMP ..."
- ahora subo los cambios a la rama de mi repositorio
  git push angelmoya webinar_20200325_01 ; pongo angelmoya porque es el nombre de mi remote
- El PR es como indicamos que queremos subir nuestros cambios al proyecto original,
  - los cambios los hacemos en nuestro proyecto, angelmoya
  - proponermos para subir al proyecto original, aeodoo
  - se hace desde la web:
    - con el enlace que aparece temporalmente en la web
    - o en pull/crear