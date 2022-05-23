Feature: 安徽社区个人端自动化用例集

  Scenario: 手机号验证码登录
    When 手机个人端登录获取验证码
    Then 手机个人端登录

  Scenario: 手机号密码登录
    When 手机个人端登录获取验证码
    Then 手机个人端登录