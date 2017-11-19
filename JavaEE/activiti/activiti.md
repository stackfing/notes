
## 用户任务属性

assignee 指定用户任务处理人

candidateUsers 指定用户任务的候选人,多个用户分开

candidateGroups 用来指定候选组,多个要用户分开

dueDate 设置用户任务到期日,通常用变量代替而不是指定一个具体的到期日

priority 用户任务的优先级,取值区间 [0,100]

## 脚本任务属性

scriptFormat 指定符合 JSR-223 规范脚本语言

resultvariable 把脚本处理结果保存在一个变量中




***

## 添加用户
```
	@Test
	public void testAddNewUser() {
		User user = identityService.newUser("stackfing");
		identityService.saveUser(user);
	}
```

## 添加用户组
```
	@Test
	public void testAddNewUser() {
		Group group = identityService.newGroup("admin");
		identityService.saveGroup(group);
	}
```
## 将用户添加到用户组
```
identityService.createMembership("stackfing", "admin");
```