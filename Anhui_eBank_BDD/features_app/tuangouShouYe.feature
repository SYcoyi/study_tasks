Feature: 安徽社区团购

  Scenario:首页团购商品展示
    When 团购商品列表  #/api/user/product/top
    Then 团购商品查看更多   #/api/user/product/group/search


  Scenario:搜索团购商品
    When 用商品名称搜索团购商品  #/anhui/m/cheapList
    Then 