package lectures.part2oop


object MethodNotations extends App {

  class Person(val name: String, favoriteMovie: String, val age: Int = 0) {
    def likes(movie: String): Boolean = movie == favoriteMovie
    def hangOutWith(person: Person): String = s"${this.name} is hanging out with ${person.name}"
    def +(person: Person): String = s"${this.name} is hanging out with ${person.name}"
    def +(nickname: String): Person = new Person(s"$name $nickname", favoriteMovie)
    def unary_! : String = s"$name, what the heck?!"
    def unary_+ : Person = new Person(name, favoriteMovie, age + 1)
    def isAlive: Boolean = true
    def apply(): String = s"Hi, my name is $name and I like $favoriteMovie"
    def apply(n: Int) : String = s"$name watched $favoriteMovie $n times"
    def learns(thing: String) = s"$name is learning $thing"
    def learnsScala = this learns "Scala"
  }
  import scala.language.postfixOps

  //val exitStatus = url #> outfile !


  val mary = new Person("Mary", "Inception")
  println(mary.likes("Inception"))
  println(mary likes "Inception") // equivalent
  // infix notation = operator notation example of syntactic sugar

  // "operators" in Scala
  val tom = new Person("Tom", "Fight Club")
  println(mary hangOutWith tom)
  println(mary + tom)
  println(mary.+(tom))

  println(1 + 2)
  println(1.+(2))

  // ALL OPERATORS ARE METHODS.
  // AKKA actors have ! or ?

  // prefix notation also syntactic sugar
  val x = -1 //- is a unary operator or method
  val y = 1.unary_-
  // unary_prefix only works with -,+, ~, and !

  println(!mary)
  println(mary.unary_!) // same as above notation

  // postfix notation
  println(mary.isAlive)
  println(mary isAlive)

  // apply
  println(mary.apply())
  println(mary())


  /*
  1.  Overload the + operator
      mary + "the rockstar" => new person "Mary(the rockstar)"
  2.  add an age to the Person class
      add a unary + operator => new person with the age +1
      +mary => mary with the age incrementer
  3.  add a "learns" method in the Person class  => "Mary learns Scala"
      add a learnsScala method, calls learns method with "Scala"
      Use it in postfix notation.
  4. overload the apply method
      mary.apply(2) => "Mary watched Inception 2 times"
  */
  println((mary+"the rockstar")()) // calling apply method on expression
  println((+mary).age)
  println(mary learnsScala)
  println(mary(10))
}
