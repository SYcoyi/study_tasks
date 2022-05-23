Feature: 安徽社区个人端创建名优特惠订单并支付

  Scenario:创建名优特惠订单并现金支付
    When 手机个人端密码登录
    Then 创建名优特惠订单    #/api/user/order/generate
    Then 现金支付     #/api/user/cashier/payOrders
    Then 获取支付结果     #/api/user//order/getPayRes

  Scenario:创建名优特惠订单并积分支付
    When 手机个人端密码登录    #帐号须有积分
    Then 创建名优特惠积分支付订单
    Then 获取支付结果      #/api/user//order/getPayRes


  Scenario:创建名优特惠订单并积分+现金支付
    When 手机个人端密码登录     #帐号须有积分
    Then 创建名优特惠订单并勾选积分选项
    Then 积分+现金支付
    Then 获取支付结果    #/api/user//order/getPayRes
