import csv
import re
import pymysql
import datetime
from jsonpath_ng import parse
import json

class Tools:
    def get_current_time(self):
        # 获取当前系统时间
        now = datetime.datetime.now()
        # 格式化为 xxxx-xx-xx xx:xx:xx
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
    #把csv文件读成列表
    def csv_to_dict_list(self,file_path, encoding='utf-8'):
        with open(file_path, mode='r', encoding=encoding) as file:
            csv_reader = csv.DictReader(file)  # 使用 DictReader 自动解析表头
            return list(csv_reader)  # 转换为列表，每个元素是一个字典

    def get_str_by_re(self,text, left_boundary=None, right_boundary=None):
        """
        根据左右边界提取文本内容（非贪婪模式）

        参数:
            text: 要提取的原始文本
            left_boundary: 左边界字符串，默认为字符串开始
            right_boundary: 右边界字符串，默认为字符串结束

        返回:
            提取到的文本内容，如果未找到返回None
        """
        # 处理左边界
        if left_boundary is None:
            left_pattern = r'^'
        else:
            left_pattern = re.escape(left_boundary)

        # 处理右边界
        if right_boundary is None:
            right_pattern = r'$'
        else:
            right_pattern = re.escape(right_boundary)

        # 构建完整正则表达式（使用非贪婪模式）
        pattern = f'{left_pattern}(.*?){right_pattern}'

        # 进行匹配
        match = re.search(pattern, text, re.DOTALL)

        if match:
            return match.group(1)
        return None

    def sql_runner(self,sql):
        # 1.创建数据连接
        con = pymysql.connect(
            user='root',
            password='root',
            host='localhost',
            port=3306,
        )
        # 2.创建一个游标(语句执行器)
        cur = con.cursor()
        #3.执行sql
        cur.execute(sql)
        #4.提交事务
        con.commit()
        #5.存储查询结果
        result = cur.fetchall()
        #6.关闭数据库
        con.close()
        #7.返回查询结果
        return result

    def get_jsonpath_value(self, data, jsonpath_expr):
        """
        使用 jsonpath-ng 获取 JSONPath 对应的值

        Args:
            data: JSON 对象或 JSON 字符串
            jsonpath_expr: JSONPath 表达式

        Returns:
            匹配的值或值列表
        """
        # 如果输入是字符串，先解析为 JSON
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError as e:
                raise ValueError(f"无效的 JSON 字符串: {e}")

        # 解析 JSONPath 表达式
        jsonpath_expr = parse(jsonpath_expr)

        # 执行匹配
        matches = [match.value for match in jsonpath_expr.find(data)]

        # 根据匹配结果返回
        if not matches:
            return None
        elif len(matches) == 1:
            return matches[0]
        else:
            return matches

    def count_string_elements(self, text):
        """
        统计字符串中的字母、数字和符号数量
        :param text: 输入的字符串
        :return: 包含统计结果的字典
        """
        letters = 0
        digits = 0
        symbols = 0
        
        for char in text:
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                digits += 1
            else:
                symbols += 1
                
        return {
            "letters": letters,
            "digits": digits,
            "symbols": symbols
        }

if __name__ == '__main__':
    goods_name = '自动化测试数据'+Tools().get_current_time()
    print(goods_name)