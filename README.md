# Untitled
Softdev database project -- collab story engine

## Team
| Name       | Role            |
|------------|-----------------|
|Yicheng W.  | Leader          |
|Felicity N. | UX              |
|Michael M.  | Backend         |
|Sally B.    | Middleware      |

## Features
- Sign Up / login / logout
    - Sessions / automatic logout after 20 min. of inactivity
- Edit stories (1 sentence at a time with some char limit)
- View other stories (open pre-edited version)
- Sentence-based database
- Favorite a story
- Notifications

## Backend Design
### Data-tables
Stories data-table (story ID, sentence, author, time)
User data-table (username, password-hash)
Favorite data-table (username, storyID)

## Frontend

## Middleware Design
