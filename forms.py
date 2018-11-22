from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Regexp


# DataRequired() 防止传空格！
class addUserForm(FlaskForm):
    username = StringField('username',
                       validators=[
                           # Length(max=18, min=6, message="name长度需在6-18个字符间"),
                           Regexp(r"^[a-zA-Z][a-zA-Z0-9_]{4,15}$", message="字母开头，允许5-16字节，允许字母数字下划线"),
                           DataRequired()])

    password = PasswordField('password',
                             validators=[
                                 # Length(max=20, min=8, message="password长度需在6~18个字符间"),
                                         Regexp(r"^[a-zA-Z]\w{5,17}$",message="以字母开头，长度在6~18之间，只能包含字母、数字和下划线"),
                                         DataRequired()])

'''
WTForms支持的HTML标准字段
StringField 文本字段
TextAreaField 多行文本字段
PasswordField 密码文本字段
HiddenField 隐藏文本字段
DateField 文本字段，值为 datetime.date 格式
DateTimeField 文本字段，值为 datetime.datetime 格式
IntegerField 文本字段，值为整数
DecimalField 文本字段，值为 decimal.Decimal
FloatField 文本字段，值为浮点数
BooleanField 复选框，值为 True 和 False
RadioField 一组单选框
SelectField 下拉列表
SelectMultipleField 下拉列表，可选择多个值
FileField 文件上传字段
SubmitField 表单提交按钮
FormField 把表单作为字段嵌入另一个表单
FieldList 一组指定类型的字段

常见的验证函数
Email 验证电子邮件地址
EqualTo 比较两个字段的值；常用于要求输入两次密码进行确认的情况
IPAddress 验证 IPv4 网络地址
Length 验证输入字符串的长度
NumberRange 验证输入的值在数字范围内
Optional 无输入值时跳过其他验证函数
Required 确保字段中有数据
Regexp 使用正则表达式验证输入值
URL 验证 URL
AnyOf 确保输入值在可选值列表中
NoneOf 确保输入值不在可选值列表中
'''