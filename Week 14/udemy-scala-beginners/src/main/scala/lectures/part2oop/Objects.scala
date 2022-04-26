package lectures.part2oop

object Objects {

  //  SCALA DOES NOT HAVE CLASS-LEVEL FUNCTIONALITY ("Static")
  object Person { // type + its only instance
    // "static"/"class"-level functionality
    val N_EYES = 2
    def canFly : Boolean = false

    // factory method (sole purpose is to build new objects)
    def apply(mother: Person, father: Person): Person = new Person("Bobby")
  }
  class Person(val name: String) {
    // instance-level functionality
  }
  // companions (same scope same name)
  def main(args: Array[String]): Unit = {
    println(Person.N_EYES)
    println(Person.canFly)

    // Scala object = SINGLETON INSTANCE
    val mary = new Person("Mary")
    val john = new Person("John")
    println(mary == john)

    val person1 = Person
    val person2 = Person
    println(person1 == person2)

    val bobby = Person(mary, john)
  }
  // Scala applications
  // a scala application is a scala object with a particular definition
  // def main(args: Array[String]): Unit
  // code doesn't run if you don't make it an application
  // or you can put extends App at the beginning of the code
}
