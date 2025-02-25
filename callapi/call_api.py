import base64
import hashlib
import json
import time
import requests

def get_timestamp_and_sign(app_id, app_secret):
    """ 获取时间戳和签名 """
    # 获取时间戳
    timestamp = str(int(time.time() * 1000))
    # 获取签名
    # 拼接 appId, appSecret 和 timestamp
    to_hash = f"{app_id}{app_secret}{timestamp}"
    print('to_hash:', to_hash)
    # 计算 MD5 哈希值
    md5_hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
    print("md5_hash:", md5_hash)
    # Base64 编码
    sign = base64.b64encode(md5_hash.encode('utf-8')).decode('utf-8')
    return timestamp, sign


def generate_insert_sql(data, year, terms):
    """ 生成批量插入 SQL 语句 """
    table_name = "temp_bks_xk"
    columns = ["课程序号", "学号", "学年", "学期"]

    # 创建批量插入语句的开头
    insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES "

    # 创建插入的每一行
    values = []
    for record in data:
        try:
            # 检查每个字段是否存在
            course_code = record.get('课程序号', '')
            student_id = record.get('学号', '')
            academic_year = record.get('学年', '')
            term = record.get('学期', '')

            # 学年学期必须是函数的参数
            if academic_year != year or term != terms:
                continue

            # 根据每个记录的值创建对应的插入值
            values.append(f"('{course_code}', '{student_id}', '{academic_year}', '{term}')")
        except KeyError as e:
            print(f"Missing key: {e} in record {record}")
            continue

    # 将所有的插入值合并为一个字符串
    if values:
        insert_sql += ", ".join(values)
        return insert_sql

    return None


def save_sql_to_file(sql, file_path):
    """ 将 SQL 保存到文件中 """
    try:
        # 如果文件不存在，程序会创建文件
        with open(file_path, 'a', encoding='utf-8') as f:  # 使用 'a' 模式进行追加写入
            f.write(sql + ";\n")  # 在 SQL 语句后面加上分号并换行
        print(f"SQL successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving SQL to file: {e}")


if __name__ == '__main__':
    app_id = '*******'
    app_secret = '**********'
    academic_year = '2024-2025'
    term = '2'

    url = 'https://cdsp.nwupl.edu.cn/cdsp/data-api/v2/cdsp_1676530906380193794'
    headers = {
        'appId': app_id,
        'appSecret': app_secret,
        'Content-Type': 'application/json'
    }

    params = {
        '$skip': 0,
        '$count': 'true'
    }

    # 设置保存的 SQL 文件路径
    sql_file_path = "batch_insert.sql"

    for i in range(59):
        print(f'第:{i + 1}页')

        (timestamp, sign) = get_timestamp_and_sign(app_id, app_secret)
        params['$skip'] = i * 10000
        headers['timestamp'] = timestamp
        headers['sign'] = sign

        print("querying... url:", url, "params:", params, "headers:", headers)

        response = requests.get(url, headers=headers, params=params)

        # 检查请求是否成功
        if response.status_code == 200:
            print("Response Content:", response.text)
            try:
                # 解析响应中的 JSON 数据
                data = json.loads(response.text)["value"]

                # 生成批量插入的 SQL 语句
                insert_sql = generate_insert_sql(data, academic_year, term)

                # 保存 SQL 到文件
                if insert_sql:
                    save_sql_to_file(insert_sql, sql_file_path)
            except json.JSONDecodeError:
                print("Failed to parse JSON response")
        else:
            print("Request failed with status code:", response.status_code, ' text:', response.text)
            break