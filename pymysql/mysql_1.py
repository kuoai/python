# -*- coding: utf-8 -*-
import pymysql
db = pymysql.connect("localhost", "root", "123456", "abc")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS info01")
sql="""CREATE TABLE `info01` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `salary` int(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `grade` varchar(255) NOT NULL,
  `company` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=498 DEFAULT CHARSET=utf8;"""
cursor.execute(sql)


# 关闭数据库
db.close()

