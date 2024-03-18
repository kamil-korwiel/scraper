# New Way of Testing
 - Define What program do
 - Define How it will work
 - Create a Simple Generateor for testing purposes 
 - Then refractor if you waht to add new featur to code of optimise

## PyStacTest
 - jupiter (learnig how works imported library and what data are given to you)
 - pytest + generator

# Scraper
## Crawler

### Zdefinuj Co ma robić Crawler (Co ... )
 - ustalić głebokość 
 - pobierać kod html ze strony
 - znaleść wszystkie linki storny
 - z normalizować je
 - przefiltrować wszystkie linki (usunąć odwiedzone)
 - zapisać do historii
 - dodać stos do słownika dic\[stos\]  {url : {stos} }
 


### Zdefinuj Jak ma działac  (Jak ... )
1. reuest.get
2. extract data
3. filter
4. add to stos
5. copy stos tu history
6. two strateges:
    - 6.1. get all data form curetn url stac (iterate)   
    - 6.2. use reqursion (go to 1) get data from current url
    - stop if empty stac 
    - or achive limit of deep 

### Test (Create Generator)
- generate imput data and end data in the way thats link togeder by some method



