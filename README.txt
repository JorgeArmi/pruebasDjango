Pruebas con Django y posible Manual para documentar todos los pasos y mejoras que se vayan haciendo.

Lo primero que debemos observar son los models de la aplicación data_jars, donde he considerado que la clave foranea debería ser
el jar, ya que 1 jar va a tener dependencia con varias uuaas y además va a encontrarse, relacionado con un war y un ear por lo que ambos campos,
son hasta el momento un OnetoOneField con este jar con el que van relacionados.Al no determinar un campo en concreto como PrimaryKey django por
defecto coloca un id a todos los campos que hace las veces de clave primaria.

Para poder hacer la visualizació n mas clara en el administrador que trae django por defecto he editado el administrador para cada modelo para poder 
visualizar los campos que sean de nuestro inyteres así como la posibilidad de editarlos o filtrarlos in situ.

En primer luhar para lograr pasarle los datos de la BBDD a la plantilla HTML es necesario, declarara un queryset.
Hay que pasarselo en el contexto y devolverlo con el metodo render para poder  cargar la tabla en el HTML.


