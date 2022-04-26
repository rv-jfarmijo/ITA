package lectures.part2oop

object Generics extends App {

  class MyList[+A] {
    // use the type A inside the class definition
    def add[B >: A](element: B): MyList[B] = ???
    /*
      A = Cat
      B = Animal
    */
  }

  val listOfIntegers = new MyList[Int]
  val listOfStrings = new MyList[String]

  // generic methods
  object MyList {
    def empty[A]: MyList[A] = ???
  }
  val emptyListOfIntegers = MyList.empty[Int]

  // variance problem
  class Animal
  class Cat extends Animal
  class Dog extends Animal

  // 1. yes List[Cat] extends List[Animal] = covariance
  class CovariantList[+A]
  val animal: Animal = new Cat
  val animalList: CovariantList[Animal] = new CovariantList[Cat]
  // animalList.add(new Dog) ??? Hard question turns list into something more generic
  // from list of cats to list of animals

  // 2. No list of cat and list of animals 2 different things == INVARIANCE
  class InvariantList[A]
  val invariantAnimalList: InvariantList[Animal] = new InvariantList[Animal]

  // 3. Hell NO CONTRAVARIANCE
  class Trainer[-A]
  val trainer: Trainer[Cat] = new Trainer[Animal]

  // bounded types
  class Cage[A <: Animal] (animal: A)// only accepts generic type A which are subtypes of Animal
  val cage = new Cage(new Dog)

  class Car
//  val newCage = new Cage(new Car) // this won't work because CAr is not a type of Animal


  // expand MyList to be generic

}
