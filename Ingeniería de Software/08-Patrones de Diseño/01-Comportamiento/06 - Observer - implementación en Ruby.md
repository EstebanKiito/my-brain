---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[05 - Patrón Observer|Patrón Observer]]"]
---
# Observer: implementación en Ruby

Implementación de referencia de [[05 - Patrón Observer|Observer]]: un sujeto con estado aleatorio y dos observadores que reaccionan según ese estado.

## Código
```ruby
# The Subject interface declares a set of methods for managing subscribers.
# @abtracta
class Subject
  # Attach an observer to the subject.
  def attach(observer)
    raise NotImplementedError
  end

  # Detach an observer from the subject.
  def detach(observer)
    raise NotImplementedError
  end

  # Notify all observers about an event.
  def notify
    raise NotImplementedError
  end
end

# ----------------------- ---------------------- -------------------
class ConcreteSubject < Subject
  # For the sake of simplicity, the Subject's state, essential to all
  # subscribers, is stored in this variable.
  attr_accessor :state

  def initialize
    @observers = []
  end

  # @param [Obserser] observer
  def attach(observer)
    puts 'Subject: Attached an observer.'
    @observers << observer
  end

  # @param [Obserser] observer
  def detach(observer)
    @observers.delete(observer)
  end

  # ------- The subscription management methods ----------
  # Trigger an update in each subscriber.
  def notify
    puts 'Subject: Notifying observers...'
    @observers.each { |observer| observer.update(self) }
  end

  def some_business_logic
    puts "\nSubject: I'm doing something important."
    @state = rand(0..10)

    puts "Subject: My state has just changed to: #{@state}"
    notify
  end
end

# ------------- Observadores ---------------------
class Observer
  # Receive update from subject.
  def update(_subject)
    raise NotImplementedError
  end
end

class ConcreteObserverA < Observer
  def update(subject)
    puts 'ConcreteObserverA: Reacted to the event' if subject.state < 3
  end
end

class ConcreteObserverB < Observer
  def update(subject)
    return unless subject.state.zero? || subject.state >= 2

    puts 'ConcreteObserverB: Reacted to the event'
  end
end

#-------- The client code ---------
subject = ConcreteSubject.new

observer_a = ConcreteObserverA.new
subject.attach(observer_a)

observer_b = ConcreteObserverB.new
subject.attach(observer_b)

subject.some_business_logic
subject.some_business_logic

subject.detach(observer_a)

subject.some_business_logic
```

> [!tip] Complemento — lectura del código
> - `@observers` es la lista de suscriptores; `attach` agrega y `detach` quita.
> - `notify` llama a `observer.update(self)`: **el sujeto se pasa a sí mismo**, así cada observador puede leer `subject.state`.
> - `ConcreteObserverA` reacciona si `state < 3`; `ConcreteObserverB`, si `state` es 0 o mayor o igual a 2.
> - Después de `detach(observer_a)`, la última llamada solo puede hacer reaccionar a B.
> - La salida varía en cada ejecución porque `rand(0..10)` es aleatorio.

## Preguntas de repaso

1. ¿Qué parámetro recibe `update` y por qué?
> [!question]- Respuesta
> El sujeto (`self`), para que el observador pueda consultar el estado que le interesa (`subject.state`).

2. Si el estado cambia a 1, ¿qué observadores reaccionan?
> [!question]- Respuesta
> Solo A (1 < 3). B no, porque 1 no es 0 ni es mayor o igual a 2.

3. ¿Qué cambia después de `subject.detach(observer_a)`?
> [!question]- Respuesta
> A deja de recibir notificaciones; en el siguiente `notify` solo se llama a `update` de B.
