# Sy54315_test
UI自动化测试框架基于python-selenium-unittest-HTMLTestRunner

互联网公司更新迭代比较快，版本发布频率较高，在每次上线之前要做一次整体的回归测试，所以留给测试人员的时间并没有很多，
实施UI自动化测试，构建到jenkins上进行周期的运行，提测后，或者上线前都会进行运行测试，保障每一次更新迭代功能不受影响。

框架主要使用了page_obje模式，对每个页面进行封装，需要操作时直接调用封装的方法，这样做的好处是如果页面发生变化，不需要
去调整用例，只需要对封装的方法进行调整。
