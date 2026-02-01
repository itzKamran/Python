class Calculator:
      def add (self , a ,b):
            return a + b 
      def substract (self , a ,b):
            return a - b 
      def multiply (self , a ,b):
            return a * b 
      def div (self , a ,b):
            return a / b 
            
calc = Calculator()

x= int(input(" Enter A Number One"))
y =int(input("Enter A Number Two :"))

print("Addition :", calc.add(x , y))
print("Addition :", calc.substract(x , y))
print("Addition :", calc.multiply(x , y))
print("Addition :", calc.div(x , y))
