package lectures.part2oop

object Exceptions extends App {

  val x: String =  null
  // println(x.length)
  // this will crash with a Null Pointer Exception (NPE)
  // throwing and catching exceptions

 // val aWeirdValue = throw new NullPointerException

  // throwable classes extend the Throwable class
  // Exception and Error are the major Throwable subtypes

  // how to catch exceptions
  def getInt(withExceptions: Boolean): Int =
    if (withExceptions) throw new RuntimeException("No int for you!")
    else 42

  val potentialFail = try {
    // code that might throw
    getInt(false)
  } catch {
    case e: RuntimeException => 43
  } finally {
    // code that will get executed no matter what
    // finally blocks are optional
    // do not affect the return type of the expression.
    // use only for side effects
    println("finally")
  }

  // define your own exceptions
  class MyException extends  Exception
  val exception = new MyException

  // throw exception

  /*
  1. Crash your program with an OutofMemoryError
  2. crash with StackOverflowError
  3. PocketCalculator
    - add (x,y)
    - subtract (x y)
    - multiply (x, y)
    - divide (x, y)

      THROW
      - OverflowException if add (x, y) exceeds int.max_value
      - underflow exection if subtract (x, y) exceeds Int.Min_value
      - mathCalculationException for division by 0
  */

  // OOM out of memory
  // val array = Array.ofDim(Int.MaxValue)

  // Stack overflow SO
//  def infinite: Int = 1 + infinite
//  val noLimit = infinite


class OverflowException extends  RuntimeException
class UnderflowException extends RuntimeException
class MathCalculationException extends RuntimeException("Division by 0")

  object PocketCalculator {

    def add(x: Int, y: Int) = {
      val result = x + y
      if (x > 0 && y > 0 && result < 0) throw new OverflowException
      else if (x < 0 && y < 0 && result > 0) throw new UnderflowException
      else result
    }

    def subtract(x: Int, y: Int) = {
      val result = x - y
      if (x > 0 && y < 0 && result < 0) throw new OverflowException
      else if (x<0 && y > 0 && result > 0) throw new UnderflowException
      else result
    }

    def multiply(x: Int, y: Int) = {
      val result = x * y
      if (x > 0 && y > 0 && result < 0) throw new OverflowException
      else if (x < 0 && y < 0 && result < 0) throw new OverflowException
      else if (x > 0 && y < 0 && result > 0) throw new UnderflowException
      else if (x < 0 && y > 0 && result > 0) throw new UnderflowException
      else result
    }

    def divide(x: Int, y: Int) = {
      if (y == 0) throw new MathCalculationException
      else  x / y
    }

  }

//  println(PocketCalculator.add(Int.MaxValue, 10))
  println(PocketCalculator.divide(2, 0))

}
