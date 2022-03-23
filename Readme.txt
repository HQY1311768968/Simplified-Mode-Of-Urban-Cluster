1.运行RunAllModelFinal.py进行自动建模、时程分析及结果输出；
2.需要修改的参数为RunAllModelFinal.py里的：
(1)14行的ID修改为需要的结构在表格里的顺序集，ID为list格式变量；
(2)16行的循环开始的range(1,2)相应的改为输入的ID的长度；
(3)62行的地震波数量，其余地震波的相应信息在GroundMotionAccel和GroundMotionInfo内对应修改；