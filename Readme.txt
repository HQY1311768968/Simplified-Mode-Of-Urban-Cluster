1.运行RunAllModelFinal.py进行自动建模、时程分析及结果输出；
2.需要修改的参数为RunAllModelFinal.py里的：
(1)'ID = list(range(1,946))':为需要的结构在表格里的顺序集，ID为list格式变量；
   'ii in range(1,946)':修改为对应ID的长度的循环数；
(2)'numberOfRunIDs = 44':地震波数；
(3)'AllScales = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]':IDA强度缩放系数
(4)其余地震波的相应信息在GroundMotionAccel和GroundMotionInfo内对应修改；
