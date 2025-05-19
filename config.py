class Config:
    SECRET_KEY = 'compaq123456789'
    SQLALCHEMY_DATABASE_URI = 'postgresql://trainee:compaq123@localhost:5432/flasktrainee'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = 1800  # 30 minutes
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True