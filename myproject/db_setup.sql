CREATE TABLE "user_accounts" (
	"user_id" SERIAL PRIMARY KEY,
	"user_name" VARCHAR(255) NOT NULL,
	"email_address" VARCHAR(255) NOT NULL,
	"password_hash" VARCHAR(255) NOT NULL
);

CREATE TABLE "user_posts" (
	"post_id" SERIAL PRIMARY KEY,
	"subject" VARCHAR(100) NOT NULL,
	"main_post_content" VARCHAR(255) NOT NULL,
	"date_created" TIMESTAMP NOT NULL,
	"user_id" INTEGER NULL DEFAULT NULL,
	CONSTRAINT "user_id" FOREIGN KEY ("user_id") REFERENCES "user_accounts" ("user_id") ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE "post_replies" (
	"reply_id" SERIAL PRIMARY KEY,
	"post_id" INTEGER NOT NULL,
	"user_id" INTEGER NULL DEFAULT NULL,
	"reply_content" VARCHAR(255) NOT NULL,
	"date_created" TIMESTAMP NOT NULL,
	CONSTRAINT "post_id" FOREIGN KEY ("post_id") REFERENCES "user_posts" ("post_id") ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT "user_id" FOREIGN KEY ("user_id") REFERENCES "user_accounts" ("user_id") ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE "recipe_calories" (
	"recipe_id" SERIAL PRIMARY KEY,
	"recipe_name" VARCHAR(100) NOT NULL,
	"calories" INTEGER NOT NULL
);

INSERT INTO recipe_calories ("recipe_name", "calories") VALUES
	('Chicken Quesadilla', 315),
	('Roasted Brussels Sprouts', 164),
	('Green Beans Almondine', 79),
	('Lemon Rosemary Salmon', 226),
	('Orange Honey Chicken', 216),
	('Sweet Potato Chips', 61),
	('White Bean Soup', 351),
	('Thai Basil Chicken', 220),
	('Italian Parmesean Chicken', 290);
