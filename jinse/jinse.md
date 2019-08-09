# 需求

* 抓取页面 https://www.jinse.com/ 中的所有数据

* 相关 url
    * 热文 url: https://api.jinse.com/v6/information/list?catelogue_key=hot&limit=23&information_id=0&flag=down&version=9.9.9

    * 新闻 url: https://api.jinse.com/v6/information/list?catelogue_key=news&limit=50&information_id=0&flag=down&version=9.9.9
    
    * 政策 url: https://api.jinse.com/v6/information/list?catelogue_key=zhengce&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 相对论 url: https://api.jinse.com/v6/information/list?catelogue_key=TOR&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 人物 url: https://api.jinse.com/v6/information/list?catelogue_key=personage&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 行情 url: https://api.jinse.com/v6/information/list?catelogue_key=fenxishishuo&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 投研 url: https://api.jinse.com/v6/information/list?catelogue_key=capitalmarket&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 技术 url: https://api.jinse.com/v6/information/list?catelogue_key=tech&limit=23&information_id=0&flag=down&version=9.9.9
    
    * 百科 url: https://api.jinse.com/v6/information/list?catelogue_key=baike&limit=23&information_id=0&flag=down&version=9.9.9

* 规律
    * url: https://api.jinse.com/v6/information/list?catelogue_key={}&limit=50&information_id=0&flag=down&version=9.9.9
    * 主要参数：
        * catelogue_key=news
        * limit 最大为50
        * information_id 默认为0，下一页为 bottom_id 值
    * 校验参数：
        * flag=down
        * version=9.9.9

* 构造数据
{
    "news": 50,
    "count": 50,
    "total": 0,
    "top_id": 495051,
    "bottom_id": 492409,
    "list": []
}

* 结束条件：
{
    "message": "The given data failed to pass validation.",
    "status_code": 500
}

* url 去重
    * 反爬：重复数据

* 爬虫速度

* 爬虫需要有日志

* 要有**逻辑**组织爬取的数据