# Full Java Tutorial

This tutorial follows the complete five-unit Java syllabus:

1. Java introduction, fundamentals, OOP, packages
2. Exception handling, I/O, multithreading
3. Modern Java features
4. Java Collections Framework
5. Spring Framework and Spring Boot REST APIs

Use this file as study notes. Copy code examples into `.java` files when you want to run them.

---

# Unit I: Java Fundamentals, OOP and Packages

## 1. Why Java?

Java is a high-level, object-oriented, platform-independent programming language.

Java is popular because it is:

- **Platform independent:** Java code can run on any system with a JVM.
- **Object-oriented:** Java programs are organized using classes and objects.
- **Secure:** Java avoids direct pointer manipulation and runs inside JVM security rules.
- **Robust:** Java has strong memory management and exception handling.
- **Multithreaded:** Java supports concurrent programming.
- **Portable:** Java bytecode can move across platforms.
- **Widely used:** Java is used in backend development, Android, enterprise apps, banking systems, and web services.

## 2. History of Java

Java was developed by James Gosling and his team at Sun Microsystems in 1995.

Important points:

- Original project name was **Oak**.
- Later renamed to **Java**.
- Main goal was platform independence.
- Slogan: **Write Once, Run Anywhere**.
- Oracle acquired Sun Microsystems in 2010.

## 3. JVM, JRE and JDK

### JVM

JVM means Java Virtual Machine.

It executes Java bytecode. Java source code is compiled into bytecode, and JVM runs that bytecode.

### JRE

JRE means Java Runtime Environment.

It contains:

- JVM
- Java class libraries
- Runtime support files

JRE is used to run Java programs.

### JDK

JDK means Java Development Kit.

It contains:

- JRE
- Java compiler `javac`
- Debugging tools
- Development tools

JDK is used to develop and run Java programs.

## 4. Java Environment

To write and run Java programs, install JDK and set environment variables.

Common commands:

```bash
javac Hello.java
java Hello
```

`javac` compiles source code into bytecode.

`java` runs the compiled bytecode using JVM.

## 5. Java Source File Structure

A Java source file usually contains:

- Optional package declaration
- Import statements
- Class declaration
- Fields
- Constructors
- Methods
- `main()` method

Example:

```java
package demo;

import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}
```

## 6. Compilation and Execution

Java program flow:

1. Write source code in `.java` file.
2. Compile using `javac`.
3. Compiler creates `.class` bytecode file.
4. JVM executes bytecode using `java`.

Example:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Run:

```bash
javac Hello.java
java Hello
```

## 7. Defining Classes in Java

A class is a blueprint for creating objects.

```java
class Student {
    String name;
    int age;

    void display() {
        System.out.println(name + " " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Rahul";
        s1.age = 20;
        s1.display();
    }
}
```

## 8. Constructors

A constructor is a special method used to initialize objects.

Rules:

- Constructor name is same as class name.
- Constructor has no return type.
- It is called automatically when object is created.

```java
class Student {
    String name;
    int age;

    Student(String n, int a) {
        name = n;
        age = a;
    }

    void display() {
        System.out.println(name + " " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student("Aisha", 21);
        s.display();
    }
}
```

## 9. Methods

A method is a block of code that performs a task.

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.println(c.add(10, 20));
    }
}
```

## 10. Access Specifiers

Access specifiers define visibility.

| Specifier | Access |
|---|---|
| `public` | Accessible everywhere |
| `private` | Accessible only inside same class |
| `protected` | Accessible in same package and subclasses |
| default | Accessible in same package |

```java
class Account {
    private double balance = 1000;

    public double getBalance() {
        return balance;
    }
}
```

## 11. Static Members

Static members belong to the class, not to individual objects.

```java
class Counter {
    static int count = 0;

    Counter() {
        count++;
    }
}

public class Main {
    public static void main(String[] args) {
        new Counter();
        new Counter();
        System.out.println(Counter.count);
    }
}
```

## 12. Final Members

`final` is used to prevent modification.

- final variable cannot be changed.
- final method cannot be overridden.
- final class cannot be inherited.

```java
class Demo {
    final int MAX = 100;
}
```

## 13. Comments

```java
// Single-line comment

