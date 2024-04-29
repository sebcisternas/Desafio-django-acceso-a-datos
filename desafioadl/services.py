from desafioadl.models import *


def recupera_tareas_y_subtareas():
    
    tareas = Tarea.objects.filter(eliminada=False) # selecciona todas las tareas activas (eliminada=False) desde la base de datos
    # itera sobre cada tarea recuperada
    for tarea in tareas:
        subtareas = tarea.subtarea_set.filter(eliminada=False) # filtra todas las subtareas asociadas a la tarea actual
        print(f"Tarea: {tarea.descripcion}")# imprime la descripción de la tarea
        # itera sobre cada subtarea asociada a la tarea actual
        for subtarea in subtareas:
            print(f"  Subtarea: {subtarea.descripcion}")
    return list(tareas)


def crear_nueva_tarea(descripcion):
    # crea una nueva tarea en la base de datos con la descripción proporcionada
    nueva_tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_subtareas()


def crear_subtarea(descripcion, tarea_id):
    # crea una nueva subtarea asociada a la tarea especificada en la base de datos
    nueva_subtarea = SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)
    return recupera_tareas_y_subtareas()


def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id) # obtiene la tarea con el ID especificado de la base de datos
    tarea.eliminada = True # marca la tarea como eliminada estableciendo el campo eliminada en True
    tarea.save()
    return recupera_tareas_y_subtareas()


def elimina_subtarea(subtarea_id):
   
    subtarea = SubTarea.objects.get(pk=subtarea_id) # obtiene la subtarea con el ID especificado de la base de datos
    subtarea.eliminada = True # marca la subtarea como eliminada estableciendo el campo eliminada en True
    subtarea.save()
    return recupera_tareas_y_subtareas()


def imprimir_en_pantalla(tareas):
    for i, tarea in enumerate(tareas, start=1): # itera sobre cada tarea en la lista de tareas proporcionada
        print(f"[{i}] {tarea.descripcion}")# imprime el número de la tarea y su descripción
        for j, subtarea in enumerate(tarea.subtarea_set.filter(eliminada=False), start=1): # filtra y itera sobre cada subtarea asociada a la tarea actual
            print(f".... [{i}.{j}] {subtarea.descripcion}")