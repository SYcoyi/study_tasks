Feature: 安徽社区团购商品详情

  Scenario:团购商品详情
    When 团购商品详情  #/anhui/m/cheapDetail
    Then 团购详情_查看图文详情   #/api/user/product/detail
    Then 团购详情_适用门店列表    #/api/user/merchant/outlet/list
    Then 团购详情_查看更多团购商品   #/anhui/m/cheapList

