<?php
  // https://www.codewars.com/kata/string-repeat

  // Write a function called repeatStr which repeats the given string string exactly n times.

  // repeatStr(6, "I") // "IIIIII"
  // repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

  function repeatStr($n, $str) {
    return str_repeat($str, $n);
  }
?>