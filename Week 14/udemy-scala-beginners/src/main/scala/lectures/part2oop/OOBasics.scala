package lectures.part2oop

object OOBasics extends App {

  val person = new Person("John", 26)
  println(person.x)
  person.greet("Daniel")


  val author = new Writer("Charles", "Dickens", 1812)
  val imposter = new Writer("Charles", "Dickens", 1812)
  val novel = new Novel("Great Expectations", 1861, author)

  println(novel.authorAge)
  println(novel.isWrittenBy(imposter))

  val counter = new Counter
  counter.inc.print
  counter.inc.inc.inc.print
  // counter.inc(10000).print
}

// constructor
class Person(name: String, val age: Int = 0) {
  // body
  val x = 2

  println(1 + 3)

  // method
  def greet(name: String): Unit = println(s"${this.name} says: Hi, $name")

  // overloading defining methods with same name but different signatures
  // overloading is allowed if the methodds are defined  with different signatures meaning dif numbers of parameters, parameters of  diff types or returns diff types

  def greet(): Unit = println(s"Hi, I am $name")

  // multiple constructors
//  def this(name: String) = this(name, 0) could add a default parameter to accomplish same thing.
  def this() = this("John Doe")
}

// class parameters are NOT FIELDS

class Writer(firstName: String, lastName: String, val year: Float) {
  def fullName : String = firstName + " " + lastName
}

class Novel(name: String, yearOfRelease: Float, author: Writer) {
  def authorAge: Float = yearOfRelease - author.year
  def isWrittenBy(author: Writer) = author == this.author
  def copy(newYear: Int): Novel = new Novel(name, newYear, author)
}

class Counter(val count: Int = 0) {
  def inc = {
    println("incrementing")
    new Counter(count + 1)  // immutability
  }

  def dec = {
    println("decrementing")
    new Counter(count - 1)
  }

  def inc(n: Int): Counter = {
    if (n <= 0) this
    else inc.inc(n-1)
  }

  def dec(n: Int): Counter =
    if (n <= 0) this
    else dec.dec(n-1)

  def print = println(count)
}