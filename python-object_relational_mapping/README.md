|| Spanish Version ||
=====================

¿Qué es un ORM ??
===

El mapeo objeto-relacional (ORM) es una técnica de programación utilizada para acceder a una base de datos. Expone su base de datos en una serie de objetos. No tiene que escribir comandos SQL para insertar o recuperar datos, usa una serie de atributos y métodos adjuntos a objetos.

Puede parecer complejo e innecesario, pero pueden ahorrarle mucho tiempo y ayudarlo a controlar el acceso a su base de datos..

Aquí hay un ejemplo. Diga que cada vez que inserte una contraseña en su base de datos, la eliminará, como se explica en la seguridad de la contraseña del sitio web Cada sitio web seguro lo hace con su contraseña Todo sitio web seguro lo hace con su contraseña ¿Alguna vez se ha preguntado cómo los sitios web mantienen su contraseña a salvo de los datos? infracciones? Lee mas . Esto no es un problema para casos de uso simple: usted hace el cálculo antes de insertarlo. ¿Pero qué sucede si necesita insertar un registro en muchos lugares del código? ¿Qué pasa si otro programador se inserta en su mesa y usted no sabe nada??

Al utilizar un ORM, puede escribir código para asegurarse de que siempre y cuando se acceda a cualquier fila o campo de su base de datos, se ejecute primero su otro código personalizado..


-----------------
importante
==========
-----------------

<h2>Orms</h2>
Que es?

El mapeo objeto-relacional (más conocido por su nombre en inglés, Object-Relational mapping, o sus siglas O/RM, ORM, y O/R mapping) es una técnica de programación para convertir datos entre el sistema de tipos utilizado en un lenguaje de programación orientado a objetos y el utilizado en una base de datos relacional, utilizando un motor de persistencia. En la práctica esto crea una base de datos orientada a objetos virtual, sobre la base de datos relacional. Esto posibilita el uso de las características propias de la orientación a objetos (básicamente herencia y polimorfismo). Hay paquetes comerciales y de uso libre disponibles que desarrollan el mapeo relacional de objetos, aunque algunos programadores prefieren crear sus propias herramientas ORM.

<a href:"https://es.wikipedia.org/wiki/Mapeo_objeto-relacional">mas información en wikipedia</a>
<h2>Threads relacionados en PyAr</h2>

<a href:"http://thread.gmane.org/gmane.org.user-groups.python.argentina/53971">Que ORM python me recomiendan?</a>
<h2>Alternativas</h2>
<h3>Sqlalchemy</h3>

SQLAlchemy es el toolkit SQL python y mapeador objeto relacional que provee a desarrolladores con el poder completo y la flexibilidad de SQL.

Provee un conjunto completo de conocidos patrones de persistencia de nivel enterprise, diseniados para acceso a base de datos eficiente y de alta performance, adaptado en un lenguaje de dominio especifico simple y pitonico.

<a href:"http://www.sqlalchemy.org/">Pagina del proyecto<a>
Notas

    MarianoGuerra: muy poderoso, pero a veces muy complejo para lograr cosas simples. A mi entender el mas mantenido y completo de todos los ORMs independientes de un framework.

SQLObject

SQLObject es un gestor objeto relacional que provee interfaces de objetos a tu base de datos con tablas como clases, filas como instancias y columnas como atributos.

SQLObject incluye un lenguaje de consultas basado en objetos Python que hace SQL mas abstracto, y provee independencia sustancial de la base de datos para aplicaciones.

<a href:"http://www.sqlobject.org/">Pagina del proyecto</a>
<h3>Elixir</h3>

Elixir es una capa declarativa sobre la librería SQLAlchemy, es una capa bastante fina, que provee la habilidad de crear simples clases en python que mapean directamente a tablas de una base de datos relacionales (este patrón es conocido como el patrón de disenio Active Record), proveyendo muchos de los beneficios de las bases de datos tradicionales sin perder la conveniencia de los objetos python.

Elixir tiene la intención de reemplazar la extensión ActiveMapper de SQLAlchemy, y el proyecto TurboEntity pero no intena reemplazar las características básicas de SQLAlchemy, en su lugar se enfoca en proveer una sintaxis mas simple para definir modelos de objetos cuando no necesitas la expresividad del mapeo manual de definiciones de SQLAlchemy.

<a href:"http://elixir.ematia.de/trac/wiki">Pagina del proyecto</a>
Notas

    MarianoGuerra: una herramienta muy útil para facilitar el uso de SQLAlchemy, según tengo entendido no esta siendo activamente mantenido.