/*
Multi-line comment
*/

/**
 * Documentation comment
 */
```

## 14. Data Types

Java data types are divided into primitive and non-primitive.

Primitive data types:

- `byte`
- `short`
- `int`
- `long`
- `float`
- `double`
- `char`
- `boolean`

```java
public class DataTypesDemo {
    public static void main(String[] args) {
        int age = 20;
        double marks = 91.5;
        char grade = 'A';
        boolean passed = true;

        System.out.println(age);
        System.out.println(marks);
        System.out.println(grade);
        System.out.println(passed);
    }
}
```

## 15. Variables

Types of variables:

- Local variables
- Instance variables
- Static variables

```java
class Student {
    String name;              // instance variable
    static String college;    // static variable

    void show() {
        int age = 20;         // local variable
        System.out.println(age);
    }
}
```

## 16. Operators

Java operators:

- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Relational: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`, `!`
- Assignment: `=`, `+=`, `-=`, `*=`
- Increment/decrement: `++`, `--`
- Ternary: `condition ? value1 : value2`

```java
public class OperatorsDemo {
    public static void main(String[] args) {
        int a = 10, b = 3;

        System.out.println(a + b);
        System.out.println(a > b);
        System.out.println(a > 5 && b < 5);

        String result = a % 2 == 0 ? "Even" : "Odd";
        System.out.println(result);
    }
}
```

## 17. Control Flow

### if-else

```java
int marks = 75;

if (marks >= 40) {
    System.out.println("Pass");
} else {
    System.out.println("Fail");
}
```

### switch

```java
int day = 2;

switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    default:
        System.out.println("Invalid day");
}
```

### for loop

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

### while loop

```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
```

### do-while loop

```java
int i = 1;
do {
    System.out.println(i);
    i++;
} while (i <= 5);
```

## 18. Arrays

An array stores multiple values of the same type.

```java
public class ArrayDemo {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40};

        for (int number : numbers) {
            System.out.println(number);
        }
    }
}
```

## 19. String

String is a sequence of characters. In Java, `String` is a class.

```java
public class StringDemo {
    public static void main(String[] args) {
        String text = "Java Programming";

        System.out.println(text.length());
        System.out.println(text.toUpperCase());
        System.out.println(text.toLowerCase());
        System.out.println(text.charAt(0));
        System.out.println(text.substring(0, 4));
        System.out.println(text.contains("Java"));
    }
}
```

## 20. Object-Oriented Programming

### Class and Object

A class is a blueprint. An object is an instance of a class.

```java
class Car {
    String brand;

    void drive() {
        System.out.println(brand + " is driving");
    }
}
```

### Encapsulation

Encapsulation means binding data and methods together and hiding data using private fields.

```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public double getBalance() {
        return balance;
    }
}
```

### Inheritance

Inheritance allows a class to use properties and methods of another class.

```java
class Animal {
    void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking");
    }
}
```

### Super Class and Sub Class

The parent class is called superclass. The child class is called subclass.

```java
class Vehicle {
    String type = "Vehicle";
}

class Bike extends Vehicle {
    void show() {
        System.out.println(type);
    }
}
```

### Method Overriding

Overriding means redefining a superclass method in subclass.

```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}
```

### Method Overloading

Overloading means same method name with different parameters.

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```

### Polymorphism

Polymorphism means one name, many forms.

```java
class Shape {
    void draw() {
        System.out.println("Drawing shape");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing circle");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape s = new Circle();
        s.draw();
    }
}
```

### Abstraction

Abstraction means hiding implementation details and showing only essential features.

### Abstract Class

```java
abstract class Shape {
    abstract void draw();

    void message() {
        System.out.println("Shape class");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing circle");
    }
}
```

### Interface

An interface contains abstract methods and constants. A class implements an interface.

```java
interface Printable {
    void print();
}

