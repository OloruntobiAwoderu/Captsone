import os
SECRET_KEY = os.urandom(32)


basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN": "oloruntobi.auth0.com",
    "ALGORITHMS": ["RS256"],
    "API_AUDIENCE": "image"
}
database_credentials = {
    "development_database": "casting",
    "test_database": "casting_test",
    "username": "postgres",
    "password": "florence",
    "port": 'localhost:5432'
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9VWXpRVFk0UmtSRU5FTXdOVGhCUXpVNU5rUTVNMEkyTVVWQk5UVkJOVFkzTTBFMFFrSkNRZyJ9.eyJpc3MiOiJodHRwczovL29sb3J1bnRvYmkuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZTc0OGJiZTQ2NDdiMDAxMzcyMzc4YiIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTkyMjIwOTI4LCJleHAiOjE1OTIzMDczMjgsImF6cCI6InR6dFEzRk84RXdvM00xNlQxR0Q5MUd6WmxkY0JFZ1hkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.gkNyX8S_mhayn-xxj3AUaKILAWmr4y7v6YoWVJsiAnY-ssiVL2h0L6Zu8il7Z9mCe3Rm9zeRyRqH2j-sf2s9gZdR-ojVQwu9NQYsfhpZFUfTBIetxJk-GU8dMybeRqQxcnhvqsVp6fwptSF5eYX3kN8B_uOIJ6oyo5y1tWSl_MEY4p3nbqxtNbFZ5zCsv_NaSIq-UglPnTdB8TD_0HgF8sEhNITgvmrsA1zGHuL2tQ2Eo3BGIu1hcP5vuT2OkPPhKe2ri0MV3So8d_n_luCFsiIskSThXdkep_vW08MNxaNQM3GuNX5M-OYQwWeVtn2AkuGBDL3Jko8ngQwPS-FW2w",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9VWXpRVFk0UmtSRU5FTXdOVGhCUXpVNU5rUTVNMEkyTVVWQk5UVkJOVFkzTTBFMFFrSkNRZyJ9.eyJpc3MiOiJodHRwczovL29sb3J1bnRvYmkuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZTc0ODVhOTIyZDEzMDAxOTE4NjVmZiIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTkyMjIxNDA1LCJleHAiOjE1OTIzMDc4MDUsImF6cCI6InR6dFEzRk84RXdvM00xNlQxR0Q5MUd6WmxkY0JFZ1hkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.pzJF7l1f6VvIT80A-UcHwCHGIlPPNqC2JcM_VP-cFthyvPajo50ccRM7AEq0-vMDkdDhOBrgtlNmDzWmkCHHTFat2Lb56QUbPUflQBdMDTPA7_ekLhXwe_0feHhslTwS4X2QnsuEaBH7BBQZTUl60QOJXlgJfJEkTPTQmgl7a02wtU0iywVLJ6srXVTqY6wHbmtyYRi1v6bOASQfhsB9JbVWianYBYD8d-umfpwbe6lsPvXONA3LJtQfwW60z5v-Ek7crVrOzw9rEcX-kxdjcj6ReVkSbWpv2RS9p0PDbhLNH6Lf7b5K7krVVdmF7mAT6b_9MUgPecEbnIOsQSL-rg",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9VWXpRVFk0UmtSRU5FTXdOVGhCUXpVNU5rUTVNMEkyTVVWQk5UVkJOVFkzTTBFMFFrSkNRZyJ9.eyJpc3MiOiJodHRwczovL29sb3J1bnRvYmkuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZTc0ODE3MGZmNTAyMDAxMzdmNjgzMSIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTkyMjIxMTY5LCJleHAiOjE1OTIzMDc1NjksImF6cCI6InR6dFEzRk84RXdvM00xNlQxR0Q5MUd6WmxkY0JFZ1hkIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBvc3Q6YWN0b3JzIl19.m1t1RFlr3RsOFLGj390E-ySxKZGbkO7h8Nd6MOZjwQtrZjA87nJyuqXvCgxicnFHPtE4JP20ZMjCa5hxn2e_lhK5etOq2Xriori3xRFjaM0vLxB7q_Gp18qZI6b8SWFa58jhqmAXCgUKBOUlSI4nsMo2hUFzYGHt2v0wFDl8eBEJ4vS2rYImuPeIelRT5zP5Q0TLZpMWQh0nkHiwhzamViCZK8_ehO1KyYQ-BhMSWlCRi7EAvSuINXiek1o44_bwfFSZlSIVhAfSulU1cFfWRNxkkoAhm5kZwJ2xk9Za4Zyjv5ejgTtT1H3cq14xHUjdc0iyWKoGpeh2GEIWaqVHqw"
}

pagination = {
    "views_per_page": 10
}

