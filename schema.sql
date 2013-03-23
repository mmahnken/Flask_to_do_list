



-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Users'
-- 
-- ---
		
CREATE TABLE `Users` (
  `id` INTEGER,
  `email` VARCHAR(64),
  `password` VARCHAR(64),
  `first_name` VARCHAR(64),
  `last_name` VARCHAR(64),
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Tasks'
-- 
-- ---		
CREATE TABLE `Tasks` (
  `id` INTEGER,
  `user_id` INTEGER,
  `title` VARCHAR(120),
  `created_at` DATETIME,
  `completed_at` DATETIME,
  PRIMARY KEY (`id`)
);

-- ---
-- Foreign Keys 
-- ---


-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Users` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Tasks` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Users` (`id`,`email`,`password`,`first_name`,`last_name`) VALUES
-- ('','','','','');
-- INSERT INTO `Tasks` (`id`,`user_id`,`title`,`created_at`,`completed_at`) VALUES
-- ('','','','','');
