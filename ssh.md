## 1. struts2
1. 导入jar包
2. 创建action类，在其中定义execute()方法
3. 在src目录下配置struts.xml文件（配置action的访问路径）
4. 在web.xml中配置StrutsPrepareAndExecuteFilter过滤器

#### struts.xml的配置

1. Action 
    + struts2的特点：
    + struts1创建action后将action放入缓存，对用户后面的请求从缓存中调action（单例模式）
    + struts2对用户的每一个请求都会创建一个action，action是线程安全的
       
        &lt;action>标签，默认class是ActionSupport
                    默认method是execute
        &lt;result>标签，默认name是success

    + 动态方法调用：
        1. 在action的name属性后面添加`！method`
            例如：loginAction!login 对应的method为login
        2. action通配符：
            ```xml
            <action name="loginAction_*" class="cn.hit.action.LoginAction" method="{1}">            
                <result name="login">/index.jsp</result>
            </action>
            ```
            例如：loginAction_login 对应的method为login
        3. 指定method属性值为方法名

2. 常量设置：
```xml
    <constant name="struts.action.extention" value="do" />
    <constant name="struts.i18n.encoding" value="UTF-8" />
    <constant name="struts.configuration.xml.reload" value="true" />  
    <constant name="struts.objectFactory" value="spring" /> 
    <constant name="struts.multipart.maxSize" value="1000000000000" />
    <constant name="struts.enable.DynamicMethodInvocation" value="false" /> 
```

3. 配置文件 为应用指定多个配置文件
```xml
    <struts>
        <include file="xxx.xml" />
        <include file="yyy.xml" />
    </struts>
```

#### 自动类型转换
1. 局部：
    定义DateTypeConverter继承DefaultTypeConverter；
    是否需要双向转换；
    注册转换器：
        新建ActionName-conversion.properties，放置到Action所在包；
        指定action中要转换的属性；例如：birthday=cn.hit.DataTypeConverter

2. 全局：


## 2. Hibernate

#### Entity.hbm.xml的配置

1. 引入约束文件
    ```xml
    <!DOCTYPE hibernate-mapping PUBLIC
    "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
    "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">
    ```
2. ORM配置（位置实体类的包下，命名Entity.hbm.xml）
```xml
    <hibernate-mapping>
        <!-- 1.配置类和表对应：class标签
            name:实体类全路径
            table:数据库表名称
        -->
        <class name="cn.entity.User" table="t_user">
            <!-- 1.配置实体类id和表id对应
                 hibernate要求实体类有一个属性唯一值，表有一个字段唯一值
            -->
            <!-- id标签
                name:实体类里面id属性名称
                column:生成的表字段名称
            -->
            <id name="uid" column="uid">
                <generator class="native"></generator>
            </id>
            <property name="username" column="username"></property>
            <property name="password" column="password"></property>

        </class>
    </hibernate-mapping> 
```

### hibernate核心配置（位置src下，命名hibernate.cfg.xml）
1. 引入约束文件dtd
    ```xml
    <!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
    ```
2. 配置
```xml
    <hibernate-configuration>
        <session-factory>
            <!-- 1.配置数据库信息（driver,url,username,password） 必须 -->
            <property name=""> ...</property>

            <!-- 2.配置hibernate信息() 可选 -->
            <!-- 自动建表，若表已存在则更新 -->
            <property name="hibernate.hbm2ddl.auto">update</property>
            <!-- 配置数据库方言：让hibernate识别不同数据库自己的方言 -->
            <property name="hibernate.dialect">org.hibernate.dialect.MySQLDialect</property>

            <!-- 3.把映射文件放到核心配置文件中 必须 
                resource相对与src下
            -->
            <mapping resource="cn/entity/User.hbm.xml" />
        </session-factory>
    </hibernate-configuration>
```
3. hibernate操作过程中，只会 **加载核心配置文件**
    + 配置数据库信息
    + 配置hibernate信息
    + 把映射文件放到核心配置文件中
    
#### 实现添加操作（代码）

1. 加载hibernate核心配置文件
2. 创建SessionFactory对象
3. 使用SessionFactory创建session对象
4. 开启事务
5.  **写具体的CRUD操作**
6. 提交事务
7. 关闭资源