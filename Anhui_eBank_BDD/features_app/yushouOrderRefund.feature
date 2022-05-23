Feature: 安徽社区个人端名优特惠订单退款

  Scenario:进入名优特惠退款页面发起退款
    When 手机个人端密码登录
    Then 创建名优特惠订单    #/api/user/order/generate
    Then 现金支付     #/api/user/cashier/payOrders
    Then 获取支付结果     #/api/user//order/getPayRes
    Then 申请退款_进入申请退款页      #/api/user/view/refundInfo
    Then 申请退款_选中商品种类/数量    #/api/user/refund/do
    Then 提交退款申请          #/api/user/refund/do
    Then 退款详情页展示       #/api/user/refund/details

  Scenario:银行端退款审核    ##待定
    When 银行端省联社登录
    Then  初审通过
    Then  复审通过
