# endterm_CSCS5118_2023
Mini news portal.

Urls:

GET news/ - gets all news from all moderators. Does not require auth

POST auth/ - generate auth token for moderators

POST news/create - creating news. Needs auth. Only for moderators

GET news/by-token - gets all news of authorized moderator

PUT news/:id/update - changes news of moderator

Postman collection: https://galactic-zodiac-385481.postman.co/workspace/web-2023~6ab735d1-0625-46db-959f-9c75dc753b66/collection/10483724-00cc8fc2-b607-469f-85c5-1609753ceb8b?action=share&creator=10483724

Or can use browser to test handlers while running locally:
![Screenshot from 2023-12-15 23-38-32](https://github.com/Defaultse/endterm_CSCS5118_2023/assets/45491587/9e0d4476-dc2b-4204-a798-cb968145ea60)
