/* This is a multiline String
 * Line 1
 * Line 2
 * End
 */
struct A {
  let text = "This is a String";
  let decimal = 10 /* Integer */
  let float = 10.5 // floating point number
  let calc = (10.5 + 10 - 11) / 3 * 33
}

class B {
  var a: A
  init(a: A) {
    self.a = a
  }
  
  func getA() -> A {
    return self.a
  }
}
