Idea: sort of like SWAPI, this api stores data on Chinese characters and their equivalent cangjie inputs. Users can use the API told build their own set of data, or make use of "base" data on most common input characters. Users, in this case, must create and connect to their own db instance.

Can use get methods without authentication; post/patch/delete require unique db connection

Possible issues - 
lots of raw data entry to setup initial base data, unless I can scrape the wiki 
    
  Who are the developers that could benefit from your API (their domain, needs, goals, and so on)?
    -anyone who's building an open source app that needs to incorporate cangjie input on qwerty keyboards

  How can you incorporate their needs into your API?
    -easy to use UI accessible anywhere 

  How can you provide a better developer experience?
    -thorough documentation, bundling, 
  
  Tools you need to provide along with your API (developer programs, SDKs, documentation, educational resources, and so forth).
    -base data set they can build on according to their needs


  Routing
    GET - fetch an input string (or chinese character) based in keyboard input
    POST - add new input string or character to DB
    PUT - when would I use this? So clients can build their own character databanks?
    PATCH - entries can be updated and revised if user is authenticated
    DELETE - delete entry

Questions: 
- how to avoid doing the data entry legwork
- isn't auth unecessary if they're handling their own db and the data is open source
- is node/express really the best choice for this?
- noSQL or SQL? Do I need acid compliance

Plan:
1. Design UI (Robert?)
2. Model DB
3. Instantiate DB
4. Build scraper (https://en.wiktionary.org/wiki/Appendix:Chinese_Cangjie) in Python
5. Populate db for base set
6. write routes and middleware
7. write readme, focus on use of middleware with outside data sets

