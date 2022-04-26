package lectures.part3fp

object WhatsAFunction extends App {

  // use functions as first class elements
  // work with funcitons like you would with values
  // problem: coming from object oriented world/ OOP

  val doubler = new MyFunction[Int, Int] {
    override def apply(element: Int): Int = element * 2
  }

  println(doubler(2))

  // function types = Function1[A, B]
  val stringToIntConverter = new Function1[String, Int] {
    override def apply(string: String): Int = string.toInt
  }

  println(stringToIntConverter("3") + 4)

  // Function types Function2[A,B,R] === (A,B) => R
  // ALL SCALA FUNCTIONS ARE OBJECTS

  val adder: ((Int, Int) => Int) = new Function2[Int, Int, Int] {
    override def apply(v1: Int, v2: Int): Int = v1 + v2
  }

  /*
  1. a function whcih takes 2 strings and concatenates
  2. transform MyPredicate and MyTransformer into functions
  3. define a funciton witch takes an int and returns tanother furnciton which takes an int an retunrs an int
  */

  def concatenator: (String, String) => String = new Function2[String, String, String] {
    override def apply(v1: String, v2: String): String = v1 + v2
  }

  println(concatenator("Hello ", "Scala"))

  // higher order function
  // Function1[Int, Function1[Int, Int]]

  val superAdder: Function1[Int, Function1[Int, Int]] = new Function1[Int, Function1[Int, Int]] {
    override def apply(x: Int): Function1[Int, Int] = new Function1[Int, Int] {
      override def apply(y: Int): Int = x + y
    }
  }

  val adder3 = superAdder(3)
  println(adder3(12))
  println(superAdder(4)(13)) // curried function

}


trait MyFunction[A, B] {
  def apply(element: A): B
}