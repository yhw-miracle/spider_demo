# 请求有道翻译
* url
post http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

* request headers
    * Cookie: OUTFOX_SEARCH_USER_ID=-1473530863@10.168.8.64; JSESSIONID=aaar3zlxnbn4jfaTFw7Xw; OUTFOX_SEARCH_USER_ID_NCOO=1472877600.7083225; ___rl__test__cookies=1565437688138
    * Referer: http://fanyi.youdao.com/
    * User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36

* form data:
```form_data
i: 我是中国人
from: AUTO | en
to: AUTO | zh-CHS
smartresult: dict
client: fanyideskweb
salt: {15654376881421}
sign: {1a3a8cec61bc0152e1ae42ca1c7625ba}
ts: {1565437688142}
bv: 7e3150ecbdf9de52dc355751b074cf60
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME | FY_BY_CLICKBUTTION | lan-select
```

* js 部分
```js
var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
        }
    };
```