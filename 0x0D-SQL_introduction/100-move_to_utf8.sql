-- Convert the hbtn_0c_0 database to UTF8 in the server.
ALTER TABLE `hbtn_0c_0`.`first_table` MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
