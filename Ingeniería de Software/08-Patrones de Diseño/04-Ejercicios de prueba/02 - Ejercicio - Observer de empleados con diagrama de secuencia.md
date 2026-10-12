---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, ingsoft/ejercicio, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[05 - Patrón Observer|Patrón Observer]]", "[[06 - Diagrama de secuencia UML|Diagrama de secuencia UML]]"]
---
# Ejercicio: Observer de empleados con diagrama de secuencia

Ejercicio de prueba que combina el **patrón Observer** con un **diagrama de clases** y un **diagrama de secuencia**: un `Employee` observado por `JobsLog` y `SalariesLog`.

## Ejercicio de prueba (método observador + diagrama de secuencia): enunciado
![Ejercicio Observer - enunciado empleados](../adjuntos/Ejercicio%20Observer%20-%20enunciado%20empleados.png)

> [!note]- Transcripción del enunciado
> Se ha construido un trozo de código que usa un patrón observador para vigilar y actuar frente a cambios en el sujeto, que en este caso es un objeto de la clase `Employee`. Los empleados tienen solo 3 atributos: *name*, *job* y *salary*. Los observadores son instancias de 2 clases, `JobsLog` y `SalariesLog`, y se activan cuando el sujeto cambia:
> - `JobsLog` imprime el nuevo cargo: `*** Pepe es un analista ***`
> - `SalariesLog` imprime el nuevo sueldo: `*** el sueldo de Pepe es 1.000.000 ***`
>
> ```ruby
> jaime = Employee.new('Jaime', 'Programador Junior', 1000000)
> jobslog = JobsLog.new
> salarieslog = SalariesLog.new
> jaime.add_observer( jobslog )
> jaime.add_observer( salarieslog )
> jaime.job = "Programador"
> jaime.salary = 1500000
> jaime.delete_observer( jobslog )
> jaime.job = "Programador Senior"
> jaime.salary = 2000000
> ```
> Output:
> ```
> *** Jaime es un Programador ***
> *** el sueldo de Jaime es  1000000 ***
> *** Jaime es un Programador ***
> *** el sueldo de Jaime es  1500000 ***
> *** el sueldo de Jaime es  1500000 ***
> *** el sueldo de Jaime es  2000000 ***
> ```
> a) Escriba las clases `Employee`, `SalariesLog` y `JobsLog` y dibuje el diagrama de clases correspondiente.
> b) Dibuje un diagrama de secuencia que ilustre toda la secuencia de prueba y que permita explicar el output generado.

## Solución
![Ejercicio Observer - solución código](../adjuntos/Ejercicio%20Observer%20-%20solución%20código.png)

![Ejercicio Observer - solución diagrama de secuencia](../adjuntos/Ejercicio%20Observer%20-%20solución%20diagrama%20de%20secuencia.png)

> [!note]- Transcripción de la solución
> ```ruby
> class Employee
>   attr_reader :name, :job
>   attr_reader :salary
>   def initialize( name, title, salary )
>     @name = name
>     @job = job            # (ver aviso: debería ser title)
>     @salary = salary
>     @observers = []
>   end
>   def salary=(new_salary)
>     @salary = new_salary
>     notify_observers
>   end
>   def job=(new_job)
>     @job = new_job
>     notify_observers
>   end
>   def notify_observers
>     @observers.each do |observer| observer.update(self) end
>   end
>   def add_observer(observer)
>     @observers << observer
>   end
>   def delete_observer(observer)
>     @observers.delete(observer)
>   end
> end
>
> class JobsLog
>   def update( changed_employee )
>     puts("*** #{changed_employee.name} es un #{changed_employee.job} ***")
>   end
> end
>
> class SalariesLog
>   def update( changed_employee )
>     puts("*** el sueldo de #{changed_employee.name} es  #{changed_employee.salary} ***")
>   end
> end
> ```
> **b)** Diagrama de secuencia: el cliente hace `new` de `jaime:Employee`, `jobslog:JobsLog` y `salarieslog:SalariesLog`, y luego dos `add_observer`. `job=` provoca `notify_observers` (self-call), que hace `update` a jobslog y a salarieslog. `salary=` hace lo mismo. Después viene `delete_observer` (X en la línea de vida de jobslog). Los siguientes `job=` y `salary=` llaman a `notify_observers`, que solo hace `update` a salarieslog.
>
> *"Observar que hay 6 veces que se invoca un update: dos para cada uno de los dos observadores primero, y luego dos para el observador de sueldos que queda después de eliminar el de jobs."*

> [!warning] Posible error en la solución (registrado en `_meta/DUDAS.md`)
> `initialize(name, title, salary)` hace `@job = job`. `job` no es el parámetro (se llama `title`), así que llama al getter `job`, que en ese momento devuelve `nil`. Debería ser `@job = title`. No cambia el output del ejercicio, porque el cargo se imprime solo después de `job=`. La X en la línea de vida de jobslog representa que **deja de observar**, no que el objeto se destruya.

> [!tip] Complemento — diagrama de clases (parte a)
> ```mermaid
> classDiagram
>   class Employee { +name +job +salary -observers +job=(new_job) +salary=(new_salary) +add_observer(o) +delete_observer(o) -notify_observers() }
>   class JobsLog { +update(changed_employee) }
>   class SalariesLog { +update(changed_employee) }
>   Employee o--> JobsLog : observers
>   Employee o--> SalariesLog : observers
> ```
> Un diseño más limpio agrega una clase abstracta `Observer` con `update` y hace que `JobsLog` y `SalariesLog` hereden de ella. Así `Employee` se asocia con una sola interfaz.

## Preguntas de repaso

1. ¿Por qué aparece dos veces "el sueldo de Jaime es 1500000"?
> [!question]- Respuesta
> Porque cada cambio, de cargo o de sueldo, notifica a todos los observadores. El `job = "Programador Senior"` también hace que SalariesLog imprima el sueldo vigente (1500000).

2. ¿Por qué no aparece "Jaime es un Programador Senior"?
> [!question]- Respuesta
> Porque antes de ese cambio se ejecutó `delete_observer(jobslog)`: JobsLog ya no recibe notificaciones.

3. ¿Cuántas veces se llama a `update` en total?
> [!question]- Respuesta
> 6: 2 cambios × 2 observadores mientras ambos están suscritos (4), más 2 cambios × 1 observador después del `delete_observer` (2).
