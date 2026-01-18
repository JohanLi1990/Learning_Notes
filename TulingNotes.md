- [性能优化-JVM-MYSQL](#性能优化-jvm-mysql)
  - [全面理解JVM](#全面理解jvm)
  - [类加载机制实在（升值加薪之旅）2025-09-17](#类加载机制实在升值加薪之旅2025-09-17)
  - [JVM内存模型深度剖析与优化 (JVM model Deep Analysis) 2025-09-18](#jvm内存模型深度剖析与优化-jvm-model-deep-analysis-2025-09-18)
  - [JVM对象创建与内存分配机制深度剖析 2025-09-19](#jvm对象创建与内存分配机制深度剖析-2025-09-19)
  - [This lesson is very hardcore, there are alot of useful informa-XX:+EliminateLock by default, so nothing ttions. Lesson 3 and lesson 4 are worth revisiting.](#this-lesson-is-very-hardcore-there-are-alot-of-useful-informa-xxeliminatelock-by-default-so-nothing-ttions-lesson-3-and-lesson-4-are-worth-revisiting)
  - [深⼊理解 JVM 执⾏引擎 2025-09-20](#深理解-jvm-执引擎-2025-09-20)
  - [Summary for last 5 days](#summary-for-last-5-days)
  - [垃圾收集器ParNew\&CMS与底层三色标记算法详解 (Tri-color marking) 2025-09-21](#垃圾收集器parnewcms与底层三色标记算法详解-tri-color-marking-2025-09-21)
  - [垃圾收集器G1\&ZGC详解 2025-09-22](#垃圾收集器g1zgc详解-2025-09-22)
  - [JVM调优工具详解及调优实战 (Practicals JVM tools) 2025-09-23](#jvm调优工具详解及调优实战-practicals-jvm-tools-2025-09-23)
  - [JVM调优实战及常量池详解 (Practicals JVM tools) 2025-09-24](#jvm调优实战及常量池详解-practicals-jvm-tools-2025-09-24)
  - [JDK新特性梳理 2025-09-25](#jdk新特性梳理-2025-09-25)
  - [JDK17的GC调优策略 2025-09-26](#jdk17的gc调优策略-2025-09-26)
  - [全面理解Mysql架构 2025-09-28](#全面理解mysql架构-2025-09-28)
  - [深入理解Mysql索引底层数据结构与算法 2025-09-29](#深入理解mysql索引底层数据结构与算法-2025-09-29)
  - [Explain详解与索引优化最佳实践](#explain详解与索引优化最佳实践)
  - [MySql索引优化一](#mysql索引优化一)
  - [Mysql索引优化实战二](#mysql索引优化实战二)
  - [MySQL事务原理及优化](#mysql事务原理及优化)
  - [Mysql锁机制与优化实践以及MVCC底层原理剖析](#mysql锁机制与优化实践以及mvcc底层原理剖析)
  - [Innodb底层原理与Mysql日志机制深入剖析](#innodb底层原理与mysql日志机制深入剖析)
  - [Mysql全局优化与Mysql 8.0\&Mysql9.0新特性详解](#mysql全局优化与mysql-80mysql90新特性详解)
  - [MySQL 8.0 主从复制原理分析与实战](#mysql-80-主从复制原理分析与实战)
  - [Mysql8.0高可用集群架构实战](#mysql80高可用集群架构实战)
- [分布式专题](#分布式专题)
  - [Pre-requisite, setting up of VMWare workstations](#pre-requisite-setting-up-of-vmware-workstations)
  - [Redis](#redis)
    - [Redis核心数据结构实战+服务搭建](#redis核心数据结构实战服务搭建)
    - [深入理解Redis线程模型](#深入理解redis线程模型)
    - [Redis进阶二之Redis数据安全性分析](#redis进阶二之redis数据安全性分析)
    - [大厂生产级Redis高并发分布式锁实战](#大厂生产级redis高并发分布式锁实战)
    - [一线大厂高并发缓存架构](#一线大厂高并发缓存架构)
    - [Redis缓存设计与性能优化](#redis缓存设计与性能优化)
    - [京东热点缓存探测系统JDhotkey架构剖析](#京东热点缓存探测系统jdhotkey架构剖析)
  - [RabbitMQ](#rabbitmq)
    - [Key Components](#key-components)
    - [Practical](#practical)
  - [Kafka](#kafka)
    - [Kafka 上手](#kafka-上手)
    - [Kafka 客户端详解](#kafka-客户端详解)
    - [Kafka 集群工作机制详解](#kafka-集群工作机制详解)
    - [Kafka 日志索引详解](#kafka-日志索引详解)
    - [Kafka 功能扩展](#kafka-功能扩展)
  - [深入理解网络通信和TCPIP协议](#深入理解网络通信和tcpip协议)
  - [BIO实战、NIO编程与直接内存、零拷贝深入辨析](#bio实战nio编程与直接内存零拷贝深入辨析)
  - [深入Linux 内核理解epoll](#深入linux-内核理解epoll)
  - [Netty使用和常用组件辨析](#netty使用和常用组件辨析)
  - [Netty面试难题分析](#netty面试难题分析)
  - [Netty 源码](#netty-源码)
  - [Netty实战 1](#netty实战-1)
  - [Netty + Disruptor实战](#netty--disruptor实战)
    - [Day 1 takeaway: Simple Disruptor (one producer one consumer)](#day-1-takeaway-simple-disruptor-one-producer-one-consumer)
    - [Day 2 takeaway: Mutli consumer \& Backpressure](#day-2-takeaway-mutli-consumer--backpressure)
    - [Day 3 takeaway: Netty refresher, I/O Threading \& Backpressure](#day-3-takeaway-netty-refresher-io-threading--backpressure)
    - [Day 4 takeawy: Netty Disruptor Handoff (core OMS pattern)](#day-4-takeawy-netty-disruptor-handoff-core-oms-pattern)
    - [Day 5 Design considerations](#day-5-design-considerations)
      - [**Design A**](#design-a)
      - [**Design B**](#design-b)
      - [Desgin C Hybrid](#desgin-c-hybrid)
    - [Day 5 Takeaways](#day-5-takeaways)
      - [Session 2](#session-2)
      - [Session 3](#session-3)
    - [Day 6 Benchmark takeaway](#day-6-benchmark-takeaway)
      - [1️⃣ What p50 / p95 / p99 really mean (and why you care)](#1️⃣-what-p50--p95--p99-really-mean-and-why-you-care)
      - [2️⃣ How to calculate percentiles (the only way that matters)](#2️⃣-how-to-calculate-percentiles-the-only-way-that-matters)
      - [3️⃣ Lost updates are not theoretical](#3️⃣-lost-updates-are-not-theoretical)
      - [Secondary (but important) Day 6 lessons](#secondary-but-important-day-6-lessons)
      - [📌 Final Day 6 mental checklist (write this in your notebook)](#-final-day-6-mental-checklist-write-this-in-your-notebook)
    - [Day 7, GC, Allocation, Structural protections](#day-7-gc-allocation-structural-protections)
      - [GC \& Allocation](#gc--allocation)
      - [Latency Measurement](#latency-measurement)
      - [Queueing \& Backpressure](#queueing--backpressure)
      - [Overload Handling](#overload-handling)
      - [Systems Thinking (Big Picture)](#systems-thinking-big-picture)
    - [Day 7 番外篇 📓 HDRHistogram — Practical \& Conceptual Notes (Low-Latency Context)](#day-7-番外篇--hdrhistogram--practical--conceptual-notes-low-latency-context)
      - [1. What HDRHistogram **is** (and is not)](#1-what-hdrhistogram-is-and-is-not)
      - [2. What happens when you record a value](#2-what-happens-when-you-record-a-value)
      - [3. Is the value “lost”?](#3-is-the-value-lost)
      - [4. How percentiles (p95 / p99) are computed](#4-how-percentiles-p95--p99-are-computed)
      - [5. Why HDR uses a linear scan for percentiles](#5-why-hdr-uses-a-linear-scan-for-percentiles)
      - [6. Why HDR is NOT a Fenwick Tree (BIT)](#6-why-hdr-is-not-a-fenwick-tree-bit)
      - [7. Is HDR doing “bucket sort”?](#7-is-hdr-doing-bucket-sort)
      - [8. Accuracy model (very important)](#8-accuracy-model-very-important)
      - [9. Why HDR reduced OS jitter in practice](#9-why-hdr-reduced-os-jitter-in-practice)
      - [10. Interval histograms vs cumulative data](#10-interval-histograms-vs-cumulative-data)
      - [11. One-sentence mental model (keep this)](#11-one-sentence-mental-model-keep-this)
      - [12. Why this matters for low-latency systems](#12-why-this-matters-for-low-latency-systems)
      - [Final takeaway](#final-takeaway)
    - [Disruptor Paddings 番外篇](#disruptor-paddings-番外篇)
- [算法与数据结构番外](#算法与数据结构番外)
  - [(Classic) Red Black Tree](#classic-red-black-tree)
    - [Background](#background)
    - [Core logics](#core-logics)
- [并发编程](#并发编程)
  - [Concurrency and Multithreading 101](#concurrency-and-multithreading-101)
  - [Future \& CompletableFuture 实战](#future--completablefuture-实战)
  - [ThreadLocal详解](#threadlocal详解)
  - [深入理解CAS和Atomic原子类操作详解](#深入理解cas和atomic原子类操作详解)
  - [并发锁机制之深入理解synchronized](#并发锁机制之深入理解synchronized)
  - [JUC并发同步工具类在大厂中应用实战](#juc并发同步工具类在大厂中应用实战)
  - [深入理解AQS之独占锁ReentrantLock源码分析](#深入理解aqs之独占锁reentrantlock源码分析)
  - [Semaphore, CountDownLatch and Cyclic Barrier 源码分析](#semaphore-countdownlatch-and-cyclic-barrier-源码分析)
  - [并发容器（Map、List、Set）实战及其原理分析](#并发容器maplistset实战及其原理分析)
    - [ConcurrentHashmap  DeepDive](#concurrenthashmap--deepdive)
      - [1. What `sizeCtl` means](#1-what-sizectl-means)
      - [2. `initTable`](#2-inittable)
      - [3. `helpTransfer`](#3-helptransfer)
      - [4. `putVal`](#4-putval)
      - [5. `transfer`](#5-transfer)
    - [Takeaway while reading ConcurrentHashMap source code.](#takeaway-while-reading-concurrenthashmap-source-code)
      - [What `@IntrinsicCandidate` really means?](#what-intrinsiccandidate-really-means)
  - [阻塞队列BLOCKINGQUEUE实战及原理分析](#阻塞队列blockingqueue实战及原理分析)
  - [线程池实战及原理分析](#线程池实战及原理分析)
  - [ForkJoinPool实战及原理分析](#forkjoinpool实战及原理分析)
  - [深入理解并发原子性、可见性、有序性与JMM内存模型](#深入理解并发原子性可见性有序性与jmm内存模型)
  - [CPU缓存架构详解](#cpu缓存架构详解)
  - [并发编程面试总结](#并发编程面试总结)
  - [Key Takeawys, AQS Design philosopy (lock free until it is absolutely unavoidable):](#key-takeawys-aqs-design-philosopy-lock-free-until-it-is-absolutely-unavoidable)
- [Spring源码专题](#spring源码专题)
  - [Spring核心原理整体脉络](#spring核心原理整体脉络)
    - [How is a Bean created:](#how-is-a-bean-created)
    - [Constructor Inference](#constructor-inference)
    - [AOP Big picture](#aop-big-picture)
    - [Spring Transactions.](#spring-transactions)
  - [Spring手写核心源码](#spring手写核心源码)
  - [Spring手写循环依赖](#spring手写循环依赖)
  - [Spring IOC-加载bean定义源码详解](#spring-ioc-加载bean定义源码详解)
  - [Spring IOC-bean的生命周期源码详解](#spring-ioc-bean的生命周期源码详解)
  - [Spring AOC 底层源码解析](#spring-aoc-底层源码解析)
  - [Spring 声明式事务底层源码](#spring-声明式事务底层源码)
    - [事务解析](#事务解析)
    - [事务解析创建代理 (Bean initiliazation)](#事务解析创建代理-bean-initiliazation)
    - [事务调用 (core)](#事务调用-core)
    - [Transaction begin](#transaction-begin)
    - [Business logic](#business-logic)
    - [Transction submission](#transction-submission)
    - [事务回滚](#事务回滚)
    - [**Most important breakpoints \& SUMMARY**](#most-important-breakpoints--summary)
  - [Spring事件监听使用和原理源码](#spring事件监听使用和原理源码)
  - [Spring IOC container extension point](#spring-ioc-container-extension-point)
  - [Spring之整合Mybatis底层源码解析](#spring之整合mybatis底层源码解析)
    - [How do we create bean for `@Mapper`?](#how-do-we-create-bean-for-mapper)
    - [FactoryBean](#factorybean)
    - [`MybatisMapperScan` extends `ClassPathBeanDefinitionScanner`](#mybatismapperscan-extends-classpathbeandefinitionscanner)
    - [Question: what happened if you invoke `findOrderService` from one of the interface?](#question-what-happened-if-you-invoke-findorderservice-from-one-of-the-interface)
    - [Final Note on Mybatis](#final-note-on-mybatis)
      - [Mybatis is not a ORM. it is a SQL -\> Object mapper](#mybatis-is-not-a-orm-it-is-a-sql---object-mapper)
      - [What JPA / Hibernate add on top](#what-jpa--hibernate-add-on-top)
      - [Why Mybatis becomes painful with complex domains](#why-mybatis-becomes-painful-with-complex-domains)
      - [Why JPA feels easier for rich domains](#why-jpa-feels-easier-for-rich-domains)
      - [The hidden cost of JPA (important)](#the-hidden-cost-of-jpa-important)
      - [Summary](#summary)
  - [Spring AOT提前优化](#spring-aot提前优化)
    - [Mitagation techniques](#mitagation-techniques)
    - [Spring AOT under the hood](#spring-aot-under-the-hood)
  - [SpringMVC无XML启动流程和请求流程](#springmvc无xml启动流程和请求流程)
  - [SpringMVC子父容器启动流程](#springmvc子父容器启动流程)
  - [MyBatis解析全局配置文件](#mybatis解析全局配置文件)
    - [what is the differenece between JPA and Hibernate?](#what-is-the-differenece-between-jpa-and-hibernate)
    - [What is the role of Spring-ORM?](#what-is-the-role-of-spring-orm)
    - [why Spring-ORM exists?](#why-spring-orm-exists)
    - [How does a MyBatis Mapper work:](#how-does-a-mybatis-mapper-work)
    - [Why do we need MyBatis, what is wrong with just JDBC?](#why-do-we-need-mybatis-what-is-wrong-with-just-jdbc)
    - [MyBatis Parsing Configuration](#mybatis-parsing-configuration)
  - [MyBatis源码—SQL操作执行流程源码深度剖析](#mybatis源码sql操作执行流程源码深度剖析)
  - [Java Reflection, Class Loading \& Spring IOC - Key Insights Summary](#java-reflection-class-loading--spring-ioc---key-insights-summary)
    - [3 Distinct layers you must never mix up](#3-distinct-layers-you-must-never-mix-up)
    - [What the ClassLoader actually does (and does NOT do)](#what-the-classloader-actually-does-and-does-not-do)
    - [How Spring finds `@Component` classes](#how-spring-finds-component-classes)
    - [Where Spring actaully mutates `beanClass`](#where-spring-actaully-mutates-beanclass)
    - [What `Class.forName()` really is](#what-classforname-really-is)
    - [Why `Class.forName` ≠ `new Car()`](#why-classforname--new-car)
    - [Why Spring must avoid eager loading](#why-spring-must-avoid-eager-loading)
    - [`Class<?> clazz` clarified](#class-clazz-clarified)
    - [Correct final mental model](#correct-final-mental-model)
    - [ANOTHER final note on `Class.forName`](#another-final-note-on-classforname)
    - [ANOTHER ANOTHER final note on `Class.getDeclaredConstructors0(boolean var1)`](#another-another-final-note-on-classgetdeclaredconstructors0boolean-var1)
    - [JVM Class Metadata, `Klass`, and Metaspace - Notes](#jvm-class-metadata-klass-and-metaspace---notes)
      - [`Klass` vs `java.lang.Class`](#klass-vs-javalangclass)
      - [Where calss metadata lives](#where-calss-metadata-lives)
      - [Annotation Lifecycle](#annotation-lifecycle)
      - [Metaspace mental model (refined)](#metaspace-mental-model-refined)
      - [Metaspace vs native memory (important distinction)](#metaspace-vs-native-memory-important-distinction)
      - [Reflection and native methods](#reflection-and-native-methods)
      - [Why metadata is not on the heap](#why-metadata-is-not-on-the-heap)
      - [ClassLaoding Summary](#classlaoding-summary)
    - [What does parent delegation model ensure](#what-does-parent-delegation-model-ensure)
- [React](#react)
  - [React Crash Course - Day 1](#react-crash-course---day-1)
  - [React Crash Course - Day 2](#react-crash-course---day-2)
    - [React 18 StrictMode (Dev)](#react-18-strictmode-dev)
    - [useState](#usestate)
    - [useEffect(\[\])](#useeffect)
    - [useEffect cleanup](#useeffect-cleanup)
    - [installHook.js](#installhookjs)
    - [Summary](#summary-1)
  - [React Crash Course - Day 3 RTK Query, Async Data, and Server State](#react-crash-course---day-3-rtk-query-async-data-and-server-state)
    - [1. the Big mental shift](#1-the-big-mental-shift)
    - [2. Server State vs UI State (critical distinction)](#2-server-state-vs-ui-state-critical-distinction)
    - [3. What `useGetTodosQuery()` really is](#3-what-usegettodosquery-really-is)
    - [4. Where the HTTP request actually happens](#4-where-the-http-request-actually-happens)
    - [5. How to navigate to source code in `node_modules`](#5-how-to-navigate-to-source-code-in-node_modules)
    - [6. Cache, Tags, and invalidatesTags](#6-cache-tags-and-invalidatestags)
    - [8. onQueryStarted — the missing piece](#8-onquerystarted--the-missing-piece)
    - [9. Optimistic Update Pattern (core pattern)](#9-optimistic-update-pattern-core-pattern)
    - [Summary](#summary-2)
  - [React, Javascripts Fundamentals](#react-javascripts-fundamentals)


# 性能优化-JVM-MYSQL

## 全面理解JVM

- How is Java program executed. (tools: UltraEdit for byte code, jclasslib for analysis and understanding). Java execution has to abide Java Language Specification
  
- Class loading mechanism (sandbox protection, cache + parent + bootstrap loader)
  - bytecode, exception table, miscellanous
  - ![JVM架构图](image.png)

- Garbage Collection (tools: arthas for diagnostic)
  - Java opts, -, -X, -XX
  - default collector G1, 
  - print and analyze GC logs

- Notable interview question 
  - Where is `this` stored in JVM? 
  - Why tomcat could do hot reload for jsp, but not for jar?
  - Why do we need custom class loader? how is it implement (by overriding loadClass method in ClassLoader)
  - Why cannot child class override static method from main class (invokevirtual vs invokestatic in JLS)

## 类加载机制实在（升值加薪之旅）2025-09-17
- JDK8 classloading summary:
  - Classloading cache (in native methods)
  - Parents delegations: upward delegations, downward loading
  - domain protection (sanbox protection) : `preDefineClass` method in `ClassLoader.java`

- Linking process (the subtle native `resolveClass` method in `ClassLoader.java`)
  - Verfication: is the bytecode aligned with JLS, is there CAFEBABE? is there any children of final class, which is forbidden etc
  - Preparation: setting up memory for static fields of a class, and assign default value.
  - Resolution:
    - Purpose: Replace symbolic references in the constant pool with direct references.
    - Symbolic references are strings like "java/lang/Object" or "doSomething:()V".
    - Resolution turns these into actual pointers (to Class objects, method table entries, field offsets). Done lazily in some JVMs: the JVM spec allows resolution to happen at use time, not strictly during linking. 
- 实战
  - `OADemo2.java`: use URLCalssLoader to load jar from remote web server or file directory
  - `OADemo3.java`: Customized ClassLoader + ByteCode Obfuscation
  - `OADemo5.java`: Hot reloading of Class: create a new Classloader instance everytime you calculate salary. Performance not good, huge GC burden.
  - `OADemo6.java`: Customized ClassLoader still delegates class loading to AppClassLoader, and if there is a SalaryCaler class under the current src directory, src/SalaryCaler.java will be loaded before our custom jar from another directory. We need to break the parent delegation and prioritize loading with the current file from jar. 
  - `OADemo9.java`: Use JDK SPI and Spring Boot SPI to return services implementations for use, dynamically, without reflection.
    - Note that for **Any** Custom ClassLoader, if you call `super.loadClass()`, you will inevitably trigger the default Parents Delegations in JDK, so all services in current directory that matches your class fullname will get loaded.

## JVM内存模型深度剖析与优化 (JVM model Deep Analysis) 2025-09-18
- JVM Model: ![JVM Model](JVM_model.png)

- Runtime Data Areas: PC, Method Area (MetaSpace), Heap, Stack, Native Method Stack
- For each method call there will be Stack Frame:
  - For each frame contains:
    - Local Variables (primitive types, object references)
    - Operand Stack (for intermediate calculations)
    - Frame Data (method return address, etc)
    - Dynamic Linking (reference to the runtime constant pool)
- JVM options:
  - Standard options, `java -h`
  - Non-standard options, `java -X`
  - Advanced options, `java -XX:+PrintFlagsFinal`
- Notable JVM applications in Spring Boot:
  - Tomcat/catalina.sh: 
  ```java
    java ‐Xms2048M ‐Xmx2048M ‐Xmn1024M ‐Xss512K ‐XX:MetaspaceSize=256M ‐XX:MaxMetaspaceSize=256M ‐jar microservice‐eureka‐server.jar
  ```
  we fix the size of `MetaspaceSize` and `MaxMetaspaceSize` to avoid dynamic expansion of metaspace, to avoid full GC pauses.

- Notable Intervew Questions: Why do we need to do STW? why can't we do GC while application is running?
  - Answer: we cannot becuase during GC, objects may be moved, if the object marked for moving is no longer needed (because app is running at the same time), we are wasting resource moving them to old generation. Also, if we are moving objects while app is running, the app may be accessing the object at the same time, leading to data inconsistency.
- Tools: jstat, jmap, jstack, jinfo, jcmd, VisualVM, VisualGC, Mission Control, et

## JVM对象创建与内存分配机制深度剖析 2025-09-19

- This lesson deepdives into JVM, and even analyzes how certain process are called in C++ code in HotSpot JVM.
- Metaspace (JDK8+), PermGen (JDK7 and below)
  - Class metadata, static variables, constants
  - Metaspace is allocated in native memory, not in heap memory
  - Default size is 21MB, can be adjusted with `-XX:MetaspaceSize` and `-XX:MaxMetaspaceSize`, it is best practice to set both to the same value to avoid dynamic expansion
  - When metaspace is full, it will trigger a full GC to reclaim space
  - Common issues: `java.lang.OutOfMemoryError: Metaspace`, can be solved by increasing metaspace size or reducing class loading/unloading
- During production, based your business load, you can actually calculate the required JVM memory size, and set the JVM options accordingly.
  - For example, if you have 300 orders/sec, that could amount to 300kb/sec in object creations, 
  - There are other things that comes with the order (coupons, stocks etc) so lets amplify by 20 , 200 * 300kb/sec,
  - if there are other order queries, we might amplify by another 10 times, 10 * 200 * 300kb/sec = 60 MB/sec
  - However those orders are short lived orders, if we do this `-Xmn2048m` so we increase the young gen to 2G, we can reduce full gc
- JVM object creations:
  - class loading
  - memory allocation
  - initialization
  - set object header
  - run init method
- Notable concepts: 
  - Pointer Compression (default in 64bit JVM, actually just left shift by 3 bits so we can reduce memory footprint), TLAB (Thread Local Allocation Buffer),
  - JVM Stack allocation, escape analysis: stack allocation, scalar replacement, lock elision (there is another hardware level lock elision which is chip dependent)
This lesson is very hardcore, there are alot of useful informa-XX:+EliminateLock by default, so nothing ttions. Lesson 3 and lesson 4 are worth revisiting. 
---
## 深⼊理解 JVM 执⾏引擎 2025-09-20
 - Just In time Compiler, Interpreter + c1 compiler + c2 compiler.
 - Hotspot code detection (Invocation counter and Back Edge Counter)
 - Compiler Optimization techniques: 
   - inline, 
   - vectorization, 
   - **Escape Analysis** -> **Scalar Replacement(-XX:+EliminateAllocation)** + **Stack Allocation**, 
   - lock elision (there is another hardware level lock elision which is chip dependent)
   - loop unrolling: fewer branch instructions, easier to spot vectorization opps (SIMD)-XX:+EliminateLock by default, so nothing t

## Summary for last 5 days
1. **Compilation (outside JVM)**
   - `javac SomeClass.java` → produces `SomeClass.class` (bytecode).

2. **JVM Startup**
   - JVM process starts.
   - Initializes core classloaders:
     - **BootstrapClassLoader**
     - **PlatformClassLoader**
     - **AppClassLoader**
   - Chooses a **GC algorithm** (e.g., G1, ZGC, Shenandoah) and spawns dedicated **GC worker threads**.

3. **Class Loading & Linking**
   - `SomeClass.class` is located and loaded by AppClassLoader.
   - Linking steps:
     - **Verification**
     - **Preparation**
     - **Resolution**
   - Initialization: run `<clinit>` (static blocks, static fields).

4. **Class Metadata Storage**
   - Class structure, constant pool, vtables, etc. stored in **Metaspace**.
   - At this point: still no objects, only metadata.

5. **Program Execution Begins**
   - `main()` is invoked.
   - Bytecode is executed by the **interpreter**.
   - On `new SomeClass()`:
     - JVM allocates memory in heap (usually Eden region).
     - Sets **object header** (mark word, klass pointer).
     - Initializes instance fields.

6. **Profiling & Hotspot Detection**
   - JVM collects runtime profiles (method invocation counts, branch frequencies, type profiles).
   - Identifies “hot” methods (frequently executed code paths).

7. **JIT Compilation**
   - Hot methods compiled into native code:
     - **C1 (client compiler):** quick, lightweight optimizations.
     - **C2 (server compiler):** deeper optimizations (inlining, escape analysis, lock elision (there is another hardware level lock elision which is chip dependent), vectorization, etc.).
   - Compiled code replaces interpreted execution.-XX:+EliminateLock by default, so nothing t

8. **Native Execution**
   - CPU executes optimized machine code directly.
   - If speculative optimizations prove wrong (e.g., unexpected type at a call site):
     - The method is **deoptimized**.
     - Falls back to interpreter.
     - May be recompiled later.

9. **Garbage Collection (Always Running in Background)**
   - GC worker threads continuously monitor allocation and heap pressure.
   - When thresholds are exceeded (e.g., Eden fills, old gen grows, metaspace expands):
     - **Stop-The-World (STW)** pauses: all app threads frozen briefly.
     - **Concurrent phases**: GC threads run alongside app threads.
   - Dead objects reclaimed, heap compacted (depending on GC algorithm).

10. **Repeat Cycle Until Shutdown**
    - Execution ↔ Profiling ↔ JIT ↔ GC cycles continue for the life of the JVM process.
    - On shutdown, JVM may run a final GC and then tear down threads and memory.
  
## 垃圾收集器ParNew&CMS与底层三色标记算法详解 (Tri-color marking) 2025-09-21
- Various collection algorithms, Garbage collectors usually employ one or more algorithms in its implementations
- Algorithms:
    - Copying collection: usually in young generation
      - From space and to Space (Survior 1 and Survivor 2)
    - Mark and Sweep
    - Mark-Sweep-Compact
    - Generatonal Collection (a trategy not a new algorithm): Copying for young gen (fast) + Mark-Sweep-Compact for old gen (handles large objects avoid fragmentations)
- Concurrent Mark Sweep Collector
  - initial Mark: STW
  - Concurrent Mark: 
  - Conccurrent Preclean
  - Remark: STW
  - Concurrent Seep
  - Concurrent Reset:
- If there are sudden heavy load on the app, CMS can degrade to PrallelOld, which is fully STW.
- Tricolor marking: 
  - Black (Node visited and all children visited  will be grey)
  - Grey (process about to visite the node but hasn't reached yet)
  - white (not visited node)
  - **Strong invariant: No black -> white edges exist**
  - **Weak invariant: Black -> white edges may exist but every such edge is recorded so the collector will re(scan) it**
  - However if not careful, there could be some white nodes being refered back to black node during concurrent Marking phase. Then if there are no procedures to protect thos white nodes, they will be garbage collected and then our applicaiton will throw Exceptions.
  - Two ways to resolve the previous problem:
    - Incremental - Update (aka insertion barrier)
      - On pointer write, if we store a refere x-> y we either Grey the target y immediately or Record the modfied slot/card so the source will be rescanned:
        ```c
        on_write(field, newRef):
        if marking_in_progress:
          if object(holder(field)) is BLACK:
            record_modified_card(holder(field))   // or shade(newRef)
        
        ```
      - Effect: prevents a black object from “silently” pointing to white—either the target becomes gray, or the card with the black source is rescanned later.
    - SATB - Snapshot-At-The-Beginning.
      - Freeze the heap graph at `initial marking`, On overwrite, log the **old** reference so anything that was reachable at the snapshot remains marked.
        ```c
        on_write(field, newRef):
        if marking_in_progress:
          oldRef = *field
          if oldRef != null:
            enqueue_SATB_buffer(oldRef)  // old ref will be marked
        *field = newRef
        ```
      - Effect: ensures objects that were reachable at the beginning can’t be lost even if the mutator drops the last reference during marking.
  - Which JVM collectors use what?
    - CMS: Incremental-update write barrier + card table; remark rescans dirty cards.
    - G1: SATB barrier; logs old refs in per-thread buffers; remark drains these.
    - Shenandoah: SATB + load barriers for concurrent evacuation.
    - ZGC: heavy use of load barriers with colored pointers; maintains reachability and remapping without long pauses (conceptually enforces the invariant on loads rather than stores).

## 垃圾收集器G1&ZGC详解 2025-09-22
- G1 GC: **initial Mark** -> **Concurrent Mark** -> **Remark** -> **Cleanup**
  - Regions based, still generational, but a lot of regions
  - Humongous regions to take care of big objects, not moving them anymore. 
  - User could customize pause goal, which is very helpful for managing GC time
  - YounGC: it is **not triggered** immediately when Eden is full, it will calculate how long it takes to collect Eden, if it is very fast, then increase the Eden regions
  - MixedGC: `-XX:InitiatingHeapOccupancyPercent` Collect all Young and part old and humongous, how many to collect depends on the `MaxGCPauseMilis` value.
  - FullGC: like SerialGC, very time consuming.
- Notable Interview Question on G1 applications
  - A kafka system, 10 thousands order per sec is normal
  - We need to increase young gen size to accomodate all short-lived, large objects, so that they do not trigger GC that often.
  - However if we have alot of short lived large objects, and we use ParNew, It will be quite lenthy STW, because Young Gen size if large now!
  - If we apply G1 to manage young gen, we can have a consistent pause goal, User will not feel a thing. App could collect garbage while handling business.
- ZGC: **TB heaps**, **10ms GC pause time**, 
  - Colored pointer: instead of storing GC information in object headers, now ZGC stores it in refernce pointer. 
  - Then it uses load barrier to update the reference pointer lazily (via ForwardTable)

## JVM调优工具详解及调优实战 (Practicals JVM tools) 2025-09-23
- **jstat**: `jstack -gc <pid> <frequency> <times>`
  - e.g. `jstack -gc 1604 2000 1000` track pid 1604, print gc info every 2 seconds, 1000 times
- **jinfo**: check the jvm opts flags for current application
  - e.g. `jinfo -flags 1604`
- Based on jstat info there are alot of informations to investigate:
  - why are YGC so frequent? what causes Eden to grow so fast?
  - Calculate how much objects are moved to Old gen.
  - Why are FGC so often, how much time are spent.
- **Optimizing Goal**: At the end of day, we **want low to no FullGC**, and henceforth **we want, after each YGC, the size of surviving objects to be less than 50% of S0/S1 regions**, so that no objects have to be moved to old gen

## JVM调优实战及常量池详解 (Practicals JVM tools) 2025-09-24
- Arthas techniques:
  - `arthas: dashboard`
  - `arthas: heapdump`
  - `thread <thread-id>` , use `thread` to see thread info.
  - use `jad` to de-compile.
  - highly dangerous: use `ongl` to modify only java objects.
- Arthas used `Java Agent`, `Instrumentations Api`, under the hood.
- Constant pool
  - Literals and Symbolic references
    - `int a = 1`, `1` is literal, `a` is symbolic reference.
  - when Constant pool is loaded into jvm, the symbols will be dynamic linked to the reference (actual object) in memory.
  - String constant pool
    - be careful of `new String("<your string literal>")`, it will create two objects.
    - like a hastable, it is located in heap.
  - Integer, Long, Character, Byte, Boolean all have `Cache`, which is equivalent of constant pool.

## JDK新特性梳理 2025-09-25
- What are some of the new features in JDK 17+?
  - Syntax Sugars: String block, Switch expression, 
  - Record class (good for DTO), record class does not support invocation by reflection, even safer,
  - Hidden Class, get class from bytes. better obfuscations
    - use ASM library to manipulate byte directly: [baeldung article](https://www.baeldung.com/java-asm)
  - Sealed Classes: choose which children is allowed
  - **Virtual Thread**: Kindof like co-routine
  - modules
  - vector api
  - G1GC is used everywhere
  - GraalVM, + Truffle Lnaguage Implementation Framework, you can imlement your own programming language.

## JDK17的GC调优策略 2025-09-26
- Look at famous open source application, (e.g. RocketMQ) to see how it is optimized.
- JDK JVM:
  - On Heap: OBjects
  - off heap: Thread Stack, Metaspace, CodeCache, ClassSpace, direct buffer + mapped buffer
- Important optimzation parameter IHOP, MaxGCPauseTime.

## 全面理解Mysql架构 2025-09-28
- Two layers: Server Layer and Storage Engine
- Server layer: Mysql-connector, Query cache, query parser, query optimizer, query executor
- Storage layer: different types of storage engine, default is innoDB.
  ![MySQL architecture](mysql_architecture.png)
- Redo log:
  - it recored the physical change to the DB server.
  - WAL technology, 
  - All updates will be written to redolog first, and then executed on disk when innoDB engine is not busy
  - Crash safe, If I some how my disk got destroyed, I can still replay my redo log to recreate my DB.
- Bin log:
  - Implemented by Mysql server (not part of storage engine)
  - it recorded the **original sql logics**
- MySQL, Two phase commits
  - Prepare phase
    - InnnoDB writes transaction changes into its redo log buffer, and marks it as prepared
    - InnoDB gurantees it can be later either commited or rollback.
    - nothing is yet written to binlog
  - Commit phase
    - Server writes the transactions binlog entry(SQL/row events) and flushes it to disk (sync_binblog=1 ensure durability)
    - Then innoDB writes the commit record into the redo log (`innodb_flush_log_at_trx_commit=1` ensure durability)
    - Only after both are persisted, the transaction is considered commited
    ```
    This way:
    - If MySQL crashes after prepare but before binlog flush, InnoDB recovery will roll back the prepared transaction.
    - If crash happens after binlog flush but before redo log commit, recovery sees a “prepared but not committed” transaction in InnoDB → it can replay commit using the binlog (binlog is authoritative).
    ```
## 深入理解Mysql索引底层数据结构与算法 2025-09-29
- How is MySQL storage engine implemented? (MYISAM, InnoDB)
  - **Binary Search Tree**: logN time, but may degrade to O(N) due to how it is built (becomes linked list for steady increasing sequence)
  - **Red Black Tree**: Red black tree solves the previous problem because it is always self-balancing, but there are no ways for us to know the height: `h` of the tree. The height `h` determines how fast we can find our data.
  - **B-Tree**: B Tree solves the previous problem by putting, not one, but multiple index + data into each tree-node. Each index is sorted in ascending order, and we can control the height of the tree very easily. At the the non-leaf node, we use Binary Search algorithm to quickly identify the index/range of index, and then retrieve data.
  - **B+ Tree**: (innodb implementation)
    - For B tree it is not very good for range query/
    - so B+ tree, we put extra index (redundant index) and place all data into leaf-node. All leaf node are connected using double pointers, so we can quickly retrieve data for range query. 
    - **Clustered index**, index are together with data in leafnode
- Composite index
  - **THE ORDER** of column in the index matters!! Because when we query, we query from the left!!
- **Notable Interview Questions**
  - "Why is it recommended for MySQL tables to have a *Int* type primary key that is also *mono increasing* ?
    ```
     An integer type is easier to compare than varchar.
     Auto increasing because it is more efficient to add data to B+ tree that way. If the index is not mono-increasing, B+ tree will have to do self-balancing, and that affects performance. 
    ```
  - "Why does our secondary index refer to primary index in its leaf nodes, instead of the actual data?"
    ```
     This is for cost concerns. It is costly to have multiple copies of the same data in SSD.
     Also if we were to have more copies of the same table, it is really hard to coordinate updates. This is the consistency concern. 
    ```
## Explain详解与索引优化最佳实践
- Important Points:
  - Type Column: system > const > eq_ref > ref > range > index > ALL, you need to try optimizing your query to `ref`
  - possible_keys vs keys column. 
  - we can use key_len to calculate what are the columns used in the index search.
  - In Extra column, if `Using Tempororary` is seen, we need to optimize it.
- Best Practices:
  - Full value matching, for **every column in the composite index**
  - **LeftMost Prefix Rule**
  - **Do not** apply functions on columns:
    ```sql
      EXPLAIN SELECT * FROM employees WHERE name = 'LiLei';
      EXPLAIN SELECT * FROM employees WHERE left(name,3) = 'LiLei';
    ```
  - Storage engine cannot use any conditions on the right of a range query
    ```sql
    EXPLAIN SELECT * FROM employees WHERE name= 'LiLei' AND age = 22 AND position ='manager';
    <!-- Cnanot use positions -->
    EXPLAIN SELECT * FROM employees WHERE name= 'LiLei' AND age > 22 AND position ='manager'; 
    ```
  - BE specific, use Covering index
  - Using `!`, or  `<>` or `not in`, `not exists` might lead to scanning `All` table. 
  - `is null` or `is not null` **might** lead to `ALL` scanning.
  - `%ABC` in `LIKE` will lead to `ALL` scanning, you should use `ABC%`


## MySql索引优化一
- Use Covering Index
  - If you specify columns in your `SELECT` statements, and the columns selected are all in your composite index, then MySQL will definitely use the composite index, and that will improve performance. If you just put `*` in `SELECT`, mysql will have to do `double lookup` which hurts performance. 
- `IN` and `OR` will only lead to index search when amount of rows are huge, if the amount of data is not alot, it might go for `ALL` type scanning.

- `LIKE` is not like `>` range operator.
  - `LIKE` will always use index, **Index Condition Pushdown** (> Mysql 5.6)
  - do prefilter in secondary index first, before checking primary clustered index for the actual data. 

- **Trace** tools for investigation
  - You have to investigate Trace if you don't know why your index is not applied to your `SELECT` query.
- `Order by` and `Group by` optimization
  - Check the `Extra` column, did we use `fileSort` (no index when ordering) or `Using index condition`
  - alway aim for `Using index` 
  - `Using index` will happen, if `order by` condition satisfy the `left prefix principle`
  
- Two Algorithms to `filesort`: Single-Read Sort vs Two-Read Sort
  - `<sort_key, additional_fields>` 
    `<sort_key, packed_additional_fields>` Single Read
  - `<sort_key, rowid>` Two-Read Sort
  - Basically the choice of which is a result of how much buffer you have set in MySQL, if buffer is large you can do Single-Read Sort.
- **Optimization techniques**
  - Code first, index later
  - Based on your sql query, build **Composite Index**
  - Do not build single index on Column that has small distinct values. 
  - Use **prefix** (e.g. `name(20)`) to build composite index, to reduce disk size usage. But this way you cannot use `order by` on the index.
  - Prioritize `where` over `order`
    - because this way we can quickly filter out rows, and that can reduce time for ordering

## Mysql索引优化实战二
- Paginated Query Optimization
  - `select * from employees limit 10000, 10;` very inefficietn. it reads 10010 rows.
  - `select * from employees where id > 90000 limit 5` is much more efficient because it uses index.
  - when `order by` is involved:
    - `select * from employees ORDER BY name limit 90000,5;` this query will not use index, becasue there are too many rows, no point using index.
    - but if you do this: `select * from employees e inner join (select id from employees order by name limit 90000,5) ed on e.id = ed.id;`
    you can force the order by and pagination to happen first, and then retrive the row with id. This way, less columns are returned when doing order by. so faster. 
- Join Opitmization
  - Nested Loop Join vs Blocked Nested Loop Join
    - make sure small table drives big table.
    - **index** the columns used after `on`

## MySQL事务原理及优化
- Transaction nomrally has the four principles: ACID
  - Read Uncommited: dirty read
  - Read Commited: Non-repeatable read, phantom Read
  - Repeatable Read: Phantom Read
  - Serailizable
- Locks and MVCC enables us to maintain ACID compliance while under heavy load.
  - Optimistic (CAS) vs Pessimistic
  - Shared lock vs X lock.
  - Intention lock.

## Mysql锁机制与优化实践以及MVCC底层原理剖析
- Read lock (Shared lock) multiple query can view the same row at the same time no problem.
- Write lock( exclusive lock) if update is not done, will block other locks:
  - `select * from T where id=1 lock in share mode`
- Intention lock: like a dog marking its terriroty. If a transaction is adding a shared / exclusive lock on the row, the transaction will also marke the table with `intention lock`. If anther transaction tries to add a table lock, it will not have to check every row. 
`IS` and `IX`
- Gap lock and Next-Kye locks, -- how mySql solves the phantom read problems
- MVCC principles
  - undo log will be created when multiple transactions modify the smae row of data. 
  - Under RR, a readview will be generated the first time `Select` is run. and **it will not change until txn is finished**
  - ReadView consist of `array of on-going transaction-ids` and `maxTransActionId`
  - During a `Select`:
    - If row `txnid` < minTrxId in array, data is visible.
    - if row `txnid` > `max_id` txn does not exist
    - if row `txnid` within `min_id` <= `max_id`
      - if `txnId` in the array: on going, not visible
      - else `txn` already committed, visible
- Summary:
  - Read View = defines what a transaction is allowed to see.
  - Undo version chain = stores the row’s history of changes.
  - Together, they let each transaction read the right version of a row, ensuring consistency under concurrency

## Innodb底层原理与Mysql日志机制深入剖析
- What happened under the hood (step 1 to 8)
  ![MySQL under the hood](./MySQL_InnoDB_lowerLevel.jpg)
- Redo Log: (can be number of redo log files)
  - write pos: write positions
  - check point: the place before which you can write your data freely, if at check-point, then cannot write, must dump redolog to disk first before writing (move the check point)
  -  **The write to disk strategy**
     -  `innodb_flush_log_at_trx_commit` this condition controls when should we flush redo log onto disks.
        -  if 0, never, relies on innoDB daemon thread to dump logs to disk (every 1s). Risking losing data.
        -  if 1, always write to disk every time, low performance, but safe
        -  if 2, only writes to page-cache. then relies on the aforementioned innoDB daemon thread to dump data to disk. if DB is down, data will not be lost, because whatever is in Page-Cache will be eventually synced to disk by `fsync`. But if OS is down, then we lose the data.
- BinLog
  - consists of multiple `mysql-binlog.xxxx` files, They are base64 encrypted data of past `update`, `insert`, `delete` statements on the database
  - BinLog format: Statement (risk: master slave mismatch due to functions like `UUID()`, `SYSDATE()`), ROW (Copies every row, no master slave mismatch, but low performances), MIXED(dynamically choose which format to write binlog in)
  - You can recover the DB using BinLog.  
    ```bash
      mysqlbinlog  --no-defaults --start-position=219 --stop-position=701 --database=test D:/dev/mysql-5.7.25-winx64/data/mysql-binlog.000009 | mysql -uroot -p123456 -v test
      <!-- Use command line -->
      mysqlbinlog  --no-defaults --start-datetime="2023-1-27 23:32:24" --stop-datetime="2023-1-27 23:34:23" --database=test D:/dev/mysql-5.7.25-winx64/data/mysql-binlog.000009 | mysql -uroot -p123456 -v test
    ```
    The premise of using binLog to recover DB is that you do periodic DB dump yourself.
    ```bash
      mysqldump -u root 数据库名>备份文件名;   #备份整个数据库
      mysqldump -u root 数据库名 表名字>备份文件名;  #备份整个表

      mysql -u root test < 备份文件名 #恢复整个数据库，test为数据库名称，需要自己先建一个数据库test

    ```

## Mysql全局优化与Mysql 8.0&Mysql9.0新特性详解
- New Descending order index in innodb engine
  ```sql
   explain select * from t1 order by c1,c2 desc;
   <!-- The above sql query will use index instead of filesort -->
  ```
- No more `order by` default:
  ```sql
  select count(*),c2 from t1 group by c2;   --8.0版本group by不再默认排序
  ```
- Invisible index:
  Trying to delete an index, but not sure what is the impact? set it to `invisible first`, if no other queries are impacted, we can delete it safely, else, we simply reverse the action and make it visible again.
- Function Index:
  - in MySQL 5 if we reference function in our Select statments, the query will not use index
  - Therefore in MySQL 8, we start to have function index:
  ```sql
  create index func_idx on t3((UPPER(c2)));  --创建一个大写的函数索引
  ```
- innodb storage engine skip the lock:
  ```sql
  select * from t1 where c1 = 2 for update nowait;
  select * from t1 for update skip locked;  --查询立即返回，过滤掉了第二行记录
  ```
- Extended thinking: why for many internet companies, they do not use `Foreign Key`, whereas in Banks, we use `FK` everywhere?
  ```
    In Oracle-based enterprise systems like UBS → FKs are essential for consistency and auditability.
    In MySQL-based internet systems (esp. China) → FKs are avoided for scalability, sharding, and agility.
    The difference is not “right vs wrong”, it’s a trade-off between data integrity and distributed scalability.
  ```

## MySQL 8.0 主从复制原理分析与实战
- What is Replication: Copying data from SOURCE(Master) to REPLICA(Slave)
  - Replication Algorithm relies on State machines (Snapshot + Binlog)
- Different Replication Technique:
  - Async
  - Semisynchronous Replication (feels like Kafka and Redis), SOURCE relies on ACK to decide when to finish a transactions
- Different approach to replication:
  - Using binlog, 
    - very hard to synchronize SOURCE and REPLICA if there is a problem
    - have to manually find the position, and skip errors. If the errors skipped are not trivial, we will have data mismatch.
  - Using GTID (eaiser, based on Global Transaciton ID)
    - SOURCE calculates difference in GTID between itself and REPLICA
    - then write the differences to relay log in REPLICA
  - **MySQL GROUP Replication (MGR)** (best approach)
    - based on PAXOS protocol. GROUP write (atomic and consistent), instead of SOURCE async write to REPLICA. 
    - it lacks the router to tell client which node is accessible, that is why we need *innoDB cluster*
    - Single Primary vs Multi Primray
  - Extended Thinking: *why do we need XCOM plugins for MGR? why cannot just append to binLog, and use binlog to ensure Global orders?*

    | Question                                  | Answer                                                                                              |
    |-------------------------------------------|------------------------------------------------------------------------------------------------------|
    | Why not just append to binlog?            | Because binlog has only *local ordering*, not *global* ordering.                                    |
    | Why do we need XCom?                      | To reach quorum agreement on the *next transaction order*, ensuring atomic, consistent replication. |
    | What does XCom provide that binlog can’t? | Leader election, total order broadcast, quorum-based commit, and automatic view changes.            |
    | Is XCom storing the data?                 | No — it’s deciding the *order* in which data is written locally.                                    |
  
    for Single Writer many reader, binlog is okay. But for multiprimary we are screwed because there is no global order.

## Mysql8.0高可用集群架构实战
- Inno DB cluster architecture:
  ![innodb cluster](innodb.png)

  - Use MySQL shell to for admin work
  - Use MySQL router for client app connection.
  - If primary node is down, cluster will automatically elect a new primary
- InnoDB replicaSet: not very useful, no automatic failover, manual failover

# 分布式专题

## Pre-requisite, setting up of VMWare workstations

- VMwareWorkstations pro free for personal use
- Download Ubuntu LTS 24.04
  - allow both `Install OpenSSH server` and `allow password authentication over SSH`
- Configure three network adapters
  - NAT: for internet access
  - Host-Only: talk to other VM directly on private network, i.e. my old laptop
    - Disable DHCP
  - Bridged: for direct access via other laptops within the same network. 
  
  node 0
  
  ```yml
  network:
    version: 2
    ethernets:
      ens33:
        dhcp4: true
        dhcp4-overrides:
          route-metric: 200
      ens37:
        dhcp4: false
        addresses: [192.168.88.10/24]
        nameservers:
          addresses: [1.1.1.1, 8.8.8.8]
      ens38:
        dhcp4: false
        addresses: [192.168.10.31/24]
        routes:
          - to: 0.0.0.0/0
            via: 192.168.10.1
        nameservers:
          addresses: [192.168.10.1, 8.8.8.8]
        dhcp-identifier: mac
        dhcp4-overrides:
          route-metric: 100
  ```
  
  - After updating yml file, do `sudo netplan apply`
  - SSH status should be up
    - check  `sudo systemctl status ssh`
    - if not `sudo systemctl enable --now ssh`
  - ![host-only-config](./Host-Only.PNG)
- After configuring everything, create linked clones

## Redis
### Redis核心数据结构实战+服务搭建
- How to set up redis cluster
  - redis master slave replication (kinda like mysql 1 master 2 slave)
  - sentinels (usually multiples and odd number) usually used together with one master + multiple slave topologies
  - clusters: multiple master + sharding, automatic failover without needing sentinel
  ```
    Redis replication is asynchronous, so:
    When the master (redis-1) fails,
    The replica (redis-4) might be slightly behind,
    Any write that was acknowledged by redis-1 but not yet replicated to redis-4 is lost.
    ➡️ Redis Cluster does not guarantee zero data loss during failover.
  ```
- Core Redis Datastructure:
  - String, `help @string`, `SETNX` (good for distributed lock)
  - Hash, `help @hash`
  - LIST, it is a deque, `BRPOP` can be usedas blocking queue. 
  - SET, just normal set (lucky draw, *like button*, *unlike button*)
    - `SADD like:[msg-id] [user-id]`
    - `SREM like:[msg-id] [user-id]`
    - users who likes: `SMEMBERS like:[msg-id]`
    - number of users who likes: `SCARD like:[msg-id]`
  - ZSET: ScoreBoard / Hot Search/ Trending Topic
    - `ZINCRBY hotNews:20190819 1 Capture-Capitol`
    - `ZREVRANGE hotNews:20190819 0 9 WITHSCORES`
    - `ZUNINOSTORE hotNews:20190813-20190819 7`
  - BITMAP: Bloom Filter + 签到
    - Daily punch in : `SETBIT dailycheck:1 100 1` user-1 checked-in on day 100
    - Count the numebr of dailychecks `BITCOUNT dailycheck:1`
    - Advantage: fast, performant, memory efficient
  - HyperLogLog (HLL): a probablistic datastructure for estimating cardinals of a set
    - extremly performant, use constant space (12kb) for upto 2^64 items. with an error rate of 0.81%
    - [hyperlog introduction](https://antirez.com/news/75)
  - GEO: Location servies, check the distance from real longitude and lattitude locations
  - STREAM: Redis MQ, not widely used, offers blocking queue + pub/sub
  - SpringBoot + rdis:
    - Becareful of your serializers, your serializer may transform your key and value into something else.
    - Define your own serializer in `RedisTemplate` if necessary.

### 深入理解Redis线程模型
- Intro
  - Redis at 2024: not just a cache but a DB ecosystem.
  - Mostly single threaded but there are other threaded operations such as UNLINK, slow IO accesses... refer to redis.conf (~/redis/redis.conf)
  - Highly performant becuase it is using epoll for io-multiplexing, so that one thread can respond to many socket connection request. 
- Redis Transaction
  - Not fully Atomic perse, MULTI is more like  group transactions, not atomic transactions like mysql. 
  - if one op fails, the others **still gets executed!!** DANGEROUS.
  - so how do we ensure atomicity? using watch
    - `Watch key2`
    - `MULTI` start transactions
    - Any other clients modified `key2`
    - When doing `EXEC` current transaction will fail.  Try again. 
  - If server fails during a redis transaction, then AOF will have mismatch with data, thne next time redis server starts, there will be errors. You will need reds-check-aof to repair AOF. 
- Pipeline
  - e.g. `cat command.txt | redis-cli -a <your password>`
  - save RTT (round trip time)
  - the same as `printf "AUTH <yourpassword>\r\nPING\r\nPING\\r\n" | nc localhost 6379` where `nc localhost 6379` basically is what redis-cli do. 
  - Do batch processing of data during non-peak hours. 
- LUA scripts (used a lot for distributed lock)
- Redis function: a convenient way to call Lua Script.

### Redis进阶二之Redis数据安全性分析
- Redis Benchmark: `redis-benchmark`
- Redis persistence in depth:
  - [link](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
  - RDB + AOF
    - AOF is event based, RDB is snapshot
    - AOF log, if corrupted, server will not start.
- Redis Master + Replica practicals
  - [official docs](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
  - *use replicaof to make a redis instance a copy of another redis server*
  - Master receives writes, replicate exact copy
  - Downside: replication will take time, hit performance
    - Also if master is down, manual selection of master. This why we have Sentinel cluster
- Sentinel Cluster
  - [official docs](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
  - monitor + quorum: if I found out one master is down, `S_DOWN = 1`, however if `>=quorum` amount of sentinels believe master is down, then `O_DOWN = 1`, then we do failover. (Raft Algorithm, similar to the PAXOS used in MYSQL Group Replication Set)
  - Downside, when master ip changes, client need to change their write destination too.
  - Data not safe, Data may get clost
- Redis Cluster
  - ![Cluster](image-1.png)
  - Gossip protocol
  - Solves 3 problems:
    - clients have to change their write ip if master changes
    - when server side has a lot of data, single replication set cannot handle.
    - when master is down, **automatic failover** for HA.
    - Redis has 16384 slot, every key will be `HashSlot = CRC16(key) mod 16384` and distributed to a hashslot
    - Depending on how many masters you have, this 16k slots will be distributed evenly across the shards (number of masters).
    - if one shard is down, *the cluster* through gossip will have to first come to consensus that it is down, and then promotes slave to master. Since slave already have all the data no need to mirgrate any buckets, 
    - if Redis cluster has to rebalance, Redis uses `MIGRATE` to copy keys slot by slot to new master nodes, then updates cluster metadata.
    - **NOTE:** you **cannot** do `mset k1 v1 k2 v2`, because all those keys might be on different Redis node, and doing so basically will require **distributed transaction** which complicates things, so it is forbidden.
    - Gossip protocol is not strong consistency, it is eventual consistecy.
    - Questions, how does Redis Cluster ensure failure detection and automatic failover?
      ```
      🧩 Short Answer
      🧠 Redis Cluster uses a Gossip protocol for cluster state propagation,
      and a majority-vote mechanism (not full Raft) for failover decision.
      It’s not Raft or Paxos — but Raft-like in spirit (majority agreement), combined with Gossip-based failure detection.
      ```
    - Redis Enterprise even safer.
    - Redis Cloud, part DB, part cache

### 大厂生产级Redis高并发分布式锁实战
**NOTE: Best live demo on redis I have ever seen**
- Demostrate, at the source code level how *Redisson* helps us implement a distributed lock.
- Conceptually it is very straight forward, but implementation is very smart and well thought off.
  - Every thread use redisson lock to try `hsetnx` a redis key.
  - if not able to acquire the lock (via semaphore) , the thread gets parked (in waiting state)
  - if able to subscribe, it will return
  - when the thread holding the lock finishes, it will `unlock`
    - delete the `key` from redis
    - also updating in a `redis_lock_pub_sub` channel, that current thread has relinquished the lock
  - All waiting threads' watchdogs/monitor threads subscribing to the channel gets notified of this event, and subsequently released the lock on semaphore. 
  - All waiiting threads will start competing for this semaphore (unfair lock)
  - **you need to watch the video again, and practice on your local!!!**
- *worthy mentioning* : Valkey is an opensource alternatives to Redis8, and it is free, and has a growing communities using it, and can be applied to many platforms. 
- You need good understanding of JUC. Some complementary knowledge:
  - Semaphore tryacquire(timeout) will put current threads in `WAITING` state, which waits for `SIGNAL` to wake up. In a `BLOCKED` thread, thread is waiting for a `LOCK` to be available. 
  - Semaphore tryacquire basically is using `CAS` in `AbstractSynchronizedQueue`. You need to read up on concurrency courses.

### 一线大厂高并发缓存架构
- Basic Redisson PubSubLock, 
- Big Prom scenario:
  - Use segment locking, product_101_1 : 100, product_101_2:100 ... product_101_10:100, 
  - Why do we need re-entrant locking? So that we can do read and write separation, i.e. RedissonReadWriteLock
- Cach Breakdown: Data missing in cache, resulting in large amount of request at DB side
  - influencer effects
  - backend DCL, but this way we also blocks requests concerning other products
  - Better alternative : Redisson lock,  
- Cache Penetration: Data does not exist in cache nor DB, 
  - DDos attack
  - Preventions: use API rate limiter, put an `EMPTY_PRODUCT` inside redis. 
- What happens if your redis cache and your DB have mismatches? how do you prevent that?
  - We have this `Read and Update` process: check the DB, and then update cache
  - this has to be atomic, 
  - so we continue to use Distributed lock.
- How to optimize the locks used in above 2 scenarios?
  - When we have *Lots of read, little write*, use RedissonReadWriteLock.
  - For the influence effects, using readwrite lock might not be able to do much better, because using distributed lock we already have quite a performance. However we can use `tryLock(ttl)` for better performances, i.e. after `TTL` time, all the waiting threads give up and start reading from cache. in this case we assume the thread which acquired the lock successfully the 1st time, has already completed populating the cache. **But that may not be true**
- How to deal with Super Influence / Hot Trending event
  - Millions of fans will start searching for this event/news/product...
    - Redis cannot take such concurrency... hangs, webapp hangs, frontend hangs... 
    - System in failure mode.
    - Cache Avalanches
  - Preventions: Use multi level caches
    - use JVM internal caches, such as ConcurrentHashMap. JVM internal caches can take millions of concurrent request. super fast. 
    - What happens when there is a write request? use Redis pubsub (i.e. MQ)
    ![mq](multilevelCache.drawio.png)
    - But then you have this *eventual consistency* trade off.
- In BAT, what they do is they have a separate system called `Hot Spot system` (热点系统)
  - By (e.g. via AOP) intercept all actions on Redis, they analyze new `host spot` event, and update frontend cache accordingly
  - so that response is faster. 
  - Big data related

### Redis缓存设计与性能优化
- Multilevel cache in depth:
- Cache penetrations: 
  - soln1: empty-cache with ttl.
  - bloom-filter, intercept ddos.
- Cache avalances:
  - Sentinel or Hystrix circuit breaker. 
  - rate limiting, i.e. only allow 80000 concurrent request.
- Cache and DB write mismatch: use RedissonLock
  - Better: use Redisson ReadWriteLock
  - **Note**: data you put in redis-cluster should be those that do not require strong consistency, if you need strong consistency, just use DB. If DB performance cannot make it, use Redis as temproary storage, and then asyn writes to DB.
- Best practices:
  - Keys keep it short
  - value keep it small, please no `bigkey`, e.g. huge set of string.
    - Processing bigkey will take too much time, cause blocking
  - do not `del` key from set
  - Optmize big key by using segment lock
- Redis Client best practices (e.g. Jedis)
  - maxTotal, maxIdle, minIdle
  - set maxTotal = maxIdle, and warm up the `redis-client` thread pool.
- Redis eviction policy
  - normal scenarios LRU is enough
  - however, if encountered with hotspot scenario, LFU could be better. 

### 京东热点缓存探测系统JDhotkey架构剖析
- Very lightweight, elegant solution for hotkey detection. 
- Built on ***Netty***, long http connection. 
- Source [Code](https://gitee.com/jd-platform-opensource/hotkey/blob/master-v0.0.4/README.md)
- Architect [Blog](https://mp.weixin.qq.com/s/xOzEj5HtCeh_ezHDPHw6Jw)
- Architecture:
  ![jd hotkey](JDHotKey.png)

- Key takeaways:
  - Netty `SO_KEEPALIVE`, long connection
  - Client will be referenced by actual server
  - Worker ip information are managed by etcd cluster (cloud native, Kubernates Services)


## RabbitMQ
### Key Components
![Rabbit MQ diagra](./exchanges-topic-fanout-direct.png)
- Queue
  - a **buffer** that stores messages
  - Owned by RabbitMQ
  - Consumed by one or more consumers
- Exchange (**Routing Brain**)
  - Receives messages from producers
  - Decides which queue(s) get the message
  - Never stores messages
- Connection (TCP session to the broker)
  - A long-lived TCP connection
  - Between client and RabbitMQ broker
  - Authenticates, negotiates protocol, heartbeats
  - Properties:
    - Expensive
    - Thread-safe
    - Should be shared
    - One per app instance (usually)
- Chanel (**Virtual connection, hot path**)
  - A lightweight virtual connection
  - Multiplexed over a single TCP connection
  - Where all real work happens

  - What happens on a Channel
    - publish
    - consume
    - ack
    - declare queues/exchanges
  - Why Channels exist
    - TCP connections are expensive
    - AMQP multiplexes many channels over one socket
    - Critical rules (very important)
    - ❌ Channels are NOT thread-safe
    - ✔️ One channel per thread / logical flow
    - ✔️ Cheap to create

- 🧠 Low-Latency / Backend Perspective (Your world)
  - Connection ≈ Netty EventLoopGroup
  - Channel ≈ logical pipeline / session
  - Exchange ≈ routing table
  - Queue ≈ bounded buffer + consumer backpressure
  - RabbitMQ optimizes:
    - Routing correctness
    - Reliability
    - Delivery guarantees
    - **not** raw p99 latency

### Practical
**TODO**

- Consumer 
  - **push** `channel.basicConsume(String queue, boolean autoAck, Consumer callback);`
  - **pull** `channel.basicGet(QUEUE_NAME, boolean autoAck);`
- Message Listening, and Callback
  ```java
    String basicConsume(String queue, DeliverCallback deliverCallback, CancelCallback cancelCallback, ConsumerShutdownSignalCallback shutdownSignalCallback) throws IOException;
  ```
- [Rabbit MQ Tutorials](https://www.rabbitmq.com/tutorials)
  ![Rabbit MQ Model](./6_rabbit_mq_models.png)

- Headers Routing

## Kafka
### Kafka 上手
- prerequisite is a must! at least you need to setup `HostOnly` and `Nat` network adapter
- need to setup zookeeper and java
- ZooKeeper config:
```sh
root@chenyang-ubuntu:/app/zookeeper/apache-zookeeper-3.8.5-bin# cat conf/zoo.cfg
tickTime=2000
initLimit=10
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just
# example sakes.
dataDir=/app/zookeeper/data
# the port at which the clients will connect
clientPort=2181
server.1=192.168.88.10:2888:3888
server.2=192.168.88.11:2888:3888
server.3=192.168.88.12:2888:3888
```
  **NOTE** "Host-Only" ip in `zoo.cfg`

- Kafka server.properties:
```sh
root@chenyang-ubuntu:/app/kafka/kafka_2.13-3.8.1# cat config/server.properties
############################# Server Basics #############################

# The id of the broker. This must be set to a unique integer for each broker.
broker.id=1

############################# Socket Server Settings #############################

# The address the socket server listens on. If not configured, the host name will be equal to the value of
# java.net.InetAddress.getCanonicalHostName(), with PLAINTEXT listener name, and port 9092.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
#listeners=PLAINTEXT://:9092
listeners=PLAINTEXT://192.168.10.31:9092

# Listener name, hostname and port the broker will advertise to clients.
# If not set, it uses the value for "listeners".
#advertised.listeners=PLAINTEXT://your.host.name:9092
#advertised.listeners=PLAINTEXT://192.168.10.31:9092
num.network.threads=3
num.io.threads=8
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600
log.dirs=/app/kafka/logs
num.partitions=1
num.recovery.threads.per.data.dir=1
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1

############################# Log Retention Policy #############################
log.retention.hours=168
log.retention.check.interval.ms=300000

############################# Zookeeper #############################
zookeeper.connect=worker1:2181,worker2:2181,worker3:2181

# Timeout in ms for connecting to zookeeper
zookeeper.connection.timeout.ms=18000
group.initial.rebalance.delay.ms=0

```
**Note**: worker1, worker2, worker3 are `Host-Only` ips (ens37), they are defined in `/etc/hosts`. **For client connections**, we cannot use them, unless the client is on the same host. That is why for `listeners`, we use `PLAINTEXT://192.168.10.31:9092` which is ens38 address, so that Kafka can listen to the ip that the current walking machine can write to. 
![Kafka-Zookeeper-VM-Setups](network_connection.png)

-   cluster after setting up:
```sh
//shell
nc -z 192.168.10.31 9092
// powershell
Test-NetConnection 192.168.10.31 -Port 9092

```
### Kafka 客户端详解
- **Pre-requisite create Topic (e.g. disTopic)**  
  - `bin/kafka-topics.sh --bootstrap-server worker1:9092 --create --topic disTopic --partitions 3 --replication-factor 2`
- Kafka client api is written in java, you can source it via maven central
- `KafkaProducer.java`:
  - mandatory configs:
    - `ProducerConfig.BOOTSTRAP_SERVERS_CONFIG`
    - `ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG`
    - `ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG`
    - define your `TOPIC`
  - send msg: `ProducerRecord<String, String> record = new ProducerRecord<>(TOPIC, Integer.toString(i), "MyProducer" + i);`
- `KafkaConsumer.java`:
  - mandatory configs:
    - `ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG`
    - `ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG`
    - `ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG`
    - Define Consumer Group: `GROUP_ID_CONFIG`
  - polling msg: `ConsumerRecords<String, String> records = consumer.poll(Duration.ofNanos(100))`
  - commit offset: `commitSync`, `commitAsync`
- Consumer Group:
  - messages in partition --> only **CONSUMABLE by ONE Consumer (within one Consumer Group)**
  - `Offset`, how many msgs each Consumer Group has consumed per Partition. Crucial to control progress. 
  - `Offset` determines the progress of our consumers. 
  - Sometimes it is easier to manage it, if we manage our own offset (Put in Redis) instead of relying on Kafka Offset. So we know **for sure** the message (for example an order) has been processed. This is because *Receiving an msg successfully* and *Successfully processed the message* doesn't have to be hard coupled.
- `ProducerInterceptor`: `filters`, `Interceptor`, `SoapHandler`
- Serializers: Compact binary with json schema (`Avro`)
- Message Routing:
  - Producers:
    - Default Sticky strategy.  Send messages until `batch.size` == 16K, or `linger.ms` reached, after that RoundRobin.
    - `PARTITIONER_CLASS_CONFIG = "partitioner.class"` for customized ParitionedProducer.
  - Consumers:
    - `PARTITION_ASSIGNMENT_STRATEGY`
    - `RangeAssignor`, `RoundRobinAssignor`, `StickyAssignor`
- Producer Messages Buffer 
  - Send messages in batch. 
  - batches are stored in `Dequue` in `RecordAccumulator`, then send to brokers.
  - `linger.ms`
- ACK 
  - `acks = 0`
  - `acks = 1`
  - `acks = all` or `acks = -1`
    - if `min.insync.replicas` of partions have been written, then return `ACK` to producer. Configured in `broker.conf`
- Producer Message `Idempotency`
  - if Broker no response, message considered not sent, so `Producer` retries. 
  - `ProducerConfig.RETRIES_CONFIG`
  - `at least once`, `at most once`, `exactly once`
    - `exactly once` Implementations:
      - control order using `PID` and `Sequence Number`
- Producer Message Compression.
  - broker.conf --> zstd
- Producer Message Transactions:
  - Group Transaction when writing multiple messages.
  - if one fail all fails
  - use customized `TRANSACTIONAL_ID_CONFIG`, can be any value, but it better has something to do with business
- Spring boot integration:
  - very easy, a Wrapper over the client-api above
  - you can add customized kafka configuration (if not already provided by Spring boot):
    - e.g. `spring.kafka.producer.properties.interceptor.classes=com.roy.kfk.basic.MyInterceptor`
    -  they will put <`interceptor.classes`, `com.roy.kfk.basic.MyInterceptor`> in `properties` map and pass it to the `kafka` client.
- Summary:
  ![Kafka Client Side flow](kafka_client_side_process_flow.png)

### Kafka 集群工作机制详解
- Zookeeper Cluster data management:
  - Among brokers, elect a **Controller**, to manage leader partitions and follower partitions
  - Among partitions, elect a **Leader**, which will oversea data transfer with the client app.
  - leverages LEO (log end offset), HW (high watermark)
  - Intellij, ZooKeeper plugins
- **Controller Broker Elections**, oversaw by zookeeper, only one broker will become controller. 
  - monitor `/brokers/ids`, and ids changes, see if brokers are down.
  - monitor `/brokers/topics`, detect changes in topic and corresponding partitions
  - monitor `/admin/delete_topic`, delete topic
  - also in charge of pushing metadata to other brokers.
- **Leader Partition**
  - `AR`, `ISR`, `OSR`
  - to check `AR` and `ISR`, `[root@192-168-65-112 kafka_2.13-3.8.0]# bin/kafka-topics.sh --bootstrap-server worker1:9092 --describe --topic disTopic`
  - **Election**: choose acording to orders in `AR` List.
  - **Self Auto Balance**:  
    - Leader partition is busy, so kafka tries to place it on different **broker node** to spread the workload.
    - However if there is a partition changes, and new elections, this balance might be destoryed. i.e. we have multiple leader partitions on one Broker.
    - That is why we have the Leader Partitions Auto Re-Balancing mechanism.`auto.leader.rebalance=true`
- **Partition Recovery**
  - LEO: Log End Offset (when leader partition received and saved message from producers, its LEO + 1; all follower paritions will have to sync from Leader, and do +1 on their own LEO)
  - HW: High Watermakr, the Minimum of all LEO in a group of partitions.
    - Conceptually, it is the **highest offset that is guaranteed to be safely replicated to all ISR replicas**, and Consumers are **only allowed to read up to HW**, WHY??
    - Consistency after leader failover: If ledaer crashes, the new Leader must
      - keep all offsets <= HW
      - Trancate anything > HW (those are uncommited)
    - Gurantee only replicated messages are visible
      - Consumers **must never see data** that can be lost after failover.
  - **Scene 1: When follower is down**
    - follower partition exits ISR, and leader and other follower continue to receive messages
    - when the follower is back up, it will not join ISR immediately. It will read its local HW, delete all its logs that have higher offset than its HW, and start syncing messages again with leader partition from its local HW.
    - When the follower's LEO is >= Partion's HW, it will be back into ISR. This means the folower has finally caught up with Leader.
  - **Scene 2: When Leader is down** (we are fuxxed)
    - Leader is down, new election among ISR. One follower will be promoted to Leader. At thsi time, the message sync between old leader and the followers might not have completed. So we may have a new leader with LEO < than the previous LEO.
    - Since Kafka messages are based on copies in the Leader's partition, all followers will have to remove logs entries >= leader's HW, and then start syncing again.
    - When old leader recover, it will be come follower, and start message re-sync 
    - **So we might lose quite a lot of messages, what can we do??**
      - if server side cannot handle it, leave it to Client side. Set producer `ACKS = -1 or all`, force/makesure server-side sync across partitions, otherwise resend the message
  - **HW is a distributed value, how do we make sure it is consistent/correct among brokers?**
- **Leader Epoch mechanism**
  - Intuition: a stale follower may still think it is the leader and write data past the HW.
    - this creates log divergenece
    - inconsistent HW
    - uncommited data , consumers sees phantom data
  - What is leader Epoch?
    - eacht time a new leader is elected for a partition, kafka increments a number
    - `<ledaer epoch id>, <start..end offset range that leader was responsible for>` e.g. `0 0 500`
  - What it protect
    - it protects epoch race. Where old leader thinks it is still leader, whereas new leader alreadyh elected. Old leader conitnues writing -> corruption
    - Kafka prevents above by attaching the leader epoch to every produce request sent to the leader.
    - if request arrives with an old epoch:
      - Kafka immediatelyh rejects the write
      - the stale leader must stop appeding data
      - it reverts to follower mode
      - it fetches the new ledaer's log to catchup.
    - This enforces the gurantee: **only actor with the highest epoch can append to the partition log**
  - How does this gurantee HW consistency:
    - Epoch prevents stale leader writes by killing stale leaders instantly. 
    - e.g. Old leader wakes up -> receives producer request with epoch 6 -> wait a minute, I am epoch 5, i am no longer king!! -> transition to follower state -> start fetching from new leader -> catches up discard stale tail if needed.
    - Or, Old leader wakes up -> receives new metadata from **cluster controller** -> see that a new leader has been elected -> transition to follower mode
    - Remeber cluster controller is a special broker/node that is elected to control cluster metadata by Zookeeper/Kraft.
- **What if Leader Partition and Controller failed at same time?!**
  - some leader paritions, and the controller for a cluster may happen to be on the same broker/node. if the node is down (Broker A), they are all down, so what happens afterwards?
  - Suppose Brokers, A, B, C
    - A is controlelr
    - A is also leader for partitions P0, P3
    - B and C have follower replicas of P0, P3 (in ISR)
  - Step 1: ZK or Kraft notices Broker A is gone:
      - **ZK**: One of (B, C) wins the race to create /controller -> say B becomes new controller
      - **KRaft:** The controller Raft quorom elects a new leader controller (which may or may not be B)
  - Step 2: new controller elects new leaders
    - for each parition that hand leader == A:
      - looks at ISR list,
      - picks a new leader (e.g. B for P0, C for P3)
      - increments the leader epoch
      - broadcast new metadata to all brokers
      - so e.g. P0: leader moves A -> B, P3: leader moves A -> C
  - Step 3: Clients refresh metadata and continue
    - producers/consumers periodically refresh cluster metadata,
      - they learn that P0 leader is B, and P3 leader is C
      - they reconnect writes/reads to the new leaders.

### Kafka 日志索引详解
- Kafk only append entries to log files. No delete or updates.
- For every consuemer group, its progress is written to __consumer__offsets topic. 
- Why is Kafka IO so performant?
  - Kafka data file structure, multiple parition under the same topic has independent log.
  - Zero Copy:
    - What is zeroy copy: zero copies between Kernel and User. 
    - Without Zero-Copy: `Disk → Kernel → User Space → Kernel → Socket → NIC`, copy btes 4 times
    - With Zero-copy: `Disk → Kernel → Socket → NIC` 
  - Disk sequential writes (600 MB/s), always in append mode.
    - Used `FileChannel` + `DirectByteBuffer`, best for predictable write semantics
  - MMAP (memory mapped files): **Random access reading of index files**
    - Used for index lookups in Kafka
    - Good for small random access
    - Not exactly zero copy for network sending
  - sendfile(Truly Zero Copy):
    - **used for network send, not for writing logs**
    - **used for replication + consumer fetch**
    - `[PageCache] -> NIC (DMA)`
    - broker says, “Kernel, please send bytes [offset : offset+count] from this file to that socket.”
    - just a syscall, `fileChannel.transferTo(position, count, socketChannel);`
    - send those bytes from disk/page-cache directly to socket, Dont copy them to user-space first. 
    - Path: `Disk/page-cache → kernel → socket → NIC`, the **real high throughput part**
    - User-mode does not care about content of data, just `sendfile` only. so zero copying from kernel to user. kernel mode straight away send FileDescriptor to Socket buffer zone.
  - Summary:
    - **Write Path: (Producer -> Broker)**
      - `Network → DirectByteBuffer → FileChannel.write() → Page Cache → Disk`
    - **Read path (Broker → Consumer / Follower)**
      - `Page Cache → sendfile() → NIC`, TRUE 0-copy
    - **Index look up**
      - `mmap → memory access → find physical file offset`
      - Not zero-copy but extremely fast.

### Kafka 功能扩展
- Monitoring, Kafka Eagle 
- KRaft cluster:
  - `bin/kafka-server-start.sh -daemon config/kraft/server.properties`
  - for kraft cluster, you need to define cluster id :
    - cluster-id: `bin/kafka-storage.sh random-uuid j8XGPOrcR_yX4F7ospFkTA`, this has to be the same across cluster. 
    - `bin/kafka-storage.sh format -t j8XGPOrcR_yX4F7ospFkTA -c config/kraft/server.properties`
  - After that pretty much similar to zooKeeper. 
- **Kafka Stream**: KStream (make Kafka stateful)
  - Used for 
    - Windowed joins
    - continous aggregations
    - stateful operators
    - repartition topics
    - local rocksDB state
    - exactly once streaming pipelines
  - It is fast not becase it pulls faster, but because
    - All transformation are local (no network calls)
    - local state store (RocksDB) ver fast random access
    - Batch-pulling + Batch-processing -> efficient CPU + IO
    - Zero coordination scaling -> new instance = auto rebalance
    - Operators are compiled java code, no external SQL engines
  - Under the hood:
    - topology (a graph of transformations).
    - data goes through topology before being handed over to business logic. 
  - Real World example, 
    - Use Case # 1 - Real-Time VWAP / TWAP / Rolling Aggregations (Trading), 
      - Nightmare to implement in normal consumer
      - need to maintain rolling window manually. 
      - If use KStream: one line of code. 
    - Use Case #2 — Customer 360 / Unified Profile
      - create a continuously updated real-time materialized view for each customer
      - KTable join
    - Use Case #3 — Fraud / AML Real-Time Rules Engine
      - detect patterns like 3 failed logins in 10 minutes
      - $20k transferred in < 5 mins. 
    - Use Case #4 — Enrichment Pipelines
      - Orders  → add static data
      - Trades  → add instrument info
      - Market data → join with reference data

## 深入理解网络通信和TCPIP协议
- OSI seven vs TCP IP model
  ![Logical Mapping](./logicalMapping_OSI_TCPIP_model.png)
- To help our understandings
  - Network layer: Network Adapter
  - Datalink Layer: Network Adapter Driver
  - IP and TCP layer: Our OS deals with them
  - Application layer: our own spring boot applications
- TCP (reliable) vs UDP (unreliable)
- How does data flow in a TCP model
  - each layer adding its header to the packet
  - transport over network
  - each layer read its own header to see if it is for them, if yes read, if no, discard.
  ![Data Transfer](./data_transfer_TCPIP.png)

- Address:
  - MAC address: physical address, factory produced.
    - `ipconfig /all`
    - `ifconfig -a`
  - IP Adress: IPv4 (32 bits, 4 Bytes), IPv6
- Port:
  - the address of programs, 22 SSH, 3309 RDP, 80 HTTP
  - **65535** port number, why?
    - because TCP/UDP use 16 bits field to store port number in its headers. 2 ^ 16 = 65536. port 0 represents "all" ports, so those usable are 65535. 
  - To monitor port use the following command:
    - Windows: `netstat -ano`, `netstat -ano | findstr <port number>`
    - Linux: 
      - `lsof -i:<port number>`
      - `netstat -tunlp`: show tcp, udp port and process information
      - `netstat -tunlp | grep <port number>`
- Address & Port:
  - What is a connection in OS perspective?:
    - Unique combination of:
    - Source IP
    - Target IP
    - TCP version
    - Source Port
    - Target Port
  - **A server can only maintain 65535 TCP connections, is that right?**:
    - Absolutely not, any elements in the above 5 elements change is a new connects,
    - so we should have max = 2^16(targt ports) * 2^32(target ip) * 1 (source ip) * 1 (source target)  = 2^48 = 200 trillion connections

- **TCP characteristics**
  - reliable: guranteed by **RTO: retransmission time out** + **SYNC-ACK, 3-ways handshkes**
  - RTO: determins RTT (round trip time) dynamically to decide when to resend.
  - include sequence number, when ip "upload" the data to TCP layer
    - it sequences the packets and do validations
    - if error, ask for resend.
  - Full duplex, 
  - **3-way Handshakes**: `ack` is Acknoledgement Number, not the actual `ACK` field
    - **How**
      - Client (SYNC_SENT)   - `SYN = 1, seq = J`        -> SERVER
      - Client <- `SYN = 1, ACK = 1, ack =J + 1, seq=K ` -  SERVER (SYNC_RCVD)
      - Client (ESTABLISHED)  `ACK = 1, ack = K + 1`     -> SERVER
      - Client (ESTABLISHED)   `no more transmission`    -  SERVER (ESTABLISHED)
    - **Why**
      - 3 is the minimum numbers for 2 connections to
        - **know** starting sequence of **each other** (e.g. J and K in the previous example)
        - and **confirm** that they know each other's starting sequence
    - **Common pitfalls**:
      - SYN flooding (a type of DDOS attacks)
        - Aims to blow up the in-memory queue that maintains client's IP, which is fake of course.
      - How to counter?
        - Do monitoring on all connections, 
        - Delayed TCB allocation (Transmission Control Block)
          - kernel's internal data structure that stores everything about a TCP connection
          - `connection object`
          - Only assign a `TCB` after 3-time handshakes
  - **4-way handshakes(goodbyes)**
    - **Why do we need 4-way handshakes?**: TCP is full duplex, it needs both side to confirm termination
    -  FIN = 1, seq = u
    -  ACK = 1, seq = v, ack = u + 1
    -  FIN = 1, ACK = 1, seq = w, ack = u + 1
    -  ACK = 1, seq = u + 1, ack = w + 1
    -  TIME-WAIT
   -  **Why do we need TIME-WAIT**
      -  need to reliably terminate TCP connections
      -  so to make sure the other side actually received our last `ACK = 1, seq = u + 1, ack = w + 1`, if didn't receive we can resend.
      -  Without it, Linux might create a new connection on this port, and this port might receive obsolete data, which is not right.
   -  **What could be the reason that MySQL servers experience large amount of TIME_WAIT**
      -  MySQL use short TCP connections, afterwards, system will recycle resources. 
      -  Because of huge amount of requests, there are alot of connections.
      -  If programmer didn't do `mysql.close`, MySQL will invoke `wait_timeout` mechanism, many connections will be in `TIME-WAIT` states. 
  -  Use Wireshark or `tcpdump` to sniff packets.
  -  **How does an OS removes a TCP connections**
     -  A TCP connection = a TCB (Transmission Control Block)
     -  when a FIN/ACK/FIN/ACK happens, kernel updates TCB state
     -  when app calls `close`
        -  removes the FD from the process FD tbale
        -  decrements refcount on the socket
        -  kernel cannot free TCB yet, because it may still be waiting for ACK , transimitting FIN, waiting in TIME_WAIT, draining buffers
     -  kernel clesn socket buffers (sk_buff)
        -  outing send buffers are freed, ACKed receive buffers are freed
        -  this release memory in TCP send queue, TCP receive queue
     -  Kernel removes TCB from connection tbales
        -  TIME_WAIT finished, for active closer
        -  removes the TCB from has tables
        -  removes routing cache entries
        -  free memory allocated for the TCP control block
     -  Time wheel entries and retransmission timers removed
        -  RTO, Delayed ACK Timers, Keepalive timer, TIME_WAIT expiry timer, ...
     -  Memory is freed, (the actual remove)
        -  `kfree(tcp_sock);`

-  **UDP, UDT, QUIC**
   -  all UDP connections (User Datagram Protocol)
   -  no gurantees, so support unicast and multicast
   -  UDT and QUIC are very new.

## BIO实战、NIO编程与直接内存、零拷贝深入辨析

- **Socket**
  - What is a socket? an *abstraction layer*, between *Application Layer* and *TCP Layer*
  - provided by OS. 
    - ![socket](./Socket_example.png)
  - **Short** connection: A TCP connection that only exists briefly and then closes.
    - An application level pattern, not a protocol feature.
    - Open a TCP connection -> send one request -> receive one response -> immediately close the connections
    - Opposite to long connection
  - **Long** connection: 
    - Socket connection stays, no matter whether it is in use or not.
  - When you have alot of data to send, use Long Connections, otherwise use short connection. But Http1.1 and Http2, Http3(based on QUIC) might be using Long connection as default.

- **Blocking IO**
  - why is blocking? 2 parts
    - When a server is ready, its main thread just stays there waiting (while loop) for connections,
    - When a connection is established, it is there (blocked) waiting for request from client. New connections on the socket cannot be handled. 
  - Always used in conjuction with Threads and ThreadPool
  - New thread for connection, request and response.
    - All read and writes, have to be blocked within a thread.
    - 1:1 relationship to number of clients visit. Waste thread, which is precious resources in Java. 
  - We can also use ThreadPool to manage request,
    - each thread could handle multiple thread.
    - But if there are many long blocking calls concurrently. Then all requests **have to wait**, huge problems.
  - *RPC framework (with BIO)*: 
    - ![RPC framework](./RPC_architecture.jpeg)

- **NIO, New IO**
  - NIO, is buffer oriented, made up of  `Selector`, `Channel`, `buffer`
  - Non-Blocking:
    - Normal IO `read` or `write`, thread will be blocked. 
    - NIO does not have to wait, that is why it can manage multiple `Channel`
  - `Reactor`
    - IoC
    - one manager, caters to many customers
    - ![reactor](./reactor.png)
  - `Selector`:
    - Many channels can be registered under the same `Selector`
    - One thread to manage this `Selector`
  - `Channel`:
    - Implements `SelectableChannel`
    - `ServerScoketChannel`: all TCP connections listening channel, support UDP and TCP, used by application to implement IO multiplexing.
    - `SocketChannel`: TCP Socket listening channel, one socket is equivalent to one unique TCP connection (src ip : port , dest ip : port)
  - `Buffer`:
    - An array supporting read an write between App and SocketChannel
    - `capacity`
    - `limit`: in write-mode, equals `capacity`, under read-mode becomes the `position` in write-mode
    - `position`: the next place to read or write in the current buffer
    - `flip()`: switch from write to read mode, `limit = position; position = 0`
  - ![NIO-Architect](./nio_archi.png) 
  - What is a `SelectionKey`:
    - represents the identity of a `SelectableChannel` for a `Selector`. 
    - Created during registration, e.g. `serverSocketChannel.register(selector,SelectionKey.OP_ACCEPT);`
    ```java
    public class SelectionKeyImpl extends AbstractSelectionKey {
      final SelChImpl channel;
      public final SelectorImpl selector;
      private int index;
      private volatile int interestOps;
      private int readyOps;

      SelectionKeyImpl(SelChImpl var1, SelectorImpl var2) {
          this.channel = var1;
          this.selector = var2;
      }
      // other methods
    }
    ```
    - Cancelled `SelectionKeys` will not be immediately removed from `Selector`, but added to `cancelledKeys`, which will be removed during next `select()`
    - This is why when we want to use a `SelectionKey`, we need to check `isValid` first
    - `interestOps`
      - `OP_READ`: react only when *OS* read buffer contains data.
      - `OP_WRITE`: react only when *OS* write buffer is available, which is almost all the time for normal usecases. So normally this op is not necessary (otherwise wasting CPU dealing with all the `OP_WRITE` events), unless we are doing write intensive tasks, such as file downloading, buffer could be full, then this op becomes necessary. Also remeber to clear this op after write.
      - `OP_CONNECT`: for client to invoke `SocketChannel.finishConnect()` if necessary. This is because sometimes `SocketChannel.connect()` many not return `true` immediately, so need to retry or `finishConnect`
        ```java
          private void  doConnect() throws IOException{
            /*非阻塞的连接*/
            if(socketChannel.connect(new InetSocketAddress(host,port))){
                socketChannel.register(selector,SelectionKey.OP_READ);
            }else{
                socketChannel.register(selector,SelectionKey.OP_CONNECT);
            }
          }
        ``` 
      - `OP_ACCEPT`: only for server (to accept a coonection request)
      - `ServerSocketChannel` -> `OP_ACCEPT`
      - Server `SocketChannel` -> `OP_READ`, `OP_WRITE`
      - Client `SocketChannel` -> `OP_READ`, `OP_WRITE`, `OP_CONNECT`
  
  - **Single Reactor Framework**: 
    - all I/O `accept()` `read()`, `write()`, `connect` are on the **SAME** thread.
    - But for current framework, not only IO are on Reactor thread, non-IO operations are on I/O thread too. So we need to separate non-IO logics from IO operations to improve speed. Therefore we introduce ThreadPools
  
  - **Single Reactor + Worker Threadpool Framework**:
    - So often the implementation is single thread `Reacotr` +  worker `ThreadPools`
    - Sometimes if there are thousands of connection, NIO thread becomes overloaded and bottle neck.
    - ![reactor-worker](./reactor_worker.png)
  
  - **Reactor with Threadpool + Worker Threadpool Framework**
    - one Reactor threadpool, each reactor thread has its own `Selector`, event and logic loops
    - one `mainReactor` but multiple `subReactor`
      - `mainReactor` accepts client connection requests, and pass the `SocketChannel` to `subReactor`, which will take over communication with client.
      - `subReactor` usually lives in a threadpool
      - `subReactor` will be in charge of I/O `read()`, the data read will be process by threads from worker threadpool. If there is data to write back, it will also be in charge of the I/O `write()` operation.
    - ![multi-reactor](./nultiple_reactor.png)

- **DirectBuffer**
  - Every TCP Socket has `SO_SNDBUF` and `SO_RECVBUF`
  - When Java does IO, it will have to invoke `write()` to `SO_SNDBUF`.
    - However the address (of data that we want to send) that we pass to C library via JNI cannot be obsolete.
    - In Java, due to GC, this address **very possibly** will be obsolete.
    - So wee need to put it in a place that cannot be GC-ed. Off-Heap. basically, `DirectBuffer`
    - If we use HeapBuffer, e.g. `ByteBuffer.allocateDirect(1024)`, 
      - JVM must copy heap data -> temp off-heap buffer
      - Pass that off-heap buffer to `write()`
    - If instead we use `ByteBuffer.allocateDirect(1024)`
      - Then NIO can pass the **same off-heap pointer** directly OS. no extra copy, higher throughput IO.
    - That is why all high performance JAVA IO frameworks use driect buffers: Netty, Aeron, Kafka (uses mmap + direct buffers), Disruptor, Chronicle Queue/Map
    - OffHeap `DirectBuffer` is not affected by Minor GC, only affected when we do Full GC.
      ```
      +----------------------------+
      | Java object (on-heap)      |
      | class: DirectByteBuffer    |
      |   - attachment             |
      |   - capacity               |
      |   - address (long*) ----+  |
      +----------------------------+
                                    \
                            +------------------------+
                            | Off-heap native memory |
                            | allocated by Unsafe    |
                            +------------------------+

      ```
    - The On-heap object is tiny (16 - 32 bytes), the real memory lives Off-heap

- **Zero Copy (revisited)**:
  - Reduce the needs for
    - Unnecessary copying by CPU from *kernel space* to *userspace*, and
    - the Unnecessary context switching by CPU (from user space to kernel space, e.g.) when carrying out above tasks.
  - Clasic Copy:
    - `buffer = file.read(...)`
    - `Socket.send(buffer)`
    - ![Classic Copy](./classic_copy.png)
    - `read` and `send` are both OS commands, which involves context switching between User space and Kernel space.
    - 4 Context Switching + 4 Copies(2 DMA copies, 2 CPU copy)
  - MMAP:
    - just map the data from hard disk to application buffers, without actually copying.
    - ![MMAP](./MMAP.png)
    - Java NIO `FileChannel.map()`
  - `sendfile`:
    - When sendfile is called, DMA copy data to kernel buffer
    - Then DMA copy kernel buffer to socket buffer, but not the data, just the address and length to socket bugger.
    - DMA straight away copy the data from kernel buffer to NIC. 
    - 3 or 2 Copies; 2 , 2 DMA copies that is for sure, if DMA supports copying using address and length; otherwise CPU has to copy every data to SOCKET BUFFER, which is one more CPU copy
    - ![sendfile](./sendFile.png)
    - `File Pages -> Socket send queue(SKB), no copying of file data -> NIC DMA -> network`
    - in JAVA NIO, `FileChannel.transferTo`, `FileChannel.transferFrom`
  - `splice`:
    - Doesn't need DMA hardware support
    - When data reaches kernel buffer, a pipe is established between kernel buffer and socket buffer.
    - pointer of page cache (where file data lives) are transfered between kernel buffer to socket buffer
    - O(number_of_pages) **NOT** O(bytes)
    - `sendfile` is a specialized faster version of splice, 
    - ![splice](./splice.png)
    - `File Pages -> Pipe buffers -> Socket send queue (pointer passing only) -> NIC DMA -> network`
    - no Java equivalent, not supported in JAVA
  - `tee`:
    - duplicates pipe buffer reference from one pipe to another without copying data.
    ```
      Pipe A                     Pipe B
      ---------                 ---------
      | page1 |                 |       |
      | page2 |     tee() ----> |       |
      | page3 |                 |       |
      ---------                 ---------

    ```
    ```
            Pipe A                     Pipe B
      ---------                 ---------
      | page1 | --------+------>| page1 |
      | page2 | ----+---+------>| page2 |
      | page3 | --+----+------->| page3 |
      ---------   |             ---------
                  | (same exact kernel pages)

    ```
    - Amazing for a linux proxy or packet sniffer
      - consider a transparent proxy: `client -> proxy -> server`
      - you want to forward all traffic to the server
      - without tee you have to read to userspace, copy to buffer, write to socket, write to disk
      - With tee, you just have to do
      ```
        socket → pipe1 → splice (to server)
                    ↘
                    tee → pipe2 → splice (to disk)
      ```
      - Everything stays in kernel, zeor copy, zero wakeups, zero user space overhead
      - This is how high-performance monitoring proxies like `tcplogger`, `nginx mirror` and some HFT proxies work.
    - No Java equivalent, only C/C++/Rust

- **Zero Copies in Netty**
  - **DirectBuffers**, off heap, we hold the byte by reference (memory address) and we just read/write from address. 
  - `CompositeByteBuf`, merge multiple `ByteBuf` into one logical `ByteBuf`, reduce copies across `ByteBuf`
  - `FileChannel.transferTo` (sendfile)

- **Extra Questions**:
  - **If Tomcat is non-blocking IO, why does Spring MVC still do one thread per request model?**
    - NIO at the network layer != Non-blocking at the application layer.
    - SpringMVC is based on Servlet Specification: *Thread-per-request*, *Synchronous semantics*, *blocking*
    - Tomcat uses NIO for network operations, but Spring MVC remains blocking because it sits on top of the Servlet API, which is a synchronous, thread-per-request model.
    - True end-to-end non-blocking requires WebFlux (Reactor), which was built separately because MVC cannot be made non-blocking without breaking the Servlet model.
  - **For a brand new company issued laptop (Dell-A), how does it query google server, for the first time， on company campus?**
    - First DHCP DORA (DISCOVER, OFFER, REQUEST, ACK)
    - 1) Dell-A generates the following message: 
        ```
          Source IP: 0.0.0.0
          Dest IP: 255.255.255.255
          Dest MAC: FF:FF:FF:FF:FF:FF
          Source MAC: laptop MAC
        ```
        - this frame goes into a **switch** -> broadcast to all ports, including router
        - this frame goes to wifi -> wifi AP sends them through the tunnel to the wireless controller
    - 2) Wirelsees Controller receives DCHP DISCOVER
      - it decrypts and decapsulates wi-fi frmaes
      - place the client into correct VLAN
      - Acts as DHCP relay `DHCP DISCOVER -> DHCP server` unicast
    - 3) DHCP server sends DHCP OFFER back
      - contains IP Address
      - subnet mask
      - DNS servers
      - internal default gateway
      - lease time
      - domain serach suffix 
      - (sometimes) securityh classification
    - 4) Wireless controller passes DHCP OFFER back to AP -> laptop
    - 5) Dell-A then sends DHCP REQUEST (broadcast)
      - AP -> tunnels it
      - Controller -> relays it via DHCP relay -> DHCP server
    - 6) DHCP server sends DHCP ACK
      - Your assigned IP
      - Gateway
      - DNS
      - Lease time
      - Domain
      - MTU (corporate Wi-Fi sometimes sets 1400)
      - Possibly PXE parameters or host-class attributes
      - Wireless controller relays this back to laptop.
    - 7) Laptop now has IP but no internet yet
    - 8) User passes the corporate Wi-Fi autho (802.1X etc)
    - 9) User types `google.com` and press `Enter`
    - 10) Chrome normalizes the url to `https://google.com`
    - 11) Chrome then check its own cache
      - Browser DNS Cache
      - HTTP Cache (maybe you already have parts of Google cached, not possible in this case)
      - HSTS lists (force HTTPS for know sites)
      - if it finds a fresh cached answer, it might skip DNS, or network, but first time, not possible
    - 12) DNS: "what ip is google.com?"
      - Chrome asks the OS resolver, "give me the ip for google.com"
      - OS checks caches first (hosts file)
      - OS DNS cache
      - if not found, ask DNS Server
    - 13) Laptop sends DNS query
      - usually UDP port 53
      - Destination IP = DNS server you got from DHCP, likely an internal UBS DNS or resolver.
      - if your laptop doesnt know the gateways mac yet, it ARPS for it (Link-layer detail (ARP / Neighbor Discovery))
        - Broadcast: " who has gateway IP? Tell me you MAC"
        - Gatway replies with its MAC
      - Now your DNS packet can be sent to the gateway.
    - 14) Decide the route: Is that IP local or external?
      - OS checks routing table
      - is google's IP in my subnet? NO
      - so send to default gateway
    - 15) TCP onnection to Goolge (or QUIC)
      - Option A: HTTP/3 over QUIC (UDP 443)
        - Laptop sends QUIC initail packet to google ip UDP port 443.
        - QUIC includes encryption handshake
      - Option B: HTTPS over TCP 443
        - if QUIC isn't possible Chrome uses TCP:
        - TCP 3-way handshake
          - `SYN` ->
          - `SYN - ACL` ->
          - `ACK`
    - 16) TLS handshake (encryption + identity)
      - After transport is up (QUIC or TCP), Chrome does TLS:
        - Agree on encryption keys
        - verify you are talking to Google
      - Chrome sends "ClientHello"
      - Google responds "ServerHello + Certificate"
        - Certificate is signed by trusted CA
        - Cert matches google.com
        - Not expired / not revoked. 
      - Handshake completes -> encryption keys ready
    - 17) HTTP request: "GET /"
      - Now chrome sends the actual request.
    - 18) Google CDN responds
      - google edge server replies with
      - HTML for the main apge
      - Headers telling caching rules, cookies, security policies, etc
    - 19) Browser parases HTML and triggers many more requests
      - Chrome build the DOM Tree
      - Builds CSSOM tree
      - RUNS JS
      - dicsover more resources (CSS files, JS bundle, images, fonts, tracking pixels, api calls)
      - May reuse the same HTTP/2/3 connection
      - or open additional connections if needed
      - and caches aggressively
    - 20) Rendering on Screen
      - DOM + CSSOM -> Render Tree
      - layout (compute positions)
      - Paint
      - GPU compositing
  - Summary:
    - Typing google.com → page shown
    - Browser cache check
    - OS / browser DNS cache check
    - DNS query to corporate resolver → get IP
    - ARP gateway MAC address if needed
    - Transport connect (QUIC 443 or TCP 443)
    - TLS handshake + cert verify
    - HTTPS GET request
    - HTML response
    - Many sub-requests (CSS/JS/images/APIs)
    - Render pipeline → pixels on screen

## 深入Linux 内核理解epoll
- Linux 5 I/O model
  - **Sync**
    - blocking io (JDK Blocking IO)
    - nonblocking io
    - io multiplexing (JDK NIO)
    - signal driver io (sigio)
  - **async**
    - async io.
- Linux IO multiplexing programming
  - **FileDescriptor** 
    - in linux everything is file, including drives, mouse, everyhting is file
    - FileDescriptor is an index, of a per-process kernel table called the file descriptor table. 
    ```
      Process File Descriptor Table:
      FD 0 → stdin
      FD 1 → stdout
      FD 2 → stderr
      FD 3 → socket to 10.1.1.5:8080
      FD 4 → open file: /var/log/app.log
      FD 5 → pipe
      ...
    ```
    - Linux has 2 more levels of metadata
    ```
    Process
      → File Descriptor Table (FD → File Table Entry)
            → File Table Entry (open file description)
                    → Inode (metadata of file on disk)
    ```
    - File Descriptor Table (per process), each entry contains
      - A pointer to a file table entry
      - Access mode (read/write)
      - File offset(for seekable files)
      - Flags (O_APPEND, O_NONBLOCK)
    - File Table Entry (shared)
      - contains, current file offset (shared by duplicated FDs)
      - open flags
      - Pointer to the inode
    - Inode (filesystem - level)
      - Owner
      - Permissions
      - Timestamps
      - Block locations
    - In Java `FileDescriptor`(int fd) is direct mapping of linux FD integer.
      - `FileInputStream` -> wraps FD for a disk file
      - `SocketChannel` -> wraps FD for a socket
      - `Pipe` -> wraps FD for a pipe (used for cross thread signaling, useful for waking up selectors)
  
  - **`select`**
    - `int select (int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);`
    - monitors 3 types of file descriptors: read, write, except
    - blocked, until any fd is ready (meaning have data, can read, can write, or encounter exceptions), or timeout
    - when `select` return, we can travers `fdset` again to find the ready `fd`
    - very dumb traversing, don't even know which fd is ready, have to traverse every set.
    - Can only monitor up to 1024 fds. Low performance, but supported by alomost all platforms

  - **`poll`**
    - `int poll (struct pollfd *fds, unsigned int nfds, int timeout);`
    - no 1024 limit, pollfd is a pointer (linkedlist)
    - after returning, still need to traverse `pollfd` to find the ready `fd`, still dumb

  - **`epoll`**
    - `int epoll_create(int size)`
      - JDK `selector = Selector.open()`
      - size only for reference, only a recommended initial size, 
      - occupies a fd value (int), returns the fd, which belongs to the newly created `event_poll` instance.
      - have to call `epoll.close`, otherwise fd memory leaks.

    - `int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)；`
      - JDK `scoketChannel.regsiter()`
      - `epfd`, the fd of `event_poll` (created by `epoll_create`)
      - `op`, 3 enums, `EPOLL_CTL_ADD`, `EPOLL_CTL_DELL`, `EPOLL_CTL_MOD`
      - `fd`, the fd to be monitored
      - `epoll_event`, what kind of event kernel must monitor/listen to, got enums such as `EPOLLIN` (read available), `EPOLLOUT` write available.
  
    - `int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);`
      - wait for io events from `epfd`, returning max `maxevents` events.
      - JDK `selector.select()`
  
  - **What are the differences between select, poll, and epoll**
    - all of them are implementations of IO-Multiplexing
    - Max connections:
      - select -> 1024
      - poll -> linked list, no limit
      - epoll -> no limit
    - IO problems when number of FD increases:
      - select -> traversing all FDs, slow
      - poll -> same, slow
      - epoll -> implemented by `callback` function from `fd`, so only active socket would inovke `callback`, when there are not a lot of active sockets, epoll does not have the slow problem like the above, but when every socket is active, we might have a performance problem.
    - Message transfer method
      - select -> kernel need to copy message to user space, CPU copy
      - poll -> same
      - epoll -> share space between kernel and user space. 
  
  - **Epoll mechanism under the hood, why is it so powerful**
    - how does PC accepts data from network? Network NIC, DMA copy to kernel, then CPU read.
    - But how does CPU knows that data is ready? using `interrupt`
    - CPU invoke soft interrupt, then go back to working, then ksoftirqd detects soft interrupt and starts to receive packets using `poll`, then send to different protocol for porecssing (IP, TCP), and then put the packets inside user socket recv queue
    - when a process is doing `recv`, it is blocked ,and placed on the waiting queue of a socket
    - When data comes, it will be unparked and added to CPU schedule again.
    
    - The question is how do we monitor multiple sockets:
      - **select**. default implementations, add current process to all monitoring socket; every wake up requires removal of process from each monitored sockets, very costly. And still you don't know exactly who woke you up, so you need to traverse socket fd all again.
      - **epoll**
        - separation of concerns, `epoll_ctl` add all monitoed sockets into the wait-queue of `epfd` (created by `epoll_create`), then use `epoll_wait` for data
        - `epfd` corresponds to `eventpoll` object, which has its own waiting queue, and `rdlist` (ready list).
        - For every socket to monitor (registered by `epoll_ctl(ADD, fd)`), we create a node called `epitam`
        - instead of adding process to waiting queue of the monitored socket, we add `epitam` to the waiting queue of socket, AND we add `epitam` to the RB tree of `event_poll`, for easy searching and updates later
        - we add process to the waiting queue of `event_poll`
        - when socket has incoming data, `epitam` will be woken up, and added to `rdlist`
        - when ever rdlist changes, `event_poll` informs process in its waiting list, with `rdlist`, then process knows exactly which sockets are changed. Process then consumes from head of the `rdlist`, and pops from back. 
        - in `eventpoll` struct, `rdlist` is a doubly-linked list, to monitor sockets, it uses redblack tree, for ease of searching, and avoid repeated add.
        - Time Complexity for dealing with Socket that is ready : O(1)
        - O(logN) for adding epitam to rbtree
        - O(logN) for looking up epitam, this usually happens when you want to change the `interestOps` of a thread to socket, i.e. doing `epoll_ctl(MOD, fd)`

- **Additional**:
  - How many ways for inter process communications?
    - signal
    - pipe
    - shared memory
    - FIFO queue
    - Message QUEUE
    - unix domain socket (docker.sock, podman.sock)

## Netty使用和常用组件辨析
- Core Components:
  - Bootstrap: client BootStrap, and ServerBootStrap
  - Channel: just like Java NIO channel, just like a literal channel, where data can pass in or out.
  - EventLoop can be seen as a thread, EventLoopGroup can be seen as a threadpool
- Event and ChannelHandler, ChannelPipeline
  - channel pipeline holds all the channel hanlders, 
  - events travel through pipelines, getting process by one or more ChannelHandler
- EventLoop and EventLoopGroup in depth
  - async processing meaning, we can manage many connections with just a few threads
  - EventLoopGroup assigns a Eventloop to the new Channel (round robin)
  - Architecture: ![eventloopGroup](./EventLoopGroup.png)
  - Channel created -> ELG register channle to EventLoop -> Channle uses the eventloop to handle all IO events in its lifecycle
- Channel:
  - Very close to NIO socket.
  - Channel Unregistered, Channel Registered, ChannelActive, ChannelInactive
  - important channel apis, `evnetloop()`, `pipeline()`, `isActive`, `localAddress`, `remoteAddress`, `write`, `flush`, `writeAndFlush`
- ChannelPipeline and ChannelHandlerContext
  - Every Channel has its own pipeline, 
  - Every ChannelPipeline holds a linkedlist (doubly) of ChannelHandlers
  - `ChannelInboundHandler` and `ChannelOutboundHandler`, each with different bit mask
  - Important method: `addFirst`, `addBefore`, `addAfter`, `adddLast`
- ChannelHandlerContext
  - Like a Node in Linkedlist, but hold much more information
  - **Event propagations**
    - if you call `channle.write()` or `ChannelPipeline.fireChannelRead()`, they will propagate through the entire ChannelPipeline, but - if you invoke `ChannelHandlerContext.write`, it will start propagating from the current `ChannelHandlerContext` (Node)
- **ChannelHandler**
  - Main Compoennt
  - we can customize our `ChannelInboundHandler` and `ChannelOutboundHandler`
  - we can also extends `ChannelInboundHandlerAdapter` or `ChannelOutboundHandlerAdapter` to override methods we need.
  - `ChannelOutboundHandler` read method, is to send a `read()` command, i.e. "I want more data"
    - real implementation in `HeadContext` (`DefaultChannelPipeline`), bridge from pipeline -> channel implementation
    - `Unsafe.beginRead` transport-specific logic to prepare or perform the actual read from the OS. 
  - If you want FullDuplex handling of data (both inbound and outbound) use `ChannelDuplexHandler`
- Sharing Handler
  - we can share handler in multiple different Channel/ChannelPipeline. 
  - just use the `@ChannelHandler.Sharable`
  - if you use `Sharable` make sure the `ChannelHandler` is threadsafe
- Resource management (to avoid memory leak)
  - In Java NIO, we need buffer (`ByteBuffer.allocate(1024)`) to write and read data
  - Netty needs buffer too, so we need to **release buffer** to avoid memory leak.
  - In order to do that we have `TailContext` and `HeadContext`
  - Internet -> `Head/HeadContext` -> `My handlers` -> `Tail`
  - it is nice, but sometimes if we have `Inbound handler` or `outbound handler` that did not propagate events or data to the next handler, we will never get to release the buffer.
  - That is why we have a default, memory safe, implementation `SimpleChannelInbounHandle`, which has a `finally` clause to release buffer (`channelRead`)
  - **Note: 🧠 Rule of Thumb,  If your handler**
    - ✔ consumes the ByteBuf (e.g., transforms it, logs it, then discards):
      ```
        Do NOT retain.
        Just let auto-release clean up.
      ```
    - ✔ forwards the original ByteBuf:
        `YOU MUST retain().`

    - ✔ is the very last inbound handler:
      ```
        If it forward → retain.
        If it stops event → do not retain.
      ```
- **Channel Option**
  - ChannelOption.SO_BACKLOG
    - controls the max number of completed incoming connections that the OS can queueu before your server accepts them
    - Linux OS has 2 queues, SYN Queue + Accept Queue, SO_BACKLOG limits the accept queue
  - SO_REUSEADDR
    - allows binding to a port even if old sockets on that port are in
      - `TIME_WAIT`
      - `CLOSE_WAIT`
      - Other 'lingering' TCP states
      - allow server to restart quickly
  - SO_REUSEPORT: really port shraing across process, parallel accept on multi-core CPUs.
  - SO_KEEPALIVE
  - SO_LINGER, TCP_NODELAY

- **ByteBuf**
  - equavalent to NIO ByteBuffer, 
  - heapBuffer() vs driectBuffer()
    - heap buffer lives on heap, is backed by an Array, 
    - direct buffer lives in native memory (**not JVM managed memory**), via `Unsafe.allocateMemory()` or `DirectByteBuffer` via JNI:
    ```
    +--------------------------------------------+
    |  JVM Process Virtual Address Space         |
    |                                            |
    |  +--------------+                          |
    |  | Java Heap    |   (GC managed)           |
    |  +--------------+                          |
    |  +--------------+                          |
    |  | Metaspace    |   (class metadata)       |
    |  +--------------+                          |
    |  +--------------+                          |
    |  | Code Cache   |   (JIT compiled code)    |
    |  +--------------+                          |
    |                                            |
    |  +--------------+                          |
    |  | Direct ByteBuf Memory (native)  <---- not part of JVM "regions"  , but part of Java Process
    |  +--------------+                          |
    |                                            |
    +--------------------------------------------+
    ```
  - HeapBuffer takes more time to read/write, but less time to allocate
  - DirectBuffer takes less time to read/write, but more time to allocate
  - we need to release resources: `ReferenceCountUtil.release()`
    - refcount has to be zero for it to be released
    - you can use `-Dio.netty.leakDetection.level=PARANOID` or `ResourceLeakDetector.setLevel(ResourceLeakDetector.Level.PARANOID);` to detect leaks;
  - Use of ByteBuf Pool
    - DirectBuffer alloc and unalloc is very time consuming
    - so we use a pool to preallocate some **buffer** beforhand
    - Rsizing: before 4M (default threshold); after 4M, just plus 4M. 

- **Solving message coalescing, and partial packet**
  - Nagle algorithm, many packets are sent together. 
  - Data input larger than socket SND_BUFFER
  - **Ways to resolve this**
    - `LineBasedFrameDecoder`, `DelimiterBasedFrameDecoder` to handler

- `ChannelRead` vs `ChannelReadComplete`
  - Pseudocode:
  ```
    epoll says FD is readable ->
    Netty enters read loop ->
      - read some bytes
      - decode messages
      - fire channelRead() per message
    read loop ends (no more bytes available) ->
    fire channelReadComplete()

  ```
  - why does Netty separate the 2?
    - because `channelReadComplete()` is the right place to 
      - flush accumulated writes (e.g. autoread=false patterns)
      - Request next read if autoread is off
      - Batch outbound writes for performance
      ```java
            @Override
        public void channelReadComplete(ChannelHandlerContext ctx) {
            ctx.flush();
        }

      ```
- **CODEC**: used at networking level to encode/decode protocol frame; understands framing
  - encoder, decoder
  - `ByteMessageDecoder`
  - `MessageToMessageDecoder`

- **SERDES**: serialize/deserialize general objects, used at Messaging/storage(Kafka, DB logs); doesn't understand framing
  - JDK Serdes really sucks. Performance terrible
  - `Avro`, `Kryo`, `MessagePack`, `Protobuf`
  - Codec usually comes before Serdes, it extracts payload; Serdes convert payload into domain object.
  - `TCP bytes → [CODEC: framing] → payload bytes → [SerDes] → Order object`

## Netty面试难题分析
- **NIO Selector cpu 100% bug, how does Netty resolve that？**
  - Bug itself has been fixed in JDK 11+, and modern verison of linux.
  - But defensive logic is still there:
  ```Java
  // NioHandler.java --> select method
                long time = System.nanoTime();
                if (time - TimeUnit.MILLISECONDS.toNanos(timeoutMillis) >= currentTimeNanos) {
                    // timeoutMillis elapsed without anything selected.
                    selectCnt = 1;
                } else if (SELECTOR_AUTO_REBUILD_THRESHOLD > 0 &&
                        selectCnt >= SELECTOR_AUTO_REBUILD_THRESHOLD) {
                    // The code exists in an extra method to ensure the method is not too big to inline as this
                    // branch is not very likely to get hit very frequently.
                    selector = selectRebuildSelector(selectCnt);
                    selectCnt = 1;
                    break;
                }
  ```
  - `selectRebuildSelector`, not only recreates Selector, but also transfers all `SelectionKeys` from old selector to new Selector
  - Note how `selectRebuildSelector` is triggered by `selectCnt`? `selectCnt` is normally reset to 1 when the event is a normal event (Read, Write, Accept); however if `selector` is waken up with non-sense, it can grow to very large. 


  - **Note the performance optimization technique of `selectRebuildSelector`**, 
    - we want the critical path which is `select` (parent method) to be optimized by C2 compiler (inlining)
    - if we include a branch that is rarely reached in `select`, the method size might get too large to be inlined, thus 99.999% of code 
    - Why selectRebuildSelector() is not inlined:
      - Keeping the hot loop small allows the JVM to inline it fully.
      - A rare slow path inside the hot method would exceed JIT thresholds.
      - It improves:
        - CPU branch prediction
        - Instruction cache locality
        - JVM optimizations (escape analysis, loop optimizations)
        - This is intentional "**cold-path splitting**" used by all high-performance Java frameworks.

- **How do we support one million of TCP Long connections, with single machine, with Netty?**
  - From 3 perspectives, **Hardware/OS level**, **Netty/Code level**, **JVM level**
  - **Hardware level/OS level**
    - one default size of socket buffer is 4k, so we need 8k per connection (sendbuffer , receivebuff)
    - 1 mil connections * 8 k = 8G, so for ram, we need at least 16G ram to begin with.
    - At **OS** level:
      - check `ulimit -n`, which limits the number of files a process can open at a time.
      - need to set this to at least `ulimit -n 1000000` if we want to support 1M sockets opened at the same time
      - if the above operation failed, need to update the soft limit, and hard limit from `/etc/security/limits.conf`
        - `* soft nofile 1000000`
        - `* hard nofile 1000000`
      - Also need to update `/etc/pam.d/login`
        - `session required /lib/security/pam_limits.so`
      - check the system level maximum number of files that can be opened from `cat /proc/sys/fs/file-max`, if it is smaller than 1 million:
        - `vi /etc/sysctl.conf`
        - add `fs/file_max=1000000`
        - `sysctl -p`

  - **Netty** level
    - Boss EventLoopGroup + Worker Eventloop Group, Boss group focus on general new IO events (handshakes, authorizations, authentications), Worker Group focus on handling event (business logics) for individual connection; Optimize the number of threads used for EventLoopGroup.
    - Optimize the HeartBeat mechanism
      - Need to detect obsolete/idle connections, remove them if necessary to avoid OOM.
      - Use Netty's built-in `IdleStateHandler`, detects read-idle, write-idle, and readwrite-idle.
    - Reduce TCP send and recv buffer size, when msg size is not big
    - Use Netty PooledBuf to reuse ByteBuf so that we do not have to
    - Use `FlowControllChannelHandler` to do rate lmiting in `ChannelActive()`; if the rate hits a threashold, do `ctx.close()`

  - **JVM** level: GC optmizations
    - SERVER side GC is going to lead to many clients connection broken + backlog building up.
    - When Server is back from GC there might be tons of clients sending data and doing reconnection, and that might break the server.
    - So GC goal
      - Throughtput
      - latency
      - Heap occupancy
      - Principles:
        - Try to reclaim as much as possible during MINOR GC
        - Throuhgput Latency, and Heap Occupancy cannot get all, must choose between Latency and THroughput based on your business needs. 

- **What is Level Trigger, and what is Edge Triggered**

  Level-triggered (LT):
  - As long as the FD remains readable/writable, epoll_wait keeps returning the event.
  - If the application does not read all data, it will be notified again next time.
  - select() and poll() are LT.
  - epoll supports LT by default.

  Edge-triggered (ET):
  - epoll_wait notifies only when the state transitions from "not ready" → "ready".
  - If you do not fully drain the socket (read until EAGAIN), you may never get another notification.
  - ET is more efficient because it reduces repeated wakeups for the same readiness state.

  JDK NIO:
  - Java's Selector uses epoll in LT mode internally; but at API level, there is a `selected-key set` mechanism; JDK will not re add the FD until app consume the event and remove the key from selectedKeys. So it is PSEUDO ET.

  Netty Epoll:
  - Netty’s native epoll transport uses ET mode for read/write events, but includes its own logic to drain buffers to avoid missing events.


## Netty 源码
- Netty High Level architecture, boss-worker pattern
![Booss-worker](./Netty_High_level.png)

- Part I detailed flow
  ![Part I detailed flow](./Netty1-drawing.drawio.svg)
  - ServerBooStrap init Channel
  - register channel with its own boss ELG.
  - start one **Server EL** from Boss-ELG:
    - `runIO` tasks:
      - run loops on IO events, if no io events return;
      - if there is io event process it, process `SelectionKey`
      - normally at the beginning, there is no events; even if there is , it will not be handled because there is no handler yet. 
    - `runAllTask`: Execute tasks via EL from `taskQueue`
      - At the beginning, a few tasks are already in the queue. 
      - invokeHanlders -> invoke ServerBootStrap.init ->Add `ServerBootStrapAcceptor` to handle new client connections -> remove the current handler
      - bind to ip and port (use `invokeLater` to add the task `fireChannelActive` to EL)
      - fire channel active -> fire read if auto read is true

- Part II detailed flow
  ![Part II detailed flow](./Netty2-drawing.drawio.svg)
  - Client initialize `BootStrap`
  - Client send connection request to Server -> **Server EL** detects via `runIo`
    - `processSelectedKeys` -> fireChannelRead in `ServerSocketChannel`
    - `ServerBootStrapAcceptor` handles fireChannelRead -> add initializer from user code , register chanel with child ELG (workerGroup)
    - Start one **Worker EL**:
      - `runIO` tasks: initially no tasks.
      - `runAllTask`
        - Follow the same registration process above, but with less tasks in `runAllTask`: only adding child handlers
    - subsequently loop, start processing other io event like read.


## Netty实战 1

- Simple HTTP Server with TLS, all handled by Netty libs.
  - `OptionalSSLHandler`
- **Day 3**: ByteBuf 
  - Direct vs Heap
    - ByteBuf, refCount(), released when refCount() == 0
    - `readerIndex`, `writerIndex`
    - `duplicate()`, `slice()`, `retainedSlice()`, all operates on underlying `ByteBuf`
  - Pooled vs Unpooled
    - Pooled ByteBuf, maintains a pool of ByteBuf; can be reused, efficient memory allocation
    - Unpooled, always create new instance of ByteBuf
- **Day 4**: Backpressure handling / Msg coalescing , partial message
  - `ctx.read()` starts a read loop, you are telling Netty, "Please drain as much as you think is reasonable from the socket."
    - So Netty may:
      - call kernel read() multiple times
      - decode many frames
      - fire many channelRead events
      - and only then fire one channelReadComplete
  - `AUTO_READ=false` means: Netty won't read unless you call ctx.read.
  - **Never block the IO Thread, always offload slow business logic**
    - Correct Approach:
      - IO thread: decode -> enqueue -> immediately return
      - Business threads:
        - dequeue one message
        - process slowly (200ms)
        - schedule `ctx.read()` on the IO thread.
    - This gives us non-blocking IO, controlled pacing via business logic, fast ingestions of bursts
    - **risk!:** Memory ballooning, need for explicit queue bound and overflow policies.
  - Client side backepressure mechanism: `isWritable`
    - Netty tracks channel writability based on:
      - outbound Netty buffer size
      - hi/lo watermarks
      - OS send buffer occupancy
      - TCP window size from the server
      - **when server is slow:**
        - server OS receive buffer fills
        - TCP window shrinks
        - client OS send buffer fills
        - Netty outbound buffer hits high watermark
        - client sees `isWritable`= false
      - **This is wirelevel backpressure**
  - **Stateful** send loop, what goo citizen netty client looks like
    - `channelActive`: start sending while channel is writable
    - if `isWritable == false`:
      - pause sending
    - when `isWritable == true`:
      - resume sending from where you left off
    - **all done in the same event loop**, no extra threads needed.  
    - **client should obey isWritable, otherwise they will overflow the pipeline**
  - E2E backpressure chain:
  ```
    Slow business logic (server)
          ↓
    Server inbound queue grows
          ↓
    Server OS receive buffer fills
          ↓
    TCP window shrinks
          ↓
    Client OS send buffer fills
          ↓
    Netty outbound buffer hits high watermark
          ↓
    Client isWritable=false
          ↓
    Client application pauses sending
  ```

- **Day 5**: Mini Fix protocol
  - Why not use Thread.sleep in Netty handler?
    - channelActive runs on event loop thread → blocking prevents all I/O.
    - For delaying partial sends, use ctx.executor().schedule(), not sleep.
  - Where should exceptions be handled?
    - Protocol errors → handled inside decoder (emit RejMessage).
    - Unexpected runtime errors → handled by a final exception handler at pipeline tail.
    - BusinessHandler should not be the global exception sink.
  - Encoder bug: why client didn’t receive ACK?
    - Because encoder output was byte[], which Netty does not write directly.
    - Fix: encoder must output ByteBuf.
  - How partial packets (半包) and sticky packets (粘包) behave?
    - No newline yet → LineBasedFrameDecoder buffers → decoder is not called.
    - One read may contain multiple \n → LineBasedFrameDecoder emits multiple frames → decoder called multiple times.
  - Handling malformed input: throw or emit RejMessage?
    - Better: decoder emits a RejMessage instead of throwing.
    - BusinessHandler handles RejMessage and optionally sends REJ back to client.

- **Day 6**: Life Cycles
  
  - Pipeline events vs Lifecycle events
    - Pipeline events (read/write/exception) are processed inside runIo().
    - Lifecycle events (close, register, deregister, handlerRemoved) run inside runAllTasks(), because Netty schedules them onto the EventLoop.

  - Exception always happen before channel close:

    ```
    handler throws
    → exceptionCaught (synchronous, in runIo)
    → ctx.close() schedules a task
    → channelInactive (later)
    → channelUnregistered
    → handlerRemoved
    ```
  - Summary: “Netty processes I/O synchronously in runIo(), but all lifecycle transitions (close, deregister, inactive) happen asynchronously in runAllTasks() — which is why exceptionCaught always happens before the channel actually dies.”

- **Day 7**: 
  - For each order request, Gateway Order FSM:
    - Creates & updates a small OrderContext in memory (current state, timestamps, routing info…)
  - Decides what to do with each new event (NewOrder, DownstreamAck, Timeout, Cancel, etc.)
  - Ensures every path ends in a well-defined state + client response (REJECTED, ACCEPTED, TIMED_OUT, TOO_LATE_TO_CANCEL, etc.)
  - It’s not about FIX session, and not full OMS lifecycle.
  - It’s just: “what is the state of this order inside this gateway, and what should I do now?”
  - [Order Gateway Design Practice](/OrderGatewayDesign-updated.drawio.svg)

## Netty + Disruptor实战

### Day 1 takeaway: Simple Disruptor (one producer one consumer)

- Backpressure is built-in (and unavoidable)
  - Disruptor backpressure is enforced via gating sequences:
  - producer cannot overwrite slots that consumers haven’t processed
  - If any consumer is slow:
    - the ring buffer fills
    - the producer stalls (blocks/spins/yields depending on strategy)
    - Disruptor never drops events by default — it forces the system to slow down.

- Blocking work in handlers is dangerous
  - Blocking IO (JDBC, REST, etc.) inside a handler:
    - freezes that handler’s sequence
    - becomes the slowest gating sequence
    - eventually stalls the producer
  - One slow handler can halt the entire pipeline.
  - Rule: if a handler can block for “internet latency”, it does not belong on the Disruptor thread.

- “Handing off to another thread” is not cheating
  - Handoff does not increase throughput if downstream is slow.
  - Its real purpose is:
    - isolating slow stages (bulkheads)
    - making backpressure explicit
    - preventing IO latency from freezing critical coordination paths
  - The mistake is not handoff — the mistake is unbounded handoff.

- Performance lessons from your experiment
  - Printing/logging inside onEvent destroys throughput.
  - BlockingWaitStrategy is slower but CPU-friendly.
  - Ring buffer size matters (too small hurts batching).
  - JVM warmup matters.
  - With minimal handler logic: ~12 million events/sec (≈83 ms for 1M events) is healthy and expected.

### Day 2 takeaway: Mutli consumer & Backpressure

- Consumer Graph semantics:
  - `A -> B` means B is gated by A, not 'runs on the same thread'
  - Each `EventHandler` runs on its **own thread** by default
  - Ordering is enforced by sequence barrier. not thread confinement. 
  ```
  Disruptor = data-flow ordering
  Netty = thread-confinement ordering
  ```

- Fan-out vs pipeline
  - Path1: `Producer -> A -> B`
  - Path2: `Producer -> C`
  - Terminal gating sequences are B and C
  - producer cursor is constrained by `min(sequece(B), sequence(C))`

- What “backpressure” really means in Disruptor
  - Producer can burst ahead up to ~ringSize sequences.
  - Once slack is exhausted, producer blocks.
  - Slow consumers drain backlog; producer resumes when capacity frees.
  - This creates a burst → block → drain rhythm

- Producer TPS vs slow consumer TPS (the subtle but critical point)
  - Incorrect mental model: “Producer TPS must equal slowest consumer TPS”
  - Correct mental model:
    - Producer TPS is bounded by the slowest gating consumer.
  - Over long-run average, producer TPS converges toward the slowest terminal path.
  - Over short windows, TPS can be:
    - higher (during burst)
    - lower or zero (during block)
    - Equality is an asymptotic property, not a per-window guarantee.

- Lag is the truth signal
  - For any consumer X: `lagX = producerCursor - consumerXSequence`
  - Invariant: `ΔlagX = Δproducer - ΔconsumerX`
  - If producerTPS > X-TPS → lag grows
  - If producerTPS < X-TPS → lag shrinks
  - Lag hovering near ringSize = producer is capacity-limited by X

- Measuring correctly (hard-won lessons)
  - **Do**:
    - Measure **TPS from sequence deltas**, not counters
    - Snapshot sequences once per interval
    - Compute lag from the same snapshot
  - **Avoid**:
    - Per-event logging
    - “get() then set(0)” counter resets
    - Reading volatile sequences multiple times per calculation. (Too costly for CPU)
    - Interpreting drain-phase metrics as steady state

- Slow consumer simulation (important!)
  - Empty loops can be JIT-eliminated
  - volatile writes inside loops distort results (memory fences ≠ CPU work)
  - **Good slow-work pattern**:
    - Do real computation in a local variable
    - Publish result once per event

- Why producer TPS can be 0
  - Producer TPS = 0 means:
    - Ring is full
    - Producer is blocked
    - Consumers are draining
This is expected, not a bug.

**Summary**
> Disruptor throughput is governed by gating sequence
> 
> The slowest terminal consumer bounds system throughput
> 
> The ring buffer allows short-term bursts, so producer TPS may fluctuate per window, but
> 
> long-run average converges to the slowest path

**Another Takeaway**
> Netty is a system Framework.
> 
> Disruptor is a dataflow primitive.
> 
> Netty brings data in safely; Disruptor process it deterministically.


### Day 3 takeaway: Netty refresher, I/O Threading & Backpressure

- Netty backpressure is edge-triggered, not continuous
  - channelWritabilityChanged() fires only when writability flips true → false (crossed high watermark), false → true (dropped below low watermark)
  - Writing more data does not trigger more events unless a flip occurs
  - One big burst → typically two events only

- Write buffer watermarks define a hysteresis band
  - High watermark (default): 64KB
  - Low watermark (default): 32KB
  - Flip rules:
    - pendingBytes > HIGH → channel becomes unwritable
    - pendingBytes < LOW → channel becomes writable
  - This prevents flip-flopping and stabilizes throughput

- BytesBeforeUnwritable and BytesBeforeWritable are derived values
  - `BytesBeforeUnwritable` → how many more bytes can be enqueued before hitting HIGH
  - `BytesBeforeWritable` → how many bytes must drain before dropping below LOW
  - Values depend on:
    - size of last write
    - TCP socket drain timing
    - buffer expansion and alignment

- Continuous backpressure requires a write-resume loop
  - To see repeated flips:
    - write until isWritable == false
    - pause
    - resume writing when isWritable == true
    - This creates a stable producer ↔ consumer feedback loop

- ByteBuf ownership is strict (this caused the refCnt error)
  - Golden rule:
    - Once you pass a ByteBuf to ctx.write(...), you no longer own it.
  - Correct patterns:
    - Echo only → ctx.write(msg) and do NOT release
    - Observe + forward → fireChannelRead(msg) and do NOT release
    - Write + forward/store → retain() for extra ownership
    - Double-release or use-after-release leads to IllegalReferenceCountException.

- Pipeline design determines buffer lifecycle
  - Multiple inbound handlers must agree on:
    - who writes
    - who propagate
    - who releases
  - SimpleChannelInboundHandler auto-releases
  - ChannelInboundHandlerAdapter requires manual ownership discipline

- Netty backpressure ≈ Disruptor backpressure (conceptual mapping)

  | Netty                     | Disruptor                      |
  | ------------------------- | ------------------------------ |
  | ChannelOutboundBuffer     | RingBuffer                     |
  | High watermark            | Cursor catches gating sequence |
  | Low watermark             | Consumers advance              |
  | isWritable                | hasAvailableCapacity           |
  | channelWritabilityChanged | producer unblocked             |

  **fast producer slowed by slow consumer.**


### Day 4 takeawy: Netty Disruptor Handoff (core OMS pattern)

- **Cannonical OMS Gateway**
  ```
    Netty EventLoop (I/O)
    → Disruptor Ring (business pipeline)
        → Netty EventLoop (write-back)
  ```
  - EventLoop never blocks
  - Business logic never touches sockets directly
  - All writes are scheduled back onto the EventLoop

- **What backpressure really meant**
  - **Waiting strategy ≠ Backpressure Policy**
    - **WaitingStrategy**(BLOCKING, BUSYSPIN, YIELDING)
      - Consumer-side only
      - Controls how consumers wait when there is no data
      - Trades CPU for latency
      - ❌ Does NOT decide reject/block behavior
    - **Backpressure / Admission control**
      - Producer-side decision
      - Happesn when the ring buffer is full
      - implemented via:
        - `tryNext()` / `tryPublishEvent`
        - `InsufficientCapacityException`
  - 👉 Rejecting events is a producer policy, not a waiting strategy.

- **The most important bug you found (and fixed)**
  - **WRONG!!!**
  ```java
    long seq = -1;
    try {
        seq = ringBuffer.tryNext();
        ...
    } catch (...) {
        ...
    } finally {
        ringBuffer.publish(seq);   // ❌ publishes -1
    }
  ```
  - This **corrupts the ring** and causes:
    - consumer to stall
    - responses to `disappear`
    - system to silently stop progressing
  - ✅ Golden rule, only publish a sequence you successfully claimed.

- **Experiment B — Noisy neighbor behavior (expected results)**
  - Results you observed (correct):
    - Fast client:
      - Very high reject rate
      - Completes quickly (“fails fast”)
    - Slow client:
      - Much lower reject rate
      - Takes longer to complete
  - Interpretation:
    - With global admission control, whoever hits the door more often gets rejected more often.
    - This is expected physics, not unfairness.

- Why reject is better than queueing
  - Your final 100k test demonstrated the core gateway truth:
    - Rejecting:
      - Preserves latency
      - Preserves throughput
      - Makes overload visible to clients
    - Queueing:
      - Hides overload
      - Explodes latency
      - Eventually collapses the system
  - 👉 Reject early, fail fast, stay alive.

> **Note**
> * Day 4 taught me that low-latency systems are governed by admission control not raw speed.
> * Disruptor enforces backpressure; Netty enforces I/O discipline
> * Latency under load is dominated by queueing, and the correct response is fast rejection, not blocking.
---

### Day 5 Design considerations
Day 5 practices are pivoted to take into this OMS consideration:
> **Tasks are correlated into families; tasks from the same family _has to be executed by one thread_ only at any given time, in FIFO sequence**

[Day5 Code](https://github.com/JohanLi1990/buildWithJdk25)

#### **Design A**
```
                ┌─────────────────────┐
                │     Netty IO         │
                │ (event loop thread)  │
                └─────────┬───────────┘
                          │
                          │ decode → TaskEvent
                          │ extract familyKey
                          ▼
                ┌─────────────────────┐
                │   Router / Hasher   │
                │ hash(familyKey)     │
                │   & (N - 1)         │
                └───────┬─────────────┘
                        │
        ┌───────────────┼────────────────┬───────────────┐
        ▼               ▼                ▼               ▼
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ Disruptor  │   │ Disruptor  │   │ Disruptor  │   │ Disruptor  │
│ Partition0 │   │ Partition1 │   │ Partition2 │   │ Partition3 │
│ RingBuffer │   │ RingBuffer │   │ RingBuffer │   │ RingBuffer │
└─────┬──────┘   └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
      │                │                │                │
      ▼                ▼                ▼                ▼
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ Consumer   │   │ Consumer   │   │ Consumer   │   │ Consumer   │
│ Thread 0   │   │ Thread 1   │   │ Thread 2   │   │ Thread 3   │
│ (FIFO)     │   │ (FIFO)     │   │ (FIFO)     │   │ (FIFO)     │
└────────────┘   └────────────┘   └────────────┘   └────────────┘
      │                │                │                │
      ▼                ▼                ▼                ▼
   process          process          process          process
 (families         (families         (families         (families
 serialized        serialized        serialized        serialized
 per partition)    per partition)    per partition)    per partition)

```
Properties (write this next to the diagram)

✔ FIFO per family (guaranteed by routing)

✔ Excellent cache locality

✔ Very predictable latency

✘ Parallelism capped at N partitions

✘ Hot family can dominate its partition

#### **Design B**
```
                ┌─────────────────────┐
                │     Netty IO         │
                │ (event loop thread)  │
                └─────────┬───────────┘
                          │
                          │ decode → TaskEvent
                          ▼
                ┌─────────────────────┐
                │   Disruptor / Queue │   (optional but common)
                │   (bounded buffer)  │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Dispatcher /        │
                │ FamilyScheduler     │
                │                     │
                │ CHM<familyKey,      │
                │   FamilyState>      │
                └─────────┬───────────┘
                          │
          ┌───────────────┼────────────────────────┐
          │               │                        │
          ▼               ▼                        ▼
┌────────────────┐ ┌────────────────┐    ┌────────────────┐
│ Family A State │ │ Family B State │ .. │ Family X State │
│ busy flag      │ │ busy flag      │    │ busy flag      │
│ pending queue  │ │ pending queue  │    │ pending queue  │
└───────┬────────┘ └───────┬────────┘    └───────┬────────┘
        │                  │                     │
        ▼                  ▼                     ▼
┌────────────────────────────────────────────────────────── ┐
│                  Worker Thread Pool                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ Worker 1 │ │ Worker 2 │ │ Worker 3 │ │ Worker N │      │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘      │
│       │              │              │              │      │
│       ▼              ▼              ▼              ▼      │
│   process A1      process B1     process C1     process D1│
│   process A2      process B2                        ...   │
└────────────────────────────────────────────────────────── ┘
```
Properties (write this next to the diagram)
✔ FIFO per family (enforced by scheduler)

✔ Parallelism up to pool size

✔ Hot family doesn’t block other families

✘ More moving parts

✘ CHM / queue contention if not careful

✘ Higher latency variance if poorly tuned

- Comparison: **Option A has lower p99 because**
  - no CHM
  - no CAS storms
  - no cache line bouncing
  - deterministic single thread execution
- **But**
  - head-of-line blocking exists
  - large synthetic families (e.g. TBR) can poison a partition
- **Mitigations**
  - route synthetic / hot fmailies to dedicated partitions
  - keep default path simple and fast


#### Desgin C Hybrid

```
             ┌─────────────────────┐
             │       Netty IO       │
             │  (event loop thread) │
             └──────────┬───────────┘
                        │ decode → TaskEvent
                        │ extract familyKey
                        ▼
             ┌─────────────────────┐
             │   Router / Hasher   │
             │ p = hash(familyKey) │
             │     & (N - 1)       │
             └───────┬─────────────┘
                     │
 ┌───────────────────┼───────────────────┬───────────────────┐
 ▼                   ▼                   ▼                   ▼

┌────────────┐      ┌────────────┐      ┌────────────┐      ┌────────────┐
│ Disruptor  │      │ Disruptor  │      │ Disruptor  │      │ Disruptor  │
│  P0 ring   │      │  P1 ring   │      │  P2 ring   │      │  P3 ring   │
└─────┬──────┘      └─────┬──────┘      └─────┬──────┘      └─────┬──────┘
      │                   │                   │                   │
      ▼                   ▼                   ▼                   ▼
┌────────────┐      ┌────────────┐      ┌────────────┐      ┌────────────┐
│ Consumer   │      │ Consumer   │      │ Consumer   │      │ Consumer   │
│ Thread P0  │      │ Thread P1  │      │ Thread P2  │      │ Thread P3  │
│ dispatcher │      │ dispatcher │      │ dispatcher │      │ dispatcher │
└─────┬──────┘      └─────┬──────┘      └─────┬──────┘      └─────┬──────┘
      │                   │                   │                   │
      ▼                   ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ FamilyMap P0 │    │ FamilyMap P1 │    │ FamilyMap P2 │    │ FamilyMap P3 │
│ (family→state)│   │ (family→state)│   │ (family→state)│   │ (family→state)│
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼
┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│ WorkerPool P0  │  │ WorkerPool P1  │  │ WorkerPool P2  │  │ WorkerPool P3  │
│ (k threads)    │  │ (k threads)    │  │ (k threads)    │  │ (k threads)    │
└────────────────┘  └────────────────┘  └────────────────┘  └────────────────┘

```

Dedicate one partition for TBR, because they might get heavy.

*Concern about false sharing in ConcurrentHashMap bins is mostly theoretical in this design. CHM bins are pointer-based heap objects and do not cause cache-line sharing across bins. The real false-sharing risk lies in hot fields inside FamilyState (e.g. busy), but this is negligible at 10–20ms task durations. Partitioned schedulers already eliminate the dominant sharing risks. Cache-line padding should be considered only after p99 profiling proves scheduler overhead dominates.*

### Day 5 Takeaways

#### Session 2

* **Key takeaway**
  * Multilple Netty evenloop threads can publish into the same partition
    * use `ProducerType.MULTI` instead of `ProducerType.SINGLE`
  * Logging Strategy:
    * Sample logging to avoid hot-path overhead
    ```java
      if ((totalCounts & 0x3FFF) == 0) {
        log.info("published={}, rejected={}", published, rejected); 
      }
    ```
  * Routing Strategy:
    * Correlated Task: `partition = floorMode(correlationId, N)`
    * Uncorrelated Task: `partition = floorMod(System.identityHashCode(ctx.channel()), N);`

#### Session 3

- **Key Takeaway**
  - Disruptor Events must not escape the consumer thread
    - RingBugger resuses TaskEvent objects
    - Queuing them into `pending` causes data corruption.
  - **Recursive drain on completion**
    - Every dispatched task **must schedule the next one, or release busy**
    ```java
    dispatchAndDrain(state, task):
      async work
      onComplete:
        next = pending.poll()
        if next != null:
           dispatchAndDrain(state, next)
        else:
           busy = 0
           race fix:
             if new task arrived → re-acquire busy → dispatch
    ```
    - This guarantees exactly 1 in-flight task per family
    - FIFO preserved
    - no family can wedge permanently
  
  - **Lost wakeup prevention pattern**
    ```java
    onComplete():
        task = queue.poll()
        if (task != null) {
            run(task)
            return
        }
    
        flag = IDLE
    
        // ---- race fix ----
        task = queue.poll()
        if (task != null && CAS(flag, IDLE, BUSY)) {
            run(task)
        }
    ```
    - Problem Statement:
      - 2 threads coordinates via a `flag` and a `work queue`
      - The operations `check queue` and `release flag` are not atomic
    - Pattern solution:
      - After releasing the flag, recheck the queue and reclaim ownership if work exist

---

### Day 6 Benchmark takeaway

#### 1️⃣ What p50 / p95 / p99 really mean (and why you care)

- p50 (median)
  - → “Typical” request latency
  - → In your steady runs: ≈ service time (~15ms)

- p95
  - → “Bad but common” tail
  - → Often shows mild contention, scheduling jitter

- p99
  - → “System stress indicator”
  - → Tells you where latency comes from:
    - If **p99 ≈ svc** → work-bound
    - If **p99 ≫ svc and q dominates** → queueing / overload
    - If **execQ** dominates → executor / scheduling / core starvation

#### 2️⃣ How to calculate percentiles (the only way that matters)

- Collect raw latency samples (long nanos)
- Snapshot a window
- Sort
- Index:
  ```
  p50 = samples[0.50 * n]
  p95 = samples[0.95 * n]
  p99 = samples[0.99 * n]
  ```

Two important truths you verified empirically:

- Percentiles cannot be computed incrementally (averages lie)
- Sample size matters:
  - p99 is meaningless with 10 samples
  - starts becoming trustworthy with hundreds+

#### 3️⃣ Lost updates are not theoretical

- What went wrong
  ```
  int i = idx;
  ...
  idx = i + 1;

  ```

- With multiple threads:
  - two threads read the same idx
  - both write to the same slot
  - one sample silently disappears
- Why volatile did NOT save you
  - volatile → visibility
  - not atomicity
  - read–modify–write is still a race
- The fix you applied (correct)
  ```
  int i = idx.getAndIncrement() & (CAP - 1);
  ```
  And the proof:
  - Server showed 300 tasks completed
  - Recorder originally showed ~260
  - After fix → 300 recorded

That’s not an academic race — that’s production-grade data corruption.
You caught this because you trusted counters over intuition. That’s the right instinct.

#### Secondary (but important) Day 6 lessons

You also implicitly learned:

- Client behavior affects server latency
(writability, batching, scheduling matter)
  - Writing 50 msgs per second but not flushing it will not create the steady rate you expect! It will create a batch flush which essentially is a tiny burst. 
  - Solution: Delegate to `ctx.executor` to execute the write and flush asynchronously
- Executor defaults lie
  - (core=1 + bounded queue ⇒ serial system)

- Tail latency ≠ throughput problem
  - You had great throughput and bad p99 in some configs

- Fairness ≠ starvation freedom
  - Cold p99 ≈ svc + 1 slot ≠ starvation

#### 📌 Final Day 6 mental checklist (write this in your notebook)

- is p99 coming from **q**, **execQ** or **svc**
- is my **measurement correct** (no lost updates, enough samples)?
- is the system overloaded or just poorly scheduled?
- is the client accidentally creating bursts?

### Day 7, GC, Allocation, Structural protections

#### GC & Allocation
- **Per-task** allocation in hot paths is lethal to p99, even if small
- Allocation pressure manifests as svc tail latency, not just GC logs.
- GC frequency matters more than GC pause max for latency stability. 
- Always force allocation side effects(`sink`) or JIT will eliminate them.

#### Latency Measurement
- p50 lies; **p99 tells the truth**
- e2e = q + svc; you must decompose to understand tail behavior
- Sorting-based percentile snapshots are expensive and can perturb results.
- Logging tasks that throw exceptions silently stop ScheduledExecutorService unless caught.

- > **Unhandled exceptions in scheduled tasks cancel future executions silently**
  
  **There is no stack trace at ALL!!! so you need to catch and print them!!!!**

  **Correct Implementation**
  ```java
      private void schedulePartitionLogging(int partitionId) {
          // Log every 1 second
          if (partitionId != 3) return;
          statsScheduler.scheduleAtFixedRate(() -> {
              try {
                  //            partitionMetricsLogging(partitionId);
                  partitionLatencyLogging(partitionId);
              } catch (Throwable t) {
                  log.error("stat-logger task failed for partition {}", partitionId, t);
              }

          }, 5, 5, TimeUnit.SECONDS);
      }
  ```

#### Queueing & Backpressure
- Bounding memory ≠ bounding latency.
- pendingLimit=1024 bounded memory but allowed seconds of queueing.
- Correct formula: `pendingLimit ≈ latency_budget / svc_p99`
- Structural limits must be latency-driven, not arbitrary.

#### Overload Handling
- Sustained overload (not bursts) is required to test backpressure.
- Rejections must be:
  - explicit
  - cheap
  - observable (metrics)
  - Hot-family overload must not poison cold families.

#### Systems Thinking (Big Picture)
- Tail latency is a systems problem, not a single-line fix.
- GC, scheduling, executor sizing, logging, and backpressure interact.
- Low-latency engineering is about bounding worst cases, not improving averages.


### Day 7 番外篇 📓 HDRHistogram — Practical & Conceptual Notes (Low-Latency Context)

#### 1. What HDRHistogram **is** (and is not)

**HDRHistogram is:**

* A **fixed-size histogram** with logarithmic buckets
* An **online frequency distribution**
* A **bounded-error percentile estimator**
* Designed for **hot-path safety** and **low jitter**

**HDRHistogram is NOT:**

* ❌ A sorting-based percentile calculator
* ❌ A Gaussian / probabilistic estimator
* ❌ A Fenwick Tree / BIT
* ❌ A bucket sort implementation
* ❌ A raw sample store

> Key idea: **HDR never stores raw latency samples.**

---

#### 2. What happens when you record a value

When you call:

```java
histogram.recordValue(latencyNs);
```

What actually happens:

1. HDR computes a **bucket index** from the value

   * Uses bit operations (`highestSetBit`, shifts)
   * Effectively `log2(value)` + sub-bucket offset
2. HDR increments a **counter**

   ```text
   counts[bucketIndex]++
   ```
3. The original value is **discarded**

**No allocation. No sorting. No comparison. No locking (Recorder).**

> The value is **classified**, not stored.

---

#### 3. Is the value “lost”?

**Yes — the exact raw value is discarded.**
**No — the statistical information is not lost.**

What is preserved:

* Frequency
* Order of magnitude
* Rank (relative position)
* Distribution shape

What is discarded:

* Exact nanosecond precision within a bucket

This is **intentional** and **safe** for latency work.

---

#### 4. How percentiles (p95 / p99) are computed

HDR **does not interpolate** and **does not assume any distribution**.

Percentile computation is:

```text
targetRank = totalCount * percentile
cumulative = 0

for bucket in ascending order:
    cumulative += bucket.count
    if cumulative >= targetRank:
        return bucketRepresentativeValue
```

This is:

* Rank selection
* Based on **actual observed counts**
* Not curve fitting
* Not Gaussian
* Not probabilistic estimation

---

#### 5. Why HDR uses a linear scan for percentiles

HDR percentiles are computed by **scanning all buckets**.

Why this is correct:

* Bucket count is **small and fixed** (~1k–4k)
* Scan cost is **bounded and predictable**
* Cache-friendly (contiguous memory)
* Snapshot happens **infrequently**
* Recording happens **constantly**

Trade-off chosen by HDR:

* `record()` → **O(1)**
* `snapshot()` → **O(number_of_buckets)**

This asymmetry is **exactly right** for latency tracking.

---

#### 6. Why HDR is NOT a Fenwick Tree (BIT)

HDR and BIT both involve prefix sums, but:

| Aspect          | Fenwick Tree | HDRHistogram       |
| --------------- | ------------ | ------------------ |
| Update cost     | O(log N)     | **O(1)**           |
| Memory access   | Scattered    | **Contiguous**     |
| Cache behavior  | Poor         | **Excellent**      |
| Concurrency     | Hard         | **Easy (striped)** |
| Snapshot cost   | Low          | Low                |
| Hot-path safety | ❌            | **✅**              |

HDR avoids BIT intentionally because:

* Recording is on the **hot path**
* Percentile queries are **cold path**
* Cache behavior matters more than asymptotic Big-O

---

#### 7. Is HDR doing “bucket sort”?

**No — but it looks similar at a glance.**

Difference:

* **Bucket sort**:

  * Stores values in buckets
  * Sorts or concatenates them
  * Produces a fully ordered list

* **HDRHistogram**:

  * Stores **only counts**
  * Never stores or reorders values
  * Produces percentiles from frequency distribution

Correct description:

> HDRHistogram performs **bucket classification**, not bucket sorting.

---

#### 8. Accuracy model (very important)

HDR percentiles are **approximate**, but:

* Error is **bounded**
* Error is **configurable**
* Error is **relative**, not absolute

Example:

* Real p99 = 48.32 ms
* HDR p99 = 48.5 ms
* Error ≈ 0.4%

This error is:

* Much smaller than OS jitter
* Much smaller than GC noise
* Much smaller than scheduler variance

---

#### 9. Why HDR reduced OS jitter in practice

Switching from array+sort to HDR reduced jitter because:

* ❌ No allocation on snapshot
* ❌ No `Arrays.sort()` CPU bursts
* ❌ No large memory copies
* ❌ No cache eviction storms
* ❌ Fewer safepoints

HDR provides:

* Constant CPU cost
* Stable memory footprint
* Scheduler-friendly behavior
* Cache-friendly access pattern

> Instrumentation became **non-invasive**.

---

#### 10. Interval histograms vs cumulative data

Using **interval histograms** means:

* Metrics reflect **recent behavior**
* Snapshot cost stays bounded forever
* No “history bloat”
* No degradation over time

Your log means:

* p95 / p99 = **last interval**
* Not entire run
* Not misleading once understood

---

#### 11. One-sentence mental model (keep this)

> HDRHistogram maps values into logarithmic buckets at record-time, stores only frequency counts, and derives percentiles via prefix sums with bounded error — trading precision for stability and low jitter.

---

#### 12. Why this matters for low-latency systems

In low-latency systems:

* Measurement **is part of the system**
* Measurement jitter **becomes tail latency**
* Stable approximation beats exact but disruptive measurement

That’s why:

* Disruptor users use HDR
* Aeron uses HDR
* Trading systems use HDR

---

#### Final takeaway

You didn’t just “optimize logging”.

You **changed the physics** of your system:

* from bursty, allocation-heavy observation
* to constant-time, cache-friendly observation

That is *real* low-latency engineering.

If you want next, we can:

* formalize **error bounds** for your HDR config
* design **production-grade latency telemetry**
* or compare HDR vs DDSketch / t-digest

But this summary is already something most engineers never reach.

---
### Disruptor Paddings 番外篇
- **How is padding done to protect hot area from false sharing**
  - Disruptor padding is designed to reduce false sharing, which happens when:
    - different CPU cores write to different variables
    - those variables live on the same cache line
    - causing cache line invalidation (“ping-pong”) via MESI protocol
    - > False sharing is primarily a write–write (or write-heavy) problem, not a read problem.
  
  ```
      SingleProducerSequencer object in memory
  ┌──────────────────────────────────────────────────────────┐
  │  Header (mark + klass ptr)                               │
  ├──────────────────────────────────────────────────────────┤
  │  AbstractSequencer fields:                               │
  │    int bufferSize                                        │
  │    WaitStrategy waitStrategy (ref)                       │
  │    Sequence cursor (ref)                                 │
  │    Sequence[] gatingSequences (ref)                      │
  │  (these are not the ultra-hot counters typically)        │
  ├──────────────────────────────────────────────────────────┤
  │  SingleProducerSequencerPad: 56 bytes of byte padding    │
  │  (front pad)                                             │
  ├──────────────────────────────────────────────────────────┤
  │  SingleProducerSequencerFields:                          │
  │    volatile long nextValue   <-- very hot write          │
  │    long cachedValue          <-- hot read/write          │
  │    ... maybe other hot longs                             │
  ├──────────────────────────────────────────────────────────┤
  │  SingleProducerSequencer: 56 bytes of byte padding       │
  │  (tail pad)                                              │
  └──────────────────────────────────────────────────────────┘
  ```

- **HotSpot Object layout mental model**
  - Java inheritance does not create multiple objects
  - For `SingleProducerSeqeuncer`
  ```
    SingleProducerSequencer
      extends SingleProducerSequencerFields
        extends SingleProducerSequencerPad
          extends AbstractSequencer
  ```
  - Hotspot creats one contiguous object in memory
  ```
    [ object header ]
    [ AbstractSequencer fields ]
    [ SingleProducerSequencerPad (front padding) ]
    [ SingleProducerSequencerFields (hot fields) ]
    [ SingleProducerSequencer (tail padding) ]
  ```
  - Padding in superclasses and subclasses is a deliberate way to control field placement inside one object.

- **Why padding is done via class hierarchy**
  - Disruptor uses a Pad → Fields → Pad sandwich pattern:
    - *Pad (superclass): front padding
    - *Fields: hot fields only
    - concrete class: tail padding
  - Reasons:
    - keeps hot fields insulated even if new fields are added later
    - avoids accidental layout regression
    - works without JVM flags or non-portable annotations
    - historically more reliable than @Contended

- **Why nextValue and cachedValue are not padded apart**
  - In `SingleProducerSequenceFields`:
  ```java
  long nextValue;
  long cachedValue;
  ```
  - Both are
    - written by the same producer thread
    - accessed together in the hot path
  - Therefore:
    - no write-write contention across cores
    - packing them into the same cache line improves cache locality
    - padding them apart would waste cache space and hurt performance
  - Rule of thumb:
    - > same thread writes both -> do not pad
    - > different threads write -> pad or isolate

- **What padding actually protects**
  - Padding does not isolate every field.
  - It protects the hot write region as a whole from:
    - other fields in the same object that might be touched by other threads
    - cache line sharing with adjacent objects in memory (object-edge sharing)
    - Padding is placed around the hot fields, not everywhere.

- **Interpreting your JOL output (key insight)**
  - you can use openjdk.jol to print out the layout of a class in machine
  - From JOL, the Sequencer looks like:
  ```java
    com.lmax.disruptor.SingleProducerSequencer object internals:
    OFF  SZ                              TYPE DESCRIPTION                                 VALUE
    0   8                                   (object header: mark)                       N/A
    8   4                                   (object header: class)                      N/A
    12   4                               int AbstractSequencer.bufferSize                N/A
    16   4   com.lmax.disruptor.WaitStrategy AbstractSequencer.waitStrategy              N/A
    20   4       com.lmax.disruptor.Sequence AbstractSequencer.cursor                    N/A
    24   4     com.lmax.disruptor.Sequence[] AbstractSequencer.gatingSequences           N/A
    // omitted...
    87   1                              byte SingleProducerSequencer.p13                 N/A
    88   8                              long SingleProducerSequencerFields.nextValue     N/A
    96   8                              long SingleProducerSequencerFields.cachedValue   N/A
    104   1                              byte SingleProducerSequencer.p14                 N/A
    105   1                              byte SingleProducerSequencer.p15                 N/A
    106   1                              byte SingleProducerSequencer.p16                 N/A
    107   1                              byte SingleProducerSequencer.p17                 N/A
    // omitted...
    153   1                              byte SingleProducerSequencer.p75                 N/A
    154   1                              byte SingleProducerSequencer.p76                 N/A
    155   1                              byte SingleProducerSequencer.p77                 N/A
    156   4                                   (object alignment gap)                      
    Instance size: 160 bytes
    Space losses: 0 bytes internal + 4 bytes external = 4 bytes total
  ```

- **Why cursor and gatingSequences look “too close to the edge”**
  - Refer to the layout above, `cursor` and `gatingsequence` are quite close to the edge., so are they at risk of false sharing?
  - Not really because
    - these are **references** not hot counters
    - the reference slots are not frequently written
    - the hot writes occur inside the referenced `Sequence` objects
  - Therefore:
    - not false sharing problem at those offsets.
    - Disruptor does not waste padding budget on cold or mostly-immutable references.
    - > the hot field is `Sequence.value`, not `AbstractSequencer.cursor` (the reference)

- **Where cursor contention is actually handled**
  - The real shared coordination happens in:
    - `Sequence` objects (typically containing a volatile long value)
    - which are often padded or contended separately
  - So false-sharing analysis must follow object references, not just field positions.

- **Practical rules you can follow** when designing low-latency structures:
  - pad only **hot write-heavy fields**
  - pack fields written by the same thread.
  - Separate fields written by different threads.
  - Use class hierachy or `@Contended` intentionally - never cargo-cult
  - Verify assumptions with **JOL** not intuition.

- **Tooling takeaway**
  - JOL (org.openjdk.jol) is essential for low-latency work:
  - shows exact field offsets
  - lets you map fields to cache lines
  - removes guesswork from padding decisions
  - > If it’s performance-critical, measure the layout.

- **Summary**
 > padding  in disruptor is surgical not blanket
 >
 > isolate the hot write zone, keep same-thread data together and don't pay for padding where it doesn't buy anthing
 > 
 > that is why the code looks "over-engineered" until you see it through HotSpot + cache-coherences lenses.
 
 - **The naming, why is it p10..p17, p20..p27, why not p1..p56** ?
   - The names p10…p17, p20…p27, etc. are a deliberate trick to prevent the JVM from reordering or coalescing padding fields, and to make the padding visually grouped by cache-line blocks.
   - if you write p1...p56, JIT might collapse them, move them around..
   - p10..p17 , p20..p27, namings are not conventional less likely to get collpased and reordered. (so p10...p17 is one block, p20..p27 is one block)
   - Not so relevant today, we can just use `@Conteded`
   - but back in the days no `@Conteded`

# 算法与数据结构番外

*[Interesting Read on Red Black Tree](https://github.com/zarif98sjs/RedBlackTree-An-Intuitive-Approach/blob/main/README.md)*

## (Classic) Red Black Tree 

### Background
- BST is very good `Olog(N)`, but its worst case is `O(N)`, degrading to `LinkedList`, which is sad.
- So we need a perfectly self-balancing tree, to improve the **worst case** scenario.
- **Intuition 1:** Wouldn't it be easier to auto-reblance? Hence AVL trees (left height - right height <= 1)
  - However AVL trees have more rotations, which can be costly if my data increases
- **Intuition 2:** Why don't we have more than one key in node, so that, we don't rotate so much? 
  - so instead of just 2-Node (1 key, 2 child), what if we have 3-Node, 4-Node
  - less rotations, comparable look up time. 
  - During insertions, push the middle key upward.
  - Logically sound
  - But, so hard to code right? you need to maintain `2-Node` class, `3-Node` class...etc, and During lookup, you have to traverse all keys within a Node? That is so much maintenance overhead. The reason we want a better tree is to gurantee **worst case** performance. In another word, an insurance. If the cost of insurance is even higher than the worst case itself, it doesn't make sense to have!!
- **Intuition 3:** What if we can keep only the classic `2-Node` structure, but somehow use `binary encoding` to show that the child node and parent node in fact belongs to one larger (3-Node, 4-Node)
  - so if a Node is **red**, it belongs to its parent's node, and doesn't count when we calculate height, and thus achieving a loose sense of balance!!
- **Therefore the 4 properties of RBT:**
  - **Root must be black**
  - **All leaves are black**
  - **Red Children:** if a node is red, both of its children **must be black**
  - **Black Height:** Every single path from a given node to any of its descendant leaves has the same number of black nodes.

### Core logics
- Instead of remembering the logics about uncles and what not, try to imagine how would you do if it is a 3-Node, or 4-Node. 
  ```java
  void fixInsert(Node cur) {
    while(cur.parent.color == 1) {
      if (cur.parent == cur.parent.parent.left) {
        Node u = cur.parent.parent.right;
        if (u.color == 1) {
          // flip color
          u.color = 0;
          cur.parent.color = 0;
          cur.parent.parent.color = 1;
          cur = cur.parent.parent;
        } else {
          if (cur == cur.parent.right) {
            cur = cur.parent; // assign value here, so that cur always points to grandson.
            rotateLeft(cur);
          }
          // now cur is at the bottom
          cur.parent.color = 0;
          cur.parent.parent.color = 1;
          rotateRight(cur.parent.parent); // rebalance the current
        }
      } else {
        Node u = cur.parent.parent.left;
        if (u.color == 1) {
          u.color = 0;
          cur.parent.color = 0;
          cur.parent.parent.color = 1;
          cur = cur.parent.parent;
        } else {
          if (cur == cur.parent.left) {
            cur = cur.parent;
            rotateRight(cur);
          }
          cur.parent.color = 0;
          cur.parent.parent.color = 1;
          rotateLeft(cur.parent.parent);
        }
      }
      if (cur == root) break;
    }
    root.color == 0;
  }

  ```



# 并发编程

## Concurrency and Multithreading 101

- Context Switching:
  - Save (push) current process’s register values into its PCB (Process Control Block).
    - Program counter, stack pointer, general registers, etc.
  - Load (pop) the next process’s registers from its PCB into the CPU.
  - CPU resumes execution exactly from where that process left off.
  - So during context switching, the OS essentially swaps out the register state to simulate as if each process “owns” the CPU exclusively.

- Java is Born with concurrency, you can use `ThreadMXBean.dumpAllThreads(false, false)` to see all Threads
- Two ways to create threads: `Thread` & `Runnable`
- Thread states
  CPU perspective
  ```
    ┌────────────┐
    │    New     │
    └──────┬─────┘
           │ admitted
           ▼
    ┌────────────┐
    │   Ready    │◄──────────┐
    └──────┬─────┘           │
           │ dispatched      │
           ▼                 │
    ┌────────────┐     I/O wait / sleep
    │  Running   │───────────────►┌────────────┐
    └──────┬─────┘                │  Blocked   │
           │ time slice over      └──────┬─────┘
           ▼                             │ event complete
    ┌────────────┐                      │
    │ Terminated │◄─────────────────────┘
    └────────────┘

  ```

  Java perspectives
  ```
   ┌────────────┐
   │    NEW     │
   └─────┬──────┘
         │ start()
         ▼
   ┌────────────┐
   │  RUNNABLE  │◄───────────-─┐
   └─────┬──────┘              │
         │ enters synchronized │
         ▼                     │
   ┌────────────┐              │
   │  BLOCKED   │              │
   └─────┬──────┘              │
         │ gets lock           │
         ▼                     │
   ┌────────────┐              │
   │  RUNNABLE  │──────────────┘
   └─────┬──────┘
         │ sleep(), wait(), join()
         ▼
   ┌───────────────┐
   │WAITING /      │
   │TIMED_WAITING  │
   └─────┬─────────┘
         │ notify(), timeout, interrupt
         ▼
   ┌────────────┐
   │  RUNNABLE  │
   └─────┬──────┘
         │ run() finished
         ▼
   ┌────────────┐
   │TERMINATED  │
   └────────────┘

  ```

- `sleep` vs `yield`
  - `sleep` : `RUNNABLE` -> `TIMED_WAITING`, will lead to context switching, guranteed blocking.
  - `yield`: `RUNNABLE(OS_running)` -> `RUNNABLE(OS_Ready)`, no context swithcing.
  - Both mechanism requires no locks to release control of current cpu.

- Thread Priority
- `join()`: Blocked, waiting for all threads to finish

- Thread stoping mechanism: let it run naturally or interrupt, and catch interruption, no `stop()`
- Interrupting `sleep` `wait` `join`:
  - all the above methods will put the caller thread in `BLOCKED` state, 
  - interrrupting `BLOCKED` state will remove the interrtupted state. 
- Cooperative Thread Scheduling vs Preemptive Thread Scheduling
  - Java using preemptive model
- Java Thread model:
  - One Java thread == One os thread (Kernel Level Thread)
  - thread scheduling is totally up to OS scheduler
  - However after 21, there is Virtual Thread (which is User mode thread)
- Interthread Communication
  - Java `PipedOutputStream` (byte), `PipedInputStream` (byte), `PipedReader`(char), `PipedWriter`(char), replaced by `BlockingQueue`. Early java way to stream data between thread, block one thread until the other side consumes.
  - volatile (lightest weight communication meachanism)
    - Happens Before
    - MESI protocol (hard ware level)
    - load barrier and store barrier: if you want to read, you have to fetch from main memory; if you want to write, you force all cached writes to main memory.  
    - However this in reality:
      - might result in false sharing: 2 hot variables on different cores but within the same 64 bytes line -> every write causes invalidations and ping-pong (S -> I, E to M churn)
        - Prefer counters like LongAdder
      - Contention hot-spot: many cores writing the same line (constant invalidations, the line bounces between cores) 
      - **Note: why volatile and atomicLong are vulnerable**:
  
      ```java
            public class Counter {
                  private final AtomicLong count = new AtomicLong(0);

                  public void inc() {
                        count.incrementAndGet();
                  }
            }
      ```
      
    - Solution is LongAdder: using striped internal design, ecah thread will be assigned a bin (via hashing), and they only update that bin/cell. checkout `LongAdder`, `LongAccumulator` and `Striped64`


## Future & CompletableFuture 实战

- Future is API, implemtation is FutureTask.
- But Future is limited, it cannot:
  - Run multiple task in paralle.
  - Run multiple tasks in chains 
  - Combine multiple tasks
  - Handle Exceptions
  That is why we have **CompletableFuture**, it provides some sort of planning mechanism
- Completable Future APIs:
  ![CF Architect](CompletableFuture_Design.drawio.png)

## ThreadLocal详解

- Design principle: apply Immutablity to concurrency
- Used for internal variables for each thread.
- ThreadLocal vs Synchronized: Extra space for latency
- ThreadLocal used in Spring (DB connections, so that we don't have to pass connection information whenever we call DAO)
- ThreadLocal Design
  - Each Thread owns a ThreadlocalMap,
  - A ThreadLocalMap is `Map<WeakReference<ThreadLocal>, value>`
  - We use `WeakReference` here because in our **Thread logic**, we definitely have a strong reference to the same `ThreadLocal` object. So when we lose the strong reference, we want the key to be auto gc-ed
  - ThreadLocalMap is not a java 8 HashMap, it is a java 7 HashMap, It is using generic `Array` + `LinkedList` structure.
- Under what circumstances would ThreadLocal cause memory leak?
  - When we lose the strong reference in our code, we will **not likely** have any memory leak, because `ThreadLocal.expungStaleEntries` method
  - When we still has access to the strong reference, and **thread is reused**, then we have a problem.
  
  ```java
    static final ThreadLocal<byte[]> TL = new ThreadLocal<>();

    ExecutorService pool = Executors.newFixedThreadPool(4);

    for (int i = 0; i < 1_000_000; i++) {
      pool.submit(() -> {
        // Simulate request-scoped big object graph
        TL.set(new byte[2 * 1024 * 1024]); // 2 MB
        try {
          // ... do work ...
        } finally {
          // BUG: forgot TL.remove();
        }
      });
    }
  ```
- Why ThreadLocal may cause memory leak:

  *scene 1*

  ```
  [GC Roots]
    |
    └─> [Thread T]
          |
          └─> [ThreadLocalMap M]
                |
                └─> table[i] = [Entry E]
                          (key)   = WR(null)
                          (value) ⇒ [BigAppObject V]
  ```

  *scene 2*

  ```
  [GC Roots]
    |
    ├─> [Class MyService]
    |      |
    |      └─(static TL) ⇒ [ThreadLocal TL]
    |
    └─> [Thread T]
          |
          └─> [ThreadLocalMap M]
                |
                └─> table[i] = [Entry E]
                          (key)   = WR( [ThreadLocal TL] )
                          (value) ⇒ [BigAppObject V]
  ```
  **Always remember:** GC reachability != Code Reachability

- Food for thought today: why Java requires child class to call `super()`, when parent does not have a default constructor(e.g. it only has parameterized constructors)
  
  ```plain
    In Java, “object construction” means building real memory structure from top to bottom.
    Leaving anything half initialized will result in memoy error that happens often in C++. 
    So Java Designers forbid it explicitly from compile time to runtime. 
    In JS/TS, it just means wiring prototype links — no real “super memory” to initialize.
  ```
- **Extra Note:**
    - In java, there are 3 types of references
    - Strong Reference: normal day to day reference, will never be GC-ed
    - Soft Reference: will be GC-ed only if not enough memory
    - Weak Reference: will be eagerly GC-ed, once the **strong reference** of the instance is lost. 

## 深入理解CAS和Atomic原子类操作详解
- Compare and Swap General
  - Read + Modify + Write operations
  - Supported by `Unsafe` (prior java 9) and `VarHandle` ( > java 9)
  - Hardware level primitive that implements optimistic locking
- Downside:
  - CAS often works with while, if you cannot set value, while loop will increase CPU contention
  - only can gurantee **one** atomic operation
  - fails when there is **ABA** (vers.) problem, **ABA** is version of an object.
- Resolutions:
  - versioning with `AtomicStampedReference`
- High Performance Atomic Types
  - AtomicInteger
  - `AtomicReference`: 
    - Treiber Stack (lock free thread safe threads)
    - Storing immutable state snapshots
    - implment CAS on complex objects
  - `AtomicReferenceFieldUpadter<T, R>`
    - A reflection-based helper that lets you perform atomic CAS on a field inside an existing object, without wrapping it in an AtomicReference.
    - Why not just use `AtomicReference`
      - Because memory footprint and false sharing.
      - Every AtomicReference is a full-fledged object → extra heap allocation and pointer indirection.
      - But with AtomicReferenceFieldUpdater, you get zero wrapper objects — the field stays inline inside Foo.
        So frameworks like java.util.concurrent use it for millions of small nodes without overhead.
      - AtomicReference, each reference lives in its own separate object - random heap placement -> unpredicatable memory proximity.
  - `LongAdder`/ `DoubleAdder`
    - Uses `Cell[] cells` to manage hot contention (many thread writing on the same line) due to CAS
    - Cells are created only when needed as it is large.
    - Cells are resized twice if there are conten
    - Each Cell is a `Striped64` impl, annotated with `@Contended`
    - Hotspot JVM sees this annotation and automatically padd with bytes before and after the value so that it doesn't share a cache line with the next Cell object. This is done during **Java Object Layout Time**.
    - The padding is not visible in Java fields or reflection, but it is visible to the memory allocator and GC. (Don't exist in byte code), you can observe it with `JOL`.
    - in `Striped64.longAccumulate` there is constant checking for stale value `if (cells == cs)` to prevent race condition.
- **Extra thought**: what is the difference between `parkNanos(long nanos)` and `Thread.sleep(long milis)`
  - park is like the mini semaphore that each thread owns. when you park, you set bit to 1, and thread goes to waiting. If you set to 0, thread becomes runnable. After `nanos` time, thread becomes runnable
  - For `Thread.sleep` nothing wakes it up except interrupts. 
  - Both block the current thread and make it ineligible for CPU scheduling.
    - But: sleep() = dumb timer delay.
    - parkNanos() = intelligent wait with extra unpark + interrupt control.

## 并发锁机制之深入理解synchronized
- MESA-style Monitor in java: (`WaitSet`, `EntryList` + `cxq`, `owner`)
  ```php
  Thread arrives:
  if (owner == null && CAS(owner, null, me)) return; // fast path
  else {
    push me onto _cxq;    // single CAS, no owner interaction
    park();
  }

  Owner unlocks:
  if (_EntryList empty) drain some/all of _cxq -> _EntryList (possibly reversing)
    pick head from _EntryList as _succ
    unpark(_succ)

  notify(obj):
    m = obj.monitor
    if (m.owner != me) throw IllegalMonitorStateException
    t = dequeue_one(m._WaitSet)
    if (t != null) {
      enqueue_front(t, m._EntryList)   // make it a candidate successor
      // (HotSpot may also mark it so the unlock path will prefer it)
    }

  notifyAll(obj):
    m = obj.monitor
    if (m.owner != me) throw IllegalMonitorStateException
    while (!empty(m._WaitSet)) {
      t = dequeue_one(m._WaitSet)
      enqueue_front(t, m._EntryList) // HOTSPOT source code(OpenJDK’s ObjectMonitor.cpp), but in JVM we don't gurantee that the most recent waiting thread gets picked
    }
  ```
  - Use C++ ObjectMonitor, wrapped with OS platform monitor so as to use `mutex`:
  ```c++
    class ObjectMonitor {
    public:
        void*      _object;      // the associated Java object
        Thread*    _owner;       // owning JavaThread
        ObjectWaiter* _EntryList; // contenders waiting for lock
        ObjectWaiter* _WaitSet;   // wait() callers
        os::PlatformMonitor _lock; // OS-level condition/mutex primitive
        ...
    };
  ```
  the last line wraps the underlying platform mutex.
  - current thread goes into `WaitSet`, when, as the owner of the monitor, the thread calls `obj.wait(...)`
  - if you are not the owner, you go `IllegalMonitorStateException`
  - cxq serves as a buffer zone, do one cas and goes to treiber stack, so that the monitor does not have to server **Thundering Herd**
  - ![synchronized under the hood](monitor_cas_mutex.png)
  - Visulization of transition:
  ```
    Thread A: enters synchronized(obj)
      ↓  CAS mark word → thin lock → success

    Thread B: enters synchronized(obj)
      ↓  CAS fails (mark word points into A’s stack)
      ↓  Inflate to ObjectMonitor
            obj.mark = ptr(ObjectMonitor) | 10
            ObjectMonitor._owner = A
      ↓  Add B to EntryList
      ↓  park() → futex_wait()  ← OS mutex comes into play

    Thread A: exits synchronized(obj)
      ↓  If EntryList not empty → unpark(B)
      ↓  B wakes via futex_wake()
      ↓  B acquires monitor → continues
  ```

- Optimization techniques for `Synchronized` (intrinsic lock, as opposed to normal lock like Reentrant lock) in HotSpot
  - Lock Coarsening (Reduce number of ops to Lock and Unlock)
  - Lock Elimination / Elision (there is another hardware level lock elision which is chip dependent)
    - Done via Escape Analysis
    - `-XX:+EliminateLock` by default, so nothing to adjust here. 
  - CAS optimization, when thread contending for monitor, it uses CAS, so that it does not get suspended to avoid context switching. The number of times for a thread to spin during CAS, is **adaptive**
  - **Lightweight locking** and **Biased Locking** (before JDK 15)
    - We need lightweight locking because very often there is only one thread at a time accessing synchronized block. It is not worth it to use heavy weight locking with one thread. 

- How does Synchronized locks gets upgraded? **By contention**
  - biased --> light --> heavy
  - First of all where does the object store lock information (since we are doing `synchronized(object){}` all the time)
    - in Object Header --> Mark Word (`markOop.hpp`), 
      - `101` biased lock
      - `01` no lock
      - `10` heavy lock
      - `00` light lock
    - We can use JOL tool to print `ClassLayout`
    - Light lock stores MarkWord in `Thread Stack` --> `LockRecord.dhw`, then during multi-threading, try to CAS `LockRecord.dhw` back to Object header, if `dhw` is null, that means another thread has the light lock so current thread must return. If CAS fails, then contention, therefore upgrade to Heavy Lock.
  - Heavy lock can become no lock, but then it will become light lock, it will never be biased lock ever.
  
- Biased locking (deprecated after JDK 15) in depth
  - the problem is not only are synchronized blocks accessed one at a time most of the time, they are also accessed **by the same thread**. So to eliminate the unnecessary CAS (lightweight lock) in this scenario, we do Biased locking (a bit over engineering)
  - Only active after Hotspot starts for 4s. 
  - **Qn**: if we are calling `obj.hashCode()`, do we still get a biased locking by default?
    - biased lock will be revoked because hashcode will take up space for biased_locking_bit in MarkWord.
    - light lock keeps lock record in thread stack
    - heavy lock keeps it in Monitor.hpp
  - If you do `obj.notify` biased --> light
  - if you do `obj.wait`   biased --> heavy
  - Bulk Rebias and Bulk Revoke

## JUC并发同步工具类在大厂中应用实战

- What is difference between `Synchronized` and `Lock` interface:
  - Intrinsic lock (monitor lock) vs Explicit Lock (JUC, deep down used AQS and CAS)
- `Reentrantlock`: like `synchronized`, support re-entering.
  - similar to a ticket window selling ticket to a queue of buyers
  - Under the hood: linkedlist, with the head (which CAS AQS state successfully) being the owner of the lock. Next owner will be assigned to `head.next` (if fair lock), It can also be any newcomers (unfair lock) who successfully CAS-ed the AQS state.
  - `Condition`: more powerful, more flexible `wait()` and `notify()`
    - Use `Condition` to implement Producer Consumer pattern.
- `Semaphore`: allow multiple thread to access shared resources
  - internal counter
  - used for rate limiting or access to resource pool.
  - **NOTE: use release with caution!! ANY THREAD can release a semaphore**, it doesn't have to be the owner! 
- `CountDownLatch`: wait for everyone in the team to get on the bus, before starting the bus.
  - counter like `Semaphore`
  - but the counter is one time only. There is no `release` to add it back
  - That is why we have `CyclicBarrier`
- `CyclicBarrier`
  - can be reused
  - feels like a tour bus, every get on the bus -> go to a scene -> every get off -> park the bus
  - uses barrier point instead of counter like `CountDownLatch`, wait for all threads to reach barrier point, instead of counter becoming 0.
- `Exchanger`
  - For 2 threads to literally exchange data.
  - if one thread reaches `exchange()` first, it will wait for other thread.
  - use case inlcluding payment scenario. 
- `Phaser`
  - More flexible form of multi-threads coordinations
  - like a combination of `CountDownLatch` and `CyclicBarrier`
  - it can support **Dynamic Membership per phase**, very important, very powerful, `CyclicBarrier` cannot do that.
  - One `Phaser` object handles all rounds, with `CyclicBarrier` and `CountDownLatch` you will need multiple barriers. 
  - Graceful early exit with `arriveAndDeregister`
  - Global phase hooks, `onAdvance` gives a phase-wide callback to run houskeeping exactly when the last party arrives (e.g. sealing buffers, toggling read-only views, switching indices)
  - So powerful, yet easily replaced by `CompletableFuture.allOf(tasks.toArray(CompletableFuture[]::new)).join();`
  
- Supplementary, how to handle `if` during multithread scenario
  - **Guarded Suspension Pattern**: "Please wait for me to be ready"
    - this is actually how `join` and `future` is implemented
    - Relies on Java wait notify mechanism:
      - `synchronized` and `wait` + `notify` + `notifyAll`
      - ReentrantLock + Condition (await/signal/signalAll)
      - cas + park/unpark
  ```java
    public class GuardedObject<T> {
      private T obj;

      public T get() {
        synchronized(this) {
          while(obj == null) {
            try{
              this.wait();
            } catch (InterruptedException e) {
              e.printStackTrace();
            }
          }
          return obj;
        }
      }

      public void complete(T obj) {
        synchronized(this) {
          this.obj = obj;
          this.notifyAll();
        }
      }
    }
  ```
  - **Balking Pattern**: "Okay, if you don't need then forget it"
    - used in `synchronzied` lock inflation, only one thread to obtain the monitor object
    - DCL singleton instances
    ```java
      public class SingletonCalss {

        private static volatile SingeltonClass instance;

        public static SingletonClass getInstance() {
          if (instance == null) {
            synchronized(this) {
              if (instance == null) {
                init()
              }
            }
          }
        }
      }

    ```
    - Services initializations

## 深入理解AQS之独占锁ReentrantLock源码分析

- AbstractQueuedSynchronizer
  - AQS Condition is a modernized, explicit, and flexible version of Java’s intrinsic wait/notify model — same principles, better engineering. Difference is that AQS could have multiple condition queue, intrinsic lock only have one condition queue. 
  - `volatile int state`: `getState`, `setState`, `compareAndSetState`
  - Exclusive (ReentrantLock) vs Shared (Semaphore, CountDownLatch)
  - Sync Queue (CLH Queue): Deque, hold thread which failed to acquire lock
  - Condition queue: when thread `await()`, it will release lock, and will be added to Condition Queue, when others invoke `signal()`, it will put one node from condition queueu into Sync Queue, waiting to acquire lock again. 
- Re-entrant lock implemented using CAS + AQS. 
  - `FairSync` vs `NonfairSync`
    - key implementations details, `tryAcquire` (in `FairSync` and `NonfairSync`)
      - in `FairSync`, `tryAcuire` try to check `hasQueuedPredecessors()`, `NonFairSync` dont care
  - `addWaiter`(AQS): if I can CAS the `tail` in my Sync Queue, good, return; otherwise `enq` the node. `enq` is a `for(;;) loop`
  - `aquireQueued` -> `shouldParkAfterFailedAcquire`: here we park the thread.
  - `unlock` -> `tryRelease` (AQS)
- It is all based on AQS. nothing fancy.

## Semaphore, CountDownLatch and Cyclic Barrier 源码分析
- **Semaphore** (very similar to ReentrantLock)
  - `NonfairSync`: `tryAcquireShared` straight away go for CAS. 
  - `FairSync`: `tryAcquireShared` has `hasQueuedPredecessor`
  - state is number of permits
  - core logic lies in `doAcquireSharedInterruptibly` (AQS)
  - `shouldParkAfterFailedAcquire` and `parkAndCheckInterrupt`, 2 phase approach to park the thread at OS Level
  - The decision to to propagate or not lies in the `ws` variable of node in sync queue.
    - if it is `PROPAGATE` there might be threads that need unpark. so we need to check later during `doAcquireSharedInterruptibly`
  - Semaphore relaease, acquire entire flow
  ![Semaphore Flow](Semaphore_acquire.drawio.svg)

- **CountDownLatch**
  - Just like `Semaphore`, with its own `tryAcquireShared` and `tryReleaseShared`
  - when calling `await` ->  `getState() > 0`, we still have some thread not finished -> add the main thread to sync queue -> park
  - when `CountDownLatch.countDown()` -> CAS state( -1) -> `if getStat() == 0` -> `doReleaseShared` (just like Semaphore) -> main thread proceed
  
- **Cyclic Barrier**
  - `ReentrantLock` with `Condition`
  - Each round is a `generation`, `parties` is the number of threads that must invoke `await` before barrier is tripped, `barrierCommand` is the callback.
  - `CyclicBarrier.await()` 
    - `CyclicBarrier doWait()` all threads compete locks here 
    - `AbastractQueuedSynchronizer.ConditionObject.await()` 
    - `addConditionWaiter()` start to construct **Condition Queue** (as opposed to Sync Queue) 
    - `fullyRelease` release the current `ReentrantLock` so that others can access the exclusive lock and proceed to the above steps also.
    - `park` the current thread if it `isNotOnSyncQueue`
  - When the last thread execute `doWait`
    - count becomes = 0, trigger `barrierCommand`
    - start `nextGeneration`
    - condition `trip.signalAll`
    - `AQS.doSignalAll` transfer all nodes from Condition Queueu to **Sync Queue**, and set for each node, `node.predecessor.ws = -1` (ready for awake)
    - in the finally clause do `lock.unlock` so the lock can be free again.
  - When another thread detects it is actually on the SynQueue
    - begain to try to `acquireQueued`
    - if the node predecessor is head, then it is the current thread's turn, tryAcquire the thread
    - if succeed, return to `dowait` return index, and finally `lock.unlock()`, else retry in the for loop.
    - other threads in the same SyncQueue will do like wise.

## 并发容器（Map、List、Set）实战及其原理分析
- `CopyOnWriteArrayList`, `CopyOnWriteArraySet`:
  - replace Vector, SynchronizedList
  - used in More Read than Write Scenario. 
  - used in more static datas.
  - Real life application: **blacklist**
  - Reentrant Lock -> copy, moddification -> volatile -> unlock 
  - **Downside:** heavy on rams
  - **Not strongly consistent**
  - iterator is `fail-safe` here, as opposed to `fail-fast` in normal `ArrayList`
- `ConcurrentHashMap`
  - `computeIfAbsent`, `merge` is very important, it solves the `read -> modify -> write` problem with group transactions
  - Data strucutre: Hashmap + CAS & synchronized. 
  - CAS on table slot, `synchronized` on bucket head, CAS spinlock on `TreeBin.lockState`
  - During resize: CAS and synchronized on transfer control, cooperative resizing. 
  - **per bucket granularity**
  - **no longer using segment lock after jdk 1.7**
- `ConcurrentSkipListMap`
  - used in highly concurrent, support orderly and ranged query. O(logN) query 
  - need to control the height. 
- E-Commerce use cases:
  - **How do we record sales of each item, in a promotional event:**
    - HashMap not threadsafe.
    - HashTable to heavy, not performant
    - ConcurrentHashMap
  - **During the promotional event, record down what the user viewed, and how many times he/she viewed the item, and do it for ALL users**
    - Every body views **a lot of** items, so we are talking about **Lots of read, and lots of writes**
    - if we use `ConcurrentHashMap`, each key might have a lot of entries, and this might result in TreeBinfy.
    - and TreeBins (RBT) will have rebalances (rotateleft, rotateRight) during insertions, and removal, so this will leads to high contentions when doing TreeBin.lock
    - ConcurrentSkipListMap. more performant when it comes to LRLW(lot of read lots of write)
  - **How to keep a black list of users**
    - LRFW (lots of read few writes) , CopyOnWriteArrayList

---
### ConcurrentHashmap  DeepDive

#### 1. What `sizeCtl` means
  - `-1`  : table initializing
  - `<-1` : resize in progress
  - `>=0` : **resize threshold**
  
#### 2. `initTable`
  
  Initializing table and setting the resize threshold by updating `sizeCtl`.
  ```java
        /**
     * Initializes table, using the size recorded in sizeCtl.
     */
    private final Node<K,V>[] initTable() {
        Node<K,V>[] tab; int sc;
        while ((tab = table) == null || tab.length == 0) {
            if ((sc = sizeCtl) < 0)
                Thread.yield(); // lost initialization race; just spin; Still possible to cause 100% CPU because the same thread MIGHT get back the core every time and just do NOTHING here.
            else if (U.compareAndSetInt(this, SIZECTL, sc, -1)) { 
                try {
                    if ((tab = table) == null || tab.length == 0) {
                        int n = (sc > 0) ? sc : DEFAULT_CAPACITY;
                        @SuppressWarnings("unchecked")
                        Node<K,V>[] nt = (Node<K,V>[])new Node<?,?>[n];
                        table = tab = nt;
                        sc = n - (n >>> 2); // very smartly set the resize threshold here, n - 1/4 * n = 0.75n, same as HashMap
                    }
                } finally {
                    sizeCtl = sc;
                }
                break;
            }
        }
        return tab;
    }
  ```

#### 3. `helpTransfer`
```java
  /**
   * Helps transfer if a resize is in progress.
  */
  final Node<K,V>[] helpTransfer(Node<K,V>[] tab, Node<K,V> f) {
      Node<K,V>[] nextTab; int sc;
      if (tab != null && (f instanceof ForwardingNode) &&
          (nextTab = ((ForwardingNode<K,V>)f).nextTable) != null) {
          int rs = resizeStamp(tab.length) << RESIZE_STAMP_SHIFT;
          while (nextTab == nextTable && table == tab &&
                (sc = sizeCtl) < 0) {
              if (sc == rs + MAX_RESIZERS || sc == rs + 1 ||
                  transferIndex <= 0)
                  break;
              if (U.compareAndSetInt(this, SIZECTL, sc, sc + 1)) {
                  transfer(tab, nextTab);
                  break;
              }
          }
          return nextTab;
      }
      return table;
  }
```
**Purpose:** if we encounter a `ForwardingNode`, it means this bin has been moved and a resize is in progress.  
This method tries to **join the ongoing transfer** (help resize) and returns the `nextTable`.

**Key idea: `sizeCtl` encodes resize state**
  - `sizeCtl >= 0`: normal mode (threshold / init size)
  - `sizeCtl < 0`: resizing
  - high 16 bits = `resizeStamp(n)` (identity of this resize)
  - low bits = helper count/state

`resizeStamp(n) = numberOfLeadingZeros(n) | (1 << (RESIZE_STAMP_BITS - 1))`
- `n` is always a power-of-two table length
- the OR sets the top bit of the 16-bit stamp
- shifting it into the high bits makes the sign bit 1 → negative → "resize in progress"

`rs = resizeStamp(tab.length) << RESIZE_STAMP_SHIFT`

**Join protocol**
Loop while resize is still the same one:
- `nextTab == nextTable && table == tab && (sc = sizeCtl) < 0`

Stop helping if:
- reached max helpers: `sc == rs + MAX_RESIZERS`
- almost done / only one helper state: `sc == rs + 1`
- no work left: `transferIndex <= 0`

Otherwise CAS `sizeCtl` to `sc + 1` to register as a helper, then call `transfer(tab, nextTab)`.

#### 4. `putVal`

putval contains the previous two method and

**Insertion logic**
- Synchronize lock on the bin (could be a `Node` or `TreeBin`)
- if Node, insertion at the tail via O(N) (max O(8)) traversal
- if TreeBin, search for pos, and insert into the Red-Black Tree;
  - Note there is a `assert checkInvariants(r)` step
  - Since it is behind assert, it only runs when there is a 'ea' program argument

**Resize logic**

- `addCount`
  - Used the philosophy of LongAdder
  - `fullAddCount`, initialize `CounterCell`
  - `sumCount()` from all stripe: `BASECOUNT + CELLVALUES`
  - if the new size, `s >= (long)(sc = sizeCtl)` is larger than the current resizing threshold (`sizeCtl`) , start transferring; if another thread already started, help by transfer ablock.

#### 5. `transfer`

- `Node<K,V>[] nt = (Node<K,V>[])new Node<?,?>[n << 1];`, notice the type-erasure here, `Node<K, V>` at runtime is not permitted.
- `transferIndex`, and `stride` controls which block you can transfer.
- Very samrtly, just like HashMap, no rehashing is needed when transfer
  - during transfer, size * 2
  - So all Node from the old table; they either move to `ln` or `hn`
  
  - `ln` is the old index, and `hn == runbit | ln`
  
  - new index will only differ with old index by `int runBit = fh & n;`
    - imagine if hashkey == 5, and old capacity is 16
    - 21 and 5 will fall into the same index on the table
    - current index is `5 & (16 - 1) == 5`
    - new index is `5 & (32 - 1) == 5`
    - current index of 21 is `21 & (16 - 1) == 5`
    - new index of 21 is `21 & (32 - 1) == 21`
    - in new table, the diff in index between 21 and 5 is 16, which is actually `21 & 16 == 10101 & 10000 == 10000 == 16` which is the runbit, which so happen to be the size of old table; so if runbit is 1 meaning the key is 21, so 21 goes to hn; else key is 5, stay at ln 
  
  - the group that contains `lastRun`, its order **DID NOT** change; The other group, its order is **REVERSED** 
    - Because when we recreate the link, we insert in front
- When transferring `TreeBin` same logic is applied (`TreeNode` has `next` too)
  - BUT, if the `ln` or `hn` has reduced number, falling below `UNTREEIFY_THRESHOLD`, then it will be converted back to `LinkedList`
  
### Takeaway while reading ConcurrentHashMap source code.

####  What `@IntrinsicCandidate` really means?

This Java method body is a specification fallback.    
HotSpot may replace this call with a VM intrinsic that has different (usually weaker/faster) memory semantics but the same observable correctness guarantees.**

- Java body = correctness floor
- Intrinsic = performance ceiling

- Why this is necessary
  - run in interpreter
  - run on multiple CPUs
  - support debug / non-HotSpot VMs
  - preserve correctness under all modes

   **So** the JDK authors:
  - write a conservative Java implementation
  - let HotSpot substitute the real behavior when possible
  - This is intentional and documented, not a hack.

- How to read intrinsic methods safely
  when you see
  ```java
    @IntrinsicCandidate
    public final Object getReferenceAcquire(...) {
        return getReferenceVolatile(...);
    }
  ```
  Read it as
  ```
    “Semantics = acquire load
     Fallback = volatile load
     Intrinsic = architecture-specific acquire load”
  ```

- Example

| Method                       | Java body             | Actual intent         |
| ---------------------------- | --------------------- | --------------------- |
| `Unsafe.getReferenceAcquire` | delegates to volatile | acquire load          |
| `Unsafe.putReferenceRelease` | delegates to volatile | release store         |
| `Thread.onSpinWait`          | empty                 | CPU pause instruction |
| `Math.sqrt`                  | native                | hardware instruction  |


**Rule of thumb**: trust the method name + Javadoc + call site suage not the java body

---

## 阻塞队列BLOCKINGQUEUE实战及原理分析
- Implements `BlockingQueue Interface`, `put(e)` blocks when full, `take()` blocks when empty
- Used in ThreadPool, Producer-Consumer model, MQ, Caches, Cocurrent Task Execution.
- `ArrayBlockingQueue`: Bounded Queue based on Array
  - Simple, **one ReentrantLock**, two **Conditions**, both put and take compete for the same lock.  
  - uses `putIndex` and `takeIndex`
  - O(1) time for insertion and deletion
- `LinkedBlockingQueue`: Queue based on LinkedList
  - No bound, but recommend to have a bound
  - take from head, and add to tail, **two locks**, `takeLock`, `putLock`, read write separation, more efficient than `ArrayBlockingQueue`
  - Comparing with `ArrayBlockingQueue`:
    - at risk of OOME, if not bounded
    - creating new node / removing node each time, might be hard on GC. **ArrayBlockingQueue does not incur additional GC cost**
    - Higher throughput than ArrayBlocking queue because 2 locks. 
- `SynchronousQueue`:
  - Function like `Exchanger` from JUC.
  - Every put must wait for a take, and every take must wait for a put. So in the long run, this queue is of 0 capacity. 
  *Work handoff pattern*
  ```
    Producer (put)  --->   waits for consumer
    Consumer (take) <---   waits for producer
  ```
  - Used in Thread pools (`Executors.newCachedThreadPool`)
  - **Two internal modes**: Fair Mode (TransferQueue), Non-fair mode (default, TransferStack, Treiber Stack).
  - use cases: `Executors.newCachedThreadPool()`, it creates new threads based on needs, and recycle idle thread, threads that are idle for 60s will gets GC-ed.
  -  Synchronous queueu very likely will lead to `DeadLock`, use with Cautions
- `PriorityBlockingQueue`
  - `PriorityQueue`: Binary Heap, `parent = (i - 1) >>> 2`, `childLeft = i * 2 + 1; childRight = i * 2 + 2 `
  - `siftUp` during insertion,  and `siftDown` (with the last value in the array) during polling,
  - protected by Re-entrantLock 
- `DelayedQueue`
  - A structure that is PrioirtyQueue + RentrantLock + Condition
  - used leader follower patterns within the poll method to avoid `Stamping Herd` problem. One leader will wake up earlier than others. The followers saw that leader is define, will park and wait to be notified. 
- `LinkedBlockingDeque`
  - Can be inserted and removed from both ends, useful for implementing `work stealing` algorithm, which will be covered later. 
- **How to Choose**
  - Function, do we need the BlockingQueue to help us order and delay executions, (DelayQueue, PBQ)
  - Capacity (bounded? or unbounded)
  - need to resize?
  - performances

## 线程池实战及原理分析
- Why do we need ThreadPool: 
  - reduce energey consumption, use already created thread.
  - improve response time, no need to create thread
  - Manage threads, because threads are scarce resources
  - Extend fuctionalities, like cronjob, scheduled runners.
- Constructors: `ThreadPoolExecutor` vs `Executors`
  - important params: `corePoolSize`, `maximumPoolSize`, `keepAliveTime`, `workQueue`, `ThreadFactory`, `handler`
  - `Executors`, static methods to call `ThreadPoolExecutor`, use it if you know what you are doing
- Task Submission:
  - execute, submit
  - invokeAll, invokeAny
  - schedule(Runnable, delay, unit)
  - schedule(Runnable, initialDealy, period, unit)
- Shutdown Threadpool
  - `shutdownNow`: do it now, everyone stop, existing tasks interrrupted, at the same time return list of runnable that were interrupted. 
  - `shutdown`: no new tasks can come in, but existing running task can finish. 
- How to define values for key threadpool params
  - CorePoolSize: depending on number of input, time taken for a thread to finish processing those input.
  - workQueue size: corePoolSize / (unit time to process a task) * 2
  - maximumPoolSize: (Maixum spike input - workQueueSize) * (unit time to process a task)
  - keepAliveTime: no real recommendations. 
- **ThreadPool** Operations under the hood:
  - use core threads first -> enqueue the runnable -> queue is full, then grow the poolSize to maximumPoolSize -> still have new runnable tasks? DiscardPolicy. 
  - corePools -> workQueue -> maximumPoolSize -> DiscardPolicy
  - use `ctl` 3MSB for Threadpool State, 29 bit for worker count (500million)
  - 5 different states: RUNNING (-1 << 29), SHUTDOWN(0), STOP(1), TIDYING(2), TERMINATED(3)
    - Smart bit manipulation here because running is always negative, and it becomse really cheap/easy to check if a thread is running. e.g. `c & ~COUNT_MASK < 0`
  - use `addWorker` method to add Task to threadpools, and start it. 
  - **Why threadpool workerqueue has to be BLOCKINGQUEUE?**
    - because when there is no task, the current thread
      - has to be parked and wait for new tasks (default behaviour for thread from corePool)
      - has to wait for a `keepAliveTime` period before exiting.
      - so have to use BlockingQueue in this case
  - **When thread runs into exception, will it be removed from threadpool**
    - Yes, but if current numebr of threads < corePoolSize, a new thread will be created
- **ThreadPool Source Code**:
  - `execute`
  - `addWorker`: add and run worker thread in containers. 
    - Shutdown vs Stop logic:
      ```java
            if (runStateAtLeast(c, SHUTDOWN)
              && (runStateAtLeast(c, STOP)
                  || firstTask != null
                  || workQueue.isEmpty()))
              return false;
      ```
    - if the threadpool is shutdown mode, we can still process all the tasks that are already in workQueue. we don't have to interrupt them unless the threadpool is in STOP mode. 
  - `runWorker`
  - `processWorkerExit`:
    - if the thread ends abruptly, it will create a new Thread is `RUNNING` or `SHUTDOWN` 
    ```java
      int c = ctl.get();
      if (runStateLessThan(c, STOP)) {
          if (!completedAbruptly) {
              int min = allowCoreThreadTimeOut ? 0 : corePoolSize;
              if (min == 0 && ! workQueue.isEmpty())
                  min = 1;
              if (workerCountOf(c) >= min)
                  return; // replacement not needed
          }
          addWorker(null, false);
      }
    ```
  - `getTask`, wait for new tasks from BlockingQueue. When interrupted, check the state of threadpool, if it is stopped return.
- Concurrency Design Patterns(多线程分工模式)
  - Thread per message, easy but costly for a java thread ( could be more suitable for Virtual Thread/ Ko-routine, Go-routine)
  - WorkerThreads (Thread pool)
  - Producer Consumers: Decoupling
    - What happens if there is over saturation
      - if consumer process slower -> increase numebr of consumers
      - if consuemrs process more, but spikes in producers fill up the blocking queue -> increase queue size
      - if producer produces much more than consumers, but we cannot increase queue size, and we cannot increase consumers -> rate limit on producer. 
- Dynamic Thread Pool Parameters:
  - Important because we want our threadpool to handle varying demand during the day
  - put the threadpool constructor params in nacos/consul config
  - Meituan [DynamicTp](https://dynamictp.cn/)

## ForkJoinPool实战及原理分析
- MergeSort Example with ForkJoinPool
  - Create MergeTask with RecursiveAction
  - MergeSort with concurrency
- What is Fork Join Framework:
  - Divide and conquer model. Fork to divide task, join to merge tasks. 
  - **Use Case:** CPU heavy tasks. 
  - `ForkJoinPool` and `ForkJoinTask`
- `ForkJoinPool`:
  - constructor params: 
    - `int parallelism`: number of logical processors
    - `ForkJoinWorkerThreadFactory`
    - `UncaughtExceptionHandler`
    - `asyncMode`: What kind of queue, `FIFO`, `LIFO`
- `ForkJoinTask`:
  - `RecursiveAction`: Recursive Runnable , no return value
  - `RecursiveTask`: Recursive callable
  - `CountedCompleter<T>`: A custom hook when task completed. 
- **Common Pitfall:**
  - Stack Overflow + OOME becuase alot of tasks created, if the recursion runs too deep. 
  - Avoid lots of Blocking IO type of task (blocking IO), because it could lead to many blocked threads, without `MangedBlocker`. The blocked threads could do nothing but wait for IO to finish. 
- `ForkJoinPool Mechanism`
  - `WorkQueue[]` array
    - `WorkQueue`
      - `ForkJoinWorkerThread`
      - `ForkJoinTask`
- `ForkJoinWorkerThread`
  - When it is being created, it will create the `WorkQueue`, and place at odd number location in `WorkQueues[]`
  - When it starts, it will `scan` and start possibly stealing work from another thread. 
  - When it is `join()`ing, if `ForkJoinPool` discovered that its `WorkQueue` is empty or its task is completed, it will also steal tasks from other queue, and assign to the current `ForkJoinWorkerThread`
- `WorkQueue`: Deque
  - if it is external submited, i.e. via `submit`, WorkQueue will be assigned to even number on the `WorkQueues[]`
  -  if it is external submitted, it does not have its own `ForkJoinWorkerThread`
-  `Work Stealing Algorithm`
   -  Allow idle thread to steal work from the `WorkQueue` of a busy thread.
   -  By default, it will prioritize tasks from its own queue, but when its queue is empty, it will steal from other threads `WorkQueue`.
   -  ` private int scan(WorkQueue w, int prevSrc, int r)`
   -  ![DecisionFlowDiagram](./WorkStealing_ForkJoin.png)
   -  It tries very hard to preven thread being idle
-  Comparison with normal ThreadPoolExecutor
   -  WorkStealing, thread is always working
   -  Divide and Conquer
   -  Number of threads being (defualt) CPU logical processors number
   -  more suitable for huge parallel non-blocking task. 

## 深入理解并发原子性、可见性、有序性与JMM内存模型
- Summary of all concurrency bugs: Atomicity , Visibility, Ordering
- **Atomicity**: all pass or all fail
  - i++ is not atomic
  - How to gurantee? `synchronized`, `Lock`, `CAS`
  - Modify `long` on a 32 bits machine, the transaction is not atomic, unless you use volatile modifier. 
- **Visibility**: will i see the latest value of a shared variable
  - How to gurantee? `volatile`, `Unsafe.storeFence`, `synchronzied`, `lock`
  - `storeFence` is an `intrinsicCandidate`, which will be replace with machine code/cpu instruction like `mfence` (platform dependent) at runtime
    - so no JNI needed, no native calls to C/C++ libs, or OS system call, because JIT can emit machine code directly.
- **Ordering**: Compilers sometimes does reordering to improve performances. 
  - **Interesting observations**, the following code will *accidentally* trigger cache updates in thread:
  ```java
    while (flag) {
      shortwait(10000); // wait (empty cpu spins for 10 ms, using System.nanoTime to keeptrack)
    }
  ```
    - Why?
      - nanoTime() burns a lot of CPU instructions -> more memory loads/store, more pressure on L1 and L2 cache -> frequent pipeline flushes on `rdtscp`, this can cause the cache line containing `flag` to be evicted, invalidated or reloaded from L2/L3
      - Cache coherence traffic naturally happens when a thread is highly active, This increases the rate at which the core participates in MESI protocol traffic.
      - Branch mispredictions → pipeline flushes → memory reloads
      - JIT optimizations change depending on loop complexity:
        - for a trivial loop `while(flag){}`, JIT quickly pulls `flag` into a register and never reloads it -> Gurantee to spin forever
        - But if the loop contains native call(`nanoTime`), JIT cannot hoise the `flag` out
          - Must honor potential side effect of native calss
          - cannot optimize the loop into a pure spin
          - must reload memory from time to time
          - sometimes insert implicit memory barriers.
  - How to gurantee? `volatile`, `storeFence`, `synchronzied`

- **Java Memory Mode**, Java Concurrent/Multithreading Memory Model
  - handles shared states in multithreaded scenarios.
  - What does lock (`synchronized`) mean for ram:
    - when acquiring lock, JMM invalidates the current thread local cache
    - when releasing lock, JMM write local caches to main memory
  - What does `volatile` mean for ram
    - when writing to a `volatile` variable, JMM will write local cache to main memory
    - when reading from `volatile` variable, JMM will invalidates local thread cache, and reads directly from main memory
    - Based on the above definition, there are order gurantees in code. 
    - **Why in DCL we need to add `volatile` keyword to singleton instance?**
      - Because `new Singleton()` is essentailly 3 lines of code:
        - `memory=allocate(); ctorInstance(memory); instance=memory`
        - and the 2nd and 3rd instructions might get re-ordered.
        - if it gets reordered, some threads will read a partially initialized or not yet initialized `Singleton`
  - JMM memory fence startegy
    - x86 implements `memfence` for `StoreLoad` 
  - `Happens-Before`: the Java Memory Model’s visibility & ordering guarantee (**multi-thread** world)
    - “If A happens-before B, then any thread must see the effects of A before B.”
  - `As-If-Serial`: The compiler is free to reorder instructions as long as the final observable result is the same in a **single-threaded** program. This rule ignores concurrency completely.
  - `Volatile` vs `M-E-S-I`
    - `Volatile` = memory barriers = `lock`-prefixed instructions (`lock addl`, `lock xchg`, `lock cmpxchg`) , **or**, explicit fence instructions `mfence`, `sfence`.
      - JIT will choose whichever machine instruction that is cheapest during runtime.
      - **volatile write:** 
        - requires a store-store barrier beofre
        - a store-load barrier after
        - JIT often compiles volatile store as
        ```
          mov [addr], reg
          lock addl $0, [addr]    ; or mfence
        ```
        - the dummy lock addl forces the write to be visible to other cores
      - **volatile read:**
        - a load load barrier
        - a load store barrier
        - often implemented with an instruction like
        ```
          mov reg, [addr]
          lfence               ; or lock-prefixed read
        ```
        - But sometimes reading a volatile doesn't need an actual lock, because x86 already has strong TSO rules — so the JIT inserts cheaper fences depending on optimization.
    - `MESI`: **gurantees** a single consistent ownship of each cache line
      - At any time, exactly one core can have a cache line in Modified (M) or Exclusive (E) state.Other cores must obtain permission to write.
      - Eventual consistency (coherence) of caches
      - ✘ BUT MESI does **NOT** gurantee:
        - ordering of writes across different mem locations
        - visibility of timing guarnatees
        - prevention of reorderings
        - happens-before semantics
    - **Relationship:**
      - MESI(hardware) makes sure that when the JVM flushes a volatile write using a fence, other cores actually see it and don’t hold stale cache lines.>
      - The JMM ensures that the JVM inserts fences and prohibits reorderings per Java Semantics
      - so the JVM uses fences, and fences internally leverage coherence mechanisms like MESI, but volatile is **not MESI**, and MESI is not Java volatile in hardware
        - e.g. `lock` triggers MESI invalidation , because it locks a cache line, and no other core can hold the line in `S` or `E` state. 
        - e.g. `mfence` ensure all previous stores have reached a globally visible point. This means they cannot be stuck in store buffer - they must propagte through MESI to become visible.
        - `lfence` ensure loads are not reordered
        - `sfence` ensure store ordering. 
        - MESI handles coherence.
        - Fences enforce ordering.
        - The combination gives you language-level memory semantics.

## CPU缓存架构详解
- CPU caches are tiny storage space between CPU and main memory.
  - L1 Cache (smallest and fastes)
  - L2 Cache (larger and faster)
  - L3 Cache (Largest and fast)
  - each level stores data that belows one level below. 
  - Temporal Locality, if a register is being used, then it might get used again recently
  - Spatial Locality, if a register is being used, then chances are its neighbours are getting used.
- CPU multicore architecture
  ![multicore](./CPU-multicore.png)
  - CPU read -> L1 -> L2 -> L3 -> main
  - CPU wrie -> L1 --MESI--> L2 ---MESI---> L3
  - What kind of problems does this lead to?
    - Every core sees a copy of the SoT.
    - if one core's copy changes, all copies must change
    - There must be something to gurantee **coherence**
- CPU Cache coherence approach/mechanisms
  - Guranteed atomic operations
  - Bus locking, using the LOCK# signal and the LOCK instruction prefix.
  - Cache coherency protocols that ensure the atomic operations can be carried on cached data structures(cache lock);
- CPU cache coherence implementation techniques:
  - Bus snooping
    - Write-invalidate
    - Write-update
  - Coherence Protocol: MSI, **MESI**, MOSI, MOESI, MERSI, MESIF, write-once, Synapse, Berkeley, Firefly, Dragon
    - **MESI**: Modify, Exclusive, Shared, Invalid
      - represents 4 states for the cache line
    - False Sharing: when multiple thread from different cores are modifying **different** variables on the same cache line, there will be frequent **Invalid**, cache misses. Threads have to frequently fetch latest values from main memory, thus affecting performances.
      - `ArrayBlockingQueue` has 3 members, `takeIndex`, `putIndex`, `count`; you modify one, you invalid all 3 members. 
      - `Cache Line` size: 64 bytes
      - How to avoid ?
        - padding with random variables: 
        ```java
        class Pointer {
            volatile long x;
            //避免伪共享： 缓存行填充
            long p1, p2, p3, p4, p5, p6, p7;
            volatile long y;
        }

        ```
        - use `@sun.misc.Contended` from java 8
        - use `ThreadLocal`,

- High performance queue `Disruptor`
  - **Pain point**:
    - JUC blocking queue, uses ReentrantLock
    - In high performance system, to ensure producers do not produce too quick, only Bounded Blocking queue is chosen.
    - And locking affects performance greatly!
    - Bounded queue also uses array, but updating array in a multithreaded environment will lead to false sharing!

  - Reference: [Github LMAX disruptor](https://github.com/LMAX-Exchange/disruptor)

  - Approach:
    - RingBuffer, of size 2^n, use bit shifting to move to place ,index is long type. 
    - Lockless design; Each producer and consumer will **apply** position to operate in the RingBuffer, read/write directly from that position, whole process use atomic variable CAS to gurantee thread safety.
    - use padding lines to resolve false sharing.
    - use event driven producer/consumer patterns.

  - **RingBuffer**
    ![RingBuffer](./ringBuffer.png)
    - Array, index = sequence & (entries.length - 1)
    - What if all positions are filled, 0th position will be overwritten.
    - Will there be data loss?
      - No worries, there is `WaitStrategy`

  - **WaitStrategy**
    - `BlockingWaitStrategy`, LOCKING , limited CPU resources, and cases where latency and throughput not important
    - `BusySpingWait`,CAS , always retry, reduces context switching, recommended for cases when thread are binded to one particule core.
    - `YieldingWaitStrategy`, CAS + yield + CAS, balancing resource scarcity and performance.
  
  - **How does Disruptor avoid false sharing in its ring buffer?**
    - ❌ You cannot analyze Disruptor like a normal multi-producer queue.
    - ✔ Disruptor enforces serialization of writes on the ring buffer slots.
    - ✔ This serialization prevents two producers from writing **adjacent** array elements at the same time.
    - ✔ Thus: NO false sharing on the ring buffer itself.
    - ✔ All false-sharing-sensitive fields (sequences) are padded

  - **Practical**: `TODO`

## 并发编程面试总结
- [Why do we need to do `thread.start`, why not just directly do `run`](https://www.processon.com/view/link/5f02ed9e6376891e81fec8d5
)
  - note how JVM needs to call native method `start0`, put the new thread in wait, and bind java thread to the os thread, and then wake up the new thread to perform `run`.

- How to gracefully stop a thread:
  - let it run to completions
  - if it is in sleep, try to interrupt

- Why ThreadLocal might lead to memory leak:
  - Always remember: `GC Root -> Thread -> ThreadLocalMap -> Entry<WeakReference<ThreadLocal>, Value>` as mental model
  - so if you forgot to do `TL.remove()`, the value will be with the thread forever (even though you may not be able to reference it in code)
  - Refer to [ThreadLocal mechanism](#threadlocal详解)

- can volatile gurantee atomicity?
  - for single ops. it can. Some single ops are not single at all. Like writing to a long(64bit) in a 32bit system. 

- Under High concurrency, should we use `AtomicLong` or `LongAdder`
  - `AtomicLong` uses CAS to update, cpu contentions
  - `LongAdder` uses padded bins to collect updates, and then add together, reduces contentions 

- When `synchronized` lightweight lock becomes invalid, does it straight away lead to thread suspension?
  - Not really, it tries to get monitor right via CAS; if it cannot get monitor, then it becomes suspended.

- Under high concurrency, which is faster, CAS or Synchronized:
  - actually it depends, if read more than wright, CAS; else heavy write, use synchronized. 

- why `wait` need to be inside `while` loop?
  - need one more chance to decide whether to park the thread or not. 
  - if someone calls `notifyAll`, then your thread wrongfully proceeds

- `Synchronized` vs `ReentrantLock`: 
  - performance wise actually `synchronized` 
  - BUT `reentrantlock` has more function, conditions, fair lock, tryLock.

- Why HashMap is not thread safe
  - prior Java 7, array + linkedlist, inserting at head lead to infinite loop.
  - after Java 8, inserting at the end, no infinite loop. But put is still unsafe. 
    - no gurantee what will happen when two threads write to the same key, no volatile to gurantee happens before
    - no locking when hash collide.
    - no locking when doing resize, people may see a half old half new, weird map.
  - use ConcurrentHashMap.

- Talk about Copy-On-Write
  - highly performant read, no locks, eventually consistency.
  - when writing, copy the whole thing
  - if the list is huge, then your write is not performant.
  - [Copy-On-Write](https://www.yuque.com/u12222632/as5rgl/gautl3k31haap9p4?singleDoc#), dlmc

- 10000 QPS at a 500ms API, how do you decide on the `corePoolSize`, `maxPoolSize`, number of machine?
  - `maxPoolSize = num_cpu_core * ( 1 + IO_time / CPU_time)`
  - [system design](https://www.yuque.com/u12222632/as5rgl/dao0xb1m57t5swom?singleDoc#), dlmc

- When threadpool is full, what discard policy should we do?
  - Custome Discard policy -> send all events to MQ

- How to design a highly performant queue.
  - bounded queue
  - how to reduce contentions by using sequence (volatile), and how to reduce false sharing on heavily contended object, such as the sequence in this case.
  - reactor pattern. 


## Key Takeawys, AQS Design philosopy (lock free until it is absolutely unavoidable):
- *Establish the wake-up contract before sleeping*, like what we did in `shouldParkAfterFailedAcquire`
- *Non-blocking discipline: never block unless absolutely necessary*, for every loop, try CAS to see if you are lucky
  - **Design Discipline**: Optimistic retry before park.
- *CAS + volatile state as synchronization contract*
  - Every state change is a small handshake in a lock-free protocol. 
  - When a thread sets pred.waitStatus = SIGNAL, it’s effectively saying: “I am now depending on your release path to wake me.” 
  - That’s a **happens-before** contract. It replaces explicit condition variables with atomic state transitions.
  - **Design discipline**: Represent synchronization intentions as explicit atomic states.
- *Composability over direct blocking primitives*
  - Universal application of "set flag → retry → park if still needed" for every locks
- *deterministic safety (no missed wake-ups, no corruption) + opportunistic liveness (try again before blocking).*
- Doug Lea, is really smart

---
# Spring源码专题

## Spring核心原理整体脉络

### How is a Bean created:

- Create BeanDefinitionMap:
    - Find the directory of `AppConfig.class`;
    - Scan all Java class, if there si `@Component`, `@Service`, then Spring take the class down in a `Map<String, Class>`
    - key of the aforementioned Map will normally be className, with first letter decapitalized, unless otherwise specified in the annotation.
  - Create a Bean instance via Constructor Inference.
  - Find the members with `@Autowired`; Use spring to assign them values (Dependency injection)
  - If the class implements `BeanNameAware`, `BranClassLoaderAware` or `BeanFactoryAware` Interface; if yes, then Spring has to trigger `setBeanName()`、`setBeanClassLoader()`、`setBeanFactory()` respetively. (Aware callback)
  - Is there a method with `@PostConstruct`, if yes, then Spring will invoke the method.
  - Is the class implementing `InitializingBean` interface; if yes, that means Spring has to invoke the `afterPropertiesSet()` method
  - Last but not least, Does the class need AOP? if no, then finish, if yes, then Spring needs to construct a `Proxy` for the actuall instance. The proxy will be bean. (`BeanPostProcessor.beforeXXX`, `BeanPostProcessor.afterXXX`) 
  
  After the bean is constructed, it will be store inside a `Map<String, Object>`; key is the beanName, value is Bean. Next `getBean` call will get you the correct Bean

### Constructor Inference
- If only on constructor, then select that
- else if there is a constructor with no params, select that
- else select the constructor with `@Autowired.`

### AOP Big picture
- Does my bean need AOP?
  - Find all Aspect Bean.
  - For each method in Aspect Bean, is there `@Before`, `@After`
    - if yes, does the `Pointcut` match the current class of Bean.
      - if yes -> proceed with Proxy creation
- AOP with cglib (3rd party)
  - e.g. UserServiceProxy **extends** UserService
  - rewrite the Parent method, and inject UserService as a target (delegate)
  - when calling Bean(UserServiceProxy).test()
    - First execute the Aspect Logic (`@Before` e.g.)
    - then call `target.test()`
  - Drawbacks, UserService cannot be `final`!

- AOP with JDKProxy (JDK default)
  - implements the Interface of `UserService`
  - use reflection to invoke the method at runtime. 

CGLib generates 3 files, JDKProxy only 1 -> JDK wins at runtime
CGLib doesn't use reflection, JDKProxy uses reflection -> CGLIB slightly win , **BUT** JDK has optimized reflection under the hood. 
Overall JDK wins! Use JDK whenever necessary.

**When will AOP not work?**
- Nested calls within the same class ----> can choose to Autowire itself, works, but not graceful
- set `exposeProxy=True`, get the proxy via `AopCurrentContext`

### Spring Transactions. 

Follow the same initialization process as AOP 

**When will transaction not works**
- `Transactional` only handles `RuntimeException` by default ---> specify `@Transactional(rollbackfor = XXXException.class)`
- Nested method class ---->AOP ways to resolve it
- Multithreaded transaction ----> Transaction propagation fails from parent thread to child thread.
  - a child thread has a new `ThreadLocal<Resource>`
  - when child transaction fails, only child `ThreadLocal<Resource>` is rolledback, 
  - Parent execution is not affected. 
  - **Solution** ----> use 2pc, 3pc, SAGA (distributed transaction) **OR** programmatic transactions. (`TransactionSynchronizationManager.bindResource(dataSource, connectionHandler)`) 
  [Hack for Transaction Propagtion problem in Spring](https://www.yuque.com/geren-t8lyq/ncgl94/bpkuxseeixw3gs06?singleDoc#)

  ![Spring Overall Architecture](./1.Spring源码VIP第八期流程图.png)

## Spring手写核心源码

- Handwritten Config Scan, and how BeanDefinitionMap is created
- Handwritten `scan`
- Handwritten `registerBeanPostProcessor`
- Handwritten `preInstantiateSingleton` ---> `getBean`
- Simulates AOP with `AutoProxyCreatorBeanPostProcessord`

[Xushu Spring framework](https://gitee.com/lichenyang_b8d1/xushu-springframwrok/tree/main/src/main/java/com/xushu)
```java
    public XushuApplicationContext(Class<AppConfig> appConfigClass) throws Exception {
        // 读取配置类(配置解析成beandefinition)
        this.configClass=appConfigClass;
        // 解析配置类的扫描包
        scan(configClass);

        // 注册beanPostProcessor
        registryBeanPostProcessor();

        // 一个个创建单例bean
        preInstantiateSingletons();
    }

```

## Spring手写循环依赖
- Problem: many beans has circular dependencies.
  - Reason: when DI, bean is not fully initialized, no way out from circular depenedencies. 
- How do we resolve this ?
  - Three layers of caches.
    - **first layer： singletonObjects**: Complete, initialized beans
    - **second layer：earlySingletonObjects**: Incomplete, earlier beans.
    - **Third layer: singletonFactories**: A Map, that provide creation logic for the proxy of the bean if there is AOP involved. 
      - It is used if two classes have circular dependencies, **and**
      - one or two of the classes also requires AOP.  
  - Actually one layer of cache is enough: we just need to a way out from the circular dependency. We can have one layer cahce when a bean is first constructed.
- What is drawback of using one layer of cache?
  - two threads race condition
  - if 2 threads calls `getBean`, 
    - one thread process and add to layer one;
    - the other calls `getBean` and got a uninitialized bean, all attirbutes are null.
    - this will be problematic, and the bean returned is not usable
  - How to solve this?
    - `synchronized getBean()` ---> low performance, lock too coarse
    - use singleton design pattern ---> DCL
    - However DCL is still too coarse, that is why we need **2nd layer cache**
    - together (DCL + 2nd layer) improve performance, provide another way out.
- **The goal is to make sure**
  - 2 threads that call `getBean(A)` will both get **The complete, initialized bean!**
  - if there is a circular depency e.g. `A.b <---> B.a`, we allo `a` or `b` to be partially initialized to exit circular dependency. 

- Why do we need `singletonFactories`, the 3rd layer?
  - For circular dependices, when we resolve classes, we need to bring forward the `AOP phase` to after bean construction, before bean initialization; This way, `getBean` will return the proxy object, instead of the actual bean object.
  - However, this is an exception only for `circular dependency`; for regular beans, `AOP` should still happen after class initialization.
  - So we need `singletonFactories`: we store the logics for creating AOP in `singleton factories`
    - if another thread calls `getBean` and find that the `bean` is in `singletonFactories` ---> circular dependency ---> create bean with AOP ---> stores Bean in `earlySingletonObjects` ---> return the Bean;
    - if another thread calls `getBean`, this time the 2nd level cache can return the Bean
    - so we retrieve the AOP logic from `singletonFactories` and do AOP early;
    - otherwise, no bean in `earlySingletonObjects` --> no circular dependency ---> retrieve from `singletonObjects` ---> Do AOP after initialization ---> return Bean. 
  - **In effect**, 3rd level `singletonFactories` also becomes the way out of circular dependencies
  ```java
    // 获取单例bean
    private Object getSingleton(String beanName) {
        if(singletonObjects.containsKey(beanName)){
            return  singletonObjects.get(beanName);
        }

        synchronized (singletonObjects) {
            // 出口   二级缓存有=当前是循环依赖
            if (earlySingletonObjects.containsKey(beanName)) {

                return earlySingletonObjects.get(beanName);
            }
            // 出口   二级缓存有=当前是循环依赖
            if (factoriesObjects.containsKey(beanName)) {

                ObjectFactory objectFactory = factoriesObjects.get(beanName);
                Object aopBean = objectFactory.getObject();
                earlySingletonObjects.put(beanName,aopBean); // put inisde early singletonObjects
                factoriesObjects.remove(beanName);
                return aopBean;
            }
        }
        return null;
    }
  ```

- **Cirucular dependencies in constructor with params are not resolved by spring framework by default!!**
  - if you don't have no-args constructor, Spring will throw errors.
  - One work around: use `@Lazy`, cglib will help create proxy for the moment.
  
- **Circular dependencies for prototype bean has no resolutions!!!**
  - prototype bean has no caches, 
  - without caches, how to resolve circular dependencies??? no way

## Spring IOC-加载bean定义源码详解

- Prerequisite, Spring 6 compile
- **IOC** main components:
  ![Bean creation](./BeanCreation.png)
- `ConfiguraitonClassPostProcessors`
- `@Import`: import beans, importSelectors, or ImportBeanDefinitionRegistrar
- Difference between adding Configuration and not adding Configuration: the creation and use of CGLIB

## Spring IOC-bean的生命周期源码详解
- Spring source code in depth on bean creations
- singltonObjects, earlySingletonObject, singletonFactories in practice
- Why we do not do `synchornized` on earlySingletonObject?
  - Deadlocks.
  - They removed it but it will result in many threads getting incomplete beans.
  - but one could argue that you should not have circular dependency in the first place

- **`@Aysnc`** will result in inconsistency in circular dependencies scenario: `BeanCurrentlyInCreationException`
  - add `@Lazy`

- **Async Bean Creation**
  - `@Bean(bootstrap = Bean.Bootstrap.BACKGROUND)`
  ```java
    @Bean
    public Executor bootstrapExecutor(){
        return  Executors.newCachedThreadPool();
    }
  ```
  - > org.springframework.beans.factory.support.DefaultListableBeanFactory#preInstantiateSingleton

- **BeanPostProcessor — What It Is, What Problem It Solves**
  - In **Spring Framework**, a `BeanPostProcessor` (BPP) is:
    - > **A hook that allows you to intercept and modify every Spring bean
    - > *after instantiation* but *before it is used*.**
  
    - Concretely:
      -  Spring creates a bean instance
      -  Spring calls:
         -  `postProcessBeforeInitialization`
         -  `postProcessAfterInitialization`
    - You may:
      - return the same bean
      - or return a *wrapped / proxied* bean

    - Once returned, **that object becomes the bean used everywhere**.

  - **What problem does it solve?**
    - In large systems (OMS, gateways, infra-heavy apps):
      - You want **system-wide guarantees**
      - You do **not** want to rely on:
        - developer discipline
        - copy-paste boilerplate
        - “remember to do X”

      - Examples of guarantees:
        * latency limits
        * threading model
        * proxying / interception
        * startup validation
        * mandatory instrumentation

      - > **BPP solves the problem of enforcing non-negotiable infrastructure rules automatically.**

  - **What BPP is *not* for (important)**

    - You were right to be skeptical.
    - ❌ Not for:
      * business logic
      * order validation
      * trading rules
      * domain behavior
      * per-method logging for readability
    - If reading a class no longer explains its behavior → **bad BPP usage**.

  - **What kind of problems it *is* good at (OMS-grade examples)**
    - **Enforcing latency budgets**
      ```
      Problem:

      * “Every risk / routing / booking component must respect SLA”

      Solution:

      * Annotate beans (`@LatencyCritical`)
      * BPP wraps them with timing + fail-fast logic

      Result:

      * No boilerplate
      * No forgetting
      * Centralized enforcement

      This is **structural**, not business logic.
      ```
    
    - **Enforcing threading / execution model**
      ```
      Problem:

      * Some OMS components must:

        * run on one thread
        * preserve order
        * avoid accidental parallelism

      Solution:

      * BPP wraps beans so method calls are dispatched to:

        * a dedicated executor
        * event loop
        * Disruptor later

      Result:

      * Developers cannot violate threading guarantees accidentally.
      ```

    - **Fail-fast wiring validation at startup**
      ```
      Problem:

      * Low-latency components must not depend on:

        * blocking clients
        * transactions
        * slow infrastructure

      Solution:

      * BPP inspects beans at startup
      * Throws exception → application refuses to start

      Result:

      * Fail early
      * Fail loud
      * Production safety
      ```
  
  - **How Spring knows your BPP exists**
    This was your key question.

    > **A BeanPostProcessor is just a normal Spring bean.**

    Spring applies *no magic discovery*.

    You must register it via:

    * `@Component` **or**
    * `@Bean` in `@Configuration` (preferred for infra)

    Once registered:

    * Spring instantiates BPPs **early**
    * Registers them internally
    * Applies them to **all subsequent beans**


  - **Why ordering & dependencies matter**

    Because BPPs are created early:

    * Avoid heavy dependencies
    * Avoid accidental circular wiring
    * Prefer:

      * constructor injection
      * lazy lookup
      * minimal dependencies

    This is why infra BPPs are usually:

    * simple
    * deterministic
    * explicit


  - **How Spring itself uses BeanPostProcessor**

    This is not an exotic feature.

    Spring core features implemented as BPPs:

    * `@Autowired`
    * `@PostConstruct`
    * AOP proxies
    * `@Async`
    * `@EventListener`

    Your OMS BPPs are doing **the same thing**, just with narrower scope.

  - Final one-liner

    > **BeanPostProcessor is an infrastructure enforcement mechanism,
    > not a business abstraction.**


## Spring AOC 底层源码解析

- **Advisors are sorted using**: `PriorityOrdered`, `Order`, `@Order`
  - Not in `JdkDynamicProxy.java`
  - Ordering happens before invocation, when Spring builds the interceptor chain: `AdvisedSupport`, `DefaultAdvisorChainFactory`

- **Core Design Patterns**
  - *Chain of Responsibilty* (primary pattern)
    - Each `MethodInterceptor` is a handler
    - the request flows through the chain
    - `invocation.proceed()` passes control to the next interceptor
    - Key class `ReflectiveMethodInvocation`
  
  - *Decorator*
    - Interceptors wrap the invocation
    - Code before `proceed()` = `before advice`
    - Code after `proceed()` = `after advice`
    - Explains why:
      - befor runs in order
      - after runs in reverse order.

  - *Proxy*
    - Entry point of AOP
    - `JdkDynamicAopProxy` / `CglibAopProxy`  
    - Captures method calls and triggers the interceptor chain.

  - *Adapter*
    - Different advice types unified as `MethodInterceptor`
    - Handled via `AdvisorAdapterRegistry`
  
- **Final Mental model**: 
  > Spring AOP = proxy + Chain of Responsibility + Decorator. 
  > 
  > The same model appears in
  > * Netty pipelines
  > * Servlet filters
  > * gRPC / OkHttp interceptors 

- **Source code**:
  ```
    JdkDynamicProxy.invoke -> ReflectiveMethodInvocation.proceed ->
    
    // where the chain is assembled
    AdvisedSupport.getInterceptorsAndDynamicInterceptionAdvice
    DefaultAdvisorChainFactory
    
    // how different adivce types become interceptors
    AdvisorAdapterRegistry
    
    // where @Aspect is turned into Advisors
    AnnotationAwareAspectJAutoProxyCreator

    Read in this order — do not jump randomly:
    JdkDynamicAopProxy.invoke()
    ReflectiveMethodInvocation.proceed() ← most important
    AdvisedSupport.getInterceptorsAndDynamicInterceptionAdvice()
    DefaultAdvisorChainFactory
    MethodInterceptor implementations
    AnnotationAwareAspectJAutoProxyCreator
    This mirrors actual runtime flow.
  ```

## Spring 声明式事务底层源码

> Spring Txn = AOP + Threadlocal + PlatformTransactionManager

### 事务解析
- Just like AOP (there is advice and point cut)
- `ProxyTransactionManagementConfiguration`:
  - register `TransactionInterceptor`
  - register `BeanFactoryTransactionAttributeSourceAdvisor`
- `AnnotationTransactionAttributeSource`
  - parse `@Transactional`

### 事务解析创建代理 (Bean initiliazation)
- Search for `Advisor`:
  - `AbstractAutoProxyCreator.findAdvisorBeans`
- Proxy creation:
  - `AbstractAutoProxyCreator.postProcessAfterInitilization`

### 事务调用 (core)
- `JdkDynamicAopProxy.invoke` 
- `TransactionAspectSupport.invokeWithinTransaction`

### Transaction begin
- `PlatformTransactionManager.getTransaction`
- `DataSrouceTransactionManager.doBegin`
- `TransactionSynchronizationManager.bindResource`

### Business logic
- `invocation.proceed`

### Transction submission
- `PlatformTransactionManager.commit`
- `DataSourceTransactionManager.doCommit`

### 事务回滚 
- `TransactionAttribute.rollbackOn`
- `PlatformTransactionManager.rollback`

### **Most important breakpoints & SUMMARY**
- > `TransactionAspectSupport.invokeWithTransaction`
- > `DataSourceTransactionManager.doBegin`
- > `TransactionSynchronizationManager.bindResource`
- > Spring Tx uses AOP to intercept method boundaries
- > binds a database connection to current thread via Threadlocal
- > delegate commit or rollback decision to a PlatformTransactionManager

----
## Spring事件监听使用和原理源码
- 3 componensts:
  - ApplicationEvent
  - ApplicationEventListenr
  - ApplicationEventMulticaster
- How everything is hooked together
  - `AbstractApplicationContext.refresh`
  - `initApplicationEventMulticaster`
  - `registerlisteners` + `finishBeanFactoryInitialization`
  - `EventListenerMethodProcessor.afterSingletonsInstantiated`
- When there is event
  - `AbstractApplicationContext.publish`
  - `ApplicationEventMulticast.multicastevent`
- Key philosophy: **Observer Pattern** or **Pub-Sub Pattern**
  - **Publisher**: `ApplicationEventPublisher.publishEvent`
  - **Subscriber**: `@EventListener` or implements `ApplicationListener`
  - **Broker**: `ApplicationEventMulticaster`
  ```java
    @Configuration
    @ComponentScan
    public class MainConfig {

      /*往SimpleApplicationEventMulticaster设置taskExecutor则为异步事件
        或者使用@Async*/
        @Bean(name = "applicationEventMulticaster")
        public ApplicationEventMulticaster simpleApplicationEventMulticaster() {
            SimpleApplicationEventMulticaster eventMulticaster
                    = new SimpleApplicationEventMulticaster();


            //eventMulticaster.setTaskExecutor(Executors.newCachedThreadPool());
            return eventMulticaster;
        }
    }
  ```

## Spring IOC container extension point

![Extension points picture](./ExtensionPoints_Spring_Container.png)

- Extension Point during `BeanDefinition` registration processs
  - `BeanFactoryPostProcessor`
  - `BeanDefinitionRegistryPostProcessor`
    - `ConfigurationClassPostProcessor` (`@Component`, `@Bean`, `@Import`)
    - `@Import`
      - `ImportSelector`
      - **`ImportBeanDefinitionRegistrar`**: have to use with `@Import`
        - It is not a bean it doesn't obey bean life-cycle, 
        - but it has one advantage: `AnnotationMetadata`, it can retrieve annotations belonging to the classes that you are `@import`-ing.

- Extension Point during `Bean` creation phase
![BeanPostProcessors](./BeanPostProcessor.png)
  - **Aware** api
    - During instantiation it is very hard to use `@Autowired` to inject beans, because DI only comes later in the instantiation phase.
    - That is why classes use `Aware` to get Spring components. (e.g. `Environment`, `EmbeddedValueResolver`)
  
    ![Aware](./Aware.png)

  - Bean lifecycle call back:
    - `PostConstruct`,  or `InitializingBean`
    - `Predestroy`, or `DisposableBean`
    - `InitializingBean` is bean-level initialization lifecycle extension point, executed after dependency injection and before the bean is exposed for use.
      - Per bean
      - invoke `afterPropertiesSet()`
      - It has similar usage to `PostConstruct`, which is often preferred due to (JSR-250, less coupled to Spring)
      - Use when
        - you are writing framework-level code
        - you need ordering gurantees
        - you want explicit Spring lifecycle coupling

- Extension point after Bean instantiation (Mature state)
  - `SmartInitializingSingleton`:
    - Do something to a group of beans, instead of doing something to one bean.
    - invoked `afterSingletonsInstantiated`
    - Can be used together with other interfaces such as `Aware` to make it more powerful:
    ```java
      @Component
      public class MySmartInitializingSingleton implements SmartInitializingSingleton, ApplicationContextAware {

        ApplicationContext applicationContext;
        @Override
        public void afterSingletonsInstantiated() {
          //  applicationContext.getBeansOfType()
          System.out.println("所有bean创建完后调用.. 需要进行解析bean");
        }

        @Override
        public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
          applicationContext=applicationContext;
        }
      }
    ```
  - `SmartLifycycle`
    - contains trigger point `start`, `stop`, `isRunning`
    - called when the `AbastractApplicationContext` has `start`ed, `stop`ped...
  
  - `ContextRefreshedEvent`, event listener

- **Use extension point to recreate meituan dynamic-tp**
  - `ThreadPool` parameters:
    - `corePoolSize`
    - `maximumPoolSize`
    - `keepAliveTime`
    - `TimeUnit`
    - `workQueue`
    - `handler`
  
  - **How do we define ThreadPools from configuration yaml files?**
    - create `DtpProperties` class
    - Use `@ConfigurationProperties`
    - OR **EnvironmentAware**, this allows us to inject properties **earlier** in the bean defintion phase.
  
  - **How do we dynamically update ThreadPools parameters**
    - via `@controllers`
    - we also need to store it in a registry `DtpRegistry` for easy management later? but at which extension? `BeanPostProcessor`
    ```java
      public class DtpBeanPostProcessor implements BeanPostProcessor {
          private DefaultListableBeanFactory beanFactory;

          @Override
          public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
              if (bean instanceof DtpThreadPoolExecutor) {
                  //直接纳入管理
                  DtpRegistry.registry(beanName, (ThreadPoolExecutor) bean);
              }
              return bean;
          }
      }
    ```
    - `DtpRegsitry.refresh()`

  - Or another way is to use `ApplicationEvent` 
    - extension via `ApplicationEventPublisherAware` to get SpringApplicationEventPublisher.
    - `@EventListener(DtpEvent.class)` 
  
  - **How do we implement a monitoring function ?**
    - `DtpMonitor implements SmartLifyCycle`
    - Use scheduler to constantly check ThreadPool to check the number of threads in the threadpool, if it reaches a alarm threashold, it will send SMS or email.
  
  - **How to package our lib for other people to use**
    - `@EnableDynamicThreadPool`
    - Then use `ImportSelector`
    ```java
      @Target(ElementType.TYPE)
      @Retention(RetentionPolicy.RUNTIME)
      @Import(DtpImportSelector.class)
      public @interface EnableDynamicThreadPool {
      }

      public class DtpImportSelector implements DeferredImportSelector {
          @Override
          public String[] selectImports(AnnotationMetadata importingClassMetadata) {
              return new String[]{
                      DtpImportBeanDefinitionRegistrar.class.getName(),
                      DtpBeanPostProcessor.class.getName(),
                      DtpMonitor.class.getName()
              };
          }
      }

    ```

## Spring之整合Mybatis底层源码解析

[Mind map](https://www.processon.com/view/link/5f153429e401fd2e0deefd01)

### How do we create bean for `@Mapper`?
- Why do we need to create Bean for `@Mapper` ?
- we want user to define the **interface** such as `OrderService`, `UserService`, as well as the method such as `findAll`, `findById`; the ORM will take care of the internal implementation / mapping to SQL.
- **BUT** Spring does not support `@Component` on `Interface`.
- So we need to leverage `FactoryBean`

### FactoryBean
- A delegation / indirection mechanism by Spring to create a Bean *dynamically*
- `Bean name → FactoryBean → actual object`
- so effectively
  ```java
  @Autowired
  UserRepository repo;
      // equals
  factoryBean.getObject()
  ```
- In reality, the FactoryBean creates a proxy
  ```java
  // the actual Bean!!
  Proxy.newProxyInstance(
      UserRepository.class.getClassLoader(),
      new Class[]{UserRepository.class},
      invocationHandler
  );

  // Mybatis:
    SqlSession session = ...
    return session.getMapper(OrderMapper.class);
  ```
- Now the question is how do we  *wire* the FactoryBean into the framework? Such that no matter how many `@Repository` or `@Mapper` are there, we can create proxy Bean for all those Interfaces.
- What do we want? 
  - when scanning those interfaces marked with `@Mapper` or `@Repository`, we want to automatically create `FactoryBean` for them in `BeanDefinitionMap`, 
  - later on when during the actual Bean creations, the framwork will call getBean, which will return the actual Bean. 
  - **How do we do that ?**
     -  During Class Path scanning, we need to implement our own scanning logic to include the `@Mapper` or `@Repository`

### `MybatisMapperScan` extends `ClassPathBeanDefinitionScanner`
- Override `doScan`, for all scanned beanDefintion, create `MyBatisFactoryBean`
- override `isCandidateComponent` to only include `@Mapper` with interface.
- To include the customized scanner, we need to
  - use `@Import`
  - for `MybatisBeanDefinitionRegistrar`
  ```java
  @Retention(RetentionPolicy.RUNTIME)
  @Target(ElementType.TYPE)
  @Import(MybatisImportBeanDefinitionRegistrar.class)
  public @interface MapperScan {
      String value() default "";
  }


  @ComponentScan("com.spring.demo.component")
  @Configuration
  @MapperScan("com.spring.demo.mybatis")
  public class ApplicationConfig {

    // !! very imporant, 
    // exeuction is actually done by this guy 
    // the frameork is just responsible
    // for automatically booting up beans that 
    // later might need SqlSession from this factory
    @Bean
    public SqlSessionFactory sqlSessionFactory() throws IOException {
        InputStream inputStream = Resources.getResourceAsStream("mybatis.xml");
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
        return sqlSessionFactory;
    }

  }
  ```
### Question: what happened if you invoke `findOrderService` from one of the interface?
```
// Spring Data
Method
 → QueryMethod
 → QueryLookupStrategy
 → JpaQuery
 → EntityManager
 → Hibernate
 → SQL


// MyBatis
Method
 → MapperMethod
 → MappedStatement
 → SqlSession
 → Executor
 → JDBC

```
Under the hood is the same:
> Proxy -> Invocation Handler -> Method Metadata -> Execution Pattern
```
Interface
   ↓
Proxy
   ↓
InvocationHandler
   ↓
Method metadata
   ↓
Execution pattern
   ↓
External system (DB / network / cache)

// MyBatis
// JDK Proxy → MapperProxy → SQL execution

```

> Actually not just `MyBatis`, but also other ORM frameworks, such as `Spring Data` or `Hibernate` they follow the same **PATTERN**

### Final Note on Mybatis

#### Mybatis is not a ORM. it is a SQL -> Object mapper
- MyBatis map rows to POJOS.
- JPA/Hibernate map databses state to managed object graphs.
- Runtime Model
  ```
    SQL
    → JDBC ResultSet
    → Column values
    → Mapping rules
    → New POJO(s)
    → return
  ```
  Characteristics:
  - Every query execution creates new objects
  - No persistence context
  - No identity guarantee
  - No lifecycle tracking
  - No dirty checking
  - No automatic flushing
  
  Result mapping, not object-relational mapping

#### What JPA / Hibernate add on top

- JPA introduces a persistence context (Unit of work)
  - Identity map ( one java object per DB row per context)
  - Entity Lifecycle states (managed / detached/ removed)
  - Dirty checking
  - Cascades
  - Lazy loading
  - Relationship Management
  
  Runtime  model:
  ```
    SQL
    → Entity
    → Managed
    → Tracked
    → Flushed
    → Cached
  ```

#### Why Mybatis becomes painful with complex domains

As domain complexity grows (many 1-to-many relationships):
You must manually handle:

- Join explosion
- Object graph assembly
- Parent row deduplication
- Collection population
- N+1 avoidance
- Update ordering
- Transactional consistency
- Example pain point:
  - One Order with many OrderLines
  - SQL returns duplicated Order rows
  - You must group and merge manually

MyBatis makes domain complexity explicit — it does not hide it.

#### Why JPA feels easier for rich domains

JPA hides complexity inside the framework:
- Relationship navigation
- Cascades
- Lazy proxies
- Automatic joins
- Dirty tracking
- Result:
  - Cleaner business code
  - Rich domain models
  - Less boilerplate

But this convenience has a cost.

#### The hidden cost of JPA (important)

ORM complexity is not free:
- Unpredictable SQL
- Accidental N+1 queries
- Automatic flushes at unexpected times
- Memory overhead (snapshots, proxies)
- GC pressure
- Latency spikes (especially p99)

- This is why ORMs are risky in:
  - low-latency systems
  - trading / OMS / EMS
  - write-heavy hot paths

#### Summary

> JPA reduces application complexity by increasing framework complexity.
MyBatis reduces framework complexity by increasing application complexity.

---
## Spring AOT提前优化

- **Ahead of time compilations**
> `Code -> Native` vs `Code -> Byte Code -> Native`

- **GraalVM**
![Graal](./GraalVM.png)


- **SpringBoot AOT**
![SpringBoot-AOT](./springboot-aot.png)
> `mvn -Pnative native:compile`

- Key mental model:
  - > Native image = AOT-compiled code + a smaller Java runtime + managed heap.
  - No JIT compilation at runtime
  - still a runtime
  - still GC + GC threads
  - Still "background runtime threads" , but fewer/different than Hotspot.

- GraalVM limitations
when compiling binary executables, **mostly** must be known at build time.
  - **Reflection and dynamic access**
    - anything that relies on
      - `Class.forname`
      - `Method.invoke`
      - `Field.setAccessible(true)`
    - Why? 
      - Native image does closed-world analysis
      - only classes / methods reachable at build time are included.
      - Refelction breaks reachability analysis unless explicitly declared
    - Mitigations
      - declare reflection metadata, method/constructor access, field access
  - **Dynamic proxies & bytecode generation**
    - cglib, bytebuddy, asm all broke
    - **JDKProxy** still works.
    - because there is no classloader in the traditional JVM sense at runtime.
  - **Classloading & resource scanning**
    - No classpath, classes are compiled into the binary
  - **JNI, UNSAFE, and low-level JVM tricks**
    - partially supported
    - No hotspot intrinsics
    - No JIT-based escape analysis
    - No JVM -level biased locking tricks
    - Disruptor sytle unsafe hacks are gone.
  - **Garbage Collection limitations (important!)**
    - Graal runtime GC, 
      - no G1, ZGC, Shenandoah
      - limited GC algorithms
      - GC pause are still real, less mature than HotSpot G1/ZGC
  - **Failure moves to runtime**

### Mitagation techniques
- RuntimHints
  - ReflectionHints
  - ResourceHints
  - SerializationHints
  - ProxyHints
  - ReflectionHints
- `@RegisterReflectionForBinding`
  - Basically import all methods metada to `reflect-config.json`

- Use RuntimeHintsRegistrar (fine grained control)
  - Useful for importing 3rd party libraries metadata

- `@Reflective` on specific method (fine grained control)  

### Spring AOT under the hood

Spring AOT pre-built everything that `BeanDefinition` needs at runtime, 
Steps:
- > using `spring-boot-maven-plugin`, `ProcessAotMojo.execute()` method
- `SpringApplicationAotProcessor.process()`
- `ContextAotProcessor.doProcess()`
- `performAotProcessing()`
- `generator.processAheadOfTime(applicationContext, generationContext)`
- `ApplicationContextAotGenerator.processAheadOfTime()`
- `applicationContext.refreshForAotProcessing(generationContext.getRuntimeHints()`

just create `BeanDefinition`, no real beans.
When creating native images, all hints contribute to code gene

---
## SpringMVC无XML启动流程和请求流程

Back in the day, we used to write `web.xml` like this
```
<!--spring 基于web应用的启动-->
<listener>
  <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
<!--全局参数：spring配置文件-->
<context-param>
  <param-name>contextConfigLocation</param-name>
  <param-value>classpath:spring-core.xml</param-value>
</context-param>
<!--前端调度器servlet-->
<servlet>
  <servlet-name>dispatcherServlet</servlet-name>
  <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
  <!--设置配置文件的路径-->
  <init-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>classpath:spring-mvc.xml</param-value>
  </init-param>
  <!--设置启动即加载-->
  <load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
  <servlet-name>dispatcherServlet</servlet-name>
  <url-pattern>/</url-pattern>
</servlet-mapping>
```
**But why? and how does it work?**
**with Servlet 3.0, we don't need this anymore.**

- using **SPI(Service Provider Interface)** to hook spring with Tomcat
  - `ServletContainerInitializer` is looked up via the jar serivces api
  - The framework providing an implementation of the `ServletContainerInitializer` MUST bundle in the `META-INF/services` directory of the jar file a file called `javax.servlet.ServletContainerInitializer`, as per the jar services API, that points to the implmentation class of the `ServletContainerInitializer`
  - then use `java.util.ServiceLoader.load`

- **How does Spring MVC implements SPI?**
  - Tomcat sees calls `DispatchServelt#init()` via the Servlet
  ```
    Tomcat startup
      |
      |-- scans JARs for META-INF/services/...ServletContainerInitializer   (SPI)
      |
      |-- loads org.springframework.web.SpringServletContainerInitializer
      |
      |-- finds WebApplicationInitializer classes (via @HandlesTypes)
      |
      |-- calls WebApplicationInitializer#onStartup(ServletContext)
              |
              |-- servletContext.addServlet("dispatcher", new DispatcherServlet(...))
              |-- mapping "/", loadOnStartup, etc.
  ```
  - Tomcat invokes `DispatchServlet#init()` -> `FrameworkServlet#initWebApplicationContext()`, set parent container (not needed anymore in Spring boot, it was a legacy feature because back in the days you can choose to use Spring MVC or Struts framework, but now it is only Spring MVC.)
  
  - `configureAndRefreshWebApplicationContext(cwac)` -> register a `ContextRefreshedEvent`
  - when `IOC` container finishes creating all the beans, `FrameworkServlet.this.onApplicationEvent(event)` -> `initStrategies(context)` -> hook up all our controllers and their request mappings.

  - Take all the `ReqeustMappingHandlerMapping`, `RequestmappingHandlerAdapter`, `HandlerExceptionResolver` beans, and put them into dispatcherServlet.
  
  - Where does `ReqeustMappingHandlerMapping`, `RequestmappingHandlerAdapter`, `HandlerExceptionResolver` beans come from?
    - We used `@EnableWebMvc` -> `@Import(DelegatingWebMvcConfiguration.class)`
    ![mvc](./webMVC.png)
    - Samething applies to Spring Boot.
  
  - How does SpringMVC work under the hood?
    ![mvc](./SpringMVCProcess.png)
    - checkout `DisaptchServlet#doDispatch()`
  
  - How does @RequestMapping works under th hood.
    - Request Mapping is parsed at startup, converted into a mapping table, and at runtime Spring does **only** fast method lookups + method invocation
    ```
      startup ───────────────► mapping built
      request ───────────────► mapping lookup
      invoke ────────────────► argument resolution
      return ────────────────► response handling
    ```
    
    - **During Startup**
      - Spring finds all `@controller` beans
      - For each controller:
        - reflectively scans methods
        - looks for `@RequestMapping`
      - Each method is converted and added to  `Map<RequestMappingInfo, HandlerMethod
        - `RequestMappingInfo` = path + HTTP method + params + headers + consumes + produces
        - `HandlerMethod` = bean instance + Method + metadata
    
    - **Runtime**, when requests comes in
      - `DispatchServlet` -> HandlerMapping (RequestMappingHandlerMapping) -> find matching `RequestMappingInfo`
      - iterates mappings, apply predicate checks, 
        - path match
        - HTTP method
        - headers
        - content type
      - picks bets match --> HandlerMethod
    
    - **Invocation**: arguments resolved 
      - get Handler Adapter `RequestMappingHandlerAdapter`
      - reolves paramters via pluggable resolves:
  
        | Parameter            | Resolver                             |
        | -------------------- | ------------------------------------ |
        | `@PathVariable`      | PathVariableMethodArgumentResolver   |
        | `@RequestParam`      | RequestParamMethodArgumentResolver   |
        | `@RequestBody`       | RequestResponseBodyMethodProcessor   |
        | `HttpServletRequest` | ServletRequestMethodArgumentResolver |

      - then `method.invoke(controllerBean, resolvedArgs)`

    - **Return value handling**
      - Return value goes through
      
        | Return type      | Handler                            |
        | ---------------- | ---------------------------------- |
        | `String`         | ViewNameMethodReturnValueHandler   |
        | `@ResponseBody`  | RequestResponseBodyMethodProcessor |
        | `ResponseEntity` | HttpEntityMethodProcessor          |

      - Then  -> message convertes (`HttpMessageConverter`)
      - response written.
    
    - Internal data structure
      ```
      RequestMappingHandlerMapping
      └─ MappingRegistry
          ├─ Map<RequestMappingInfo, HandlerMethod>
          ├─ Map<String, List<RequestMappingInfo>>  (path index)
          └─ Map<HandlerMethod, CorsConfig>

      ```

## SpringMVC子父容器启动流程
- `ContextLoadListener` is the parentBeanfactory, which is in charge of core business components such as, `@Services`, `@Repository`, `@Datasource`, `@TransactionManager`, (`Spring` context)
- `DispatchServlet` is the child/non-root beanfactory which is in charge of `@Controller`s (`Spring-MVC` context)
- When child container whats to autowire beans from parent container, it will find from its own container; if it is not there, it will search parent contiainer (`AbstractBeanFactory#doGetBean`)

- **As of Spring Boot 2/3**, we don't really nee this separation of context , the defualt is a commonly single context. But you can create parent/child explicitly (and frameworks like Spring Cloud) may introduce additional parent contexts in some setups. 

- We cannot let parent container (`spring`) manage all the beans, because `spring-mvc` only search for its own container for `HandlerMethods` during intialization; without `HandlerMethods` it cannot do mappings. 


## MyBatis解析全局配置文件

### what is the differenece between JPA and Hibernate?
- JPA is a specification (API + rules)
- Hibernate is an implementation of that specification (plus a lot more)

  ```
  Your code
    |
    |  (interfaces, annotations, contracts)
    v
  JPA  ───────────►  Specification (javax/jakarta.persistence)
    |
    |  (actual working code)
    v
  Hibernate  ─────►  Concrete ORM engine

  ```

  in modern Spring APP:
  ```
    @Entity
    class Order { ... }

    @PersistenceContext
    EntityManager em;

  ```

  but at runtime
  ```
  EntityManager → HibernateEntityManager
  ```

### What is the role of Spring-ORM?
- Hibernate = ORM engine
- Spring-ORM = adapter layer that lets Spring manage ORM engines correctly.
  ```
  Your business code
    |
  Spring @Transactional / @Repository
    |
  Spring ORM  ←←← THIS LAYER
    |
  JPA / Hibernate APIs
    |
  Hibernate ORM engine
    |
  JDBC
    |
  Database

  ```
- It handles Transaction integration
  - Spring-ORM provides `JpaTransactionManger`, `HibernateTransactionManager`
  - it makes sure, for code like:
    ```
    @Transactional
    public void placeOrder() {
        orderRepo.save(order);
    }
    ```
    - Same **EntityManager/Session** is bound to the thread
    - Same **JDBC Connection** is resused
    - Commit / rollback happens correctly
    - Lazy loading works inside transaction
    - ORM flush happens at the right time.

- It handles Resource Lifecycle management (EntityManger Session)
- handles Exception Translation
- JPA bootstrap & wiring

### why Spring-ORM exists?
Before Spring-ORM:
Hibernate had its own transaction model, JTA had another, JDBC had another, mixing them was painful.
So spring them unified all of this under: `@Transactional`
```
Hibernate:
- ORM engine
- SQL generation
- Entity state management

Spring-ORM:
- Transaction coordination
- Session / EntityManager lifecycle
- Exception translation
- Integration glue with Spring Core
```

### How does a MyBatis Mapper work:
```
Your Service Code
 |
 |  calls
 v
UserMapper.findById(42)
 |
 |  (dynamic proxy)
 v
MyBatis Mapper Proxy
 |
 |  lookup statementId:
 |  "com.foo.UserMapper.findById"
 |
 v
UserMapper.xml
 |
 |  <select id="findById">
 |     SELECT * FROM user WHERE id = #{id}
 |  </select>
 |
 v
JDBC
 |
 v
Database
 |
 v
ResultSet
 |
 v
RowMapper / ResultMap
 |
 v
User POJO
```

### Why do we need MyBatis, what is wrong with just JDBC?
- Create DB connection every time, affect performance; should use a DB connection pool.
- SQL hardcoded; no separation between SQL and JAVA code; hard to maintain
- ResultSet mapping hardcoded.

### MyBatis Parsing Configuration
![parsing MyBatis](./MyBatisParsing.png)

- MyBatis Dynamic Sql Source
  - in MyBatis you can dynamically define SQL with XML Node.
    ```xml
      <select id="findUsers" resultType="User">
        SELECT id, user_name, user_creattime
        FROM user
        WHERE 1 = 1
        <if test="userName != null">
          AND user_name = #{userName}
        </if>
        <if test="startTime != null">
          AND user_creattime >= #{startTime}
        </if>
      </select>
    ```
  - At Runtime

    | Parameters passed  | Final SQL                               |
    | ------------------ | --------------------------------------- |
    | `{userName}` only  | `... WHERE 1=1 AND user_name = ?`       |
    | `{startTime}` only | `... WHERE 1=1 AND user_creattime >= ?` |
    | both               | both conditions                         |
    | neither            | no conditions                           |


---
## MyBatis源码—SQL操作执行流程源码深度剖析

All CRUD can be performed once user gets the `sqlSession`

- `openSession` process
  - Executors
    - CacheExecutor (look into secondary cache)
    - Executor (Simple, Reuse, Batch), only primary cache used
- `getMapper`
  - `MapperProxyFactory<T>`
  - `MapperProxy<T>#invoke`
  - `doQuery`
  - `query`

## Java Reflection, Class Loading & Spring IOC - Key Insights Summary

### 3 Distinct layers you must never mix up

```
[String]  ──▶  [Class<?>]  ──▶  [Object instance]
 class name     JVM type        runtime object
```

Spring deliberately moves from left to right lazily.

### What the ClassLoader actually does (and does NOT do)

- ✅ What it does
  - Given a fully-qualified class name, locate `com/xushu/Car.class`
  - Read bytes from classpath / jar
  - Define the class in JVM (create internal Klass)
  - Return a `Class<?>`
- ❌ What it does NOT do
  - Scan packages
  - **Read annotations**
  - **Decide what is a Spring Bean**
  - Load classes eagerly
- **ClassLoader is passive. Spring is active**

### How Spring finds `@Component` classes

- from anonotation  `@ComponentScan("com.xushu")`
- Spring converts package -> resource path: `classpath*:com/xushu/**/*.class`
- Spring **scans raw `.class` files using ASM**
- Spring detects `@Component`
- Spring registers a `BeanDefinition` with 
  ```
  beanClassName = "com.xushu.iocbeanlifecycle.Car"
  ```
- 🚨 No class loading happens here

### Where Spring actaully mutates `beanClass`

During Bean Creation:
```
refresh()
 └─ finishBeanFactoryInitialization
     └─ preInstantiateSingletons
         └─ createBean
             └─ doCreateBean
                 └─ createBeanInstance
                     └─ resolveBeanClass
                         └─ Class.forName(...)
```
At this momement
```
"com.xushu.Car"
↓
Class<?> Car
```
is cached back into the BeanDefinition

### What `Class.forName()` really is 

**Class loading, NOT reflection**

| Operation                   | Category      |
| --------------------------- | ------------- |
| `Class.forName(...)`        | Class loading |
| `clazz.getMethods()`        | Reflection    |
| `constructor.newInstance()` | Reflection    |

Reflection requires the class to already exist in the JVM.

### Why `Class.forName` ≠ `new Car()`

| Aspect             | `Class.forName()` | `new Car()` |
| ------------------ | ----------------- | ----------- |
| Loads class        | ✅                 | ✅           |
| Initializes class  | Optional          | Always      |
| Creates instance   | ❌                 | ✅           |
| Compile-time known | ❌                 | ✅           |
| Used by frameworks | ✅                 | ❌           |

`Class.forName` makes the type exist
`new Car()` makes the object exist.

> In a way, `Class.forName` sets up reflection later.

### Why Spring must avoid eager loading
- Eager loading causes:
  - static initializers to run too early
  - side effects during scanning
  - broken conditionals
  - circular dependency issues
  - impossible AOT optimization

- So Spring:
  - scans without loading
  - loads only when instantiating
  - caches the result

### `Class<?> clazz` clarified

```
if (beanClassObject instanceof Class<?> clazz) {
    return clazz;
}
```
- `clazz` is just a local variable
- introduced by java 16+
- equivalent to
  ```
  Class<?> clazz = (Class<?>) beanClassObject;

  ```

### Correct final mental model

```
Disk (.class files)
   ↓  (Spring scans via ASM)
BeanDefinition (String class name)
   ↓  (resolveBeanClass)
Class.forName(...)
   ↓
Class<?> (JVM Klass metadata)
   ↓  (reflection)
Constructor / Field / Method
   ↓
Object instance
```
**Spring decides what, ClassLoader decides where, JVM decides how**

> Spring IoC separates component discovery, class loading, and object instantiation into distinct phases. 

> Spring scans .class files using bytecode metadata to discover candidate components without loading them. It stores fully-qualified class names in BeanDefinitions and defers class loading until instantiation time, when it explicitly calls Class.forName to resolve the class into a Class<?>. Reflection is then used to construct and inject dependencies. 

> This separation avoids premature side effects, enables conditional configuration, supports AOT compilation, and keeps class loading deterministic.


### ANOTHER final note on `Class.forName`
- `Class.forName` establishes the Class<?> object, which is the prerequisite for all later reflection-based operations in Spring IoC.
  ```
  String className
    ↓  (class loading)
  Class.forName(...)
    ↓
  Class<?> clazz
    ↓  (reflection)
  clazz.getConstructors()
  clazz.getDeclaredFields()
  constructor.newInstance(...)
  ```

- Even though `Class<?> clazz` is unknown, can Spring still invoke constructors?

  - ✅ **Yes — and this is a key JVM insight**
  - `Class<?>` being "unknown" only means 
    - Unknown at compile time
    - known at runtime
  - At runtime, JVM knows everything about that class
    - its constructors
    - parameter types
    - annotations
    - access modifiers
  - So Spring can do:
    ```java
      Constructor<?> ctor = clazz.getDeclaredConstructor(...);
      Object bean = ctor.newInstance(args);
    ```
  - This works because
    - `clazz` is backed  by fully-loaded JVM `Klass` metadata
    - generics `<?>` are irrelevant at runtime
    - reflection is intentionally `dynamic`
  - This is excatly why framework can exists

- Spring does not require all beans to have a no-args constructor
  - ✅ The correct rule is:
  - > Spring requires that it can resolve some constructor whose arguments it knows how to supply.

### ANOTHER ANOTHER final note on `Class.getDeclaredConstructors0(boolean var1)`

- Native method, searches the internal `Klass` structure for constructors
- At this point, class has already been loaded. 
- JVM has already created the internal metadata
- Reflection is operating on already-loaded class metadata
- Internal Hotspot strucutre:
  ```
    Klass (C++ object)
    ├─ InstanceKlass
    │   ├─ constant pool
    │   ├─ method table
    │   │   ├─ <init>(...)V   ← constructors live here
    │   │   ├─ other methods
    │   ├─ fields
    │   ├─ access flags
    │   └─ annotations
  ```
- What this method does under the hood:
  - Step 1: Get the Klass* from the Class<?>
    ```
    Class<Car> → oop → Klass*
    ```
  - Step 2: Iterate over the method table
    - For each method in the class:
      - Check method name == <init>
      - Check access flags (public / non-public)
      - Filter based on publicOnly flag
    - So yes — it is literally scanning the method metadata.
  - Step 3: For each matching constructor, create a Java wrapper
    - For every <init> method found, JVM creates a `java.lang.reflect.Constructor
    - This object contains references to:
      - declaring class
      - parameter types
      - exception types
      - access flags
      - annotation metadata
      - a pointer back to the native method metadata
    - **This wrapping step is where reflection objects are born.**
  - Step 4: returns `Constructor<T>[] result;`

- Why this method must be **native**

  > This cannot be done in pure Java because:
  - Method tables live in native JVM memory
  - Java code cannot directly walk Klass / Method*
  - Performance and safety reasons
  > Reflection is a controlled, read-only window into JVM internals. 


### JVM Class Metadata, `Klass`, and Metaspace - Notes

####  `Klass` vs `java.lang.Class`

`Klass` (Hotspot Internal)

- C++ structure used by HotSpot JVM
- Represents class metadata
- Examples:
  - `InstanceKlass`
  - `ArrayKlass`
- Contains:
  - Field metatadata
  - Method metadata
  - Constant pool
  - Annotation metadata
  - VTables /itable
- Lives in Metaspace (native memory)
- Not visible to Java code

`java.lang.Class`

- Ordinary Java object
- lives on the Java heap
- Act as a mirror/handle to `Klass`
- Internally points to its `Klass`

```
Heap:
  java.lang.Class<Foo>
        |
        v
Metaspace (native):
  InstanceKlass<Foo>
```

#### Where calss metadata lives
> All class metadata lives in Metaspace, not on the Java heap

Stored in Metaspace:
- `Klass` / `InstanceKlass`
- Constant Pool
- Method bytecode + metadata
- Field metada
- **Annotation metadata**
- Classloader metadata
- Virtual dispatch tables

Not stored in Metaspace:
- Java objects
- Reflection objects (`Method`, `Field`, `Constructor`)
- Annotation proxy instance

#### Annotation Lifecycle

**At class load time**

- Annotations are parsed from .class file attributes:
  - RuntimeVisibleAnnotations
  - RuntimeInvisibleAnnotations
- Stored as raw metadata inside InstanceKlass
- No Java annotation objects created yet

**At reflection time**
```
clazz.getDeclaredAnnotations()
```
- HotSpot:
  - Reads annotation metadata from `InstanceKlass`
  - Lazily creats Java annotation proxy objects
- Annotation instances:
  - Live on **heap**
  - Can be GC'd
- Source metadata remains in **Metaspace**

#### Metaspace mental model (refined)

> Metaspace is native memory used by HotSpot C++ runtime to store JVM-level metadata that must outlive GC and be accessed efficently by the VM

Key properties:
- Native memory(outside JVM heap)
- Not managed by Java GC
- allocated in chunks
- Freed on class unloading
- Replaced PermGen (Java 8++)

#### Metaspace vs native memory (important distinction)
Metaspace ≠ all native memory
```
Native Memory
 ├─ Metaspace          (class metadata)
 ├─ Code Cache         (JIT compiled code)
 ├─ Thread stacks
 ├─ GC internal data
 ├─ DirectByteBuffer
 ├─ JNI allocations
 └─ OS / libc memory

```


#### Reflection and native methods

```
private native Constructor<T>[] getDeclaredConstructors0(boolean publicOnly);
```

What happens:
- Class already loaded -> `InstanceKlass` exisits
- HotSpot walks constructor metadata in `Klass`
- Filters `<init>` methods
- Wrap metadata into Java `Constructor` objects (heap)
> Native metadata -> heap reflection objects (lazy)

#### Why metadata is not on the heap

- Metadata lifetime != object lifetime
- Avoid GC scanning and pauses
- Faster access via C++ pointers
- Easier class unloading
- Lower heap pressure

#### ClassLaoding Summary

- Load
  - Read `.class` bytes
  - Parse:
    - Constant Pool
    - Fields
    - Methods
    - Annotations
  - **Allocate** `InstanceKlass` in Metaspace
  - Create `java.Lang.Class` mirror (heap)
  - > Metada is allocated here

- Link
  - **Verification**
    - Bytecode verification (CAFE BABE)
  - **Preparation**
    - Compute field layouts
    - Assign offsets
    - Allocate static fields (in heap, inside `Class` mirror)
  - **Resolution**
    - Symbolic refernces -> direct references
  - > Metadata structures finalized

- Initialize
  - Run `<clinit>`
  - Initialize static fields
  - Execute static blocks
  - > No new metadata created here

  ```
  .class file bytes
        ↓
  ClassLoader
        ↓
  InstanceKlass (Metaspace, native)
        ↓
  java.lang.Class (Heap mirror)

  ```

  **Note**:
  - Class loading orchestration (parent delegation, loadClass) is Java code.
  - `java.lang.ClassLoader`, parent delegation model
  - Class parsing and metadata construction (Klass, constant pool, methods, annotations) are HotSpot C++ code.

### What does parent delegation model ensure
A design choice, not a technical requirements

- Core Classes cannot be spoofed (**SECURITY**)
  ```
  loadClass("java.lang.String")
    → BootstrapClassLoader
    → always the real String
  ```
  Without it an application could define
  ```
  package java.lang;
  public class String { ... }

  ```
  💥 Consequences:

  - SecurityManager checks bypassed
  - Class.forName, File, Socket trust violated
  - JVM invariants broken
  - ➡️ Delegation ensures java.* is always trusted

- 2️⃣ Type identity remains consistent (**CORRECTNESS**)

  - In JAVA `Class identity = (class name + class loader)`
  - Parent delegation ensures:
    - One `java.lang.String`
    - One `java.lang.Object`
    - One `java.lang.Class`
  - Without it
    - `String loaded by LoaderA ≠ String loaded by LoaderB`
    - `instanceof` fails unexpectedly
    - `ClassCastException` everywhere.
    - API stops composing

- 3️⃣ Core APIs assume delegation implicitly
  - Many JDK internals assume:
  - `Object` is the Object
  - `Classloader` is *the* Classloader
  - `Throwable` is the Throwable
  - Without delegation:
    - You’d need defensive checks everywhere
    - JVM code complexity explodes
    - ➡️ Delegation keeps JDK code simple and fast
- 4️⃣ JVM bootstrap becomes possible
  - At JVM startup: Java language is not fully usable
  - Core classes must load first
  - Circular dependencies must be avoided
  - Parent delegation creates a well-defined bootstrap order:
  - `Bootstrap → Platform → Application → Custom`

> Parent delegation is not strictly necessary, but it enforces security, type consistency, and trust boundaries.
It prevents core classes from being overridden, ensures a single definition of fundamental types, and allows the JVM to safely compose code from different class loaders.
Advanced systems may intentionally break delegation, but only with great care.

# React

## React Crash Course - Day 1

- 1️⃣ Modern Frontend Mental Model
  - Frontend ≠ Backend
  - Frontend code runs:
    - in the browser
    - over the network
    - with security restrictions (CORS)
  - Therefore it needs:
    - a **dev server**
    - a **bundler**
  - fast feedback loops (**HMR**)
- 2️⃣ What Vite Actually Does
  - **Dev Server**
    - serves ES modules over HTTP
    - transforms TS / JSX on the fly
  - **HMR(Hot module Replacement)**
    - updates changed modules only
    - avoids full page reload
  - **Production bundling**
    - outputs static assets(`dist/`)
    - optimized for browser delivery
  - 👉 Browser cannot run TS / JSX directly.
- 3️⃣ React Rendering Model
  - Core rule: React re-renders UI from **state**, not from manual DOM updates
  - `setState -> re-render`
  - Component function runs again
  - JSX describe what UI should look like
- 4️⃣ State & Controlled Inputs
  
  **Controlled Input Pattern**
  ```jsx
    const [value, setValue] = useState("");

    <input value={value} onChange={e => setValue(e.target.value)} />
  ```
  - React is the **single source of truth**
  - Input value always reflects state
  - Enables validation, formatting, disabling, etc.
- 5️⃣ Derived State:
  - Derived state = computed from other state.
  - `const remaining = todos.filter(t => !t.done).length;`
  - Rules:
    - Do not store it
    - Compute it from existing state
- 6️⃣ `useEffect` - **Side Effects**
  - `useEffect` is for:
    - DOM effects (`document.title`)
    - data fencing
    - timers / subscriptions
    - syncing external systems
  - Key properties:
    - runs after render
    - re-runs when dependencies change
    - NOT a constructor
    - NOT backend “initialization”
- 7️⃣ useMemo — Cache, Not Optimizatio
  - What useMemo actually does
    - Caches a computed value
    - Returns cached value only if dependencies are === equal
  - Important Insight
    - useMemo can be more expensive than recomputing.
    - Why:
      - dependency comparison cost
      - cache bookkeeping
      - often recomputes anyway if deps change frequently
  - Rule of Thumb
    - Use useMemo only if:
      - computation is expensive
      - dependencies change rarely
      - referential stability matters
    - Otherwise: recompute.
- 8️⃣ Fake Backend Call Pattern

  **Frontend async pattern:**
  ```jsx
    setLoading(true);
    try {
      const data = await fetchStuff();
      setState(data);
    } finally {
      setLoading(false);
    }
  ```
  Key idea:
  - Async logic lives in event handlers or effects
  - Loading & error are explicit UI states

- 9️⃣ CORS (Browser Security)
  - Different origin = protocol + host + port
  - Browser blocks cross-origin reads by default
  - Server must explicitly allow via CORS headers
  
  This is enforced by the browser, not the server.

- 🔑 Day 1 Core Takeaways
  - React is a **state** -> **render** -> **effect** machine
  - Dev servers exist because browsers can't compile modern frontend code
  - Hooks are **not magic** -- the are discplined APIs around render cycles
  - `useMemo` is a cache invalidation tool, not a performance gurantee. 

## React Crash Course - Day 2

### React 18 StrictMode (Dev)

- React intentionally mounts components twice in dev
- Sequence: mount → unmount → mount
- Purpose: detect unsafe side effects
- Happens ONLY in development
- Production runs mount once

### useState
- Holds component-local state
- setState triggers re-render
- Never mutate directly

### useEffect([])

- NOT guaranteed to run once in dev
- MUST be idempotent
- Cleanup must fully undo side effects

### useEffect cleanup
 
- useEffect may run multiple times
- Returned function by useEffect is the cleanup
  ```js
    useEffect(() => {
      window.addEventListener("resize", handler);
      return () => window.removeEventListener("resize", handler);
    }, []);
  ```
- Cleanup runs:
  - on unmount
  - before effect re-runs
  - in React 18 StrictMode (dev)
- Always clean:
  - event listeners
  - timers
  - subscriptions
  - observers

### installHook.js

- Injected by React DevTools
- Used for inspection & profiling
- Not part of app code

### Summary

- ✅ Triggers: What triggers Re-render
  - `setState`
  - parent re-render
  - props change
  - context change
- ❌ Does NOT trigger:
  - local variable mutation
  - `useRef.current` change
  - `console.log`
- `useState` what it really does
  - `useState` is how `React` remembers values aross reners
  - calling `setState` schedules a re-render
  - State updates are **batched & async**
  - State mustg be treated as **immutable**

## React Crash Course - Day 3 RTK Query, Async Data, and Server State

### 1. the Big mental shift
**old mindset**: (local state / thunks/ fake fetch)
> "I call an API, wait for it, then put the result into state."

**New mindset**: (RTK query)
> My component declares a dependency on server data.
Fetching, caching refetching and lifecycle are handled by RTK Query.

### 2. Server State vs UI State (critical distinction)

- Server State (RTK Query owns this)
  - Data that comes from the backend
  - Can be refetched at any time
  - Shared across components
  - Cached globally

  Examples
  - `todos`
  - `users`
  - `orders`

  Managed by RTK Query

- UI / Client State (React/slices own this)
  - Input fields
  - Modal open/close
  - Filters, tabs
  - Temp UI-only values
  
  Examples:
  - `text` input
  - `selectedTab`
  - `isDialogOpen`
  
  Managed by `useState` or **Redux slices**

### 3. What `useGetTodosQuery()` really is

```js
const { data, isLoading, error } = useGetTodosQuery();

```
This is **not**:
- a function that “calls fetch”
- an async function
- a blocking operation

This is:
- a subscription to cached server data
- a declarative statement: “This component depends on getTodos.”

RTK Query:
- checks cache
- decides whether to fetch
- updates Redux state
- triggers re-renders

### 4. Where the HTTP request actually happens

Important realization:
- The hook does NOT send HTTP requests.

The request is sent by:
- RTK Query middleware
- via fetchBaseQuery
- using the browser fetch()

Execution path (simplified):
```
useGetTodosQuery()
 → dispatch(initiate)
 → RTK Query middleware
 → baseQuery
 → fetch()

```

### 5. How to navigate to source code in `node_modules`

- Navigate to the expression
- do `ctrl` + `shift` + `p` -> **TypeScript: Go To Source Definition**

Types describe what is allowed.
Source code shows what actually happens.


### 6. Cache, Tags, and invalidatesTags

What providesTags does
```
providesTags: ["Todos"]

```
It labels cached query results:
```
getTodos → tagged as "Todos"

```

**What `invalidatesTags` does**
```
invalidatesTags: ["Todos"]

```
After a mutation succeeds:
- Mark all "Todos" cache entries as stale
- If there are active subscribers → refetch
- Important:
  ❌ It does NOT update cache
  ❌ It does NOT merge data
  ❌ It does NOT add/remove items

It only says:
**“This data might be outdated — refetch it.”**

### 8. onQueryStarted — the missing piece

What it is
- onQueryStarted is a lifecycle hook that runs:
- immediately when a mutation starts
- before the HTTP request finishes

It gives you access to:
- dispatch
- queryFulfilled (a Promise)
- the mutation arguments

What it enables
- ✅ Optimistic UI
- ✅ Direct cache updates
- ✅ Rollback on failure

This is where you can say:

“I know how to update the cache right now.”

### 9. Optimistic Update Pattern (core pattern)

Used for add, toggle, delete.

General structure:

```js
async onQueryStarted(arg, { dispatch, queryFulfilled }) {
  const patch = dispatch(
    api.util.updateQueryData("getTodos", undefined, (draft) => {
      // optimistic change
    })
  );

  try {
    await queryFulfilled;
  } catch {
    patch.undo(); // rollback
  }
}

```
Backend analogy:

`Modify in-memory cache → async DB write → rollback on exception`

### Summary

**RTK Query cache is Redux state**
Hooks are just subscriptions
Middleware performs the side effects

## React, Javascripts Fundamentals
- `const` is like final for Java, but it is **not static**

- A React function is component is **just** a fucntion
  
  An App
  ```js
  function App() {
    const remaining = todos.filter(t => !t.done).length;
    return <div>{remaining}</div>;
  }

  ```

  **On every re-render**, React does 
  ```js
    App();
  ```

  and `remaining` gets re-calculated

  **React throws away everything and re-runs the function**





