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
stories data-table (story ID, sentence, author, time)


users data-table (username, password-hash)


favorites data-table (username, storyID)

## Frontend
Nav bar on the left side with sign up, log in

Search bar

Browse menu

Username drop down menu to log out when logged in

Alerts/Notifications when stories are updated

Separate boxes for displaying stories/contributors

Favorite button for stories

Edit and save buttons on the bottom of stories

## Middleware Design

## Agenda
- [ ] 2015-10-13: Finsih overarching design, finish login system
- [ ] 2015-10-14: Finish setting datatable
- [ ] 2015-10-15: Finish adding stories
- [ ] 2015-10-16: Create favorite system
- [ ] 2015-10-17: Finish favorite
- [ ] 2015-10-18: PENTEST
- [ ] 2015-10-19: ~~submit~~
