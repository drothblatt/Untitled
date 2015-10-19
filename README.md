# Untitled
Softdev database project -- collab story engine

> I wanted a perfect ending. Now I've learned, the hard way,
> that some poems don't rhyme, and some stories don't have a clear beginning,
> middle, and end.Life is about not knowing, having to change, taking the moment
> and making the best of it, without knowing what's going to happen next.
> Delicious Ambiguity.
>
>                               -Gilda Radner

## Team
| Name       | Role            |
|------------|-----------------|
|Yicheng W.  | Leader          |
|Felicity N. | UX              |
|Michael M.  | Backend         |
|Sally B.    | Middleware      |

## Description
This is a crowd-writing engine in which everyone can contribute to a story. In
this place, everyone can create their own story or edit the existing work of
someone else. However, there is a catch that one person can enter 140
characters (or 300 if they're creating a story) at a time. This way, the
final story would be an interesting mix of different people's inputs.

The site also allows individual users to favorite or bookmark stories they like
and get updates about them in their home page.

## Design and Toolset
### Backend
This project was built with sqlite3 and flask on the back end. It has 3 main
data-tables, one holding stories, one holding the users, and one holding the
favorites.

Each story is assigned an ID number. The stories data table has columns id,
sentence, author and time. Whever an author adds a new sentence, a new row is
added into the stories data table. The story is then gathered by sorting all
sentences by time stamp. With the first sentence being the title, and
everything else making up the story.

The favorite data table has columns of user and story id, and it's just simple
lookup/addition/deletion to check/add/remove favorites.

The user data table is pretty standard, with columns of username and hash of the
password.

### Frontend
The front end of the project is built with jinja2, bootstrap and jQuery. There
is a master html which makes up the heading and is extended by every other page.
For the most part is is pretty standard.

#### Routes
- home
- about
- login/logout
- register
- browse
- create
- edit

## Agenda
- [x] 2015-10-13: Finsih overarching design, finish login system
- [x] 2015-10-14: Finish setting datatable
- [x] 2015-10-15: Finish adding stories
- [x] 2015-10-16: Create favorite system
- [x] 2015-10-17: Finish favorite
- [x] 2015-10-18: PENTEST
- [ ] 2015-10-19: Demo
