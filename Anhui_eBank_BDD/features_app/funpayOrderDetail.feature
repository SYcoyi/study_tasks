Feature: 安徽社区个人端信e付订单列表/详情

  Scenario: 信e付订单列表展示
    When 手机个人端密码登录
    Then 我的订单_信e付订单     #/api/funpay/logic/acquiring/queryPersonOrderApp
    Then 我的订单_信e付订单_交易成功      #接口同上，使用不同参数来进行筛选
    Then 我的订单_信e付订单_交易关闭


  Scenario: 信e付订单详情页
    When 手机个人端密码登录
    Then 我的订单_信e付订单     #/api/funpay/logic/acquiring/queryPersonOrderApp
    Then 信e付订单详情页      #/api/funpay/logic/acquiring/queryPersonOrderDetail   进入任一订单