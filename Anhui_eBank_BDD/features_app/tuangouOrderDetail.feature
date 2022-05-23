Feature: 安徽社区团购/名优/预售订单详情

  Scenario: 进入团购订单详情页
    When 手机个人端密码登录       ##需要新生成么？
    Then 我的订单_团购订单     #/api/user/myorder/listsubOrder  团购名优预售为同一个接口，需筛选进行区分
    Then 团购订单详情页      #/api/user/myorder/detail  进入任一一个订单

  Scenario: 进入名优特惠订单详情页
    When 手机个人端密码登录
    Then 我的订单_名优特惠订单     #/api/user/myorder/listsubOrder
    Then 名优特惠订单详情页      #/api/user/myorder/detail

  Scenario: 进入精品预售订单详情页
    When 手机个人端密码登录
    Then 我的订单_精品预售订单     #/api/user/myorder/listsubOrder
    Then 精品预售订单详情页      #/api/user/myorder/detail
