import pymysql
import config


def insert_data(username, msg, groupnum, date, is_image):
    try:
        # 连接到数据库
        conn = pymysql.connect(
            host=config.database["host"],
            user=config.database["user"],
            password=config.database["password"],
            database=config.database["database"]
        )

        # 创建一个游标对象
        cursor = conn.cursor()

        group_name = "group_" + groupnum

        # 执行插入数据的SQL语句
        cursor.execute("USE user_msg_db")
        insert_sql = "INSERT INTO {} (username, msg, date, isImage) VALUES (%s, %s, %s, %s)".format(group_name)
        cursor.execute(insert_sql, (username, msg, date, is_image))

        # 提交更改
        conn.commit()

        # 关闭连接
        conn.close()

        return "Data inserted successfully"
    except Exception as e:
        return "Error: " + str(e)


# 调用接口插入数据
# result = insert_data("John", "Hello, how are you?", "test", "2022-01-01 12:00:00", 0)
# print(result)
