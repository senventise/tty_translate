# tty_translate
1.在百度翻译开放平台[产品服务](http://api.fanyi.baidu.com/api/trans/product/prodinfo)中选择通用翻译,点击立即使用,在控制台找到 APPID 和密钥.  
2.克隆仓库到本地 `git clone https://github.com/toushangyouxiang/tty_translate.git`   
3.进入目录新建".config"文件    
4.编辑.config  
```
{
  "APPID":你的APPID,
  "KEY":你的密钥
}
```  
5.`python3 translate.py -h` 或 `./translate.py -h` 获取使用帮助.  
