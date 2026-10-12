---
ramo: Ingeniería de Software
tema: Patrones de comportamiento
tags: [ingsoft/patrones, ingsoft/ejercicio, patron/comportamiento, origen/apuntes]
prerrequisitos: ["[[01 - Patrón Strategy|Patrón Strategy]]", "[[06 - Principio abierto-cerrado|Principio abierto-cerrado]]"]
---
# Ejercicio: Strategy para procesador de pagos

Problema de prueba: un procesador de pagos con un `case` por tipo de pago que hay que rediseñar con el patrón Strategy.

## Enunciado
![Ejercicio Strategy - enunciado procesador de pagos](../adjuntos/Ejercicio%20Strategy%20-%20enunciado%20procesador%20de%20pagos.png)

> [!note]- Transcripción del enunciado
> ```ruby
> class PaymentProcessor
>   def initialize(user, amount, payment_type)
>     @user = user
>     @amount = amount
>     @payment_type = payment_type
>   end
>
>   def process_payment
>     case @payment_type
>     when "credit_card"
>       puts "Processing credit card payment for amount: $#{@amount}"
>       # Imagine more complex logic here
>     when "paypal"
>       puts "Processing PayPal payment for amount: $#{@amount}"
>       # Imagine more complex logic here
>     when "bitcoin"
>       puts "Processing Bitcoin payment for amount: $#{@amount}"
>       # Imagine more complex logic here
>     else
>       raise "Unsupported payment type: #{@payment_type}"
>     end
>   end
> end
>
> # Example of use
> payment = PaymentProcessor.new("John Doe", 100.0, "credit_card")
> payment.process_payment
> ```
> - **A. (3 pts)** Explique por qué el código anterior no es abierto para extensiones ni cerrado para modificaciones.
> - **B. (7 pts)** Modifique el código anterior utilizando el patrón strategy.

## Solución
![Ejercicio Strategy - solución procesador de pagos](../adjuntos/Ejercicio%20Strategy%20-%20solución%20procesador%20de%20pagos.png)

> [!note]- Transcripción de la solución (B)
> ```ruby
> class PaymentProcessor
>   def initialize(user, amount, payment_strategy)
>     @user = user
>     @amount = amount
>     @payment_strategy = payment_strategy
>   end
>
>   def process_payment
>     @payment_strategy.charge(@amount)
>   end
> end
>
> class PaymentStrategy
>   def charge(amount)
>     raise NotImplementedError
>   end
> end
>
> class CreditCard < PaymentStrategy
>   def charge(amount)
>     puts "Processing credit card payment for amount: $#{amount}"
>   end
> end
>
> class PayPal < PaymentStrategy
>   def charge(amount)
>     puts "Processing PayPal payment for amount: $#{amount}"
>   end
> end
>
> class BitCoin < PaymentStrategy
>   def charge(amount)
>     puts "Processing Bitcoin payment for amount: $#{amount}"
>   end
> end
>
> # Example of use
> payment = PaymentProcessor.new("John Doe", 100.0, CreditCard.new)
> payment.process_payment
> ```

> [!tip] Complemento — respuesta a la parte A (redacción propuesta)
> No es abierto/cerrado porque, para agregar un medio de pago nuevo (por ejemplo, Apple Pay), hay que **modificar** `process_payment` y agregar otro `when`. No se puede **extender** sin tocar el código existente. Además, toda la lógica de pagos queda en una sola clase (baja cohesión): un cambio en un medio de pago puede romper los otros, y el `case` crece sin control.
>
> Con Strategy, un medio nuevo es solo `class ApplePay < PaymentStrategy` con su `charge`; `PaymentProcessor` no cambia.
>
> ```mermaid
> classDiagram
>   PaymentProcessor o--> PaymentStrategy
>   PaymentStrategy <|-- CreditCard
>   PaymentStrategy <|-- PayPal
>   PaymentStrategy <|-- BitCoin
>   class PaymentProcessor { -user -amount -payment_strategy +process_payment() }
>   class PaymentStrategy { <<abstract>> +charge(amount) }
> ```

## Preguntas de repaso

1. En la solución, ¿quién es el contexto y quiénes son las estrategias?
> [!question]- Respuesta
> El contexto es `PaymentProcessor`; las estrategias son `CreditCard`, `PayPal` y `BitCoin`, que heredan de `PaymentStrategy`.

2. ¿Qué cambia en la firma del constructor y por qué?
> [!question]- Respuesta
> En vez de un string `payment_type`, recibe un objeto `payment_strategy`. Así el procesador delega en el objeto en vez de decidir con un `case`.

3. ¿Qué código hay que escribir para agregar transferencias bancarias?
> [!question]- Respuesta
> Solo `class BankTransfer < PaymentStrategy; def charge(amount) ... end; end`. No se modifica nada existente.
