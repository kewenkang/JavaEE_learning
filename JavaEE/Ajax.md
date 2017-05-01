### itelliJ快捷键

File -> new Projecr -> new Module

1. `alt+insert` 创建getter and setter等
2. `sout+tab` 快速向console输出
3. `shift+ctrl+space`  补全
4. `ctrl+alt+space`  补全
5. `alt+enter`  代码提示

### AJAX五步

1. 创建**XMLHttpRequest**对象（针对不同浏览器）
2. 注册回调函数
3. 调用open("GET","url",true)方法
4. 向服务器发送数据send(content)
5. 在回调函数针对不同响应状态进行处理

---
### javascript实现

```javascript
    //1.获取元素节点的值
    var userName = document.getElementById("name").value;
    
    //2.创建XMLHttpRequest对象
    //需要针对IE和其他类型的浏览器建立这个对象的不同方式些不同的代码
    if (window.XMLHttpRequest){
        //针对FireFox, Mozillar, Opera, Safari, IE7, IE8
        var xmlhttp = new XMLHttpRequest();
    
    }else if (window.ActiveXObject){
        
    }
    xmlhttp.onreadystatechange = callback;
    xmlhttp.open("GET",url,true);
    xmlhttp.send(null);
    function callback(){
    }
```
---
### Jquery实现

```javascript
    //1.获取dom节点，jquery的方法返回一个jquery对象，可以继续在上面执行其他jQuery方法
    var jqueryobj = $.("#username");
    //获取节点的值
    var userName = jqueryobj.val();
    //javascript解决中文乱码的方法encodeURI()
    var url = "AjaxServer?name=" +encodeURI(userName);
    //2.使用jquery的XMLHttpRequest对象对get请求的封装
    $.get(url, null, callback);
    
    //回调函数
    function callback(data){
        //3.接收服务器返回的数据
        alert(data);
    
        //4.将服务器返回的数据，动态地显示在页面上
        //找到保存结果信息的节点
        var resultObj = $("#result");
        //动态地改变页面中div节点的内容
        reesultObj.html(data);
    }
```

```javascript
    $.ajax(
        type:"GET", 
        url:"...servlet?aa=xx",
        dataType:"script"
     )   
     $.ajax(
        type: "POST",
        url: "...servlet",
        data: "name=xxx&password=123",
        dataType: "xml",
        success: function(data){
            //回调函数
        }
        error: function(err){}
    )
```

#### 时间戳

```javascript
    function convertURL(url){
        var timetamp = (new Date()).valueOf();
        if(url.indexOf("?") >= 0){
            url += "&t="+timetamp;
        }else{
            url += "?t="+timetamp;
        }
    }
```
---


##### jquery解析xml

    1. 将data转换为jquery对象
    var domObj = $(data);
    2. dom解析

##### 返回xml数据

    1. 服务器端 response.setContentType("text/xml;charset=utf-8");
    2. 服务器返回的信息要加标签
    3. 页面端 var domObj = xmlhttp.responseXml;然后进行解析

##### 中文乱码解决方案

    String old = request.getParameter("name");
    1. 页面端对发送的数据做一次encodeURI(),var url = "AjaxServer?name=" +encodeURI(userName);
    服务器端使用String name = new String(old.getBytes("iso8859-1"), "UTF-8")
    2.页面端对发送的数据做两次encodeURI(),var url = "AjaxServer?name=" +encode(encodeURI(userName));
    服务器端String name = URLDecoder.decode(old,"UTF-8");

##### JSON

    注意事项：
    服务器回传json对象时,要加一对括号，eval("("+data+")");

##### jquery

    获取当前节点距离上，左边界距离：var offset = node.offset(),offset对象中有left，top两个属性
