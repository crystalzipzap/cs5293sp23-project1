# CS5293sp23 – Project1

Name: Chenyi "Crystal" Zhang

## Project Description

This application takes a given email or a directory of emails from [Enron Email Dataset](https://www.cs.cmu.edu/~enron/) and redact parts of the information based on the user's selection. I randomly selected a folder from the dataset and the folder contains 299 email messages. I included the selected files in the `docs/` directory in the repo.

Based on the user's selection, the application would save the redacted file in `files/` directory. A redacted file would have `.redacted` extension followed by the file's original name. Once the redacting process is complete, the application would print a stats summary, including the kind of redaction performed and the numbers of redaction performed per category. A more detailed stats, breaking down the stats per file, is saved in the `/files` directory.

The general approach for this application is to utlize `spaCy` and `Regular Expression` to identify the information to be redacted, and then use `String.replace()` to replace original content with "█".

Here is the demo showing the applications runs and passes the pytests

![demo project 1](demo_project1.gif)

Here is the .txt file output after completing the demo. The same file "redaction_stats_4.txt" can be found in the `files/` directory.

```txt
******************************
       Redaction Starts
******************************
------------------------------
 File 1_
------------------------------
 Redacted Category | Count
-------------------|----------
 Address           | 22
 Email             | 21
 Date              | 6
 Gender            | 1
 Name              | 28
 Phone Number      | 0
------------------------------
 Subtotal            78
------------------------------


------------------------------
 File 2_
------------------------------
 Redacted Category | Count
-------------------|----------
 Address           | 23
 Email             | 85
 Date              | 2
 Gender            | 0
 Name              | 27
 Phone Number      | 1
------------------------------
 Subtotal            138
------------------------------


------------------------------
 File 300_
------------------------------
 Redacted Category | Count
-------------------|----------
 Address           | 131
 Email             | 5
 Date              | 41
 Gender            | 14
 Name              | 18
 Phone Number      | 0
------------------------------
 Subtotal            209
------------------------------


------------------------------
 File 301_
------------------------------
 Redacted Category | Count
-------------------|----------
 Address           | 148
 Email             | 4
 Date              | 57
 Gender            | 30
 Name              | 47
 Phone Number      | 2
------------------------------
 Subtotal            288
------------------------------


******************************
      Redaction Summary
******************************
------------------------------
 Redacted Category | Count
------------------------------
 Address           | 324
 Email             | 115
 Date              | 106
 Gender            | 45
 Name              | 120
 Phone Number      | 3
------------------------------
 Total               713
------------------------------
 Numbers of files:   4
 Complete time:      0.32min


```

## How to install

Run the command below to install all the required packages necessary to run the application.

```shell
pipenv install
```

## How to run

Run the application via the command line. The chart below indicates the arguments:
| Argument | Function | Required |
| ---------- | ----------------------------------------- | -------- |
| \--input | specify the file(s) to be read | Yes |
| \--address | redact all address from the input file | No |
| \--emails | redact the names in the email | No |
| \--dates | redact the dates | No |
| \--genders | redact all the gender-specified pronouns | No |
| \--names | redact all the first and last names | No |
| \--output | pass the name of the redaction_stats file | Yes |

Here is the command to run the given files in the `docs/` subdirectory. Note there are 299 documents and it takes around 16 minutes to complete redacting all of them. Below is the the output summary for the redaction, and the summary per file can be found in the `files/` subdirectory.

```shell
pipenv run python redactor.py --input 'docs/*.txt' --names --dates --phones --genders --address --emails --output 'files/'  --stats 'redaction_stats_299.txt'
```

Output when complete the 299-file run:

```shell
******************************
      Redaction Summary
******************************
------------------------------
 Redacted Category | Count
------------------------------
 Address           | 5154
 Email             | 3461
 Date              | 1620
 Gender            | 270
 Name              | 2994
 Phone Number      | 170
------------------------------
 Total               13669
------------------------------
 Numbers of files:   299
 Complete time:      16.31min
```

The demo above is ran with the command below. The testdocs/ subdirectory has four files.

```shell
pipenv run python redactor.py --input 'testdocs/*' --names --dates --phones --genders --address --emails --output 'files/'  --stats 'redaction_stats_4.txt'
```

## Bugs and Assumptions

- I struggled with phone number redaction. It takes me a while to ensure the regular expression can catch most common-format phone numbers. But there are likely some limitations
- Assume the commands from user ends are correct.
- I wrote a function to add .txt extensions on the emails. I did not write a test case for the function because it worked after seeing the extension changes upon running the function. I use it to add .txt extension for every file in `/docs` directory.
- I notice that certain names used in a file attachment cannot be redacted.
