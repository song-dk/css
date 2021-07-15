# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 11:07
# @Author : songdk
# @File : css.py
# @Software: PyCharm

from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context():
    """ You can generate your context separately since you may deal with a lot
        of documents. You can carry out computations, etc in here and make the
        context look like the sample below.
    """
    return {
        'cg_date':"1234",
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


def from_template(template, signature):
    target_file = BytesIO()

    template = DocxTemplate(template)
    context = get_context()  # gets the context used to render the document

    img_size = Cm(7)  # sets the size of the image
    sign = InlineImage(template, signature, img_size)
    context['signature'] = sign  # adds the InlineImage object to the context

    target_file = BytesIO()
    template.render(context)
    template.save(target_file)

    return target_file
