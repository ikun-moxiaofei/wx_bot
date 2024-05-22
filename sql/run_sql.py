import pymysql
import config

# 连接到数据库
conn = pymysql.connect(
    host=config.database["host"],
    user=config.database["user"],
    password=config.database["password"],
    database=config.database["database"]
)

# 创建一个游标对象
cursor = conn.cursor()

# 创建数据库
create_db_sql = "CREATE DATABASE IF NOT EXISTS user_msg_db"
cursor.execute(create_db_sql)

# 切换到新创建的数据库
cursor.execute("USE user_msg_db")

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_test (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT '测试群组',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_1 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群1',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_2 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群2',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_3 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群3',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_4 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群4',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_5 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群5',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_6 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群6',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_7 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群7',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_8 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群8',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_9 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群9',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_10 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群10',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_11 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群11',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_12 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群12',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_13 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群13',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_14 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群14',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_15 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群15',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 执行建表SQL语句
create_table_sql = """
CREATE TABLE IF NOT EXISTS group_16 (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  msg MEDIUMTEXT NOT NULL,
  groupname VARCHAR(256) NOT NULL DEFAULT 'QAnything官方交流群16',
  date DATETIME NOT NULL,
  isImage INT DEFAULT 0 NOT NULL,
  PRIMARY KEY (id)
);
"""
cursor.execute(create_table_sql)

# 提交更改
conn.commit()

# 关闭连接
conn.close()

print("创建成功")
