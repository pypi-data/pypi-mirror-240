# Librer&iacute;a PyPiston

Esta librer&iacute;a Python facilita la interacci&oacute;n con una API de b&uacute;squeda de informaci&oacute;n sobre coches, permitiendo gestionar datos de clientes, coches y reservas. Aqu&iacute; se presenta un resumen de las clases clave y sus funciones.

## Clase Cliente
La clase `Cliente` representa clientes con informaci&oacute;n b&aacute;sica, incluyendo edad, nombre, residencia y una lista opcional de permisos. Proporciona m&eacute;todos para comprobar la mayor&iacute;a de edad, a&nacute;adir permisos y mostrar los datos del cliente en la consola.

## Clase ClienteExt
La clase `ClienteExt` extiende la informaci&oacute;n de la clase `Cliente`, agregando detalles como la vigencia del permiso, necesidades especiales, compromiso medioambiental y nivel del cliente. Adem&aacute;s, ofrece funciones para verificar la vigencia del permiso, añadir necesidades especiales y mostrar los datos del cliente extendido.

## Clase Coche
La clase `Coche` representa un coche deseado y proporciona funciones para buscar informaci&oacute;n sobre coches en una API. Permite la especificaci&oacute;n de criterios de b&uacute;squeda como marca, modelo, a&nacute;o, etc. Los resultados se presentan en una tabla.

## Clase Reserva
La clase `Reserva` permite realizar reservas de coches por parte de clientes extendidos. Hereda funcionalidades de las clases `ClienteExt` y `Coche`, y su m&eacute;todo `realizar_reserva` verifica la elegibilidad del cliente antes de confirmar la reserva.

## Ejemplo de Uso
El script al final del archivo ejemplifica la funcionalidad completa de la librer&iacute;a, desde la creaci&oacute;n de instancias hasta la realizaci&oacute;n de reservas, demostrando la interacci&oacute;n efectiva con la API de b&uacute;squeda de coches.

*Nota*: Se incluye la clave de la API necesaria para acceder a la funcionalidad de b&uacute;squeda de coches en la API correspondiente. Aseg&uacute;rese de mantener la confidencialidad de esta clave.

¡Disfrute utilizando esta librer&iacute;a para gestionar f&aacute;cilmente reservas de coches y explorar informaci&oacute;n detallada sobre veh&iacute;culos!