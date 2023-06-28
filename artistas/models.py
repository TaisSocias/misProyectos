from django.db import models

class Especialidad(models.Model):
    id_especialidad = models.AutoField(db_column='idEspecialidad', primary_key=True)
    especialidad = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.especialidad)

class Artista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    id_especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE, db_column='idEspecialidad')
    id_artista = models.AutoField(db_column='idArtista', primary_key=True)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)

class Obra(models.Model):
    nombre_obra = models.CharField(max_length=40)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='idEspecialidad')
    id_artista = models.ForeignKey(Artista, db_column='idArtista', on_delete=models.CASCADE)
    id_obra = models.AutoField(db_column='idObra', primary_key=True)
    def __str__(self):
        return str(self.id_obra)