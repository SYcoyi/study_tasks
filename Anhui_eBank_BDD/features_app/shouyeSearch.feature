Feature: 安徽社区首页搜索

  Scenario:搜索商户
    When 商户热词展示  #/api/user/hotWord/list
    Then 首页搜索商户  #/api/user/outlet/list


  Scenario:搜索商品
    When 商品热词展示   #/api/user/hotWord/list
    Then 首页搜索商品   #/api/user/product/list  仅支持团购、名优、预售商品的搜索

