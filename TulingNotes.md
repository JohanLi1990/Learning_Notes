# Tuling Notes

## 全面理解JVM

- How is Java program executed. (tools: UltraEdit for byte code, jclasslib for analysis and understanding). Java execution has to abide Java Language Specification
  
- Class loading mechanism (sandbox protection, cache + parent + bootstrap loader)
  - bytecode, exception table, miscellanous
![JVM架构图](image.png)

- Garbage Collection (tools: arthas for diagnostic)
  - Java opts, -, -X, -XX
  - default collector G1, 
  - print and analyze GC logs

- Notable interview question 
  - Where is `this` stored in JVM? 
  - Why tomcat could do hot reload for jsp, but not for jar?
  - Why do we need custom class loader? how is it implement (by overriding loadClass method in ClassLoader)
  - Why cannot child class override static method from main class (invokevirtual vs invokestatic in JLS)
