from multiprocessing import managers

from task_manager import TaskManager


def print_menu():
    print("\n ----gestor de tareas")   
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():

    manager = TaskManager()
    
    while True:

        print_menu()

        try:            

            choise = int(input("Seleccione una opción: "))

            match choise:
                case 1:
                    description = input("Ingrese la descripción de la tarea: ")
                    manager.add_task(description)
                    
                case 2:
                    manager.list_task()

                case 3:
                    id = int(input("Ingrese el ID de la tarea a marcar como completada: "))
                    manager.complete_tasks(id)

                case 4:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    manager.delete_task(id) 

                case 5:
                    print("Saliendo del programa...")
                    break
                
                case _:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 5.") 

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
     
