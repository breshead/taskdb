PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
-- INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$12000$UrwMiHq2egOG$/zqi8neTuiwX0Pbglc5tNzQBNEBhSdiy41Yo1nJJHvw=','2016-10-11 20:42:12.320172',1,'admin','','','doug@jshfarms.com',1,1,'2016-10-06 19:00:08.330845');
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$12000$UrwMiHq2egOG$/zqi8neTuiwX0Pbglc5tNzQBNEBhSdiy41Yo1nJJHvw=','2016-09-01',0,'Test1','One','test1@gmail.com',1,1,'2016-09-01','test1');
INSERT INTO "auth_user" VALUES(3,'pbkdf2_sha256$12000$UrwMiHq2egOG$/zqi8neTuiwX0Pbglc5tNzQBNEBhSdiy41Yo1nJJHvw=','2016-09-01',0,'Test2','Two','test2@gmail.com',1,1,'2016-09-01','test2');
INSERT INTO "auth_user" VALUES(4,'pbkdf2_sha256$12000$UrwMiHq2egOG$/zqi8neTuiwX0Pbglc5tNzQBNEBhSdiy41Yo1nJJHvw=','2016-09-01',0,'Test3','Three','test3@gmail.com',1,1,'2016-09-01','test3');
INSERT INTO "auth_user" VALUES(5,'pbkdf2_sha256$12000$UrwMiHq2egOG$/zqi8neTuiwX0Pbglc5tNzQBNEBhSdiy41Yo1nJJHvw=','2016-09-01',0,'Test4','Four','test4@gmail.com',1,1,'2016-09-01','test4');

INSERT INTO "taskgui_ttype" VALUES(1,'Task');
INSERT INTO "taskgui_ttype" VALUES(2,'Issue');
INSERT INTO "taskgui_ttype" VALUES(3,'R&D');
INSERT INTO "taskgui_ttype" VALUES(4,'Project');
INSERT INTO "taskgui_ttype" VALUES(5,'Idea');

INSERT INTO "taskgui_status" VALUES(1,'Created');
INSERT INTO "taskgui_status" VALUES(2,'In Progress');
INSERT INTO "taskgui_status" VALUES(3,'On Hold');
INSERT INTO "taskgui_status" VALUES(4,'Completed');
INSERT INTO "taskgui_status" VALUES(5,'Cancelled');
INSERT INTO "taskgui_status" VALUES(6,'Unknown');
INSERT INTO "taskgui_status" VALUES(7,'Someday');

INSERT INTO "taskgui_tag" VALUES(1,'Irrigation','Relates to the irrigation system');
INSERT INTO "taskgui_tag" VALUES(2,'Paperless','Relates to going paperless');
INSERT INTO "taskgui_tag" VALUES(3,'Legal','Relates to legal work or documentation');
INSERT INTO "taskgui_tag" VALUES(4,'Network','Releates to the physical farm network');


INSERT INTO "taskgui_context" VALUES(1,'Office');
INSERT INTO "taskgui_context" VALUES(2,'Still');
INSERT INTO "taskgui_context" VALUES(3,'Home');
INSERT INTO "taskgui_context" VALUES(4,'Phone');
INSERT INTO "taskgui_context" VALUES(5,'In Town');

COMMIT;
