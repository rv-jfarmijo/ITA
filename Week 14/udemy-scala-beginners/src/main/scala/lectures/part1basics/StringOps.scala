package lectures.part1basics

object StringOps extends App {

  val str: String = "Hello, I am learning Scala"

  println(str.charAt(2))
  println(str.substring(7,11))
  println(str.split(" ").toList)
  println(str.startsWith("Hello"))
  println(str.replace(" ", "-"))
  println(str.toLowerCase())
  println(str.length)

  val aNumberString = "43"
  val aNumber =  aNumberString.toInt
  println('a' +: aNumberString :+ 'z')
  // appending and prepending operator are Scala specific
  println(str.reverse)
  println(str.take(2))

  // Scala specific: string Interpolators

  // S-interpolators
  val name = "David"
  val age = 12
  val greeting = s"Hello, my name is $name and I am $age years old."
  println(greeting)
  val anotherGreeting = s"Hello, my name is $name and I will be turning ${age + 1} years old."
  println(anotherGreeting)

  // F-interpolators

  val speed = 1.2f
  val myth = f"$name%s can eat $speed%2.2f burgers per minute."
  // %s means string format. %2.2f means float with two characters total with 2 decimals precision
  println(myth)

  // raw-interpolator
  println(raw"This is \n newline")
  val escaped = "This is a \n newline"
  println(raw"$escaped")
  // ignores escaped characters inside raw string but escaped characters can be injected

}
