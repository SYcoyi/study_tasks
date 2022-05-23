Feature: 安徽社区个人端商品/商户评价

  Scenario:
    When 手机个人端密码登录
    Then 创建普通团购订单      #/api/user/order/generate
    Then 现金支付     #/api/user/cashier/payOrders
    Given 商户端登录
    Then 商户端团购验码
    Then 提交商品评价   #



  Scenario: 收银台页面仅展示信用卡
    When 手机个人端密码登录
    Then 创建仅信用卡类团购订单      #/api/user/order/generate
    Then 去支付_支付前检查             #/api/user/order/checkBefore
    Then 进入收银台页面      #/api/user/cashier/shoppingPayVipChannel  ##此处须判断收银台仅限信用卡
