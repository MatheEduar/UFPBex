class FacadeSingleton:
    _instance = None

    def new(cls):
        if cls._instance is None:
            cls._instance = super(FacadeSingleton, cls).new(cls)
            cls._instance.repository = RepositoryFactory.create_user_repository()
        return cls._instance

    def add_user(self, username, password):
        user = User(username, password)
        self.repository.create_user(user)

    def get_user(self, username):
        return self.repository.get_user_by_username(username)

    def get_all_users(self):
        return self.repository.get_all_users()

    def update_user(self, username, userChange):
        user = self.repository.get_user_by_username(username)
        if user:
            user.username = userChange
            self.repository.update_user(user)

    def delete_user(self, username):
        self.repository.delete_user(username)