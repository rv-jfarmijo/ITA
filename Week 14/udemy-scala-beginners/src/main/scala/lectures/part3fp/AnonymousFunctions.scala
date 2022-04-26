package lectures.part3fp

object AnonymousFunctions extends App {

  val doubler = new Function1[Int, Int] {
    override def apply(x: Int): Int = x * 2
  }
}
