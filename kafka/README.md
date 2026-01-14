```
# 后台启动所有服务 
docker-compose up -d
# 查看容器状态 
docker-compose ps

# 进入任意一个 Kafka 容器（比如 kafka1）
docker exec -it kafka1 bash

# 列出 Kafka 集群节点
kafka-topics --bootstrap-server kafka1:29092 --list

# 创建测试主题（验证集群写入）
kafka-topics --bootstrap-server kafka1:29092 --create --topic test-topic --partitions 3 --replication-factor 3

# 查看主题详情（确认副本分布在 3 个节点）
kafka-topics --bootstrap-server kafka1:29092 --describe --topic test-topic

# 生产消息
kafka-console-producer --bootstrap-server kafka1:29092 --topic test-topic

# 另开一个终端，消费消息
docker exec -it kafka1 bash
kafka-console-consumer --bootstrap-server kafka1:29092 --topic test-topic --from-beginning

# 停止集群
docker-compose down

# 停止并删除数据卷（谨慎：会清空所有数据）
docker-compose down -v
```