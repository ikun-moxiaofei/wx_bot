## 介绍
- 基于`Windows`操作系统下`pc`端微信的脚本
- 支持收发 文本、引用消息、图片（编码成`base64`格式）并存储到`MySQL`数据库
- 可以通过程序实现一些逻辑，比如检测到有人发广告可以快速把群名，发送人id和信息发送给管理员（未完成）

---

## 支持的微信版本
仅支持`Windows`操作系统下`3.6.0.18`版本的微信

- 下载链接 [WeChatSetup3.6.0.18.exe](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.6.0.18/WeChatSetup-3.6.0.18.exe)

---

## 如何开始

1. 下载代码到本地，用`pycharm`打开，终端输入以下指令安装依赖
```sql
pip install -r requirements.txt
```

2. 在配置文件`config.py`中先把`database`中的数据库配置属性修改为你自己的，`xor_value`的值作为解析图片的密钥也需要修改，如何修改会在后续步骤说明
3. 在`sql`文件夹里运行`run_sql.py`文件就会在配置好的数据库中创建名为`user_msg_db`的数据库和16张记录不同群聊的表
4. 在下载好的微信客户端中登录微信，然后启动`main.py`文件
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716271972139-d98a4e89-7f42-490b-82e9-a9dc272e10fe.png#averageHue=%233a3130&clientId=u7b82f97c-64d4-4&from=paste&height=125&id=u13dfa73f&originHeight=370&originWidth=2130&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=101204&status=done&style=none&taskId=ua09e2563-e07a-4111-9387-1dde559e530&title=&width=719.4423217773438)
日志中会输出当前登录用户的信息，如微信号和用户名等；在测试群组中发送消息`hello123`，如果收到登录微信的自动回复`world456`则表示脚本成功启动
![a9f054edcfd97d160156a353205f993.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/38886723/1716273349098-5782d192-44ee-44cb-add3-50f20b867c6e.jpeg#averageHue=%23191817&clientId=u7b82f97c-64d4-4&from=paste&height=196&id=ud3fe171a&originHeight=347&originWidth=1073&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=58956&status=done&style=none&taskId=u489e3961-7fae-4d54-b897-7de90a9a5fb&title=&width=606.4423217773438)
如果遇到显示微信版本过低无法登录的信息，目前调研到有两种解决方案
   1. 当前用户对微信应用目录没有足够的权限
   - 打开微信客户端的安装地址，在最外层目录下右键点击目录，选择 【属性】
   - 在 `属性` 对话框中，选择 【安全】页，然后选择 【编辑】
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716274933534-b9c9eebe-0e41-4eaf-85f3-633a0dbad6d4.png#averageHue=%23f5f1f0&clientId=u7b82f97c-64d4-4&from=paste&height=444&id=BJoSV&originHeight=577&originWidth=433&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=64578&status=done&style=none&taskId=ud1e771fb-caf8-4774-b8ef-87d90782109&title=&width=333.0769352941123)
   - 双击 Adminstrators 或者 Users，将两者的权限全部改为✅
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716275028339-a90d6a6c-ccaa-4dd6-bbac-813e9c2653f0.png#averageHue=%23f7f6f6&clientId=u7b82f97c-64d4-4&from=paste&height=410&id=bTFvZ&originHeight=533&originWidth=430&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=49347&status=done&style=none&taskId=u41c9c95a-339a-45ef-9972-cf184a63853&title=&width=330.7692429017743)
   - 点击【确认】至退出
   - 以上同样的操作也要用到`C:\Program Files (x86)`目录下的`Tencent`文件夹中，以确保有足够的权限
   2. 如果通过上述操作之后仍然无法登录至客户端，则可以是微信账号注册时间过短，推荐更换使用2017年之前注册的微信账号
5. 服务启动之后就可以正常记录提前标记好的16个官方交流群和测试群的文字消息了，但是对于图片来说，还需要对微信的加密的dat格式进行解密，具体操作如下
   1. 先找到微信存放图片的文件夹，这个可以在设置中找到
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716276957787-a375d4ab-93d8-4902-afae-1b5c13220b4b.png#averageHue=%23f1f0ef&clientId=ua5cf39f7-47ca-4&from=paste&height=82&id=uf81653f6&originHeight=107&originWidth=484&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=5631&status=done&style=none&taskId=ude3e63c1-735f-40b2-bf86-c21161b9294&title=&width=372.3077059638576)
   2. 使用一个可以查看16进制的工具去打开里面的dat文件，这里可以使用这个在线工具[HexEd.it - Browser-based Online and Offline Hex Editing](https://hexed.it/)
**记录所得到的编码的前四个数字**，这个得到的编码可能和下图不同，因为他就像微信号一样是作为标识的，但是你的`dat`文件都是以特定的一种或两种4位数字开头（一般是两种，对应着`jpg`和`png`两种格式），比如在此实例中需要记录的编码是`4A93`和`3C1B`
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716277791203-188fc329-63d2-40a5-a0bf-503c364844f2.png#averageHue=%23352d2b&clientId=ua5cf39f7-47ca-4&from=paste&height=168&id=RaO7U&originHeight=141&originWidth=339&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=15014&status=done&style=none&taskId=u707db032-6a22-4cc9-b216-6e2e66c0ca9&title=&width=403.76922607421875)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716278379615-167b3963-81b7-4e07-aaea-55084ebbfd56.png#averageHue=%23362b29&clientId=ua5cf39f7-47ca-4&from=paste&height=236&id=ua21b104f&originHeight=148&originWidth=254&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=11034&status=done&style=none&taskId=u78c6ef9c-81f2-4723-b19c-732ee6befd0&title=&width=405)
   3. 在使用这个16进制工具分别打开`jpg`和`png`两种格式的文件，记录他们的前四个数字编码
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716278776010-9fc26b41-e3b7-4402-9afb-214203b8c488.png#averageHue=%23302e2c&clientId=u6fb84cde-3a0d-4&from=paste&height=223&id=t4opb&originHeight=126&originWidth=223&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=8699&status=done&style=none&taskId=ua9db6eb0-e3c9-4577-b3bd-ae910dffca2&title=&width=394)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716278802890-8a2235bc-2a69-4811-b68f-0df70246ca13.png#averageHue=%23333230&clientId=u6fb84cde-3a0d-4&from=paste&height=206&id=u4f44d1ee&originHeight=105&originWidth=203&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=7633&status=done&style=none&taskId=ufb3888ba-d84f-410a-81cd-b339ccb0d7d&title=&width=398)
一般来说这两种文件的编码标识是固定的，即`jpg-FFD8`、`png-8950`，当然也可以自己分别打开记录一下
   4. 目前我们有了四组编码，分别是两组`bat`编码，一组`jpg`和`png`编码，他们之间应该是两两对应的，即其中一组的`bat`编码对应`jpg`格式，另一个`bat`编码对应`png`格式；所以下一步就是对他们进行排列组合进行分组对应
   5. 当我们用`bat`的4位数钥匙与`FFD8`或者`8950`分别做异或运算时（运算方式在下一条中会详细说明），会发现他们有一组排列组合方式会算出相同的结果，在我上面的示例中即为
`4A93 XOR 8950 = C3C3`
`3C1B XOR FFD8 = C3C3`
此时得到的一个有两个相同16进制编码的4位数字即是咱们所需要的解密密码，在我这个示例中，解密密码为`C3`
   6. 那么如何进行异或运算呢，具体操作如下
      1. 打开系统中自带的计算器，选择程序员选项
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716280389440-1b4fec71-14a9-435e-95d9-ef4da2749965.png#averageHue=%23302f2f&clientId=u8adfcfcd-8e5e-4&from=paste&height=571&id=u4bb02f7b&originHeight=742&originWidth=477&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=148066&status=done&style=none&taskId=u18dd19b6-f3cb-434a-afe6-c0596cc956d&title=&width=366.9230903817357)
      2. 输入第一个四位数字（两个`bat`编码中的一个）在选择按位异或运算
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716280712687-c809b85f-100f-42c5-abd1-b59156d81d0e.png#averageHue=%23473f49&clientId=u8adfcfcd-8e5e-4&from=paste&height=578&id=hhFSJ&originHeight=751&originWidth=488&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=87287&status=done&style=none&taskId=uca086701-ba94-4c68-a581-77394d906aa&title=&width=375.3846291536415)
      3. 直接输入第二个四位数字，在点击`=`即可得到结果
![image.png](https://cdn.nlark.com/yuque/0/2024/png/38886723/1716280959643-83ec3aa2-831a-431b-9b1b-fb7f112be4ba.png#averageHue=%23382c30&clientId=u8adfcfcd-8e5e-4&from=paste&height=578&id=u571adb3a&originHeight=751&originWidth=488&originalType=binary&ratio=1.2999999523162842&rotation=0&showTitle=false&size=58081&status=done&style=none&taskId=ueefd2771-6de7-42e3-b8f5-9f2a36cac5a&title=&width=375.3846291536415)
      4. 多次排列组合后运算，直至得到`5.5`中预期的结果，即成功计算出密钥
   7. 回到`config.py`文件中，将`xor_value`参数的值修改为你刚刚计算出的密钥，主要密钥要用16进制的值传递，即在得出的两位数字前添加`0x`前缀，在此示例中，我们计算得到的结果为`C3C3`，密钥为`C3`，`config.py`文件中参数值应为`xor_value = 0xC3`
   8. 修改之后重新运行`main.py`文件，用户在群聊里发送的图片信息就会解密为`png`格式的图片，并且以`base64`编码存储入数据库中，`temp_image`文件夹下是解码后的图片，可以查看该目录下的图片是否可以成功打开判断解码是否成功
6. 至此，我们完成的一个简易的脚本去监听并记录群聊消息


