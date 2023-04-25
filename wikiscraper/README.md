
*Scraper Doc*

-using python/beautiful soup 4 to pull data from wiktionary 
-XML parser library lxml 4.9.2

Functions are currently broken out into indv files for isolation testing. Planning to consolidate after unit tests for main functions are complete. See entryClass.py for shape of individual entries, constants.py for static values such as entry URL. 

**Current File Directory:**

files not listed here are due for obliteration. By Talos this can't be happening

1. brokenLink.py: logic for checking if link to character entry is nonexistent. returns boolean
2. dblEntryCheck.py: logic for handling entries that contain multiple characters. Returns list of completed character entries
3. entryClass.py: defines Entry object class and getters and static elements. Setters might be added for individual users as stretch feature
4. fileFinder.py: Imma be real with you, not sure what this does.
5. firstScrape.py: gets URLS to individual subappendices. Needs some encapsulation 
6. fullScrape.py: tentative step towards performing scrape from root URL. 
7. sanityCheck.js: simple console.log to check for network errors with socket. Hopefully don't need to use this again.
8. search.py: searches list of entry class objects for one that matches provided arguments. For manual debugging/sanity check purposes only
9. secondScrape.py the one that generates the entries! writes to writetest.json (see below)
10. test_scrape.py: unit test for sandbox2. In VERY early stages
11. test.html: boilerplate HTML for eventual API. 
12. writeTest.json: used to test for successful scrape in more readable format. Effectively forms mock db

