Feature: 安徽社区个人端名优特惠订单列表/详情

  Scenario: 名优订单列表展示
    When 手机个人端密码登录
    Then 我的订单_名优特惠订单     #/api/user/myorder/listsubOrder  团购名优预售为同一个接口，需筛选进行区分
    Then 名优特惠订单_待付款      #接口同上，使用不同参数来进行筛选
    Then 名优特惠订单_待发货
    Then 名优特惠订单_待收货
    Then 名优特惠订单_待评价

  Scenario: 名优特惠订单详情页
    When 手机个人端密码登录
    Then 我的订单_名优特惠订单     #/api/user/myorder/listsubOrder
    Then 名优特惠订单详情页      #/api/user/myorder/detail  任一订单






  Scenario: 进入精品预售订单详情页
    When 手机个人端密码登录
    Then 我的订单_精品预售订单     #/api/user/myorder/listsubOrder
    Then 精品预售订单详情页      #/api/user/myorder/detail
