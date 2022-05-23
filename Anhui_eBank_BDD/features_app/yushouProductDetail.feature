Feature: 安徽社区个人端名优特惠商品详情

  Scenario: 进入名优特惠商品详情页
    When 名优特惠首页展示  #/api/user/view/famousIndex
    Then 名优特惠商品详情页    #/anhui/m/famousDetail 任取一个商品


  Scenario: 名优特惠商品详情页展示
    When 名优特惠首页展示  # /api/user/view/famousIndex
    Then 名优特惠商品详情页    #/anhui/m/cheapDetail  任取一个商品
    Then 查看图文详情     #/api/user/product/detail
    Then 进入品牌      #/api/user/view/famousBrand


  Scenario:名优特惠商品详情页操作    ###与购物车/收藏模块重复，是否需要保留
    When 手机个人端密码登录
    Then 加入购物车     #/api/user/cart/add
    Then 收藏商品       #/api/user/favorite/product/add  团购、名优、预售均为该接口
    Then 立即购买进入确认订单页       #/api/user/view/tradeOrderConfirm