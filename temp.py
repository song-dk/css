# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 14:22
# @Author : songdk
# @File : temp.py
# @Software: PyCharm
from docxtpl import  DocxTemplate

doc = DocxTemplate("1.docx")
context = {'cg_date':"1234",
           'cg_num':"43212",
           'so_num':"211431",
           'merchant_id':"23532",
           'brand_name':"beuwi",
           'booth_num':"231",
           'sd_num':"12314",
           'sa':"213",
           'pay':"213",
           'pay_upper':"贰佰壹拾叁圆整",
           'balance':"2",
           'cg':"埼玉",
           'row_contents':[
               {
                   'method':"微信",
                   'money':"30"
               },  {
                   'method':"支付宝",
                   'money':"30"
               },  {
                   'method':"现金",
                   'money':"30"
               },  {
                   'method':"刷卡",
                   'money':"30"
               }
           ]
        }
doc.render(context)
doc.save("3.docx")