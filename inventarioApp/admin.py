from django.contrib import admin
from .models import Elementos
from .models import Pacientes
from .models import Sedes
from .models import Discapacidad
# Register your models here.



class PacientesAdmin(admin.ModelAdmin):
     list_display= ('id', 'PrimerApellido','SegundoApellido', 'PrimerNombre', 'SegundoNombre', 'FechaNacimiento', 'TipoDocumento','NumeroDocumento','FechaIngreso', 'FechaEgreso',  )
     search_fields= ('id', 'PrimerApellido','SegundoApellido')

  
     

admin.site.register(Elementos, )
admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Sedes)
admin.site.register(Discapacidad)