from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .auth_manager import UsuarioManager

# Create your models here.
class CategoriaModel(models.Model):
    # si no especificamos la comlumna ID django lo hara de manera predeterminada
    # con el tipo de dato AutoField y tbn lo colocara como llave primaria
    #https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)# en la bd creara varchar con 50 caracteres de longitud maxima

    class Meta:
        #sirve para definir los atributos de la clase que estamos heredanto directamente para pasarle la metadata sin utilizar el metodo super
        #sirve para modificar la configuracion y comportamiento de esta tabla en la base de datos
        #https://docs.djangoproject.com/en/4.1/ref/models/options/
        db_table = 'categorias'
        #modificamos el ordenamiento al momento de devolver los registros
        #nombre ascendente(A-Z)
        #nombre descendente (Z-A)
        #como ya sabemos que el nombre, jamas se repetira la segunda clausula de ordenamiento ,esta demas porque nunca se realizara
        ordering = ['nombre', 'id']
    
class PlatoModel(models.Model):
   # id = models.AutoField(primary_key=True, null=False)
   nombre = models.CharField(max_length=50, unique=True, null=False)
   precio = models.FloatField()
   disponiblidad = models.BooleanField(default=True)
   #auto_now_add > cada vez que cree un nuevo registro su valor sera la hora y fecha actual del servidor de base de datos por lo que ya no nos tenemos que procupar en colocar fecha
   #db_column > indicar  como se tiene que llamar sta columna en la base de datos solamente si queremos cambiar el nombre del atributo
   fechaCreacion= models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
   #Forma de indicar que accion debe tomar cuando se elimine el "padre"
   #CASCADE > Cuando se elimina una categoria en forma cascada se eliminaran los platos
   #PROTECT > Evita la eliminacion de la categoria si esa tiene platos que dependan de ell, emitira un error ProtectedError
   #RESTRICT Restringe la eliminacion, es lo mismo que el PROTECT solo que emitira un error de tipo RestricedError
   #SET_NULL > permite la eliminacion de la categoria y a los platos que dependan de ella les cambiar su valor NULL
   # SET_DEFAULT > permite la elimacion de la categoria y les cambia el valor a un valor por defecto
   # DO_NOTHING > permite la eliminacion PERO no hace nada osea mantiene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad

   #related_name > sirve para poder acceder a todos los registros dede la otra entidad, es decir desde categoria poder acceder a todos sus platos, si es que no se define su valor ser puesto por django con el nombre  de la clase TODO EN MINUSCULAS seguido de la palabra  
   categoria = models.ForeignKey(to=CategoriaModel, on_delete=models.PROTECT,db_column='categoria_id',related_name='platos')
   
   class Meta:
        db_table ='platos'


#como vamos a modificar el comportamiento de la tabla auth_user de Django entonces tenemos modificar su herencia.
class UsuarioModel(AbstractBaseUser):
    #AbstracBaseUser > me permite modificar todo lo que yo quiera  del modelo auth_user que AbstracUser solamente me permite agregar  nuevas columnas

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    #django hace una validacion para que el correo cumpla con el formato valido
    # xxxx@xxxx.xxx
    correo = models.EmailField(max_length=100)
    password = models.TextField(null=False)
    #choices (opciones)> porque el primero  es con el que se guarda en la base de datos 
    #el segundo es con el que se mostrara al momento de devolver la informacion
    tipoUsuario = models.CharField(max_length=40, choices=[
       ( 'ADMIN','ADMINISTRADOR'),
       ('MOZO', 'MOZO'),
       ('CLIENTE','CLIENTE')
    ])
    # propiedades netas para el panel administrativo
    # sirve para indicar si el usuario que quiere acceder pertenece  o no al equipo de trabajo
    is_staff = models.BooleanField(default=False)

    # sirve para indicar si el usuario es un usuario activo de la empresa
    is_active = models.BooleanField(default=True)

    #sirve para indicar la fecha en la que se creo el usuario
    createdAt = models.DateField(auto_now_add=True, db_column='created-at')

    #para el panel administrativo  para indicar cual es el atributo que debe pedir como nombre de usuario
    USERNAME_FIELD ='correo'

    #son las columnas o los atributos requeridos al momento de crear el superusuario  por consola
    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/ 
    REQUIRED_FIELDS =['nombre','apellido','tipoUsuario']

    objects=UsuarioManager()

    class Meta:
        db_table ='usuarios'
