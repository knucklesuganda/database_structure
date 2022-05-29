import environs


env = environs.Env()
env.read_env('.env')

DATABASE_URL = env("DATABASE_URL")
