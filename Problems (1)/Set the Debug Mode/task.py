IS_RELEASE_SERVER = True if input() == 'true' else False


DEBUG = False if IS_RELEASE_SERVER == True else True