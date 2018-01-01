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

AbstractRefreshableApplicationContext

AbstractRefreshableConfigApplicationContext

ClassPathXmlApplicationContext

##  从 xml 中加载 Bean

1.获取对 xml 文件的验证模式

2.加载 xml 文件，并得到对应的 Document

3.返回 Document 注册的 Bean 信息

## DTD 与 XSD 区别

DTD (Document Type Definition) 是文档类型定义，是XML 约束模式语言，是XML 文件验证机制，属于 XML 文件组成的一部分。用来保证 XML 文档格式正确有效的方法，使用非 XML 语法编写的。

XSD (XML Schemas Definition) 是 XML Schema 语言。用来验证某个XML文档，以检查该XML文档是否符合其要求，本身是使用 XML 语法编写的

XSD是DTD替代者的原因，一是据将来的条件可扩展，二是比DTD丰富和有用，三是用XML书写，四是支持数据类型，五是支持命名空间。