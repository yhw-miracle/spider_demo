# 百度翻译
* url: POST https://fanyi.baidu.com/v2transapi

* headers
    * Referer: https://fanyi.baidu.com/
    * User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36

* form data
    * from: zh
    * to: en
    * query: 我是中国人
    * transtype: realtime
    * simple_means_flag: 3
    * sign: 366362.95275
    * token: {7c3fd99e31f188110574f8090937ae88} ---> regex: token: '(.*)'
    
* sign
    * index_c8a141d.js
    * public_64cf93b.js
