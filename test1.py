"""
 * Project name(项目名称)：Python_try_except_else
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:17
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    try:
        divisor = int(input('请输入除数:'))
        result = 34 / divisor
    except ValueError as e:
        print("输入的不是整数")
        print(str(e))
    except ArithmeticError as e:
        print("除数为0")
        print(str(e))
    except:
        print("其它错误")
    else:
        print("没有发现错误")
    print("程序结束")
