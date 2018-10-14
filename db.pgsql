CREATE TABLE users_jokes(
                user_id SERIAL PRIMARY KEY,
                password hstore NOT NULL,
                jokes ARRAY,
                ip INET NOT NULL,
                request_timedate TIMESTAMP,
            )