Feature: 安徽社区个人端团购商品详情

  Scenario: 进入团购商品详情页
    When 手机个人端密码登录
    Then 首页热门团购商品  #/api/user/product/top
    Then 团购商品详情页    #/anhui/m/cheapDetail  任取一个商品


  Scenario: 团购商品详情页展示
    When 手机个人端密码登录
    Then 首页热门团购商品  #/api/user/product/top
    Then 团购商品详情页    #/anhui/m/cheapDetail  任取一个商品
    Then 查看图文详情     #/api/user/product/detail
    Then 适用门店      #/api/user/merchant/outlet/list
    Then 查看全部评价  #/api/user/comment/product/list    ###非必须