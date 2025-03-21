# 1. The General Learning Notebook

- [1. The General Learning Notebook](#1-the-general-learning-notebook)
  - [1.1. Lesson Learnt for Interview Experiences](#11-lesson-learnt-for-interview-experiences)
  - [1.2. Raod Map](#12-raod-map)
  - [1.3. JAVA JVM](#13-java-jvm)
    - [1.3.1. JVM Memory Structure](#131-jvm-memory-structure)
    - [1.3.2. Java Memory Model](#132-java-memory-model)
  - [1.4. Possible cause of Memory Leak](#14-possible-cause-of-memory-leak)
  - [1.5. Class loading](#15-class-loading)
  - [1.6. Java Garbage Collections](#16-java-garbage-collections)
    - [1.6.1. G1GC](#161-g1gc)
    - [1.6.2. Enable GC logger](#162-enable-gc-logger)
    - [1.6.3. Reading GC Logs](#163-reading-gc-logs)
    - [1.6.4. Comparison of different GC techniques](#164-comparison-of-different-gc-techniques)
  - [1.7. Java in High Concurrency Environment](#17-java-in-high-concurrency-environment)
    - [1.7.1. Race Conditions, with Example](#171-race-conditions-with-example)
    - [1.7.2. DeadLock, with Eample](#172-deadlock-with-eample)
    - [1.7.3. Visibility and Mutual Exclusions](#173-visibility-and-mutual-exclusions)
    - [1.7.4. Use Lazy Initailization Judiciously](#174-use-lazy-initailization-judiciously)
    - [1.7.5. What is threadLocal](#175-what-is-threadlocal)
    - [1.7.6. Common threadsafe datastructures](#176-common-threadsafe-datastructures)
    - [1.7.7. Producer Consumer Pattern](#177-producer-consumer-pattern)
    - [1.7.8. CompletableFuture for Asynchronous Event handling](#178-completablefuture-for-asynchronous-event-handling)
    - [1.7.9. Java Stream Parallel Processing](#179-java-stream-parallel-processing)
  - [1.8. Java New Features since Java 11](#18-java-new-features-since-java-11)
  - [1.9. Design Patterns](#19-design-patterns)
    - [1.9.1. Common Design Patterns](#191-common-design-patterns)
  - [1.10. Inversion of Control](#110-inversion-of-control)
    - [1.10.1. SOLID Principle](#1101-solid-principle)
    - [1.10.2. Design Patterns in Spring](#1102-design-patterns-in-spring)
  - [1.11. Spring Framework](#111-spring-framework)
    - [1.11.1. Spring Framework vs J2EE](#1111-spring-framework-vs-j2ee)
    - [1.11.2. Design consideration of using DispatchServlet](#1112-design-consideration-of-using-dispatchservlet)
    - [1.11.3. IoC and its implementations](#1113-ioc-and-its-implementations)
    - [1.11.4. Bean Life Cycle](#1114-bean-life-cycle)
    - [1.11.5. Bean Scope](#1115-bean-scope)
    - [1.11.6. How to gurantee thread safety for a Bean?](#1116-how-to-gurantee-thread-safety-for-a-bean)
    - [1.11.7. How does Spring solve Cycle Dependency between two Beans](#1117-how-does-spring-solve-cycle-dependency-between-two-beans)
    - [1.11.8. Autowire Need for Disambiguation](#1118-autowire-need-for-disambiguation)
    - [1.11.9. Spring AOP](#1119-spring-aop)
    - [1.11.10. Spring Transactions Management](#11110-spring-transactions-management)
    - [1.11.11. DB transaction isolation level](#11111-db-transaction-isolation-level)
    - [1.11.12. DB transaction lock](#11112-db-transaction-lock)
    - [1.11.13. Reactive Programming with Spring Webflux](#11113-reactive-programming-with-spring-webflux)
    - [1.11.14. Docker with Spring Boot](#11114-docker-with-spring-boot)
    - [1.11.15. How to design a 秒杀 系统](#11115-how-to-design-a-秒杀-系统)
    - [1.11.16. DB isolation level](#11116-db-isolation-level)
    - [1.11.17. Spring AI integration with Tensorflow](#11117-spring-ai-integration-with-tensorflow)
  - [1.12. Behaviour Interviews](#112-behaviour-interviews)
    - [1.12.1. Customer Obsession](#1121-customer-obsession)
  - [1.13. OS Interview Questions](#113-os-interview-questions)
    - [1.13.1. Process vs Threads](#1131-process-vs-threads)
  - [1.14. Network Interview Questions](#114-network-interview-questions)
    - [1.14.1. TCP/IP Model of Network](#1141-tcpip-model-of-network)
    - [1.14.2. What happens when you enter URL int a web browser](#1142-what-happens-when-you-enter-url-int-a-web-browser)
    - [1.14.3. Idempotency](#1143-idempotency)
    - [1.14.4. GET vs POST](#1144-get-vs-post)
    - [1.14.5. PUT vs PATCH vs POST](#1145-put-vs-patch-vs-post)
    - [1.14.6. HTTP vs HTTPS](#1146-http-vs-https)
    - [1.14.7. How Does HTTPS work](#1147-how-does-https-work)
    - [1.14.8. TCP vs UDP](#1148-tcp-vs-udp)
    - [1.14.9. TCP 4-way HandShake to terminate connection](#1149-tcp-4-way-handshake-to-terminate-connection)
    - [1.14.10. XSS Reflected vs Persistent vs DOM](#11410-xss-reflected-vs-persistent-vs-dom)
  - [1.15. Database Questions](#115-database-questions)
    - [1.15.1. ACID Compliance](#1151-acid-compliance)
    - [1.15.2. CAP Therom](#1152-cap-therom)
    - [1.15.3. SQL index, what are they, when do you use them?](#1153-sql-index-what-are-they-when-do-you-use-them)
    - [1.15.4. WHy not indexing all columns?](#1154-why-not-indexing-all-columns)
    - [1.15.5. Clustered vs Non-Clustered index](#1155-clustered-vs-non-clustered-index)
    - [1.15.6. Explain keyword MySQL](#1156-explain-keyword-mysql)
    - [1.15.7. MYSQL 回表](#1157-mysql-回表)
    - [1.15.8. MYSQL how to enable Master Slave Replication](#1158-mysql-how-to-enable-master-slave-replication)
    - [1.15.9. MySQL dynamically scalling](#1159-mysql-dynamically-scalling)
  - [1.16. System Design Interview](#116-system-design-interview)
    - [1.16.1. what kind of questions should I ask???](#1161-what-kind-of-questions-should-i-ask)
    - [1.16.2. Back Of Envelop Calculation](#1162-back-of-envelop-calculation)
    - [1.16.3. Basic Building Blocks](#1163-basic-building-blocks)
      - [1.16.3.1. Domain Name system](#11631-domain-name-system)
      - [1.16.3.2. Load Balancers](#11632-load-balancers)
      - [1.16.3.3. Database](#11633-database)
        - [1.16.3.3.1. SQL vs NoSQL](#116331-sql-vs-nosql)
        - [1.16.3.3.2. Data Replication](#116332-data-replication)
        - [1.16.3.3.3. Data Distributions](#116333-data-distributions)
      - [1.16.3.4. Key-Value Store](#11634-key-value-store)
      - [1.16.3.5. Distributed Search](#11635-distributed-search)
    - [1.16.4. Design of stock Exchange System](#1164-design-of-stock-exchange-system)
  - [1.17. Effective Software Engineering](#117-effective-software-engineering)
    - [1.17.1. Six pillars of Effective Software](#1171-six-pillars-of-effective-software)
    - [1.17.2. From Customer Insights to Internal Requirements](#1172-from-customer-insights-to-internal-requirements)
    - [1.17.3. Implementation and Coding](#1173-implementation-and-coding)
    - [1.17.4. Testing and Quality Assurance](#1174-testing-and-quality-assurance)
    - [1.17.5. Clean Code in Java](#1175-clean-code-in-java)
    - [1.17.6. Best Practices](#1176-best-practices)
      - [1.17.6.1. why is String final in Java](#11761-why-is-string-final-in-java)
      - [1.17.6.2. JDBC best practices](#11762-jdbc-best-practices)
- [2. How to use OPENAI API in SpringBoot Project](#2-how-to-use-openai-api-in-springboot-project)
  - [2.1. Another way to improve Grammar via GrammarBot API (Not Feasible)](#21-another-way-to-improve-grammar-via-grammarbot-api-not-feasible)
- [3. Use old laptop as a proxy server](#3-use-old-laptop-as-a-proxy-server)
- [4. Java Linux Notes](#4-java-linux-notes)
- [5. Azure](#5-azure)
- [6. Kotlin](#6-kotlin)
  - [6.1. Kotlin Coroutine](#61-kotlin-coroutine)
  - [6.2. Kotlin + Spring Boot](#62-kotlin--spring-boot)
  - [6.3. Jepack Compose](#63-jepack-compose)
- [7. Kafka](#7-kafka)
- [8. PluralSight Java Clean code practices](#8-pluralsight-java-clean-code-practices)
- [9. PluralSight Cloud Fundamental](#9-pluralsight-cloud-fundamental)
- [10. PluralSight Core-Spring](#10-pluralsight-core-spring)
- [PluralSight Python](#pluralsight-python)
- [Output](#output)
- [\[85, 46, 29, 73, 9\]](#85-46-29-73-9)

Page 23

## 1.1. Lesson Learnt for Interview Experiences

 1. keep calm
 2. it is going to be exausting, prepare snacks in between take
 3. keep calm, do not panick.
 4. how to deal with heavy reads and heavy writes?
 5. Keep practicing / keep practicing
 6. If the role requires java, study java ; Otherwise pay attention to network / OS type of interview questions

## 1.2. Raod Map

[Java Microservice RoadMap](https://github.com/in28minutes/roadmaps/blob/main/README.md#java-microservices-roadmap)
[Java Fullstack](https://github.com/in28minutes/roadmaps/blob/main/README.md#java-full-stack-roadmap)

**6 Month Plan**

- [ ] Linux bash familarity (45 hrs)
- [ ] Developing Microservices with Spring Boot (3 hrs)
- [ ] Microservices with Spring Cloud (40 hrs)
- [ ] Azure Fundamental (40 hrs)
- [ ] Develop article refining services (30 hrs)
- [ ] Deploy ARS as a spring boot to Azure (10 hrs)
- [ ] Angular.js framework (20 hrs)

188 / 180 = 1.1 hrs a day. 

## 1.3. JAVA JVM

last resort
[JVM optimization technique](https://cloud.tencent.com/developer/article/1812722)

### 1.3.1. JVM Memory Structure

- **Method Areaa**: Method Area is a part of the perm gen which is shared among all the threads. It creates when the JVM starts up. It is used to store class structure, superclass name, interface name, and constructors. The JVM stores the following kinds of information in the method area:

    A Fully qualified name of a type (ex: String)
    The type's modifiers
    Type's direct superclass name
    A structured list of the fully qualified names of super interfaces.

- **Heap Area**: actual objects, young gen, old gen. (Eden, s0, s1, old memory)

- **JVM stack area**:
  - Multiple stackframes each owned by a thread
  - stack frame: local Variable Array, Operand Stack, and Framde Data
  - stores reference to heap object / also some value (primitive type)

- **Native Method Stack** : similar to stack area but for OS native methods
- **PC register**: Stores the pointer to where the execution is.

### 1.3.2. Java Memory Model

Lesson from Bilibili
- JMM is in essence a model to support multithreading.
- Defines how different threads stores and read variable from memory

**Heap** actual objects
**Stack** object reference, maethod stack frame, primitive type

## 1.4. Possible cause of Memory Leak

- static collections, same life cycle as JVM
- singleton, holding external references
- Connections needs to close before GC can garbage collect
- A variable with inappropriate scope.
- Hash value changed, object stored in HashSet or HashMap cannot be removed.
- Inappropriate use of threadlocal. ThreadLocal 的弱引用导致内存泄漏也是个老生常谈的话题了，使用完 ThreadLocal 一定要记得使用 remove 方法来进行清除, wekareference of threadlocal is used as Key in threadLocalMap, this key can be GC-ed very easily, however, the value may not be GC-ed. Therefore, in threadlocalMap you can have null key, but valid value. thus leading to memory leak.

## 1.5. Class loading

only loads claes
--> BootStrap (contain classes in core java environment, java long object, class, class loader)
to allow others to load up the rest of the system.
--> Extension, defines its parent to booststrap, and will default to bootstrap, not widely used, but can supply override and native code for different operating system and platforms. e.g. Nashorn Engine
--> Application, loading user classes from defined classpath. it will load the dependencies first; if cannot find will delegate parent to look up for it.

## 1.6. Java Garbage Collections

| Eden | S1 | S2 | Old Generation|
| MetaSpace |

[Reference 1](https://sematext.com/blog/java-garbage-collection-tuning/#toc-what-is-garbage-collection-tuning-0)
[Oracle Docs](https://docs.oracle.com/en/java/javase/12/gctuning/introduction-garbage-collection-tuning.html)

set fixed size heap to avoid heap resizing; load memory pages into memory at the start of the application
e.g. -Xms2g -Xmx2g -XX:+AlwaysPreTouch

### 1.6.1. G1GC

[G1GC tuning tips](https://blog.gceasy.io/2020/06/02/simple-effective-g1-gc-tuning-tips/)

- Avoid limiting the young generation size to particular values by using options like -Xmn, -XX:NewRatio and others because the young generation size is the main means for G1 to allow it to meet the pause-time.
- Only set -XX:MaxGCPauseMillis
- For managing humongous object **Concurrent Mark Sweep** might be a better options

### 1.6.2. Enable GC logger

For java 9 and newer:

```bat
java -Xlog:gc*:file=/var/log/myapp/gc.log -jar my_awesome_app.jar
JAVA_OPTS=-Xms512m -Xmx4096m -XX:+UseG1GC"
```

### 1.6.3. Reading GC Logs

Pay attention to places where GC takes more than 1 sec.

### 1.6.4. Comparison of different GC techniques

| Parallel Scavenge + Parallel Old | ParNew + CMS | G1 | ZGC | Shenandoah GC |
|---|---|---|---|---|
| JDK 1.7 to JDK 9; use PS for young gen, and PO for old gen; more focus on throughput, pause time not so good| Concurrent mark Sweep, lower paus time, but there will be large amount of fragmentations, may trigger full gc since big object cannot find continous heap space when it was promoted to old gen | latency first, parallel collector like CMS, can hit GC paustime more precisely, compaction will not lead to long pauses due to full GC, some fragmentation issues, but not as serious as CMS | Very low response time while keeping throughput high, pause time will not increase with heap size | competitor of ZGC, good with huge object, manages framgementations really well, but made no promise on throughput and latency|

## 1.7. Java in High Concurrency Environment

### 1.7.1. Race Conditions, with Example

### 1.7.2. DeadLock, with Eample

### 1.7.3. Visibility and Mutual Exclusions

[Howe does volatile work](https://stackabuse.com/concurrency-in-java-the-volatile-keyword/)

whenever a variable is marked volatile, its write operations will be commited to its real address (main memory) right away
instead of local cache first.

All variables **updated** before volatile variable will be committed to main memory right away, including non-volatile ones.
however it does not gurantee mutual exclusion

### 1.7.4. Use Lazy Initailization Judiciously

**static field**

```java
// For static field, use lazy initialization holders idiom
private static class FieldHolder {
  static final FieldType field = computeFieldValue();
}

private static FieldType getField() {
  /* A typical VM will synchronize field access only to initialize the class. Once the class
is initialized, the VM patches the code so that subsequent access to the field does
not involve any testing or synchronization. */
  return FieldHolder.field; 
}
```

**instance field**

```java

/* we need volatile modifier to make sure field always make its latest value visible to all other threads
otherewise there is a geniune chance that two thread enters the last if clause
to initialize field sequentially, although in theroy the field is already initialized by first thread*/
private volatile FiledType field;

private FieldType getField() {
  FieldType res = field;

  if (res == null) {
    synchronized(this) {
      if (field ==  null) {
        return field = result = computeFieldValue();
      }
    }
  }
  return res;
}

```

### 1.7.5. What is threadLocal

a variable only visible to the thread instance()

### 1.7.6. Common threadsafe datastructures

ConcurrentHashMap(Synchronization over segments not entire DS), LinkedBlockingDeque (internal queue)

### 1.7.7. Producer Consumer Pattern

```java
// using blocking queue
public class SimpleProducerConsumerDemonstrator {
    BlockingQueue<Double> blockingQueue = new LinkedBlockingDeque<>(5);

    private void produce() {
        while (true) {
            double value = generateValue();
            try {
                blockingQueue.put(value);
            } catch (InterruptedException e) {
                e.printStackTrace();
                break;
            }
            System.out.printf("[%s] Value produced: %f\n", Thread.currentThread().getName(), value);
        }
    }

    private void consume() {
        while (true) {
            Double value;
            try {
                value = blockingQueue.take();
            } catch (InterruptedException e) {
                e.printStackTrace();
                break;
            }
            // Consume value
            System.out.printf("[%s] Value consumed: %f\n", Thread.currentThread().getName(), value);
        }
    }

    private double generateValue() {
        return Math.random();
    }

    private void runProducerConsumer() {
        for (int i = 0; i < 2; i++) {
            Thread producerThread = new Thread(this::produce);
            producerThread.start();
        }

        for (int i = 0; i < 3; i++) {
            Thread consumerThread = new Thread(this::consume);
            consumerThread.start();
        }
    }

    public static void main(String[] args) {
        SimpleProducerConsumerDemonstrator simpleProducerConsumerDemonstrator = new SimpleProducerConsumerDemonstrator();
        simpleProducerConsumerDemonstrator.runProducerConsumer();
        sleep(2000);
        System.exit(0);
    }

```

### 1.7.8. CompletableFuture for Asynchronous Event handling

We need our code to be non-blocking for most of the time.
If we need to make use of the result obtained from a execution pool
we can do

```java
  var futures = executor.invokeAll(tasks);
  for (var f : futures) {
    var result = f.get();
    // perform callback
  }

```

However this code is blocking, because f.get() will block the current thread, and the for loop also is not efficient. We have to wait for all tasks to finish.
CompletableFuture resolve this by allowing the next callback to be triggered, whenever the first is done.

```java
var cf = CompletableFuture.supplyAsync(this::getSthSlow, executor);
cf.thenAccept(results::add); // also a great way to handle callback
```

[Another Example](https://leetcode.com/problems/web-crawler-multithreaded/solutions/2973071/very-fast-java-completablefuture-solution-5ms/)

### 1.7.9. Java Stream Parallel Processing 

- What if you need to pass context (often a threadlocal type) to different threads when doing parallel stream?
  - use peek intermediate operation 

```java
// some logic ..
var curThreadLocal = ContextUtil.getCurrentContext();
var res = tasks.stream()
      .parallel()
      .peek(k -> ContextUtil.setCurrentContext())
      .map(task -> task.call())
      .collect(Collectors.toList());

```

- do prallel processing example

```java
List<Integer> numbers = new ArrayList<>();
for (int i = 0; i < 1000000; i++) {
    numbers.add(ThreadLocalRandom.current().nextInt(100));
}

//
long startTimeSeq = System.currentTimeMillis();
double averageSequential = numbers.stream()
                                 .mapToInt(Integer::intValue)
                                 .average()
                                 .getAsDouble();
long endTimeSeq = System.currentTimeMillis();
System.out.println("Sequential Average: " + averageSequential);
System.out.println("Time taken (Sequential): " + (endTimeSeq - startTimeSeq) + "ms");


//Parallel
long startTimePar = System.currentTimeMillis();
double averageParallel = numbers.parallelStream()
                               .mapToInt(Integer::intValue)
                               .average()
                               .getAsDouble();
long endTimePar = System.currentTimeMillis();
System.out.println("Parallel Average: " + averageParallel);
System.out.println("Time taken (Parallel): " + (endTimePar - startTimePar) + "ms");


//Sequential Average: 59.4451232
//Time taken (Sequential): 10ms
//Parallel Average: 59.4451232
//Time taken (Parallel): 3ms
```


## 1.8. Java New Features since Java 11

**Record Class**
a simplified pojo
[Record class](https://docs.oracle.com/en/java/javase/15/language/records.html)

**Enhanced Switch Pattern**

```java
static record Human (String name, int age, String profession) {}

public String checkObject(Object obj) {
    return switch (obj) {
        case Human h -> "Name: %s, age: %s and profession: %s".formatted(h.name(), h.age(), h.profession());
        case Circle c -> "This is a circle";
        case Shape s -> "It is just a shape";
        case null -> "It is null";
        default -> "It is an object";
    };
}

public String checkShape(Shape shape) {
    return switch (shape) {
        case Triangle t && (t.getNumberOfSides() != 3) -> "This is a weird triangle";
        case Circle c && (c.getNumberOfSides() != 0) -> "This is a weird circle";
        default -> "Just a normal shape";
    };
}

```

**Java Sealed Class and Interface**
[sealed class/ interface](https://www.baeldung.com/java-sealed-classes-interfaces)
Define super class or interface extendable only to a few subclass
This feature is about enabling more fine-grained inheritance control in Java. Sealing allows classes and interfaces to define their permitted subtypes.

**Java Virtual Threads**
TBD
[documents](https://www.happycoders.eu/java/virtual-threads/)

## 1.9. Design Patterns

Best practices evolved over a period of time by experienced software developer

### 1.9.1. Common Design Patterns

- **Singleton**: Manage global states, cache, threadpools, registries
- **Factory Pattern**: pass types to get a class. so I have decoupled myself from the actual constuctor methods. E.g. Hiring Process
Abstractions, hide implementation from requestor. However this can lead to harder to read code.
Very easy to test, just mock the abstract class or interface.
- **Observer Pattern**: one to many relationship between objects..whenever you are interested in the state, and want to be notified when there is change.
- **Strategy**: Different implementation of the same method.

- **Builder pattern**

```java
public class Pizza {
  private int size;
  private boolean cheese;
  private boolean pepperoni;
  private boolean bacon;

  public static class Builder {
    //required
    private final int size;

    //optional
    private boolean cheese = false;
    private boolean pepperoni = false;
    private boolean bacon = false;

    public Builder(int size) {
      this.size = size;
    }

    public Builder cheese(boolean value) {
      cheese = value;
      return this;
    }

    public Builder pepperoni(boolean value) {
      pepperoni = value;
      return this;
    }

    public Builder bacon(boolean value) {
      bacon = value;
      return this;
    }

    public Pizza build() {
      return new Pizza(this);
    }
  }

  private Pizza(Builder builder) {
    size = builder.size;
    cheese = builder.cheese;
    pepperoni = builder.pepperoni;
    bacon = builder.bacon;
  }
}
```

- **Iterator Pattern** : A way to access the elements of a collection in a sequential manner , without need to know its underlying implementations.

- **Proxy pattern** : Proxy pattern is used when we need to create a wrapper to cover the main object's complexity from the client.

## 1.10. Inversion of Control

```java
// instaed of doing 
public class TextEditor {

    private SpellChecker checker;

    public TextEditor() {
        this.checker = new SpellChecker();
    }
}

// we do 
public class TextEditor {

    private IocSpellChecker checker;

    public TextEditor(IocSpellChecker checker) {
        this.checker = checker;
    }
}

// handing responsibility to caller instead

```

### 1.10.1. SOLID Principle

- **Single Responsibility**: Do one thing and one thing only, if too much responsiblity need to refactor.
- **Open/Closed** : Open for Extension, Closed for Modifications
- **Liskov Substitution** : subtype should be able to replace parenttype anywhere, e.g. Bird (fly) ----> Penguine, but penguine cannot fly, so violation of liskov, instead Bird interface need to be re-defined, (introduce of FlyingBird)
- **Interface Segregation**: Do not put all methods together.
- **Dependency Inversion**: Classes should depend only on abstractions and not on their concrete implementations

### 1.10.2. Design Patterns in Spring

- Factory, Bean Factory, Application Context
- Proxy Pattern, Spring AOP is one example
- Template Pattern (Strategy pattern): JDBCTemplate RestTemplate
- Observer Pattern: ApplicationEvent
- Adapter Pattern: Spring use adapter pattern to adapt to differnet controller

## 1.11. Spring Framework

### 1.11.1. Spring Framework vs J2EE

- J2EE is a set of APIs for developing distributed, multi-tierd web-based applications.
- Spring is a lightweight open-source framework for builiding enterprise level Java applications
- Spring simplifies the design process, and reduce boiler plate codes.
- Sppring offers several features that J@EE does not provide out-of-the box, such as writing unit test for your code, and support for annotation-based configuration, which can significantly reduce the amount of XML configuration required.

### 1.11.2. Design consideration of using DispatchServlet

- Provide scalable and modular architecture for bulding web applications, direct appropriate request to controllers,
- Ability to handle multiple type of request (including HTTP,SOAP)
- Support for pluggable view technologies, so we can get rid of jsps.

### 1.11.3. IoC and its implementations

Spring Core Container : BeanFactory + Application Context
how Spring core initialize: load configuration metadata --> BeanDefinitionReader --> Create BeanDefintions --> put in Registry

### 1.11.4. Bean Life Cycle

- instantiation:
- populate:
- Initialization: Aware(setBeanName, setBeanFactory, setBeanApplicationContext) --- PreInitBeanPostProcessor - -- AfterPropertiesSet()-- Init() --- PostInitBeanPostProcessor ---- destroy
- Destruction:

### 1.11.5. Bean Scope

Prototyp - Singleton - Session - Request - Application - WebSocket

### 1.11.6. How to gurantee thread safety for a Bean?

- Singleton? Bean has to be stateless
- Prototype? Put Bean's state in a ThreadLocal wrapper.

### 1.11.7. How does Spring solve Cycle Dependency between two Beans

 only works if both are setter injections, both are attribute injections, or one of them is setter inject (setter should gets instantiated first, then constructor, doesn't work other ways)
 doesn't work if both are constructor injections.
 This is because bean populate phase and instantiation phase are separate.

### 1.11.8. Autowire Need for Disambiguation

use @Qualifier annotation
use @Primary for default

### 1.11.9. Spring AOP

**under the hood**

### 1.11.10. Spring Transactions Management

Enabled by default in Spring Boot.
When enabled we can use @Transactional to annotate a bean.

**Under the hood**
Spring AOP, when injecting class via autowired, spring analyzes whether the class being injected has any type of anonotation that needs to be interpreted and if so, instead of injecting your class, injects a proxy that encapsulates all the logic of original class. 
THen in the proxy it will define rollback, and propagtion level. proxy calls the original method via reflection. 

We can define
**Propagation** : Transaction Propagation indicates if any component or service will or will not participate in transaction and how will it behave if the calling component/service already has or does not have a transaction created already

- default is Required (only create new if not existing)
- support, check if an active transaction exist, if it does, then existing will be used, if not, executed in no transactions

**Isolation Level** : for concurrency purpose... how should other process see your changes.. Read_Uncommited is the lowest isolation level
gets all the side effects
Read.Commited prevents dirty read.
Read.Repeatable read, prevents dirty and non-repeateable reads
Read.serialized, no concurrency atall

**Roll back strategy** : rollback for exceptions

**interview question** when would transaction fail even if label exist?
- DB doesn't support. Cannot set autoCommit to false
- if rollbackFor is not specified, it will only rollback for RuntimeException or Error
- if the business method caught the exception there is nothing to rollback
- Invocation within the same class
  consider the following code:
  ```java
    public void registerAccount(Account acc) {
        createAccount(acc);

        notificationSrvc.sendVerificationEmail(acc);
    }

    @Transactional
    public void createAccount(Account acc) {
        accRepo.save(acc);
        teamRepo.createPersonalTeam(acc);
    }
  ```
  because transactional is powered by Aspect-Oriented Programming, so processing occurs when a bean is called from another bean. If the method is called from the same class no proxy can be applied. 

we can use self inject or create another layer of abstraction. 
```java
// self inject
@Service
@RequiredArgsConstructor
public class AccountService {
    private final AccountRepository accRepo;
    private final TeamRepository teamRepo;
    private final NotificationService notificationSrvc;
    @Lazy private final AccountService self;

    public void registerAccount(Account acc) {
        self.createAccount(acc);

        notificationSrvc.sendVerificationEmail(acc);
    }

    @Transactional
    public void createAccount(Account acc) {
        accRepo.save(acc);
        teamRepo.createPersonalTeam(acc);
    }
}

```
- Method use final or static
- Method is no public

### 1.11.11. DB transaction isolation level
乐观锁 悲观锁
pessimistic lock, optimistic lock
MVCC
分布式锁


### 1.11.12. DB transaction lock

### 1.11.13. Reactive Programming with Spring Webflux

- Kotlin + Spring webflux could total replace Java + Spring Webflux making code much more readable
- Kotlin + Spring Flux CRUD Important pointers
  - Spring Reactive Web + R2DBC/MongoDB + Kotlin Coroutine
  - Flux -> Flow, use map to access the entity returned by Flow
  - Mono -> {entity}? Access entity directly
  - Kotlin Syntax Sugar: .let{// non-null scope}, .run{ any scope}

### 1.11.14. Docker with Spring Boot

- Build with gradlew:
```shell

./gradlew build
```

- Create Dockerfile.yaml:
```docker
FROM openjdk:19
COPY ./build/libs/webflux-2nd-example-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

- Build the docker image
```
docker build -t webflux-2-backend . 
```

- Check that docker image is created
```
docker images
```

- run the docker image in a container
```
// use the -e options to override properties in 
docker run -p 8082:8080 -e DB_HOST=192.168.0.233 webflux-2-backend

```


https://hantsy.github.io/spring-reactive-sample/data/data-r2dbc.html 

### 1.11.15. How to design a 秒杀 系统
async Kafka + redis


### 1.11.16. DB isolation level


### 1.11.17. Spring AI integration with Tensorflow
https://medium.com/@AlexanderObregon/how-to-improve-spring-boot-applications-with-artificial-intelligence-and-machine-learning-f847bd57a40e

## 1.12. Behaviour Interviews

### 1.12.1. Customer Obsession

Story:
How to make customer happy? Understanding -> Planning -> Executing -> Assessing
*Context*:

## 1.13. OS Interview Questions

### 1.13.1. Process vs Threads

| Process | Threads |
| --------|----------|
| Processes are isolated | Threads share memeory |
| Process takes more time for context switching | Threads take less time for context switching |
| The process is less efficient in terms of communication . | Thread is more efficient in terms of communication.|
| The process takes more time to terminate. | The thread takes less time to terminate. |
| It takes more time for creation. | It takes less time for creation. |

## 1.14. Network Interview Questions

### 1.14.1. TCP/IP Model of Network

**Application Layer**: HTTP, DNS, FTP, NFS< Telnet, SNMP, SRC,
**Transport Layer**: TCP / UDP
**Internet Layer**: IP, ICMP, ARP
**DataLink**: Error prevention and Point to Point Protocol framing
**Physical Layer**: Bit transmission

### 1.14.2. What happens when you enter URL int a web browser

- broweser check cache for DNS records
  - browsers' own cache
  - OS cache
  - Router Cache
  - ISP cache
- If not in Cache, ISP's DNS Server initiates a DNS query to find the IP Address of the url
- Browser init a TCP connection with the server, (3-way Handshakes, Sync, Sync-Ack, Ack)
- Browser sends an HTTP request to the webserver
- Server sends out an HTTP response
- Browser displays HTML content

### 1.14.3. Idempotency

Property of some operations such that no matter how many times you execute them, you achieve the same result

### 1.14.4. GET vs POST

- Get put request info in url, Post put in request body; Therefore Get can only carry limited amount of request, whereas POST can carry much more; with request in url, the data is exposed, wheres for POST it is more secure.
- Get is more idempotent and secure from DATABASE perspective, it is not used to change data in database,
- Get request can be cached by browser, because it is idempotent, thereby reducing burden on the web server.

### 1.14.5. PUT vs PATCH vs POST

|S.No. | PUT | PATCH|
|------|------|------|
|1  |PUT is a technique of altering resources when the client transmits data that revamps the whole resource.  |PATCH is a technique for transforming the resources when the client transmits partial data that will be updated without changing the whole data.|
|2  |The PUT HTTP method is known to be unchanged. That means, if you retry a request numerous times, that will be equal to a single request conversion.  |The PATCH HTTP method is believed to be non-idempotent. That means, if you retry the request multiple times, you will end up having multiple resources with different URIs.|
|3  |The PUT method has high bandwidth. | Whereas, the PATCH method has comparatively low bandwidth.|

Put is idempotent,
Patch and Post are not

### 1.14.6. HTTP vs HTTPS

HTTPS implements TLS (application layer security protocol) in between HTTP / TCP

- HTTP connection relies on TCP (3-way handshakes) , HTTPS requries 3-way handshakes plus TLS handsahkes
- HTTP is clear text transmission, HTTPS is encrypted
- HTTP port is 80, HTTPS is 443
- HTTPS requires Certificate from CA, to ensure Server is reliable

### 1.14.7. How Does HTTPS work

- Client init request, connect to 443
- Server side has Digital Certificate (Public key, Issuer Org, Expiry Date)
- Server send D.C to Client
- Client receives D.C, verifies its legitimacy. If it is legit, it will generate Symetric key, encrypted by D.C's public key
- Client sends Symmetric Key (encrypted) to Server
- Server decrypt the Symmetric Key with its private key, to gain the real Symmetric key. And then use the real Symmetric Key to encrypt all future transmission.
- Client recevies transmission, and use Symmetric key to decrypt the transmission to get data.

### 1.14.8. TCP vs UDP

[TCP](https://www.spiceworks.com/tech/networking/articles/tcp-vs-udp/)
The transmission control protocol (TCP) is defined as a connection-oriented communication protocol that allows computing devices and applications to send data via a network and verify its delivery, forming one of the crucial pillars of the global internet.
**Three Way HandShakes**

Communication programs and computing devices utilize TCP for exchanging messages over a network. The task of this protocol is to carry packets across the Internet and ensure the successful delivery of messages and data across networks
[How TCP works together with UDP](https://stackoverflow.com/questions/46794420/how-do-tcp-ip-and-http-work-together)

[UDP](https://www.techtarget.com/searchnetworking/definition/UDP-User-Datagram-Protocol)

| TCP | UDP |
|-----|-----|
| Guranteed Delivery | Best effort, datagram may get lost |
| Host to Host | Process to Process |
| Handshakes | no Handshakes to ensure order|

### 1.14.9. TCP 4-way HandShake to terminate connection

|Client|Server|
|----|-----|
|FIN |     |
|     | ACK|
|      |FIN + ACK|
|ACK|       |

### 1.14.10. XSS Reflected vs Persistent vs DOM

- A Persistent XSS attack is possible when a website or web application stores user input and later serves it to other users.
- Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim’s browser. **it is not stored on the web site**. Website use the user input to create part of html without even verify it.
- DOM-based XSS vulnerabilities usually arise when JavaScript takes data from an attacker-controllable source, such as the URL, and passes it to a sink that supports dynamic code execution, such as eval() or innerHTML. This enables attackers to execute malicious JavaScript, which typically allows them to hijack other users' accounts.

[XSS Persistent](https://www.acunetix.com/blog/articles/persistent-xss/)

## 1.15. Database Questions

### 1.15.1. ACID Compliance

- Atomicity − A transaction should be treated as a single unit of operation, which means either the entire sequence of operations is successful or unsuccessful.
- Consistency − This represents the consistency of the referential integrity of the database, unique primary keys in tables, etc. Not NUl, minimum 10 etc
- Isolation − There may be many transaction processing with the same data set at the same time. Each transaction should be isolated- from others to prevent data corruption.
- Durability − Once a transaction has completed, the results of this transaction have to be made permanent and cannot be erased from the database due to system failure.

### 1.15.2. CAP Therom

- Consistency : all users should see the same data at the same time
- Availability: minimal downtime, every request received by a node should have a response
- Partition tolerance: if part of the system breaks down it still functions.

### 1.15.3. SQL index, what are they, when do you use them?

### 1.15.4. WHy not indexing all columns?

- Too much memory
- Too many index can hurt performance, especially when query a subset of the columns that are used for indexing.
- [Clustered v.s. NonClustered, Use Cases Etc](https://medium.com/fintechexplained/clustered-vs-non-clustered-index-8efed55ed7b9)

### 1.15.5. Clustered vs Non-Clustered index

P.K ---> Clustered Index
Unique ---> Non-Clustered Index

|Clustered|NonClustered|
|--- | ----|
|in-place|Collect and copied to another|
|Faster| Slower|
|Less memory to execute| More memory to execut|
|One per table | many per table|
|Natual ability to store data on the disl | not having the natural strength to store data on the disk|

[Clustered v.s. NonClustered, Use Cases Etc](https://medium.com/fintechexplained/clustered-vs-non-clustered-index-8efed55ed7b9)

### 1.15.6. Explain keyword MySQL

you can use explain keyword to help you optimize your search

### 1.15.7. MYSQL 回表

search use secondary index, but request for stuff it doesn't have, therefore need to traverse the table again for stuff.

### 1.15.8. MYSQL how to enable Master Slave Replication

- New Data written into  Master, master will update binlog
- Master create a dump thread, and push binlog to slave
- Slave when connected to master, will create an IO thread to take ino the binlog, and write to relaylog.
- Slave will open another sql thread to read the relay log and execute in slave. thus synchronize
- slave updates its own bin log.

### 1.15.9. MySQL dynamically scalling

## 1.16. System Design Interview

[系统设计面试题整理](https://juejin.cn/post/6995797668190486535)
[System Design Primer](https://github.com/donnemartin/system-design-primer/blob/master/README-zh-Hans.md#%E5%BC%B1%E4%B8%80%E8%87%B4%E6%80%A7)

### 1.16.1. what kind of questions should I ask???

[how to solve system design](https://www-zhihu-com.translate.goog/question/26312148?_x_tr_sl=zh-CN&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=sc)

- 这个系统的核心功能是什么？
- 有多少用户使用我们的产品？
- 公司的业务发展速度怎么样，3 个月、半年、一年后，规模会变成多大？
- 公司的技术栈是什么？有什么现存的服务可以简化我们的设计。
- Who is going to use it?
- How are they going to use it?
- How many users are there?
- What does the system do?
- What are the inputs and outputs of the system?
- How much data do we expect to handle?
- How many requests per second do we expect?
- What is the expected read to write ratio?

### 1.16.2. Back Of Envelop Calculation

Objectives

- number of concurrent TCP connections a a server can support
- The number of requests per second a web database or cache server can handle.
- The storage requirements of a service.

**Componenents**:

- **WebServer**(High number of processors, low ram and low hardDisk, for Handling API Calls)
  - Usually serve static content
  - e.g. Facebook 32G Ram + 500GB Storage + 16-Core

- **Application Server** (Medium Processor, high ram, medium Disk), requires extensive computational and storage resources
  - usually serves dynamic content
  - e.g. Facebook 256G ram + 6.5TB storage + quad core

- **Storage Server** (low ram + medium processor + High disk)
  - SQL or NoSQL
  - e.g. Facebook 32G ram + 120TB harddisk

**Typical Example**

**Given** 500M active user, 20 Requester per Day
A server that can handle 8000 RPS

**Calculate** number of servers needed? Storage Requirements? Bnadwidth

**Answer 1**
500M * 20 / 86400 = 115K RPS (System)
Number of server = 115K / 8000 = **-15 Servers-** Not right
Peak load: 500M RPS (all customer sending at once)
Number of servers : 500 M / 8000  = **62.5 K servers**

**Answer 2**
500M *2* 200 B = 200GB normal msg tweets
50M *2* 200 KB = 20TB
50M * 3MB = 150TB

170TB/day *10* 365 = 1700 *365 TB = 1600* 400 = 640 K * TB = **640 PB**

**Answer 3**

- Estimate the daily amount of incoming data to the service.
- Estimate the daily amount of outgoing data from the service.
- Estimate the bandwidth in Gbps (gigabits per second) by dividing the incoming and outgoing data by the number of seconds in a day.

For write bandwidth : 170TB / 86400 * 8 = 16Gb/s

For read bandwidth: Assume a user views 50 tweets/a day
Normal Tweets: 50 *500M / (86400)* 200 B = 25 *M / 86.4* 200  = 5000 / 86.4 MB *8 = 480Mb/s
Image Tweets : 5* 500M / (86400) *200KB = 500* M / 86.4 *8 = 45 Gb/s
Video: 5* 25M / (86400) *3MB = 375TB* 8 / 86400  = 3000TB / 86400 = 3 TB / 8.64 = 0.35 TB = 350Gb/s

400Gb/s read, 16Gb/s write

### 1.16.3. Basic Building Blocks

#### 1.16.3.1. Domain Name system

#### 1.16.3.2. Load Balancers

Health Cehcking(heart beat protocol)
TLS terminations

#### 1.16.3.3. Database

##### 1.16.3.3.1. SQL vs NoSQL

| SQL | NoSQL|
|-----|------|
| Impedence Mismatch | Simple Design |
| hard to scale | Horizontal Scaling |
| ACID Compliance | Highly available |

Type of NoSQL (key value pair DynamoDB / Redis, Columnar / BigTable, HBase, Cassandra, Graph Neo4j, Document / MangoDB, CouchDB)

##### 1.16.3.3.2. Data Replication

Single leader / Multileader / peer to peer
Single Lead is most effective for high read.

##### 1.16.3.3.3. Data Distributions

pros and cons

#### 1.16.3.4. Key-Value Store

#### 1.16.3.5. Distributed Search

### 1.16.4. Design of stock Exchange System


crawling - indexing - searching

## 1.17. Effective Software Engineering

Sometimes people will ask this.

### 1.17.1. Six pillars of Effective Software

- Meet users’ expectations
- No defects
- Scale out horizontally
- No dedicated production support team
- Accelerate development pace
- Double ROI per developer, team, and software

### 1.17.2. From Customer Insights to Internal Requirements

talk to customers asap.
Do white-board modelling, visualize entities and their relationships,
UML diagram or sequence diagram (Confluence)

Write Requirements and Stories in Ubiquitious language. Gherkin

Backlog refinement / sprint planning to refine work.

### 1.17.3. Implementation and Coding

- continuous Improving / refactoring
- Quality over quantity
- Use OOP Design patterns, SOLID Principles
- **Law of Demeter**, handle the exception thrown by your method
- Practice test driven developmnet
  - maximize coverage for business logic
  - Make sure to write unit tests for both back-end and front-end code
  - TDD, BDD

### 1.17.4. Testing and Quality Assurance

- Test everything and automate everything
- Test Design Per Case, Don't overload a test
- Apply Test automatiion design patterns, Gherkin test pattern
- Test Data Management, centralized / decentralized

### 1.17.5. Clean Code in Java

- Code should be Focused
- Code should be Simple
- Code should be Testable

- Naming Conventions (camelCase)
- Class structure, exactly one top level clases
- Indentations and white space
- Restrict Method Paramters (bundle some of the parameters together into type)
- Avoid Hardcoding, use values define in .properties or .config files...in environment
- Code comments, used to explain a decision.
- Logging, log meaningful error messages
- Follow SOLID principles
- DRY, Don't repeat yourself, KISS, Keep it Simple Stupid
- TDD, write test first before any code.
- use linting tools, SonarQube SonarLint

### 1.17.6. Best Practices

#### 1.17.6.1. why is String final in Java

内存(memory)
同步(synchronization)
数据结构(data structure)

1. Memory, we use String pool, multiple clients to access same String, this saves memory
2. hashcode of String will not change, doesn't have to recompute everytime, so it helps with operations involving hash such as Set.contains, Map.contains etc
3. It is widely used in class loading, so if it is mutable we might load something dangerous, and destroy our security
4. Immutable objects are threadsafe  by nature

#### 1.17.6.2. JDBC best practices

- Connection Pool is expensive, use HiKariCP. (default ConPool for Sprintboot 2)
- Try to exectute batch request,

```java
      try {
         factory = new Configuration().configure().buildSessionFactory();
      } catch (Throwable ex) { 
         System.err.println("Failed to create sessionFactory object." + ex);
         throw new ExceptionInInitializerError(ex); 
      }
      ManageEmployee ME = new ManageEmployee();

      /* Add employee records in batches */
      ME.addEmployees( );
   }
   
   /* Method to create employee records in batches */
   public void addEmployees( ){
      Session session = factory.openSession();
      Transaction tx = null;
      Integer employeeID = null;
      
      try {
         tx = session.beginTransaction();
         for ( int i=0; i<100000; i++ ) {
            String fname = "First Name " + i;
            String lname = "Last Name " + i;
            Integer salary = i;
            Employee employee = new Employee(fname, lname, salary);
            session.save(employee);
          if( i % 50 == 0 ) {
               session.flush();
               session.clear();
            }
         }
         tx.commit();
      } catch (HibernateException e) {
         if (tx!=null) tx.rollback();
         e.printStackTrace(); 
      } finally {
         session.close(); 
      }
      return ;
```

```xml
<property name = "hibernate.jdbc.batch_size">50</property>
```

- Replication and Sharding

# 2. How to use OPENAI API in SpringBoot Project

```xml
<dependency>
    <groupId>com.openai</groupId>
    <artifactId>openai-java</artifactId>
    <version>1.0.0</version>
</dependency>
```

Create a OpenAIService class that will interact with the OpenAI API.

This class should use the OpenAI class from the OpenAI Java client library to make API requests.

```java
import com.openai.OpenAI;
import com.openai.exception.AuthenticationException;
import com.openai.exception.OpenAIException;
import com.openai.model.CompletionRequest;
import com.openai.model.CompletionResponse;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class OpenAIService {
    // in application.properties, put
    // openai.apiKey=MY_API_KEY

    @Value("${openai.apiKey}")
    private String apiKey;

    private OpenAI openAI;

    public OpenAIService() {
        this.openAI = new OpenAI(apiKey);
    }

    public String generateText(String prompt, String model, int maxTokens, double temperature) throws AuthenticationException, OpenAIException {
        CompletionRequest request = new CompletionRequest.Builder()
                .prompt(prompt)
                .model(model)
                .maxTokens(maxTokens)
                .temperature(temperature)
                .build();

        CompletionResponse response = openAI.complete(request);
        return response.getChoices().get(0).getText();
    }
}

```

In your controller class, inject the OpenAIService and call the generateText() method to generate text using the OpenAI API.

```java
import com.openai.exception.AuthenticationException;
import com.openai.exception.OpenAIException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TextGenerationController {

    @Autowired
    private OpenAIService openAIService;

    @GetMapping("/generateText")
    public String generateText(@RequestParam String prompt,
                               @RequestParam String model,
                               @RequestParam int maxTokens,
                               @RequestParam double temperature) throws AuthenticationException, OpenAIException {
        return openAIService.generateText(prompt, model, maxTokens, temperature);
    }
}

```

```java
// an exmaple of usage

@RestController
public class EssayImprovementController {
    
    @PostMapping("/improve-essay")
    public String improveEssay(@RequestBody String essay) throws Exception {
        String prompt = "Please provide suggestions to improve the following essay:\n\n" + essay + "\n\nSuggested improvements:";
        
        CompletionRequest request = new CompletionRequest.Builder()
            .setEngine("text-davinci-002")
            .setPrompt(prompt)
            .setMaxTokens(100)
            .setN(1)
            .setTemperature(0.5)
            .build();
            
        CompletionResponse response = Completion.create(request);
        
        return response.getChoices().get(0).getText().trim();
    }
}

```

## 2.1. Another way to improve Grammar via GrammarBot API (Not Feasible)

**From ChatGPT**

```xml
<dependency>
    <groupId>com.github.kevinstl</groupId>
    <artifactId>grammar-bot-client</artifactId>
    <version>1.0.0</version>
</dependency>

```

This controller has a single endpoint, /check-grammar, which accepts a POST request with a JSON payload containing a single field, "text". The controller passes the text to GrammarBot API using the GrammarBotAPI instance created in the constructor, and returns a list of Correction objects in the response.

```java
import com.github.kevinstl.grammarbotapi.GrammarBotAPI;
import com.github.kevinstl.grammarbotapi.GrammarBotAPIImpl;
import com.github.kevinstl.grammarbotapi.models.Correction;
import com.github.kevinstl.grammarbotapi.models.GrammarBotResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class GrammarBotController {

    private final GrammarBotAPI grammarBotAPI;

    public GrammarBotController() {
        grammarBotAPI = new GrammarBotAPIImpl();
    }

    @PostMapping("/check-grammar")
    public ResponseEntity<List<Correction>> checkGrammar(@RequestBody String text) {
        GrammarBotResponse response = grammarBotAPI.check(text);
        List<Correction> corrections = response.getCorrections();
        return ResponseEntity.ok(corrections);
    }
}

```

Run your Spring Boot application and make a request to the /check-grammar endpoint with some text to test the integration with GrammarBot API. Here's an example using the curl command:

```bash
curl -X POST \
  http://localhost:8080/check-grammar \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "I is very happy."
}'


```

# 3. Use old laptop as a proxy server

Yes, you can use your old Windows laptop in Singapore as a proxy or VPN server to bypass internet censorship in China and access Gmail. Here's how you can do it:

    Choose a proxy or VPN server software: There are several free and paid proxy or VPN server software available online that you can use to set up your server. Some popular options include OpenVPN, SoftEther VPN, and Squid Proxy.

    Install and configure the proxy or VPN server software on your Windows laptop: Once you've chosen your software, you'll need to download and install it on your old Windows laptop. Follow the instructions provided by the software to configure the server settings, such as the IP address, port number, and authentication settings.

    Open the necessary ports on your router and firewall: To enable access to your proxy or VPN server from outside your local network, you'll need to configure your router and firewall to allow incoming connections on the necessary ports. You'll need to open the port that you have chosen to use for your proxy or VPN server, as specified in your software settings.

    Connect to your proxy or VPN server from China: Once you've set up your server and opened the necessary ports, you can connect to your proxy or VPN server from China using your laptop's public IP address and the port number you've configured. You can then use your proxy or VPN connection to access Gmail or other blocked websites.

It's important to note that using a proxy or VPN server to bypass internet censorship in China may not always work, as the Great Firewall is constantly evolving and developing new techniques to block internet traffic. Additionally, using a proxy or VPN server may be illegal or against the terms of service of your internet service provider in some countries. Be sure to check local laws and regulations before using a proxy or VPN server to bypass internet censorship.


# 4. Java Linux Notes

# 5. Azure

- **Microsoft Azure**
  - 2 (Readonly Geo-Redundant-Storage)
  - 8 I think can use admin unit to delegate control of certain group of peopl
  - 26, You are required to make sure that during the deployment, the administrative credentials are encrypted using a suitable Azure solution.
    - you should use Azure Key Vault
  - 29, Identity Protection == Conditional Access
  - 43: Azure storage is PaaS, Azure VM with MS SQL Server is IAAS
  - 45, 
  - 50: Azure Site Recovery provides fault tolerance for vm. 
  - 54, 55,
  - 57, Azure Virtual Machines is
  - 69: Azure backup is in fact PaaS 
  - 70, 82, 83, 92, 
  - 97: 
  - 100: a subscription can only be associated with one tenant, a tenant can have multiple subscription
   
  - 101, 102, 105, 106, 107, 108, 109
  - 111: Azure file is Azure's easy to use cloud file system
  - 114: tags not inherited
  - 115: Datathat is stored in the archive access tier must be rehydrated before the data can be accessed. 
  - 119: A Local Network Gateway is an object in Azure that represents your on-premise VPN device. A Virtual Network Gateway is the VPN object at the Azure end of the
VPN. A 'connection' is what connects the Local Network Gateway and the Virtual Network Gateway to bring up the VPN.
  - 121: Every Azure region has multiple data center
  - 124: Sphere=secure, central=monitor, hub=not the other two
  - 128: subscription can contain multiple resource group, one resource group belong to one subscription
  - 133: HD is hadoop 
  - 134: archive tier is not set at account level, it is at blob level
  - 143: Azure sphere is highly secure IOT solution that includes microC, and customized Linux OS
  - 152: when youn want to assign permission to several azure vm, you can simply assing permision to a resource group. 
  - 154: Azure Data Warehouse == Azure Synapse Analytics == High availability 99.9%
  - 156: Azure container instance is an Azure compute services, The term compute refers to the hosting model for the computing resources that your application runs on
  - 157: Express Route is on layer 3 of OSI model
  - 158：Application insight is a feature of azure monitor
  - 159: if you delete a resource group, all resources within are deleted. 
  - 160: You can use Power BI to analyze and visualize data stored in Azure Data Lake and Azure SQL Data Warehouse.
  - 161: Azure Portal
  - 166: From Azure Service Health, an administrator can create a rule to be alerted if an azure service fails
  - 167: use powershell to manage resources
  - 168: Help and support will show you planned maintenance on Azure subscription
  - 171: health = monitor, image = marketplace, recommendations = advisor
  - 173: Azure logic APP is a serverless computing solution, helps you schedule automate and orchestrate tasks. 
  - 178, 
  - 183, Azure Advusir does not provide recommendation on how to configure virtual network
  - 187
  - 197: you cn use azure cost management to view the usage of virtual machiens during the last three months
  - 200: Azure Databricks is an apache spark-based analytics service
  - 209: Microsoft Trust Center provides in-depth information about security, privacy compliance offerings, polices and features across microsoft cloud products
  - 213: Azure Monitor can monitor the performance of on-premises computers, also trigger alerts based on data in an Azure log analytics workspace
  - 216: use azure virtaul machines services to view service failure notifications that can affect the availability of VM1
  - 220: Azure firewall provides network traffic filtering** across multiple azure subscriptions** and virtual networks. Network security groups provide distributed network layer traffic filtering to limit traffic to resources within virtual networks in each subscription. 
  - Service health notifies you of Azure related services issues, such as region-wide downtime
  
  - MS Sql server 2019 on Azure VM is an e.g. of IAAS
  - Azure Files is IAAS
  - Service endpoints are used to expose Azure services to a virtual network; ExpressRoute is used to connect an on premises network to Azure. Nsg allow you to configure inbound and outbound ruls for virtual networks and virtual machines. Peering allows you to connect virtual network together. 

management groups can be used in environments that have multiple subscriptions to streamline the applicaiton of governance conditions. 
Resource grop can be used to organize azure resources
Admin units are used to delegate the administration of azure ad resources, such as users and groups
accounts are used to provide access to resouces. 

Health advisories are issues that require that you take proactive action to avoid service interruptions, such as service retirements and breaking changes. Service issues are problems such as outages that require immediate actions.

Two Azure subscriptions **acannot be merged into a single subscription**



# 6. Kotlin

## 6.1. Kotlin Coroutine 
Kotlin coroutine is implemented using continuation passing style. 
each suspend function will take in a continuation object.
each continuation object will have a state (indicating where the caller is at in its code) and a callback to the caller function

when suspended, the function yields the control of thread to the dispatcher. 
The dispatcher, when have free thread, will call resumeWith of the continuation object, which in turn will invoke the original suspend fucntion, with updated state. 



## 6.2. Kotlin + Spring Boot

- Kotlin Spring Boot webflux + mongodb example: https://www.mongodb.com/developer/languages/kotlin/spring-boot3-kotlin-mongodb/
- Introduction to How Kotlin can make Spring webflux easier: https://www.youtube.com/watch?v=ahTXElHrV0c
- Reactive Springboot with Kotlin and Virtual Threads: https://www.youtube.com/watch?v=szl3eWA0VRw  
- Reactive + WebClient
  - https://codersee.com/spring-5-webclient-with-spring-boot/
  - https://codersee.com/spring-webclient-with-kotlin-coroutines/
  
  - Reactive + DB
    - https://spring.io/guides/tutorials/spring-boot-kotlin
    - https://howtodoinjava.com/spring-webflux/spring-webflux-tutorial/
    - https://www.youtube.com/watch?v=1vuJFo42zko&list=PLvN8k8yxjoesNnd0C0t4s36bgVHUwJkIR&index=2
    - https://codersee.com/reactive-rest-api-with-spring-kotlin-and-coroutines/

  - Spring Secruity
    - https://codersee.com/spring-boot-3-spring-security-6-with-kotlin-jwt/
  - WebSocket with Kotlin and Spring Webflux
    - https://spring.io/guides/tutorials/spring-webflux-kotlin-rsocket

## 6.3. Jepack Compose
- Under the hood
  - Gap Buffer to store UI class
  - Positional Memoization
  - https://medium.com/androiddevelopers/under-the-hood-of-jetpack-compose-part-2-of-2-37b2c20c6cdd 
  - 数据驱动UI: like Flutter 

# 7. Kafka

In summary, the keystore is used by servers to store their private keys and certificates, while the truststore is used by clients to store certificates of trusted servers or CAs. They both play crucial roles in establishing secure communication channels over SSL/TLS.

# 8. PluralSight Java Clean code practices

- FileNotFoundException extends IOException, and it is checked Exception
- NumberFormatException is unchecked Exception, because there is nothing to handle when this error happen. Nobody knows what the original string look like for example. 
- ClassNotFoundException is checked exception

Q: which situation requires you to choose composition instead of inheriting from class A?
A: when class A provides only private constructors

- EnumSet only contains enum values, and it is represented internally as bit vectors
- EnumSet is not threadSafe

Q: what happens when you call shutdownNow() on a threadPoolExecutor?
A: it will attemp to stop all currently running tasks, but it does not wait for the tasks and threads to be stopped
The shutdownNow () method of ThreadPoolExecutor class attempts to stop all the tasks which are executing actively, halts the processing of waiting tasks and returns a list of the tasks that were awaiting execution.

Q: what happens if you use the following class in a Program?
```java
public class Person{
  private String name;
  public Person(String name) {
    this.name = name
  }
}

class Employee extends Person {
  private String department;
  public Employee(String department) {
    this.department = department;
  }
}
```
A: it doesn't compile because Employee constructor will implicitly try to use the no-args constructor of its Parent Class(Person), which does not have any. 


Q: What does the dependency inversion SOLID principle mean?
A: High level modules(which uses other modules to perform tasks, kind like a manager) should not depend on low level modules(such as me)
Both should depend on abstractions. 

Q: What is true about creating accessor methods for private fields?
A: It allows you to insert additional actions when a field is accessed.

Q: What is disadvantage of immutable classes?
A: They require one separate object for each distinct value.

Q: Which pattern allow you to change the algorithm behavior of software with the use of lambda expression based on runtime decisions?
A: Strategy Pattern

- [Command Pattern](https://www.baeldung.com/java-command-pattern)
- [Strategy Pattern](https://www.baeldung.com/java-strategy-pattern)

Q: Why won't the following code compile?
```java
public final class Car {
  private String make;
  //other fields

  public void setMake(String _make) {
    make = _make;
  }

  private String getMake() {
    return make;
  }
}

public class MyClass {
  public static void main(String[] args) {
    Car car = new Car();
    car.setMake("Toyota");
    String make = car.getMake();
  }
}

```
A: the accessor method should be declared public!
- Final class is class that cannot be further extended. 

**Wrong Quesitons**
1. Which stream method receives a predicate written as a lambda expression? 
   a. **allMatch()**
   b. findAny() 
   c. reduce()
   d. max()

2. What does the dependency inversion SOLID design principle mean? 
   a. Abstractions should depend on details.
   b.**The high-level and low-level modules should depend on abstractions.**
   c. A container should inject dependencies.
   d. The high-level modules should depend on the low-level modules.

3. What happens when you call shutdownNow() on a ThreadPoolExecutor?
   a. The shutdownNow() method puts the ThreadPoolExecutor in the shutdown state, which means that it will not accept new tasks, and then it waits until all currently executing tasks have finished before returning.
   b. The shutdownNow() method only puts the ThreadPoolExecutor in the shutdown state, which means that it will not accept new tasks, but currently executing tasks will continue to run.
   c. **The shutdownNow() method attempts to stop all currently executing tasks, but it does not wait for the tasks and threads to be stopped.**
   d. The shutdownNow() method forces all threads to stop and doesn't return until all threads in the pool have stopped.

4. What is an example of an unchecked exception? 
   a. ClassNotFoundException
   b. IOException
   c. **NumberFormatException**
   d. FileNotFoundException

5. What will happen if you use the following classes in a program?
```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }
}


class Employee extends Person {
    private String department;

    public Employee(String department) {
        this.department = department;
    }
}
```
a. It compiles without errors, but when you create an Employee object, the member variable name would be set to null.
b. **Class Employee would not compile, because its constructor implicitly tries to use the no-arguments constructor of class Person and class Person does not have such a constructor.**
c. Class Employee would not compile, because it is not a public class but its superclass Person is. A subclass cannot have a more restrictive access specifier than its superclass.
d. It compiles without errors, but there would be no way to access the name and department member variables. You must add getter methods to get the values of the member variables.

6. When would you declare an object through implementation rather than through an interface?
   a. When the implementation contains a limited number of methods that can be used on the object 
   b. When the implementation extends a class which in turn implements an interface
   c. **When the implementation provides additional methods that must be called on the declared object**
   d. When the implementation extends an abstract class which in turn implements an interface

7. What would you use to implement the strategy pattern?
   a. **One interface with concrete classes implementing the interface**
   b. One single class which ensures that only one object is created
   c. One class that implements multiple interfaces
   d. Separate classes to control the application logic, visualizations, and data flow

# 9. PluralSight Cloud Fundamental

1. Which process grants a user permission to access different levels of information and perform specific functions, depending on the rules established for different types of users?
    
    System access

    Correct -
    **Authorization**

    Incorrect -
    Authentication

    Your choice: incorrect -
    Role-based access

    Incorrect -
    I don't know yet.

2. Your organization moved all its systems to a cloud services provider. You must update the design of your business-critical applications that require the shortest failover time possible in case of a disaster affecting the local region. Which cloud provider offering will you use to achieve this requirement?

    Incorrect
    Design the application so you can deploy it across multiple regions.

    Your choice: incorrect -
    Design the application so you can deploy it across multiple clusters in an availability zone.

    Correct -
    **Design the application so you can deploy it across multiple availability zones**.

    Incorrect -
    Design the application so you can deploy it across multiple cloud providers.

    Incorrect -
    I don't know yet.

3. Which cloud storage systems allow you to retain petabytes of unstructured data?
    Network-attached storage

    Incorrect -
    File store

    Your choice: incorrect -
    Block store

    Correct -
    **Object store**

    Incorrect -
    I don't know yet.

4.  What is correct with regards to the Small Message Block (SMB) protocol?
    It it optimized for small files and have a maximum file size of 1 gigabyte.

    Incorrect -
    It is only used on Linux. 

    Incorrect -
    It does not support encryption.

    Correct -
    **It is used to transfer files in a Windows environment.**

    Incorrect -
    I don't know yet.

5. You want a system to centrally manage your users and to map out the relationship users have with the digital assets they use in your company. What system will you choose?
    A configuration management database (CMDB)

    Incorrect -
    An information technology asset management (ITAM) system

    Your choice: incorrect -
    A relational database

    Correct -
   **A directory service**

    Incorrect -
    I don't know yet.

6. What is the procedure for signing a contract with most well-known cloud service providers?
    The service provider provides a flexible contract that is adapted to your case.

    Incorrect -
    You provide a flexible contract that is adapted to your use case.

    Correct -
    **The service provider provides a standardized and non-negotiable contract.**

    Incorrect -
    You provide a standardized and non-negotiable contract.

7. Which tool is appropriate for configuration management?
    PowerShell

    Incorrect -
    Cloudability

    Correct -
    **SaltStack**

    Incorrect -
    Prometheus 

8. What service is responsible for providing an IP address and other configuration?
    Network as a service (NaaS)

    Correct -
    **Dynamic Host Configuration Protocol (DHCP)**

    Incorrect -
    Network address translation (NAT)

    Your choice: incorrect -
    Domain Name System (DNS)

9. What is true about the order of operations in a network security group?
    Rules are processed in priority order, with higher ports processed before lower ports.

    Incorrect -
    Rules are processed in priority order, with higher numbers processed before lower numbers.

    Correct -
    **Rules are processed in priority order, with lower numbers processed before higher numbers**.

    Incorrect -
    Rules are processed in priority order, with lower ports processed before higher ports.

10. Which data security standard specifies an information security management system?
    General Data Protection Regulation (GDPR)

    Correct -
    **International Organization for Standardization (ISO) 27001**

    Incorrect -
    Health Insurance Portability and Accountability Act (HIPAA)

    Your choice: incorrect -
    International Organization for Standardization (ISO) 9001

11. You deployed a legacy application into a virtual private cloud (VPC) on a public cloud provider. The app uses Ethernet broadcast to discover additional instances of the application. After migration, the application fails to detect other cases even though you deployed them within the same subnet in the VPC. What is the most likely cause of this issue?
    
  Ethernet broadcasts are a security risk in the cloud and are generally not available in VPCs.

  Incorrect -
  Ethernet broadcasts in VPCs require you to install additional software on the virtual machines.

  Correct -
  **Ethernet broadcasts hinder scalability in the cloud and are generally not available in VPCs.**

  Incorrect -
  Ethernet broadcasts require you to make configuration changes to the operating system to function within VPCs.

12.  Your organization adopted a remote working policy. You want to quickly scale as you grow your virtual desktop infrastructure (VDI) fleet without committing to expensive infrastructure components upfront. You have access to a substantial amount of commodity data center hardware with locally attached storage devices. What will you do to support this while minimizing your operational costs? 

  Deploy the VDI fleet using hybrid cloud infrastructure.

  Correct -
  **Deploy the VDI fleet using hyperconverged infrastructure.**

  Incorrect -
  Deploy the VDI fleet using software-defined infrastructure.

  Incorrect -
  Deploy the VDI fleet using public cloud infrastructure.

13. Your company’s software is awaiting feedback from potential customers. What build type is appropriate for the software?
  Beta release

  Correct -
  **Open beta release**

  Incorrect -
  Perpetual beta release

  Incorrect -
  Release candidate

14. You build a cloud-based system that requires users to connect to it securely. You do not want to manage the various components necessary for secure connectivity, however. What cloud-based service should you use?

  Software as a service (SaaS)

  Correct -
  **Public key infrastructure (PKI) as a service (PKIaas)**

  Incorrect -
  Security as a service (Saas)

  Incorrect -
  Infrastructure as a service (IaaS)

15. Which component of the critical public infrastructure is responsible for receiving certificate signing requests, verifying the identity of an end entity, and approving a proposal before the certificate can be issued?
  Validation authority (VA)

  Correct -
  **Registration authority (RA)**

  Incorrect -
  Certificate Store (CA)

  Your choice: incorrect -
  Certificate authority (CA)

16. You are designing an application that will transmit sensitive data, such as stock market data, to another system for processing. You estimate the transaction volumes to be high and to require fast data processing, and your data must be secured in transit. What encryption technology will you implement?

  Synchronous encryption

  Correct -
  **Symmetric encryption**

  Your choice: incorrect -
  Asymmetric encryption

  Incorrect -
  Asynchronous encryption

17. What is an example of a method for securely transferring files between computers using Transport Layer Security (TLS) encryption?
  Secure File Transfer Protocol (SFTP)

  Correct -
  **File Transfer Protocol Secure (FTPS)**

  Incorrect -
  Secure Shell (SSH)

  Your choice: incorrect -
  Hypertext Transfer Protocol Secure (HTTPS)

18. You need durable storage for static content and infinitely scalable data storage infrastructure at the lowest cost. What type of storage will you choose?

  File storage

  Your choice: incorrect -
  Storage area network

  Incorrect -
  Block storage

  Correct -
  **Object storage**

19. You implement controls to safely store data from an application that collects patient health and payment information. What data classification policy must you use to ensure the safety of the data?

  Use the International Organization for Standardization (ISO) 9001 framework to protect the data.
  Your choice: incorrect -Use the International Organization for Standardization (ISO) 27001 framework to protect the data.
  Incorrect -
  Classify the data as internal.

  Correct -
  **Classify the data as restricted.**

20. What allows you to locate servers close together, even on the same host, to minimize network latency?
  **Cluster placement groups**

  Incorrect -
  Network placement groups

  Your choice: incorrect -
  Hypervisor configuration rules

  Incorrect -
  Virtual machine deployment configuration

21. What hypervisor function allows the hypervisor to reclaim unused memory from a virtual machine?
  Memory over commitment

  Incorrect -
  Memory re-allocation

  Correct -
  **Memory ballooning**

  Incorrect -
  Memory reclamation

22. You want to deploy a system into a public cloud. Based on your software architecture landscape, you must create and run several virtual machines on each server machine that you use that you already virtualized inside the public cloud. Before you make your public cloud selection, what should you do?
  Ensure that you can pay for hypervisors in a pay-as-you-go manner.

  Your choice: incorrect -
  Ensure that the cloud provider you chose supports hypervisors.

  Incorrect -
  Ensure that you can deploy hypervisors on the cloud provider you chose.

  Correct -
  **Ensure that the cloud provider you chose supports nested virtualization.**

# 10. PluralSight Core-Spring

1. How will you directly add attributes to the model for a view in a controller method?
    Your choice: incorrect -
    By annotating a method parameter with @ModelAttribute

    **By annotating the method with @ModelAttribute**

    Incorrect -
    By using the @PathVariable annotation on a method parameter

    Incorrect -
    By using the @RequestMapping annotation on the method

2. While checking a Spring Cloud application code, you come across some lines that keep track of all the services the application uses along with their instances. How can you use such services in your application? 
    Correct -
    **Through service discovery**

    Incorrect -
    Through dependency injection

    Incorrect -
    Through the @EnableEurekaServer annotation 

    Your choice: incorrect -
    Through @EnableDiscoveryClient annotation 

3. If you want to set a property on the mock property source for the current environment, which method would you use?
    Incorrect -
    Environment's setActiveProfiles(String... profiles) method

    Incorrect -
    MockPropertySource's addPropertySource(String name, Object value) method

    Correct -
   **MockEnvironment's withProperty(String key, String value) method**

    Your choice: incorrect -
    MockEnvironment's addProperty(String key, String value) method

4. The Spring Framework provides built-in support for mocking which object when writing unit tests?
   
    **Environment**

    Resource

    BeanFactory

    JdbcTemplate

5. Which feature only exists in Spring Boot?
   
    **Type-safe configuration properties**

    @Conditional bean creation

    Support for YAML

    Reactive programming model

6.  What are the two components typically configured when setting up Lightweight Directory Access Protocol (LDAP) authentication in Spring Security?

    AccessDecisionManager and AuthenticationProvider

    UserService and JdbcDaoImpl

    **BindAuthenticator and LdapAuthoritiesPopulator**

    LdapAuthenticator and DaoPopulator

7. Which Java specification provides built-in mocks for unit testing in the Spring Framework?

    The Enterprise JavaBeans (EJB) specification

    **The Servlet specification**

    The Java Data Objects (JDO) specification

    The Java Persistence API (JPA) specification

8. How would you retrieve data using the WebClient class from an endpoint at URL http://localhost:2020 in the simplest way?
    Incorrect -
    ```java
    public class StudentClient {
      WebClient sclient = WebClient.create().get().uri("http://localhost:2020");
    }
    ```
    Correct -
    ```java
    public class StudentClient {
    WebClient sclient = WebClient.create("http://localhost:2020");
    // ...
    }
    ```
    Incorrect -
    ```java
    public class StudentClient {
    WebClient sclient = WebClient("http://localhost:2020");
    // ...
    }
    ```
    Your choice: incorrect -
    ```java
    public class StudentClient {
      WebClient sclient = WebClient.builder().baseUrl("http://localhost:2020").build();
    }
    ```
9. Which annotations would you apply to your code to have more control of the dependency injection process? 

    @Qualifier and @Component

    @Autowired, @Component, and @Qualifier

    @Component and @Configuration

    **@Autowired and @Qualifier**

10. Your Spring Boot application defines a configuration value as an environment variable:
GREETING="never gonna give you up"
What must you use to override this value, according to the PropertySource order that Spring Boot uses?
    
    Incorrect -
    An application.properties file packaged within your jar

    Correct
    **A command-line argument when executing the jar**

    Incorrect -
    An application.properties file in the same directory as your jar

    Your choice: incorrect -
    A @PropertySource annotation with your @Configuration class

11. Which is a key difference between Spring aspect-oriented programming (AOP) and AspectJ AOP?
    Incorrect -
    AspectJ is slower and more powerful than Spring AOP.

    Your choice: incorrect -
    AspectJ is faster but less powerful than Spring AOP.

    Incorrect -
    AspectJ is slower and less powerful than Spring AOP.

    Correct -
    **AspectJ is faster and more powerful than Spring AOP.**

12.  You are setting up an API gateway for your Spring Cloud application using Netflix Zuul. Which annotation should you apply to enable the gateway functionality?
    Incorrect -
    @EnableZuulServer

    Correct -
    **@EnableZuulProxy**

    Incorrect -
    @EnableZuulApiGateway

    Your choice: incorrect -
    @EnableApiGateway

13.  Which class resolves uncaught exceptions using @ExceptionHandler methods? 
    Your choice: incorrect -
    DefaultHandlerExceptionResolver

    Correct -
    **ExceptionHandlerExceptionResolver**

    Incorrect -
    HandlerExceptionResolver

    Incorrect -
    ResponseStatusExceptionResolver

second attempt:
14. You must write unit tests using TestNG without treating your controller classes as plain old Java objects (POJO). Which package and class will be useful for you in this case? 
    Incorrect -
    The org.springframework.test package that contains the UtilTest class

    Your choice: incorrect -
    The org.springframework.test.mockandview.web package that contains the MockTest class

    Correct -
    **The org.springframework.test.web package that contains the ModelAndViewAssert class**

    Incorrect -
    The org.springframework.test.mock.web package that contains the ModelAndTest class

15. The Authentication object has a method getAuthorities() that returns an array of GrantedAuthority objects. What are these authorities objects commonly called?
    Incorrect -
    Authentications

    Incorrect -
    Users

    Your choice: incorrect -
    AuthTokens

    Correct -
    **Permissions**

16. While making an application you add some servlet filters into your code for filtering, encryption, and decryption. The following code snippet is from the web.xml file:
    ```xml
    1. <filter>
    2.  <filter-name>myEdit</filter-name>
    3.  <filter-class>org.springframework.web.filter</filter-class>
    4. </filter>
    ```
While running the final application, the application ignores the filters and executes everything else. How can you fix this? 
    Your choice: correct -
    **Add the org.springframework.web.filter.DelegatingFilterProxy filter class in the third line.**

    Incorrect -
    Replace the second line with <name>myEdit</name>.

    Incorrect -
    Replace <filter-class> with <input> in the third line.

    Incorrect -
    Change the <filter> tag to the <filter-id> tag in the first line.

17. What mechanism can you use when you want to add Basic Authentication to all requests using RestTemplate?
    Incorrect -
    template.addHeaders(HTTPHeaders.AUTHORIZATION, "Basic");
    
    Correct -
    **restTemplateBuilder.basicAuthentication(username, password).build();**

    Incorrect -
    template.setEncoder(new BasicAuthentication(username, password));
    
    Your choice: incorrect -
    restTemplateBuilder.addHeader(HTTPHeaders.AUTHORIZATION, "Basic");

18. What would you add to the following code so it will also configure the location of files that the test uses?
```java
@RunWith(SpringRunner.class)
@SpringBootTest(SpringBootTest.WebEnvironment.MOCK, classes=Application.class)
@AutoConfigureMockMvc
public class StudentIntegrationTest{
 // ...
}
```
    Your choice: correct -
   **@TestPropertySource(location="...")**
    
    Incorrect -
    @Configuration(location="...")
    
    Incorrect -
    @SpringTest(location="...")
    
    Incorrect -
    @IntegrationTest(location="...")

19. Which annotation is required to use Java Persistence API (JPA) repositories when working with Spring Data?
    Correct -
    @**EnableJpaRepositories**

    Incorrect -
    @EnableJavaPersistence

    Incorrect -
    @EnablePersistence

    Your choice: incorrect -
    @EnableSpringDataJpa

20. Your manager shared a file with you that handles the exceptions thrown from one or more ControllerAdvice classes.
```java
    1.  class GlobalControllerExceptionHandler {
    2.  @ControllerAdvice
    3.  @ResponseStatus(HttpStatus.CONFLICT)
    4.  @ExceptionHandler(DataIntegrityViolation.class)
    5.  public void handleException() {
    6.   ....
    7.  }
    8.  }
```
    The above code produces an error on its execution. Why? 
    Correct -
    **Instead of DataIntegrityViolation, it should be DataIntegrityViolationException on line 4.** 

    Incorrect -
    @Controller is missing from the code:

    @ResponseStatus(HttpStatus.CONFLICT)
    @Controller
    @ExceptionHandler(DataIntegrityViolation.class)
    Your choice: incorrect -
    @ExceptionHandler annotation should be used at the class level.

    Incorrect -
    Instead of HttpStatus, it should be HttpStatusCode on line 3. 

21.  Consider the following snippet of a test:
    ```java
    @ContextConfiguration
    public class PersonTests {
        @Test
        public void exampleTest() {
            ...
        }
    }
    ```
In a Spring Boot application, which annotation can you use as an alternative to the @ContextConfiguration annotation?
    Incorrect -
    @RunWith(SpringBootTester.class)

    Incorrect -
    @SpringBootTestApplication

    Correct -
    **@SpringBootTest**

    Your choice: incorrect -
    @RunWith(SpringBootTestRunner.class)

22.  Aspect-oriented programming (AOP) advice runs before, after, or around method executions matched by what?
    Incorrect -
    An aspect

    Your choice: incorrect -
    A joinpoint

    Incorrect -
    An expression

    Correct -
    **A pointcut**
23.  What's the difference between POST and PUT? 
    The POST method uses the UPDATE query, whereas the PUT method uses the CREATE query.

    Incorrect -
    The POST method responses cannot be cached, whereas the PUT method responses can be cached.

    Correct -
    **The POST method allows the server to determine the new resource's Uniform Resource Identifier (URI), whereas the PUT method requires the client to specify it**.

    Your choice: incorrect -
    The POST method is idempotent, whereas the PUT method is not idempotent. 

24.  How can you configure a Spring application?
    As context, factory, or singleton

    Your choice: incorrect -
    As properties, YAML, or Gradle

    Correct -
    **As XML, Java, or annotations**

    Incorrect -
    As Java Database Connectivity (JDBC)
25.  Which annotation of Spring model-view-controller (MVC) allows an application to run heavy-load jobs on a separate thread? 
    @async because the Spring framework supports the asynchronous processing by default

    Correct -
    **@Async because the caller may or may not wait for the completion of the called method for execution**

    Your choice: incorrect -
    @Scheduled because it enables asynchronous processing with some configuration

    Incorrect -
    @async because you can apply it to private methods for fast execution

26.  How can you achieve content negotiation? 
    URL parameter and custom headers

    URL extension, path location, and accept headers 

    Path extension and custom headers

   **Path extension, URL parameter, and accept headers**

27.  When writing unit tests for Spring-based applications, what is the correct way of creating a plain old Java object (POJO)?
    Using dependency injection

    Using the factory pattern

    **Using the new operator**

    Using dependency injection with @Qualifier

28.  What does the @SpringBootTest annotation do in the following code?

    ```java
    @RunWith(SpringRunner.class)
    @SpringBootTest(SpringBootTest.WebEnvironment.MOCK, classes=Application.class)
    @AutoConfigureMockMvc
    @TestPropertySource(location="classpath:application-integrationtest.properties")
    public class ProductIntegrationTest{
    // ...
    }

    ```

    Configures the location of the classes 

    **Bootstraps the entire container**

    Specifies the classes to be loaded

    Configures the runtime environment 

29.  Given the file config.properties, how would you correctly configure it using the @PropertySource annotation in the code below?
    
    ```java

      @Configuration
      public class PropertiesWithJavaConfig {   
      @Bean   
      public static PropertySourcesPlaceholderConfigurer 
            propertySourcesPlaceholderConfigurer() {      
        return new PropertySourcesPlaceholderConfigurer();   
      }
      }

    ```
    @PropertySource("config.properties") 

    @PropertySource("value:config.properties") 

    @PropertySource("path:config.properties") 

    **@PropertySource("classpath:config.properties")**

30.  You use the following code snippet in Spring Security:
    
    ```java
    @Autowired
    public void configAuthentication(AuthenticationManagerBuilder auth) throws Exception {
    auth.jdbcAuthentication()
    .dataSource(dataSource)
    .usersByUsernameQuery("select username,email, enabled from users where username=?")
    .authoritiesByUsernameQuery("select username, office from employee where username=?");
    }
    ```
    How would you set up the authorization query?
    
    By throwing an exception 

    Your choice: incorrect -
    By using auth.jdbcAuthentication

    Incorrect -
    By using @Autowired

    Correct -
    **By using authoritiesByUsernameQuery** 

31. What is the equivalent to MockMvc for Spring WebFlux endpoints?
    
    WebfluxTestTemplate

    Your choice: incorrect -
    MockWebFlux

    Correct -**WebTestClient**

    Incorrect -
    TestWebfluxTemplate

32. In a Spring Cloud application, what is the purpose of the bootstrap context? (dperecated, using Spirng Contfig Data)

    It is responsible for initializing all dependent microservices.

    Incorrect -
    It is responsible for initializing beans with remote dependencies.

    Your choice: incorrect -
    It is responsible for loading service discovery configuration.

    Correct -
    **It is responsible for loading configuration from external sources.**

33. You want to deal with the full application context file for managing your web security beans by adding a single entry to your web.xml. Your aim is to avoid cluttering the web.xml file. How would you do this?
    
    **Use the FilterChainProxy class.**

    Incorrect -
    Use the ChannelProcessingFilter class.

    Your choice: incorrect -
    Use the SecurityFilterChain class.

    Incorrect -
    Use the ConcurrentSessionFilter class.

    **Remeber** Client -> FilterChain -> DelegatingFilterProxy (connects to Spring Bean) -> FilterChainProxy(Bean)  
    -> SecurityFilterChain -> SecurityFilter (Bean, resgitered with FilterChainProxy)

34. How would you start working with the @AspectJ annotation in your code? 
    By annotating the @Configuration annotation 

    Incorrect -
    By annotating the @ComponentScan annotation 

    Correct -
    **By annotating the @EnableAspectJAutoProxy annotation** 

    Your choice: incorrect -
    By annotating the @EnableAspectJProxy annotation 

35. What programming models does Spring WebFlux provide? 
    HTTP requests and response content

    Your choice: incorrect -
    Mono and flux API types

    Incorrect -
    Annotated controllers and functional controllers 

    Correct -
    **Annotated controllers and functional endpoints** 

36. The following code creates a custom health indicator:
    ```java
    @Component
    public class MyHealthIndicator extends AbstractHealthIndicator {

        @Override
        protected void doHealthCheck(Health.Builder builder) throws Exception {
    
            builder.up()
                    .withDetail("app", "Is alive!")
                    .withDetail("error", "Something is wrong!");
        }
    }
    ```
    How would the /health endpoint show its details, provided that the management.endpoint.health.show-details property is set to a value of always?

    InCorrect:
    ```json
    {
      "status":"UP",
      "details":{
          "details":{
            "status":"UP",
            "custom":{
                "app":"Is alive!",
                "error":"Something is wrong!"
            }
          },
        ...
      }
    }
    ```

    Incorrect:
    ```json
    {
      "status":"UP",
      "details":{
          "custom":{
            "status":"UP",
            "up":{
                "app":"Is alive!",
                "error":"Something is wrong!"
            }
          },
        ...
      }
    }

    ```

    InCorrect
    ```json
    {
      "status":"UP",
      "details":{
          "custom":{
            "details":{
                "app":"Is alive!",
                "error":"Something is wrong!"
            }
          },
        ...
      }
    }
    ```

    correct
    ```json
    {
      "status":"UP",
      "details":{
          "custom":{
            "status":"UP",
            "details":{
                "app":"Is alive!",
                "error":"Something is wrong!"
            }
          },
        ...
      }
    }
    ```



# PluralSight Python

1.  You are working on a Windows system and you must use the sys module to add a module from a custom location. The following script fails when you try to import the module. The custom location is: "D:\Projects\". Assume pydot is in the folder. Why is the script failing?
```python
import sys 
sys.path.append("D:\Projects\")
import pydot


Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pydot'

```
he module is not in that folder.

Incorrect -
You can only set the path in the PYTHONPATH environment variable.

Your choice: incorrect -
You must start with import statements and then with the append.

Correct -
**You must specify the path with raw string or escape the backslashes.**

2.  What is the output of print(type(type))?
correct - <class 'type'>

Incorrect -
<class 'str'>
Incorrect -
<class 'meta'>
Incorrect -
<class 'class'>

3. What line of code would you use to shorten the number 109.4832 to 109?

**math.trunc(109.4832)**

Your choice: incorrect -
math.round(109.4832, -2)

Incorrect -
math.floor((109.4832)2)

Incorrect -
math.ceil(109.4832, 2)

4. How would you output the following?
var = 'Let's get going'
print(var)
Incorrect -
print('Let's get going)

Your choice: incorrect -
print('Let\\'s get going')

Correct -
var = 'Let\'s get going'
print(var)

5. You issue the following command, from math import square_root, and you get the ImportError: cannot import name 'square_root' from 'math' (unknown location). What is the problem?
**The math module has no square_root function to be imported**

Incorrect -
It is a corrupted Python installation

Incorrect -
The math module is not installed

Your choice: incorrect -
The math as name for a module is invalid

6. What is the output of the following code?

```python
try:
    if 8 | True:
        print('A', end='')
except:
    print('C')
finally:
    print('H')
```

AC
H
Incorrect -
CH

Correct -
AH

Incorrect -
C
H

7. You create a Context Manager class to perform file handling as follows:
```python
class FileManager(): 
    def __init__(self, filename, mode): 
        self.filename = filename 
        self.mode = mode 
        self.file = None
 
    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file
```
The class consists of operations such as opening a file and writing/reading contents. It misses a method to close the file, however. Which code can you use to close the file and provide necessary information in case of an exception?

**def __exit__(self, exc_type, exc_value, exc_traceback):   
    self.file.close() **
    
Incorrect -
def __exit__(exc_type, exc_value, exc_traceback):   
    file.close() 
Your choice: incorrect -
def __exit__(self):   
    self.file.close() 
Incorrect -
def __exit__(self, exc_type, exc_value, exc_traceback):   
    self.close() 

8. You have two lists stored in variables First and Last. The length of the first list is five whereas the length of the second list is six. How can you add the first five elements from each list?
First = [8, 5, 7, 8, 2]
Last = [77, 41, 22, 65, 7, 5]

# Output
# [85, 46, 29, 73, 9]

correct - [i + j for i, j in zip(First, Last)]
Incorrect -
[i = First[i] + j = Last[j] for i, j in map(First, Last)]
Incorrect -
concat(First[i], Last[j])
Incorrect -
[i + j for lambda(i,j) in concat(First, Last)]

9. Consider the given class:
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
How can you create a CustomList class and add values User1 and User2 to the list?

class CustomList(lst, metaclass=ListMetaclass):
    lst = ['User1', 'User2']
    pass

lst = CustomList()
lst.add('User1')
lst.add('User2')
Your choice: incorrect -
class CustomList(metaclass=ListMetaclass):
    pass

lst = CustomList()
lst.add('User1')
lst.add('User2')
Correct -
class CustomList(list, metaclass=ListMetaclass):
    pass

lst = CustomList()
lst.add('User1')
lst.add('User2')
Incorrect -
class CustomList(lst, metaclass=ListMetaclass):
    pass

lst = CustomList()
lst.add('User1')
lst.add('User2')

10. An object named p from a class named person contains attributes for first name and last name. What code option would change the attribute last_name of the class person to "User1"?

setattr(p[last_name] == 'User1')

Your choice: correct -
setattr(p, 'last_name', 'User1')

Incorrect -
setattr(p.last_name =  'User1')

Incorrect -
setattr('p.last_name', 'User1')

11. Which list method can remove a list's elements using their index?
remove()

Incorrect -
index()

Correct -
pop()

Incorrect -
delete()

12. In Python, when does the else statement of a for loop run? (*it can useful for searching stuff, if found do somethin, not found do others*)
When the for loop encounters an error

Correct -
After the for loop completes all iterations

Incorrect -
Before each iteration of the for loop

Incorrect -
When the for loop breaks

13. Using Python, how can you get the base-10 (Unicode) code point for a single str character?
Use the Python original number function ori on the number within the unicode text.

Your choice: incorrect -
Use the Python specifier function spef on the number within the f-string value.

Correct -
Use the Python ord() function on the the actual object whose value will be formatted.

Incorrect -
Use the Python unicode function uni on the number whose value you would like formatted.

14. What syntax in functions would you use to pass a varied number of non-keyword arguments?
Correct
*args

Incorrect -
pos

Incorrect -
**kwargs

Your choice: incorrect -
**args

15. You must create an Iterator to iterate from values one to five and then stop. How can you do it using a generator expression?
Incorrect
[i for i in range(1,6)]

Correct -
(i for i in range(1,6))

Incorrect -
(i for i in range(5))

Incorrect -
{i for i in range(1,6)}

16.  What is the output of the code print(hash('decode'))?
Incorrect
An integer of type string 

Incorrect -
TypeError 

Incorrect -
decode

Your choice: correct -
An integer  

17. You have a long string with three sentences as follows:
foo = "I visited city park today with my friends. We spent about an hour talking, playing and having a lots of fun. Will you join us next time?"
You must extract the substring "playing" from foo. Applying indexing on such a big string requires counting each character until you reach the word "playing." In addition, the length of the string could increase to 100 sentences in future runs. How can you create a generic solution and extract the substring faster than the usual indexing method?

Correct
Use the partition() method with "playing" as its argument and apply indexing [1].

Incorrect -
Use the index() method and apply indexing foo[theIndex + 1: theIndex + 8].

Incorrect -
Use the index() method and apply indexing foo[theIndex: theIndex + 6]. 

Your choice: incorrect -
Use the split() method and count the index of the word "playing".