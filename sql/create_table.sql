create table if not exists user_msg_db.`group_test`
(
  `id` bigint not null auto_increment comment '主键' primary key,
  `username` varchar(256) not null comment '用户名',
  `msg` MEDIUMTEXT not null comment '用户消息',
  `groupNum` VARCHAR(256) not null comment '群号',
  `date` datetime not null comment '时间戳',
  `isImage` int default 0 not null comment '是否为图片(0为不是图片,1为是,默认为0)'
)
comment '测试数据';