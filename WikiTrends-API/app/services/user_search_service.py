from app.repositories.user_search_repository import UserSearchRepository
from app.models.user_search import UserSearch
from datetime import datetime

class UserSearchService:
    def __init__(self, db_config):
        self.user_search_repository = UserSearchRepository(db_config)
        self.user_search_repository.create_search_results_view()

    async def insert_user_search(self, search_term):
        user_search = UserSearch(search_date=datetime.now(), search_term=search_term)
        await self.user_search_repository.create(user_search)

    async def get_search_results(self, search_term):
        search_results = await self.user_search_repository.get_search_results(search_term)
        return search_results