class Document implements Printable {
    public void print() {
        System.out.println("Printing document");
    }
}
```

## 21. Packages

A package is a group of related classes and interfaces.

Benefits:

- Avoids name conflict
- Provides access control
- Organizes code
- Makes code reusable

### Defining Package

```java
package mypack;

public class Message {
    public void show() {
        System.out.println("Hello from package");
    }
}
```

### Import

```java
import mypack.Message;

public class Main {
    public static void main(String[] args) {
        Message m = new Message();
        m.show();
    }
}
```

### Static Import

```java
import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        System.out.println(sqrt(25));
    }
}
```

### CLASSPATH Setting

`CLASSPATH` tells Java where to find user-defined classes and packages.

Example:

```bash
set CLASSPATH=.;C:\myclasses
```

### Making JAR File

A JAR file bundles multiple Java class files.

```bash
jar cf library.jar mypack/*.class
```

Run a JAR:

```bash
java -jar app.jar
```

### Package Naming Convention

Package names are lowercase and often use reverse domain style.

Example:

```java
package com.example.studentapp;
```

---

# Unit II: Exception Handling, I/O and Multithreading

## 1. Idea Behind Exception

An exception is an abnormal condition that occurs during program execution.

Exception handling allows a program to handle errors gracefully instead of crashing suddenly.

## 2. Exceptions and Errors

### Exception

An exception can often be handled by the program.

Example:

- `ArithmeticException`
- `IOException`
- `NullPointerException`

### Error

An error is a serious problem usually not handled by application code.

Example:

- `OutOfMemoryError`
- `StackOverflowError`

## 3. Types of Exception

### Checked Exception

Checked at compile time.

Example:

- `IOException`
- `SQLException`

### Unchecked Exception

Checked at runtime.

Example:

- `ArithmeticException`
- `NullPointerException`
- `ArrayIndexOutOfBoundsException`

## 4. Control Flow in Exceptions

If an exception occurs inside `try`, JVM searches for matching `catch`.

- If matching `catch` is found, it runs.
- If no matching `catch` is found, program terminates.
- `finally` runs whether exception occurs or not.

## 5. JVM Reaction to Exceptions

When exception is not handled, JVM:

1. Creates exception object.
2. Searches for handler.
3. If not found, prints stack trace.
4. Terminates program.

## 6. try, catch, finally

```java
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        } finally {
            System.out.println("Finally block executed");
        }
    }
}
```

## 7. throw and throws

`throw` is used to explicitly throw an exception.

`throws` declares that a method may throw an exception.

```java
class AgeValidator {
    static void checkAge(int age) throws Exception {
        if (age < 18) {
            throw new Exception("Age must be 18 or above");
        }
        System.out.println("Valid age");
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            AgeValidator.checkAge(16);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## 8. User Defined Exception

```java
class InvalidMarksException extends Exception {
    InvalidMarksException(String message) {
        super(message);
    }
}

public class Main {
    static void validateMarks(int marks) throws InvalidMarksException {
        if (marks < 0 || marks > 100) {
            throw new InvalidMarksException("Marks must be between 0 and 100");
        }
        System.out.println("Valid marks");
    }

    public static void main(String[] args) {
        try {
            validateMarks(120);
        } catch (InvalidMarksException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## 9. Input/Output Basics

Java I/O is used to read and write data.

Two main stream types:

- Byte streams
- Character streams

## 10. Byte Streams

Byte streams handle binary data.

Important classes:

- `FileInputStream`
- `FileOutputStream`

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ByteStreamDemo {
    public static void main(String[] args) throws IOException {
        FileOutputStream out = new FileOutputStream("data.txt");
        out.write("Hello Java".getBytes());
        out.close();

        FileInputStream in = new FileInputStream("data.txt");
        int ch;
        while ((ch = in.read()) != -1) {
            System.out.print((char) ch);
        }
        in.close();
    }
}
```

## 11. Character Streams

Character streams handle text data.

Important classes:

- `FileReader`
- `FileWriter`
- `BufferedReader`
- `BufferedWriter`

```java
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CharacterStreamDemo {
    public static void main(String[] args) throws IOException {
        FileWriter writer = new FileWriter("student.txt");
        writer.write("Rahul\nCSE\n");
        writer.close();

        FileReader reader = new FileReader("student.txt");
        int ch;
        while ((ch = reader.read()) != -1) {
            System.out.print((char) ch);
        }
        reader.close();
    }
}
```

## 12. Reading and Writing File in Java

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileDemo {
    public static void main(String[] args) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("notes.txt"));
        writer.write("Java file handling");
        writer.newLine();
        writer.write("Buffered classes are efficient");
        writer.close();

        BufferedReader reader = new BufferedReader(new FileReader("notes.txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
    }
}
```

## 13. Multithreading

Multithreading means executing multiple threads at the same time.

A thread is a lightweight subprocess.

Benefits:

- Better CPU utilization
- Faster execution for independent tasks
- Useful for background operations

## 14. Thread Life Cycle

Thread states:

- New
- Runnable
- Running
- Waiting/Blocked
- Timed Waiting
- Terminated

## 15. Creating Threads

### By extending Thread

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}
```

### By implementing Runnable

```java
class MyTask implements Runnable {
    public void run() {
        System.out.println("Runnable thread running");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyTask());
        t.start();
    }
}
```

## 16. Thread Priorities

Thread priority suggests importance to scheduler.

Range:

- `Thread.MIN_PRIORITY` = 1
- `Thread.NORM_PRIORITY` = 5
- `Thread.MAX_PRIORITY` = 10

```java
Thread t = new Thread(() -> System.out.println("Running"));
t.setPriority(Thread.MAX_PRIORITY);
t.start();
```

## 17. Synchronizing Threads

Synchronization prevents multiple threads from accessing shared data at the same time.

```java
class Counter {
    private int count = 0;

    synchronized void increment() {
        count++;
    }

    int getCount() {
        return count;
    }
}
```

## 18. Inter-thread Communication

Methods:

- `wait()`
- `notify()`
- `notifyAll()`

```java
class Shared {
    synchronized void waitMethod() throws InterruptedException {
        wait();
        System.out.println("Resumed");
    }

    synchronized void notifyMethod() {
        notify();
    }
}
```

---

# Unit III: Java New Features

## 1. Functional Interfaces

A functional interface has exactly one abstract method.

```java
@FunctionalInterface
interface Greeting {
    void sayHello();
}
```

## 2. Lambda Expression

Lambda expression provides a short way to implement functional interfaces.

```java
public class LambdaDemo {
    public static void main(String[] args) {
        Greeting g = () -> System.out.println("Hello Lambda");
        g.sayHello();
    }
}
```

## 3. Method References

Method reference refers to an existing method using `::`.

```java
import java.util.Arrays;
import java.util.List;

public class MethodReferenceDemo {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Rahul", "Aisha", "Karan");
        names.forEach(System.out::println);
    }
}
```

## 4. Stream API

Stream API processes collections in functional style.

```java
import java.util.Arrays;
import java.util.List;

public class StreamDemo {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        numbers.stream()
               .filter(n -> n % 2 == 0)
               .map(n -> n * n)
               .forEach(System.out::println);
    }
}
```

## 5. Default Methods

Interfaces can have default methods.

```java
interface Vehicle {
    default void start() {
        System.out.println("Vehicle starting");
    }
}

class Car implements Vehicle {
}
```

## 6. Static Methods in Interface

```java
interface MathUtil {
    static int square(int n) {
        return n * n;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(MathUtil.square(5));
    }
}
```

## 7. Base64 Encode and Decode

```java
import java.util.Base64;

public class Base64Demo {
    public static void main(String[] args) {
        String text = "Java";
        String encoded = Base64.getEncoder().encodeToString(text.getBytes());
        byte[] decoded = Base64.getDecoder().decode(encoded);

        System.out.println(encoded);
        System.out.println(new String(decoded));
    }
}
```

## 8. forEach Method

```java
import java.util.Arrays;
import java.util.List;

public class ForEachDemo {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("A", "B", "C");
        names.forEach(name -> System.out.println(name));
    }
}
```

## 9. Try-with-resources

Try-with-resources automatically closes resources.

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesDemo {
    public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader("notes.txt"))) {
            System.out.println(reader.readLine());
        }
    }
}
```

## 10. Type Annotations

Type annotations can be used on types.

```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target(ElementType.TYPE_USE)
@interface NonNull {
}

public class TypeAnnotationDemo {
    String name = "Java";
}
```

## 11. Repeating Annotations

Repeating annotations allow same annotation multiple times.

```java
import java.lang.annotation.Repeatable;

@Repeatable(Schedules.class)
@interface Schedule {
    String day();
}

@interface Schedules {
    Schedule[] value();
}

@Schedule(day = "Monday")
@Schedule(day = "Tuesday")
class ClassSchedule {
}
```

## 12. Java Module System

Java module system organizes applications into modules.

Example `module-info.java`:

```java
module student.app {
    requires java.sql;
    exports com.example.student;
}
```

## 13. Diamond Syntax with Inner Anonymous Class

```java
abstract class Box<T> {
    abstract T getValue();
}

public class Main {
    public static void main(String[] args) {
        Box<String> box = new Box<>() {
            String getValue() {
                return "Java";
            }
        };
        System.out.println(box.getValue());
    }
}
```

## 14. Local Variable Type Inference

`var` lets compiler infer local variable type.

```java
public class VarDemo {
    public static void main(String[] args) {
        var name = "Java";
        var age = 25;

        System.out.println(name);
        System.out.println(age);
    }
}
```

## 15. Switch Expressions and Yield

```java
public class SwitchExpressionDemo {
    public static void main(String[] args) {
        int day = 2;

        String result = switch (day) {
            case 1 -> "Monday";
            case 2 -> "Tuesday";
            default -> {
                yield "Invalid";
            }
        };

        System.out.println(result);
    }
}
```

## 16. Text Blocks

Text blocks are multi-line strings.

```java
public class TextBlockDemo {
    public static void main(String[] args) {
        String html = """
                <html>
                    <body>Hello Java</body>
                </html>
                """;
        System.out.println(html);
    }
}
```

## 17. Records

Record is a compact class for storing immutable data.

```java
record Student(String name, int age) {
}

public class RecordDemo {
    public static void main(String[] args) {
        Student s = new Student("Rahul", 20);
        System.out.println(s.name());
        System.out.println(s.age());
    }
}
```

## 18. Sealed Classes

Sealed classes restrict which classes can inherit them.

```java
sealed class Shape permits Circle, Rectangle {
}

final class Circle extends Shape {
}

final class Rectangle extends Shape {
}
```

---

# Unit IV: Java Collections Framework

## 1. Collection in Java

A collection is an object that stores a group of objects.

## 2. Collection Framework

The Collection Framework provides interfaces and classes for storing and manipulating data.

Benefits:

- Reusable data structures
- Standard algorithms
- Type safety using generics
- Easy searching, sorting, insertion, deletion

## 3. Hierarchy of Collection Framework

Main interfaces:

- `Iterable`
- `Collection`
- `List`
- `Set`
- `Queue`
- `Map`

`Map` is part of Collections Framework style, but it does not extend `Collection`.

## 4. Iterator Interface

Iterator is used to traverse collections.

```java
import java.util.ArrayList;
import java.util.Iterator;

public class IteratorDemo {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        names.add("Rahul");
        names.add("Aisha");

        Iterator<String> it = names.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }
    }
}
```

## 5. Collection Interface

Common methods:

- `add()`
- `remove()`
- `size()`
- `clear()`
- `contains()`
- `isEmpty()`

## 6. List Interface

List allows duplicate elements and maintains insertion order.

### ArrayList

```java
import java.util.ArrayList;

public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");
        list.add("Java");

        System.out.println(list);
        System.out.println(list.get(0));
    }
}
```

### LinkedList

```java
import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<>();
        list.add(10);
        list.addFirst(5);
        list.addLast(20);

        System.out.println(list);
    }
}
```

### Vector

Vector is synchronized and older than ArrayList.

```java
import java.util.Vector;

public class VectorDemo {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
        vector.add("A");
        vector.add("B");
        System.out.println(vector);
    }
}
```

### Stack

Stack follows LIFO: Last In First Out.

```java
import java.util.Stack;

public class StackDemo {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);

        System.out.println(stack.peek());
        System.out.println(stack.pop());
    }
}
```

## 7. Queue Interface

Queue usually follows FIFO: First In First Out.

```java
import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();
        queue.add("A");
        queue.add("B");

        System.out.println(queue.peek());
        System.out.println(queue.poll());
    }
}
```

## 8. Set Interface

Set stores unique elements.

### HashSet

```java
import java.util.HashSet;

public class HashSetDemo {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();
        set.add(10);
        set.add(20);
        set.add(10);

        System.out.println(set);
    }
}
```

### LinkedHashSet

Maintains insertion order.

```java
import java.util.LinkedHashSet;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        LinkedHashSet<String> set = new LinkedHashSet<>();
        set.add("B");
        set.add("A");
        set.add("C");

        System.out.println(set);
    }
}
```

### SortedSet and TreeSet

TreeSet stores sorted unique elements.

```java
import java.util.TreeSet;

public class TreeSetDemo {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(30);
        set.add(10);
        set.add(20);

        System.out.println(set);
    }
}
```

## 9. Map Interface

Map stores key-value pairs.

### HashMap

```java
import java.util.HashMap;

public class HashMapDemo {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "Rahul");
        map.put(2, "Aisha");

        System.out.println(map.get(1));
        System.out.println(map);
    }
}
```

### LinkedHashMap

Maintains insertion order.

```java
import java.util.LinkedHashMap;

public class LinkedHashMapDemo {
    public static void main(String[] args) {
        LinkedHashMap<Integer, String> map = new LinkedHashMap<>();
        map.put(3, "C");
        map.put(1, "A");
        map.put(2, "B");

        System.out.println(map);
    }
}
```

### TreeMap

Stores keys in sorted order.

```java
import java.util.TreeMap;

public class TreeMapDemo {
    public static void main(String[] args) {
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(3, "C");
        map.put(1, "A");
        map.put(2, "B");

        System.out.println(map);
    }
}
```

### Hashtable

Hashtable is synchronized and does not allow null keys or null values.

```java
import java.util.Hashtable;

public class HashtableDemo {
    public static void main(String[] args) {
        Hashtable<Integer, String> table = new Hashtable<>();
        table.put(1, "Java");
        table.put(2, "Spring");

        System.out.println(table);
    }
}
```

## 10. Sorting

```java
import java.util.ArrayList;
import java.util.Collections;

public class SortingDemo {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(30);
        numbers.add(10);
        numbers.add(20);

        Collections.sort(numbers);
        System.out.println(numbers);
    }
}
```

## 11. Comparable Interface

Comparable defines natural ordering using `compareTo()`.

```java
import java.util.ArrayList;
import java.util.Collections;

class Student implements Comparable<Student> {
    String name;
    int marks;

    Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }

    public int compareTo(Student other) {
        return this.marks - other.marks;
    }

    public String toString() {
        return name + " " + marks;
    }
}

public class ComparableDemo {
    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("Rahul", 85));
        students.add(new Student("Aisha", 92));

        Collections.sort(students);
        System.out.println(students);
    }
}
```

## 12. Comparator Interface

Comparator defines custom ordering.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Employee {
    String name;
    int salary;

    Employee(String name, int salary) {
        this.name = name;
        this.salary = salary;
    }

    public String toString() {
        return name + " " + salary;
    }
}

public class ComparatorDemo {
    public static void main(String[] args) {
        ArrayList<Employee> employees = new ArrayList<>();
        employees.add(new Employee("Ravi", 50000));
        employees.add(new Employee("Aisha", 70000));

        Collections.sort(employees, Comparator.comparing(e -> e.name));
        System.out.println(employees);
    }
}
```

## 13. Properties Class

Properties stores key-value pairs as strings.

```java
import java.util.Properties;

public class PropertiesDemo {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.setProperty("username", "admin");
        props.setProperty("password", "1234");

        System.out.println(props.getProperty("username"));
    }
}
```

---

# Unit V: Spring Framework and Spring Boot

## 1. Spring Framework

Spring is a Java framework used to build enterprise applications.

Main features:

- Dependency Injection
- Inversion of Control
- Aspect-Oriented Programming
- Transaction management
- MVC web framework
- Integration with databases and REST APIs

## 2. Spring Core Basics

Spring Core provides the IoC container that manages objects called beans.

## 3. Dependency Injection

Dependency Injection means providing required objects from outside instead of creating them manually inside a class.

Without DI:

```java
class StudentService {
    StudentRepository repository = new StudentRepository();
}
```

With DI:

```java
class StudentService {
    private final StudentRepository repository;

    StudentService(StudentRepository repository) {
        this.repository = repository;
    }
}
```

## 4. Inversion of Control

Inversion of Control means object creation and dependency management are controlled by Spring container, not by programmer code.

## 5. AOP

AOP means Aspect-Oriented Programming.

It separates cross-cutting concerns like:

- Logging
- Security
- Transactions
- Monitoring

Example concept:

```java
@Aspect
@Component
class LoggingAspect {
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore() {
        System.out.println("Method called");
    }
}
```

## 6. Bean Scopes

Bean scope defines lifecycle and visibility of a Spring bean.

Common scopes:

- `singleton`: one object per Spring container
- `prototype`: new object every time requested
- `request`: one object per HTTP request
- `session`: one object per HTTP session
- `application`: one object per ServletContext
- `websocket`: one object per WebSocket session

```java
@Component
@Scope("prototype")
class ReportService {
}
```

## 7. Autowiring

Autowiring lets Spring automatically inject dependencies.

```java
@Service
class StudentService {
    private final StudentRepository repository;

    @Autowired
    StudentService(StudentRepository repository) {
        this.repository = repository;
    }
}
```

In modern Spring, constructor injection can omit `@Autowired` when there is one constructor.

## 8. Common Spring Annotations

| Annotation | Use |
|---|---|
| `@Component` | Generic Spring bean |
| `@Service` | Service layer bean |
| `@Repository` | Repository/data access bean |
| `@Controller` | MVC controller |
| `@RestController` | REST controller |
| `@Autowired` | Dependency injection |
| `@Bean` | Declares bean in config class |
| `@Configuration` | Configuration class |
| `@Scope` | Defines bean scope |

## 9. Life Cycle Callbacks

Spring bean lifecycle:

1. Bean object created
2. Dependencies injected
3. Initialization callback
4. Bean used
5. Destruction callback

```java
import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

@Component
class DemoBean {
    @PostConstruct
    public void init() {
        System.out.println("Bean initialized");
    }

    @PreDestroy
    public void destroy() {
        System.out.println("Bean destroyed");
    }
}
```

## 10. Bean Configuration Styles

Spring supports:

- XML configuration
- Annotation-based configuration
- Java-based configuration

Java config example:

```java
@Configuration
class AppConfig {
    @Bean
    StudentService studentService() {
        return new StudentService(new StudentRepository());
    }
}
```

## 11. Spring Boot

Spring Boot simplifies Spring application development.

Features:

- Auto-configuration
- Embedded server
- Starter dependencies
- Production-ready tools
- Less boilerplate configuration

## 12. Spring Boot Build Systems

Common build systems:

- Maven
- Gradle

Maven dependency example:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

## 13. Spring Boot Code Structure

Typical structure:

```text
src/main/java/com/example/demo
    DemoApplication.java
    controller/
    service/
    repository/
    model/
src/main/resources
    application.properties
```

Main class:

```java
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

## 14. Spring Boot Runners

Runners execute code after application startup.

```java
@Component
class StartupRunner implements CommandLineRunner {
    public void run(String... args) {
        System.out.println("Application started");
    }
}
```

## 15. Logger

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
class StudentService {
    private static final Logger log = LoggerFactory.getLogger(StudentService.class);

    void show() {
        log.info("Student service called");
    }
}
```

## 16. Building RESTful Web Services

REST API uses HTTP methods:

- `GET`: read data
- `POST`: create data
- `PUT`: update data
- `DELETE`: delete data

## 17. Rest Controller

```java
@RestController
@RequestMapping("/api/students")
class StudentController {
}
```

## 18. Request Mapping

`@RequestMapping` maps web requests to controller methods.

Shortcut annotations:

- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@DeleteMapping`

## 19. Request Body

`@RequestBody` reads JSON request body into Java object.

```java
@PostMapping
public Student createStudent(@RequestBody Student student) {
    return student;
}
```

## 20. Path Variable

`@PathVariable` reads value from URL path.

```java
@GetMapping("/{id}")
public String getStudent(@PathVariable int id) {
    return "Student ID: " + id;
}
```

## 21. Request Parameter

`@RequestParam` reads query parameter.

```java
@GetMapping("/search")
public String search(@RequestParam String name) {
    return "Searching: " + name;
}
```

## 22. Complete Spring Boot REST Example

Model:

```java
public class Student {
    private int id;
    private String name;
    private String branch;

    public Student() {
    }

    public Student(int id, String name, String branch) {
        this.id = id;
        this.name = name;
        this.branch = branch;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
}
```

Controller:

```java
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {
    private final List<Student> students = new ArrayList<>();

    public StudentController() {
        students.add(new Student(1, "Rahul", "CSE"));
        students.add(new Student(2, "Aisha", "IT"));
    }

    @GetMapping
    public List<Student> getAllStudents() {
        return students;
    }

    @GetMapping("/{id}")
    public Student getStudentById(@PathVariable int id) {
        return students.stream()
                .filter(student -> student.getId() == id)
                .findFirst()
                .orElse(null);
    }

    @PostMapping
    public Student addStudent(@RequestBody Student student) {
        students.add(student);
        return student;
    }

    @PutMapping("/{id}")
    public Student updateStudent(@PathVariable int id, @RequestBody Student updatedStudent) {
        for (Student student : students) {
            if (student.getId() == id) {
                student.setName(updatedStudent.getName());
                student.setBranch(updatedStudent.getBranch());
                return student;
            }
        }
        return null;
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable int id) {
        students.removeIf(student -> student.getId() == id);
        return "Student deleted";
    }
}
```

## 23. Build Web Applications

Spring Boot can build web apps using:

- Spring MVC
- Thymeleaf templates
- REST APIs
- HTML/CSS/JavaScript frontend

Controller example for web page:

```java
@Controller
class HomeController {
    @GetMapping("/")
    public String home() {
        return "index";
    }
}
```

---

# Practice Questions

1. Explain JVM, JRE and JDK.
2. Write a Java program to demonstrate variables and data types.
3. Write a Java program for method overloading.
4. Write a Java program for method overriding.
5. Explain encapsulation with example.
6. Explain abstract class and interface with examples.
7. Create a package and import it into another class.
8. Write a program using `try`, `catch` and `finally`.
9. Create a user-defined exception.
10. Read and write a file using byte streams.
11. Read and write a file using character streams.
12. Create a thread by extending `Thread`.
13. Create a thread by implementing `Runnable`.
14. Demonstrate synchronization.
15. Use lambda expression with a functional interface.
16. Use Stream API to filter even numbers from a list.
17. Explain records and sealed classes.
18. Demonstrate ArrayList, LinkedList, HashSet and HashMap.
19. Sort custom objects using Comparable and Comparator.
20. Create a Spring Boot REST API with GET, POST, PUT and DELETE.

