/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50017
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50017
File Encoding         : 65001

Date: 2011-11-01 01:07:22
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `t1`
-- ----------------------------
DROP TABLE IF EXISTS `t1`;
CREATE TABLE `t1` (
  `key1` int(11) default NULL,
  `text_pole1` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t1
-- ----------------------------
INSERT INTO `t1` VALUES ('1', 'text1t1');
INSERT INTO `t1` VALUES ('2', 'text2t1');
INSERT INTO `t1` VALUES ('3', 'text3t1');

-- ----------------------------
-- Table structure for `t2`
-- ----------------------------
DROP TABLE IF EXISTS `t2`;
CREATE TABLE `t2` (
  `key1` int(11) default NULL,
  `text_pole2` text,
  `key2` int(11) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t2
-- ----------------------------
INSERT INTO `t2` VALUES ('1', 'text1t2', '11');
INSERT INTO `t2` VALUES ('2', 'text2t2', '22');
INSERT INTO `t2` VALUES ('3', 'text3t3', '33');

-- ----------------------------
-- Table structure for `t3`
-- ----------------------------
DROP TABLE IF EXISTS `t3`;
CREATE TABLE `t3` (
  `key2` int(11) default NULL,
  `text_pole3` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t3
-- ----------------------------
INSERT INTO `t3` VALUES ('11', 'pole3');
INSERT INTO `t3` VALUES ('22', 'pole33');
INSERT INTO `t3` VALUES ('33', 'pole444');
