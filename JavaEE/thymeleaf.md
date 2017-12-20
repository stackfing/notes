# 标准方言

Thymeleaf的可扩展性很强，它支持自定义你自己的模板属性集(或事件标签)、表达式、语法及应用逻辑，它更像一个模板引擎框架。

# 标准表达式语法(Standard Expression syntax)

分为四大类：

* `${...}` 变量表达式
* `*{...}` 选择或星号表达式
* `#{...}` 消息 (i18n) 表达式
* `@{...}` URL表达式
* `~{...}` 片段表达式

# 变量表达式 ${...}

变量表达式即OGNL表达式或Spring EL表达式(在Spring术语中也叫model attributes)

`${session.user.name}`

如果是属性值，可以是这样：

`<span th:text="${book.author.name}">`

`<input type="text" name="userName" value="James Carrot" th:value="${user.name}" />`

上面这个代码意思是引用 user 对象的 name 属性值

# 选择表达式 *{...}

选择表达式很像变量表达式，不过它们用一个预先选择的对象来代替上下文变量容器(map)来执行

```
<div th:object="${book}">
  ...
  <span th:text="*{title}">...</span>
  ...
</div>
```

# 消息表达式 #{...}

消息表达式有时候也叫文字国际化表达式，它可以我们从一个外部文件获取区域文字信息( .properties )，用 key 索引 value，还可以提供一组参数 (可选)

```
<table>
  ...
  <th th:text="#{header.address.city}">...</th>
  <th th:text="#{header.address.country}">...</th>
  ...
</table>
```

# URL 表达式 @{...}

URL 表达式是把一个有用的上下文或者会话信息添加到 URL，这个过程经常叫做 URL 重写

`<a th:href="@{/order/list}">...</a>`

会转换成

`<a href="/myapp/order/list">...</a>`

# 片段表达式 ${...}

片段表达式是表示标记片段并将其移动到模板周围的一种简单方法

# 模板

新建一个文件: footer.html
```
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:th="http://www.thymeleaf.org">
  <body>
    <div th:fragment="copyright">
      © 2016 xxx
    </div>
  </body>
</html>
```

在需要使用的地方添加：`th:include="footer :: copyright`
例如：
```
<div th:include="footer :: copyright></div>
```

th:utext 可以直接输出 html 代码对应的格式

写 js 时模板引擎出错需要添加：
```
/*<![CDATA[*/

/*]]>*/
```
