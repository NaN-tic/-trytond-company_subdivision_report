=================================
Empresa. Informes y Subdivisiones
=================================

Disponemos de una nueva relación entre informes y subdivisiones de la empresa para
poder organizar por cada subdivisión el nombre de un directorio para que nos guarde
el informe.

Configuración
=============

Añade un informes y directorios relacionados con cada subdivisión de la empresa
(puede gestionar directamente en informes o en las subdivisiones de la empresa).

Este mòdulo dispone de un nuevo método (report_directory) para obtener el nombre
del directorio según la acción y la subdivisión.

Informes
========

En vuestro módulo, rescribiremos el método "execute" y llamaremos el método "report_directory".

Un diseño en el método "execute" podria ser:
* Si se dispone de directorio en el informe y el usuario dispone de subdivisión en sus prefencias,
  cuando renderizamos el informe se guardará en el directorio (con la extensión).
* Al final, si el informe dispone de la opción "Impresión directa", no devolverá el informe al cliente.

Configuración extra
===================

Configure un "watchdirectory" para la impressión automática a las impresoras.
