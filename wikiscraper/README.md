
*Scraper Doc*

-using python/beautiful soup 4 to pull data from wiktionary 
-XML parser library lxml 4.9.2

Functions are currently broken out into indv files for isolation testing. Planning to consolidate after unit tests for main functions are complete. See entryClass.py for shape of individual entries, constants.py for static values such as entry URL. 

**Current File Directory:**

1. brokenLink.py: logic for checking if link to character entry is nonexistent. returns boolean
2. constants.py: URLs needed to initiate scrape. Not for use in tests
3. doubledEntry.py: logic for handling entries that contain multiple characters. Returns list of completed character entries
4. entryClass.py: defines Entry object class and getters. Setters might be added for individual users as stretch feature
5. fileFinder.py: Imma be real with you, not sure what this does.
6. firstScrape.py: gets URLS to individual subappendices. Needs some encapsulation 
7. fullScrape.py: tentative step towards performing scrape from root URL. 
8. getEntries.py: returns list of 'td' html elements to be parsed
9. sandbox2py: combining brokenLink, doubledEntry and getEntries functionality to perform full subappendix scrape. Writes to writeTest.json
10. sanityCheck.js: simple console.log to check for network errors with socket. Hopefully don't need to use this again.
11. search.py: searches list of entry class objects for one that matches provided arguments. For manual debugging/sanity check purposes only
12. tempCodeRunnerFile.py: girl what is this....
13. test_scrape.py: unit test for sandbox2. In VERY early stages
14. test.html: boilerplate HTML for eventual API. 
15. writeTest.json: used to test for successful scrape in more readable format. Effectively forms mock db