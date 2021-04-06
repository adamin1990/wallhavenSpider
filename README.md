wallhaven spider by scrapy

1. create database   

```
CREATE DATABASE `wallhaven` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
```

2. create table

```
CREATE TABLE `wallhaven`.`Untitled`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `wid` char(20) NOT NULL DEFAULT '',
  `src` varchar(255) NOT NULL DEFAULT '',
  `width` int(6) NOT NULL DEFAULT 0,
  `height` int(6) NOT NULL DEFAULT 0,
  `tags` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `wid`(`wid`) USING BTREE
);
```

3. scrapy crawl wallhaven