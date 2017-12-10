# Spring 源码分析

编写一个简单的例子单步调试

例如最简单的：
```
private static ApplicationContext ctx;
public static void main(final String[] args) throws Exception {
	        ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
	        A a = (A) ctx.getBean("a");
	        a.send();
	    }
```

进入 `ClassPathXmlApplicationContext` 加载配置文件的代码

从上到下：

AbstractApplicationContext

将资源加载器加载好

AbstractRefreshableApplicationContext

AbstractRefreshableConfigApplicationContext

ClassPathXmlApplicationContext