package lectures.part2oop

import playground.{PrinceCharming, Cinderella as Princess}

import java.sql
import java.util.Date
import java.sql.{Date => sqlDate}

object PackagingAndImports extends App {

  // package members are accessible by their simple name
  val writer = new Writer("Daniel", "RockTheJVM", 2018)

  // import the package
  // can import above or fully qualify below
  val princess = new Princess// playground.Cinderella, Cinderella


  // packages are in hierarchy
  // matching folder structure

  // package object
  sayHello
  println(SPEED_OF_LIGHT)

  // imports
  val prince = new PrinceCharming


  // 1. Use fully qualified name
  val date = new Date()
  val sqlDate = new sqlDate(2022, 04, 01) // new java.sql.Date

  // default imnports
  // java.lang 0 String, Object, Exception
  // sacala - Int, Nothing, Function
  // scala.Predef - println, ???


}
