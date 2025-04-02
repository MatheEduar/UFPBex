class RepositoryFactory:
    @staticmethod
    def create_user_repository():
        return UserRepositoryImpl()