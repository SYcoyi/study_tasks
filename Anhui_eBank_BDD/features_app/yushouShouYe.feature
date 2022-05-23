Feature: 安徽社区个人端名优特惠商品展示

  Scenario:名优特惠首页展示
    When 名优特惠首页展示  #/api/user/view/famousIndex


  Scenario:名优特惠品牌详情页
    When 名优特惠品牌详情页      #/api/user/view/famousBrand


  Scenario:名优特惠商品展示
    When 名优特惠首页展示  #/api/user/view/famousIndex
    Then 名优特惠首页查看更多    #/api/user/view/famousList
    Then 名优特惠商品列表_筛选    ##接口同上，依不同参数进行筛选
    Then 名优特惠商品列表_商品搜索    ##同上