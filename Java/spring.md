# spring 框架

## 简介
spring 框架解决了业务逻辑层和其他各层的松耦合问题，将面向接口编程贯穿整个系统应用。 现在的Spring框架已经成为构建企业级Java应用事实上的标准了。

![](container-magic.png)

这张图摘自 Spring 官网，意思为将你的 POJO 放入 Spring，让 Spring 为你管理你的对象，在你需要的时候为你实例化

## 配置元数据

新建一个 beans.xml 文件，并且添加一下代码：

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="..." class="...">
        <!-- collaborators and configuration for this bean go here -->
    </bean>

    <bean id="..." class="...">
        <!-- collaborators and configuration for this bean go here -->
    </bean>

    <!-- more bean definitions go here -->

</beans>
```
id 属性是用来标识单个 bean 定义的字符串，在将来使用的时候需要用到这个 id。class属性定义了bean的类型并使用完全限定的类名。

## 实例化容器

