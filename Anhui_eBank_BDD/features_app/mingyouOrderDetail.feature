Feature: 安徽社区团购订单列表/详情

  Scenario: 团购订单列表展示
    When 手机个人端密码登录       ##需要新生成么？
    Then 我的订单_团购订单     #/api/user/myorder/listsubOrder  团购名优预售为同一个接口，需筛选进行区分
    Then 团购订单_待付款      #接口同上，使用不同参数来进行筛选
    Then 团购订单_待使用
    Then 团购订单_待评价


  Scenario: 团购订单详情页
    When 手机个人端密码登录
    Then 我的订单_团购订单     #/api/user/myorder/listsubOrder
    Then 团购订单详情页      #/api/user/myorder/detail  任一订单






  Scenario: 进入名优特惠订单详情页
    When 手机个人端密码登录
    Then 我的订单_名优特惠订单     #/api/user/myorder/listsubOrder
    Then 名优特惠订单详情页      #/api/user/myorder/detail

  Scenario: 进入精品预售订单详情页
    When 手机个人端密码登录
    Then 我的订单_精品预售订单     #/api/user/myorder/listsubOrder
    Then 精品预售订单详情页      #/api/user/myorder/detail
