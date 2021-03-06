# _*_coding:utf-8_*_
# @Time:2022/5/4 10:01
# @Author:Young
# @File:test2
import requests
url = "http://118.25.228.118:8082/createOrderApi.htm?param="
data = {
            "buyerid": "",
            "order_piece": "件数，小包默认1，快递需真实填写",
            "consignee_mobile": "手机号,选填。为方便派送最好填写",
            "order_returnsign": "退回标志，默认N表示不退回，Y标表示退回。中邮可以忽略该属性",
            "trade_type": "ZYXT",
            "duty_type": "DDU或DDP",
            "battery_type": "电池类型代码，联系货代提供",
            "consignee_name": "收件人,必填",
            "consignee_companyname": "收件公司名,如有最好填写",
            "consignee_address": "收件地址街道，必填",
            "consignee_telephone": "收件电话，必填",
            "country": "收件国家二字代码，必填",
            "consignee_state": "州/省",
            "consignee_city": "城市",
            "consignee_suburb": "收件区，选填",
            "consignee_postcode": "邮编，有邮编的国家必填",
            "consignee_passportno": "收件护照号，选填",
            "consignee_email": "邮箱，选填",
            "consignee_taxno": "收件人税号",
            "consignee_streetno": "街道号",
            "consignee_doorno": "门牌号",

            "shipper_taxnotype": "税号类型，邮政产品可选值：IOSS,NO-IOSS,OTHER；DHL可选值：SDT、VAT、FTZ、DAN、EOR、CNP、EIN等(类型说明参照文档底部“DHL发件人税号类型”)",
            "shipper_taxno": "发件人税号",
            "shipper_taxnocountry": "发件人税号国家,用国家二字码",
            "customer_id": "客户ID，必填",
            "customer_userid": "登录人ID，必填",
            "order_customerinvoicecode": "原单号，必填",
            "product_id": "运输方式ID，必填",
            "weight": "总重，选填，如果sku上有单重可不填该项",
            "product_imagepath": "图片地址，多图片地址用分号隔开",
            "order_transactionurl": "产品销售地址",
            "order_cargoamount": "选填；用于DHL/FEDEX运费；或用于白关申报（订单实际金额，特殊渠道使用）；或其他用途",
            "order_insurance": "保险金额",
            "cargo_type": "包裹类型，P代表包裹，D代表文件，B代表PAK袋",
            "order_customnote": "自定义信息",
            "orderInvoiceParam": [{
                        "invoice_amount": "申报总价值，必填",
                        "invoice_pcs": "件数，必填",
                        "invoice_title": "英文品名，必填",
                        "invoice_weight": "单件重",
                        "sku": "中文品名",
                        "sku_code": "配货信息",
                        "hs_code": "海关编码",
                        "transaction_url": "销售地址",
                        "invoiceunit_code": "申报单位",
                        "invoice_imgurl": "图片地址",
                        "invoice_brand": "品牌",
                        "invoice_rule": "规格",
                        "invoice_currency": "申报币种",
                        "invoice_taxno": "税则号",
                        "origin_country": "原产国",
                        "invoice_material": "材质",
                        "invoice_purpose": "用途"
            }],
            "orderVolumeParam": [{
                        "volume_height": "高，单位CM",
                        "volume_length": "长，单位CM",
                        "volume_width": "宽，单位CM",
                        "volume_weight": "实重"
            }]
}
resp = requests.post(url,json=data)
print(resp.json())