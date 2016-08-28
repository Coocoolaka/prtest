/* Multiline comment
 * Line 1
 * Line 2
 * END
 */
struct A {
  let text = "This is a string"
  let intNumber = 10
  let decimalNumber = 10.5 // Should detect the .
}

class B {
  let a: A
  
  init(a: A) {
    self.a = a
  }
}
