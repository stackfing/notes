# spring 框架

## 简介
spring 框架解决了业务逻辑层和其他各层的松耦合问题，将面向接口编程贯穿整个系统应用。 现在的Spring框架已经成为构建企业级Java应用事实上的标准了。

![](container-magic.png)

这张图摘自 Spring 官网，意思为将你的 POJO 放入 Spring，让 Spring 为你管理你的对象，在你需要的时候为你实例化

## 装配 Bean

装配 Bean 有三种方式

* XML 方式显示配置

* Java 中显示配置

* 隐式的 Bean 扫描机制和自动装配

## XML 方式自动装配 Bean

新建一个 beans.xml 文件，加入一下代码：
```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

<!-- 在这里添加代码 -->
    
</beans>
```

在里面添加一个 bean
`<bean id="myBean" class="core.MyBean"></bean>`

这样我们就可以将 core 包下的 MyBean 交给 Spring 来管理，在我们需要的时候 Spring 会为我们提供相应的对象

现在我们来使用他，需要在上下文中获得
```
ApplicationContext ctx = new ClassPathXmlApplicationContext("beans.xml");
MyBean my = (MyBean) ctx.getBean("myBeans");
my.send();
```

## Java 代码装配 Bean

通过 Java 代码装配 Bean 需要一个配置类

Config.java
```
@Configuration
public class Config {
	@Bean
	public MyBean createMyBean() {
		return new MyBean();
	}
}

```

获得上下文方式改变了：
```
ApplicationContext con = new AnnotationConfigApplicationContext(Config.class);
		MyBean b = con.getBean(MyBean.class);
		b.send();
```
## 自动装配 Bean

配置类中加入注解： @ComponentScan 和 @Configuration

获得上下文:
```
ApplicationContext ctx = new ClassPathXmlApplicationContext("beans.xml");
	        
MyBean my = (MyBean) ctx.getBean("myBean");
my.send();
```

@ComponentScan 注解是启用组件扫描，如果没有其他配置，会默认扫描与配置列相同的包。可以在注解中设置参数，具体可进入源码查看

在 beans.xml 配置文件中添加自动扫描包路径
`<context:component-scan base-package="core" />`