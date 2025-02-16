
```mermaid
classDiagram
  class Context
  Context o-- Strategy : uses
  class Strategy {
    <<abstract>>
    +execute()
  }
  Strategy <|-- ConcreteStrategy1
  Strategy <|-- ConcreteStrategy2
  ConcreteStrategy1: +execute()
  ConcreteStrategy2: +execute()
  ```
  