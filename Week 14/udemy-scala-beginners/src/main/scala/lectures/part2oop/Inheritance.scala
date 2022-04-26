package lectures.part2oop

object Inheritance extends App {

  // single class inheritance (you can only extend one class at a time)
  // can totally lockdown animal with "final" "sealed" locks it to this file
  sealed class Animal {
    // putting private will make it inaccessible to Cat
    // protected makes it only usable within this class and subclasses as in within the method--not callable
    val creatureType = "wild"
//    protected def eat = println("nom nom nom")
    def eat = println("nom nom nom")
    // final def eat = println("nom nom nom")
  }

  class Cat extends Animal {
    def crunch = {
      eat
      println("crunch crunch")
    }
  }

  val cat = new Cat
  cat.crunch

  // constructors
  class Person(name: String, age: Int) {
    def this(name: String) = this(name, 0)
  }
  //if extending a class with parameters, you have to include them.
  // can drop age because of access modifier above
  class Adult(name: String, age: Int, idCard: String) extends Person(name)

  // overriding
//  class Dog(override val creatureType: String) extends Animal{
//    override def eat = println("crunch crunch")
//    // override val creatureType: String = "domestic"
//  }
  // same as below
  class Dog(dogType: String) extends Animal{
    override val creatureType = dogType
    override def eat = {
      super.eat
      println("crunch, crunch")
    }
  }

  val dog = new Dog("canine")
//  dog.eat
  println(dog.creatureType)
  println(cat.creatureType)

  //type substitution (in a broad sense, this is called polymorphism)
  val unknownAnimal: Animal = new Dog("canine")
  unknownAnimal.eat

  //overriding vs. overloading

  // super

  // preventing overrides
  // one way is to use keyword final in method definition
  // can use final on the class to prevent it being extended
  // seal the class (can extend classes in this file but not if it is called in another file)


}